#!/usr/bin/env python3
"""Automated technical QA for a finished video (steps 5-7 of the POST PIPELINE in PLAYBOOK.md).
Usage: qa_video.py video.mp4 [--min 12] [--max 35]
Prints PASS/FAIL per check and exits 1 if any check fails. Judgement checks (is it funny,
do captions fit, does the voice match the script) still need eyes on frames + a transcript.
"""
import json, re, subprocess, sys

def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)

def main(path, dmin, dmax):
    pr = run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", path])
    if pr.returncode: sys.exit(f"FAIL cannot read file: {pr.stderr.strip()}")
    info = json.loads(pr.stdout)
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    dur = float(info["format"].get("duration", 0))
    size_mb = int(info["format"].get("size", 0)) / 1e6
    checks = []
    def chk(name, ok, detail): checks.append((name, ok, detail))
    chk("video stream present", v is not None, "")
    chk("audio stream present", a is not None, "")
    if v:
        chk("resolution 1080x1920", (v["width"], v["height"]) == (1080, 1920), f'{v["width"]}x{v["height"]}')
        num, den = (v.get("r_frame_rate", "0/1").split("/") + ["1"])[:2]
        fps = float(num) / float(den or 1)
        chk("frame rate 24-60", 24 <= fps <= 60, f"{fps:.1f} fps")
    chk(f"duration {dmin}-{dmax}s", dmin <= dur <= dmax, f"{dur:.2f}s")
    chk("file size under 100 MB", size_mb < 100, f"{size_mb:.1f} MB")
    if a:
        e = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
        mI = re.findall(r"I:\s+(-?[\d.]+) LUFS", e)
        mP = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)
        if mI and mP:
            i, p = float(mI[-1]), float(mP[-1])
            chk("loudness -17 to -13 LUFS", -17.0 <= i <= -13.0, f"{i:.1f} LUFS")
            chk("true peak <= -1.0 dBFS (no clipping)", p <= -1.0, f"{p:.1f} dBFS")
        else:
            chk("loudness measurable", False, "could not measure")
        s = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "silencedetect=n=-50dB:d=0.7", "-f", "null", "-"]).stderr
        gaps = re.findall(r"silence_duration: ([\d.]+)", s)
        chk("no dead-air gaps over 0.7 s", len(gaps) == 0, f"{len(gaps)} gap(s)" + (f": {', '.join(gaps[:4])}s" if gaps else ""))
    # plays to the end: decode everything
    d = run(["ffmpeg", "-v", "error", "-i", path, "-f", "null", "-"])
    chk("decodes to the end without errors", d.returncode == 0 and not d.stderr.strip(), d.stderr.strip()[:80])
    bad = [c for c in checks if not c[1]]
    for n, ok, det in checks: print(f'{"PASS" if ok else "FAIL"}  {n}  {det}')
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks passed")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    dmin, dmax = 12.0, 35.0
    if "--min" in args: dmin = float(args[args.index("--min") + 1])
    if "--max" in args: dmax = float(args[args.index("--max") + 1])
    main(args[0], dmin, dmax)
