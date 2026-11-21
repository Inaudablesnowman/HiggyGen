# PLAYBOOK
Living lessons file. Updated after every results report. Nothing here is data until K3 reports it.

## Standing rules
- Cost rule: free daily credits for raw clips, trim each clip to used seconds, upscale only winners (1080p, 24-30fps), Hook/Hold >= 8.
- Judge videos at 24-48h and 7d. Judge the account only after ~30 videos.
- One experiment per day, labeled E#, applied to one of three videos.

## Lessons
_None yet (no results reported)._

## Next change to test
E1: baseline bold text hook + motion in frame 1 (Gerald Ep 1).

## Open questions (verify in-app before Phase 1)
1. Pilot posting cap / campaign access. 2. AI narration allowed on shop videos? 3. Do cartoon-only videos pass shoppable-video checks? 4. Brand terms banning AI affiliate content.

## VIRAL CHECKLIST (applies to EVERY video; added 2026-11-19)
Evidence note: sources are mostly creator/marketing blogs. TikTok does not publish how much each signal counts, and nobody can measure "dopamine" on a video. Treat this as design heuristics, not guarantees. Check real numbers in TikTok analytics after posting.

**Why it works (theory, not proof):** a hook opens a *curiosity gap* (Loewenstein's information-gap idea: a noticed gap in knowledge feels like a deficit you want closed); surprise breaks a *prediction*; unpredictable payoffs keep people swiping (variable reward / Hook Model). Design every video as: open a gap, escalate, pay it off late, then open a new gap.

**Platform signals (blog consensus):** completion rate and watch time first, rewatches next, shares/saves next, comments, likes last.

**Gate before K3 sees a video (all must pass):**
1. **Frame 0:** a face or object already moving, plus a visual or audio shock (crash zoom, flash, bass hit). No title card, no logo, no slow intro. First spoken line starts within 0.3 s.
2. **Hook text:** 7 words or fewer, works with sound off. Opens an *open loop* (a question the viewer must see answered).
3. **Dialogue pace (viewers must be able to follow):** 2.2-2.8 words per second, not faster. Squeeze dead air, but keep a 0.25-0.35 s gap between lines and a 0.4-0.5 s beat before each punchline. Each caption stays on screen until the next line starts. Lines run one after another, never overlapping (K3 rule). Too slow (1.4 w/s) reads as dead air; too fast (3.3 w/s) cannot be followed.
4. **Stimulus rhythm:** something new every 1-2 s (cut, zoom, SFX, text). A bigger change (new location, twist, new sound) every 8-10 s.
5. **Escalation:** at least 3 beats with rising stakes. Every punchline gets a sound hit + zoom + flash.
6. **Surprise:** one unexpected turn per video. Vary the format between videos so it never feels predictable.
7. **Ending:** loop back to frame 0, or a cliffhanger. Last frame = "Part 2". Aim for a rewatch.
8. **Share and comment triggers:** one line a viewer would send to a friend ("send this to your roommate"), and a caption question to bait comments.
9. **Length:** 15-25 s. Cut anything that does not earn its seconds.
10. **Measure:** 3-second hold, average watch %, completion, rewatches, shares. A/B hooks one variable at a time (label E#).

**Lesson log**
- Roommate Wars Ep 1 v1 (2026-11-19): K3 said "pauses, no wow factor, not viral." Measured cause: dialogue ran about 1.4 words/s (target 2.5+), the opening was a text card then "say something" (no shock), no sound design until the end, and the opening reused the same two clips. Fix: speed dialogue up ~30% and squeeze pauses, punchier first line ("Doug. WE NEED TO TALK."), crash zoom + flash + bass hit at frame 0, slap/gasp on the hand grab, beeps + countdown, hard end on "PART 2".
- Roommate Wars Ep 1 v2 (2026-11-19): K3 said "not too fast, viewers need to follow along." Cause: I over-corrected to 3.3 words/s with 0.12 s gaps. Target 2.2-2.8 w/s, gaps 0.3 s, a beat before punchlines, longer caption holds. Also: squeezing too hard removed the staccato pauses in "Look. It. Up."; keep ~0.16 s of silence inside lines.

## STANDING RULE: every video and ad must beat the last one (K3, 2026-11-19)
- Before showing K3 anything, name **at least one concrete way it is better or more engaging than the previous one** (stronger hook, tighter pace, bigger payoff, new visual trick, better sound design, sharper caption, etc.).
- List my **top 3 weaknesses** of the new piece and fix at least one before presenting; carry the rest into the next one.
- Never repeat a hook, joke structure, or edit pattern from the last video without improving it.
- Log each "beat the last one" improvement here:
  - Roommate Wars Ep 1 v3: pace 2.5 w/s (v1 1.4, v2 3.3), 0.3 s gaps, captions held until the next line, hook flash + bass hit + crash zoom. Weaknesses still open: opening reuses two clips with zooms (no brand-new shock visual), Brenda's mouth may drift out of sync, no music yet.

## Posting rules (K3, 2026-11-19)
- Only draft/post on the **punintendedtv** TikTok channel in Buffer. Never touch any other channel (the Instagram `tryzagikonow` / Zagiko shop is completely unrelated; ignore it).
- Default to **draft only**; publish only when K3 explicitly says to post.

## Strategy update (K3, 2026-11-19)
- Cheap volume format: code-drawn skits (voiceover ~0.3 credit each) so 3/day is affordable; mix in video-clip pieces only when worth the credits.

## POST PIPELINE (K3 rule, 2026-11-21): every post goes through ALL of these steps, no exceptions
Each step is recorded pass/fail in a QA report shown to K3 with the video. A failed step is fixed and re-run before moving on.
1. **Concept check:** the pun lands without explanation; hook text 7 words or fewer; an open loop in the first 2 s.
2. **Script clarity:** read aloud, plain words, one idea per line, no tongue-twisters; pace 2.2-2.8 words/s; numbers and symbols spelled out for the voice.
3. **Rules and safety:** AI-generated label ON; no brands, logos, real people, copyrighted music, or false claims; Trevor never shown; correct channel (punintendedtv only).
4. **Voice take check:** transcribe the take and compare to the script (no tags read aloud, no missing or extra words); re-voice once if it does not match.
5. **Audio QA:** loudness -17 to -13 LUFS, true peak at or below -1 dBFS, lines never overlap, 0.25-0.35 s gaps, no dead air over 0.7 s, sound effects never mask the voice.
6. **Visual QA:** look at frames at 0 s, every beat, and the last frame; captions fully on screen and readable; no missing-glyph boxes; characters consistent; nothing cut off.
7. **Technical QA:** run `python3 assets/tools/qa_video.py <file>` (1080x1920, 24-60 fps, 12-35 s, audio present, decodes to the end, size); upload returns HTTP 200 and is confirmed.
8. **Virality pass:** score against the VIRAL CHECKLIST; Hook and Hold both 8 or higher; name one concrete way it beats the previous video; list the top 3 weaknesses and fix at least one before showing it.
9. **Caption and hashtags:** engaging caption with a share or comment trigger, 3-5 relevant hashtags including #AIgenerated, title set, no unsupported claims.
10. **Best-time slot:** choose the posting slot (see rules below), never more than 3 posts/day, at least 4 hours apart, rotate formats so two of the same kind are never back to back.
11. **Buffer staging:** create it on punintendedtv, then read it back with get_post: right channel, right video, right duration, AI flag on, caption correct. Keep scheduled posts at or under Buffer's cap of 10.
12. **Approval and scheduling:** K3 sees the QA report and says go; only then schedule (dueAt in the account timezone, America/Boise), and verify with get_post that status is scheduled at the right time. Default is draft only until K3 says otherwise.
13. **Post-mortem at 24-48 h:** pull results (Buffer metrics plus K3's TikTok analytics: 3-second hold, average watch, completion, rewatches, shares, follows), log them in TRACKING_LOG.md, and update this playbook with one change to test next.

**Best-time rules (honest version):** there is no performance data yet, so "best time" starts as a reasonable guess, not a fact. Start with Buffer's three daily slots (06:44, 12:44, 21:44 Boise time). Spread posts across all three. After about 10 posts, compare views and 3-second hold by slot and move future posts toward the winners. Check TikTok's own analytics for when the audience is active.

## Scheduling gate (K3, 2026-11-21)
Nothing is scheduled on Buffer until `python3 assets/tools/post_gate.py episodes/<slug>/QA_REPORT.json` exits 0: steps 1-11 pass, Hook and Hold at least 8, qa_video.py passed, channel is punintendedtv, AI label on, and K3 approved. Otherwise the post stays a draft.

## Generation engine notes (2026-11-21)
- This repo (HiggyGen) is already Open Generative AI v2.0.0 by Anil Chandra Naidu Matcha; there is nothing to replace.
- It runs without an API key only as the DESKTOP app with Local Models (sd.cpp images; Wan2GP video needs an NVIDIA/AMD GPU, 480p, slow). The web version needs a MuAPI key. It has no voice engine.
- It cannot run in the cloud sandbox (no GPU, no GUI). It would run on K3's computer.
