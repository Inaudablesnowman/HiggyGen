#!/usr/bin/env python3
"""Hard gate before anything is SCHEDULED on Buffer (step 12 of the POST PIPELINE).
Usage: post_gate.py episodes/<slug>/QA_REPORT.json
Exit 0 only if steps 1-11 are all "pass", hook >= 8, hold >= 8, qa_video.py passed, and K3 approved.
Anything else exits 1 and prints exactly what is missing. A post that fails this gate stays a DRAFT.
Report format:
{"steps": {"1": "pass", ..., "11": "pass"}, "hook": 8, "hold": 9, "qa_video_passed": true,
 "approved_by_k3": true, "channel": "punintendedtv", "ai_label": true}
"""
import json, sys

def main(path):
    try:
        r = json.load(open(path))
    except Exception as e:
        sys.exit(f"BLOCKED: cannot read report ({e}). No report = no scheduling.")
    problems = []
    steps = r.get("steps", {})
    for i in range(1, 12):
        v = steps.get(str(i))
        if v != "pass":
            problems.append(f"step {i} is {v!r}, must be 'pass'")
    for k in ("hook", "hold"):
        if not isinstance(r.get(k), (int, float)) or r[k] < 8:
            problems.append(f"{k} score {r.get(k)!r} is below 8")
    if r.get("qa_video_passed") is not True: problems.append("qa_video.py has not passed")
    if r.get("channel") != "punintendedtv": problems.append(f"channel is {r.get('channel')!r}, must be 'punintendedtv'")
    if r.get("ai_label") is not True: problems.append("AI-generated label is not on")
    if r.get("approved_by_k3") is not True: problems.append("K3 has not approved")
    if problems:
        print("BLOCKED - do not schedule. Stays a draft:")
        for p in problems: print(" -", p)
        sys.exit(1)
    print("GATE PASSED: all checks done and approved. OK to schedule.")

if __name__ == "__main__":
    if len(sys.argv) != 2: sys.exit(__doc__)
    main(sys.argv[1])
