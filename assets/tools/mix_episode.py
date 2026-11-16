#!/usr/bin/env python3
"""Mix separate dialogue/SFX clips into one fluent episode audio track.

Fixes the "patchy blocks of audio" problem:
  1. every clip -> same format (48 kHz mono) and same loudness (-16 LUFS dialogue)
  2. 20 ms fade-in / 40 ms fade-out on every clip (no clicks at cut points)
  3. a continuous low room-tone bed under the whole episode (no dead-silent gaps)
  4. final loudness set for TikTok (-14 LUFS integrated, -1.5 dBTP true peak)

Usage:
  mix_episode.py timeline.json out.wav
timeline.json:
  {"duration": 24.0, "bed_db": -42,
   "clips": [{"file": "doug.wav", "start": 0.3, "gain_db": 0}, ...]}
(`gain_db` is an optional per-clip offset, e.g. -6 for a background voice.)
"""
import json, subprocess, sys, tempfile, os


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def main(timeline_path, out_path):
    tl = json.load(open(timeline_path))
    total = float(tl["duration"])
    bed_db = float(tl.get("bed_db", -42))
    tmp = tempfile.mkdtemp()
    prepared = []
    for i, c in enumerate(tl["clips"]):
        dst = os.path.join(tmp, f"c{i}.wav")
        run(["ffmpeg", "-y", "-i", c["file"], "-ac", "1", "-ar", "48000",
             "-af", "loudnorm=I=-16:TP=-1.5:LRA=7,aresample=48000,"
                    "afade=t=in:d=0.02,areverse,afade=t=in:d=0.04,areverse",
             dst])
        prepared.append((dst, float(c["start"]), float(c.get("gain_db", 0))))

    cmd = ["ffmpeg", "-y",
           "-f", "lavfi", "-t", str(total), "-i",
           f"anoisesrc=color=brown:amplitude=0.3:sample_rate=48000"]
    for dst, _, _ in prepared:
        cmd += ["-i", dst]
    parts = [f"[0:a]lowpass=f=400,volume={bed_db}dB[bed]"]
    labels = ["[bed]"]
    for i, (_, start, gain) in enumerate(prepared, start=1):
        ms = int(start * 1000)
        parts.append(f"[{i}:a]adelay={ms}:all=1,volume={gain}dB[v{i}]")
        labels.append(f"[v{i}]")
    parts.append("".join(labels) +
                 f"amix=inputs={len(labels)}:normalize=0:duration=first,"
                 f"atrim=0:{total},loudnorm=I=-14:TP=-1.5:LRA=9[out]")
    cmd += ["-filter_complex", ";".join(parts), "-map", "[out]",
            "-ar", "48000", "-ac", "1", out_path]
    run(cmd)
    print("wrote", out_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
