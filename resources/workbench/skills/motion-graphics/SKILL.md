---
name: motion-graphics
description: >
  Make premium coded motion graphics with Claude: product promos, launch films, UI motion
  loops, kinetic type, explainers, animated social posts. References first, a motion design
  system, still boards approved before any render, then a deterministic HTML/canvas build
  exported with Playwright + ffmpeg, refined one note at a time. Use for "motion graphics",
  "promo video", "launch film", "animate this", "kinetic type", "product video", "explainer",
  "make a video of my site/app", "it looks like AI slop", or any code-rendered video.
  For AI-generated live-action/character films (Seedance, Higgsfield) use ai-film-pipeline.
---

# Motion Graphics

Sources: Duncan Rogoff, "Turn Claude Into a Motion Design GENIUS" (youtu.be/Wkf2IjZrRt4) and
its 5-prompt guide; build method distilled from top prompts on prompt-motion.com
(e.g. @rossaxbt's Ora 2 launch film and white-ball UI loop).

**Why first tries fail:** Claude has never seen your taste, so it guesses, and a guess looks
like everyone else's video (square, silent, copy you'd never say). References, a design system
and approved stills give it taste before anything renders.

## Step 1: References (never skip)

- Find 2 favourites on **prompt-motion.com** (every video is posted with the exact prompt and
  stack) or in the client's world. Then find 3 more with the same feel for the brand's colours
  and mood.
- For each, save: link, creator, the prompt word for word, the video, and a few frames. Report
  which candidates you turned down and why.
- **Detailed prompts carry style; one-liners leave gaps Claude fills with guesses.** Prefer
  references whose prompts specify scenes, timing and bans.
- **Never carry facts over.** A copied prompt can smuggle the original brand's numbers and
  claims ("1M visitors in 8 months") onto your screen. Take the feel; use the client's own
  words, screenshots, logos and data only.

## Step 2: Study the references

For every reference, write notes: colours, type, layouts, how text and cards move, pacing.
Then one summary: **moves worth stealing (ranked, user's favourites first)** and a
**leave-out list for this brand** (e.g. "no white scenes", "no made-up numbers"). Be honest
where something doesn't fit. The leave-out list is what stops it looking like a copy.

## Step 3: Motion design system (one file, `MOTION.md`)

Start from the brand's website/DESIGN.md (colours, fonts), borrow motion from the references,
add the user's rules. Sections:
- **Feeling** in one line
- **Look** (palette with coverage %, background, texture) and **type** (families, scale ratio)
- **4-5 signature moves**
- **Motion rules**: easing, minimum fade (≥0.3s; 0.05s reads as a pop), camera behaviour
  (e.g. continuous drift, never reset zoom on a handoff), cut timing (on beats/phrases)
- **Layout menu**: 10+ named scene layouts
- **Banned list**: e.g. hard cuts, glows, particle bursts, gradient text, highlight boxes,
  white flashes, small text under big headlines, pill labels/buttons that look AI-made
- **Defaults**: every scene fills the frame; nothing overlaps; safe margins
- Say **where each rule came from** (brand, reference, user note)

If a client DNA skill exists (design-dna), it is the source for look/type; MOTION.md adds motion.
Every later fix is written back here, **replacing** the old rule, never adding a duplicate.

## Step 4: Stills before any video

- Write a **beat map** first (scene, time range, what moves, audio cue).
- Build ~6 **still boards** as web pages, one per kind of scene (title, product UI, proof/
  review, grid of work, CTA/end card...), saved as full-size images. Real screenshots, logos and
  words from the client only.
- Inspect every still yourself: overlaps, edge crowding, contrast (e.g. dark logos on dark bg),
  duplicates (logo twice), readability at final size. Fix stills before rendering; a render
  costs 10-20 minutes, a still costs seconds.
- Show the user the stills (contact sheet) and get approval. Only then build the video, with a
  scene-by-scene plan written first.

## Step 5: Build (deterministic, reviewable)

1. **One HTML file** (DOM/SVG or canvas) at the target size (1920x1080 16:9, 1080x1920 9:16,
   1440x1440 square) and 60fps.
2. **Every frame is a pure function of time inside `seek(t)`.** No CSS transitions, timers or
   state carried between frames, so any frame renders independently and stills match the video.
3. One world + **one camera transform** (position + log-space zoom) when scenes should flow
   like a continuous shot. Closed-form springs for landings; small overshoots only.
4. Sync to measured beats: cuts on phrase starts, the music drop on the key line. If there's
   voiceover, build a word-timing table and type captions to it.
5. Render with **Playwright** (headless Chrome) frame by frame at 60fps (optionally 4-8
   motion-blur subframes), encode with **ffmpeg** (H.264, yuv420p; loudnorm to -14 LUFS if audio).
6. Before showing anything: contact sheet of stills, scan frame differences for single-frame
   pops, check the loop boundary (first = last frame) if looping, check voice vs music levels.

Remotion is an acceptable alternative stack if the project already uses React; keep the same
seek(t) determinism and stills-first rule.

**Setup check** (once): node, `npx playwright install chromium`, full ffmpeg build. Audio is
optional: royalty-free music (Pixabay), SFX (Mixkit), voice (ElevenLabs or Fish Audio, keys in
`.env` only).

## Step 6: Review like a designer (one round at a time)

- Ask for (or give) notes in plain words: what works, what doesn't, how to fix. Never accept
  "make it better" as a note; name the scene or the feeling and what's wrong.
- Good notes: "too much copy", "one big headline, no small text under it", "the buttons look
  like AI slop", "flow like one continuous camera shot". Praise matters: it says what to keep.
- One note → one revision → watch → next note. Write each fix into MOTION.md.
- If it's fundamentally wrong ("not premium, not flashy"), polish won't fix it: **change the
  input** (better references, different product angle) and restart from Step 1.

## Prompt shape for a full brief (reusable)

Write briefs in this block structure (it's how the best prompt-motion.com prompts work):
`<inputs>` what to ask the user for, with defaults → `<direction>` format, size, look, motion
rules, Banned list → `<structure>` scenes with timing → `<sound>` (optional) → `<build>`
technical steps → `<gotchas>` known failure modes → `<start>` "ask for inputs, show beat map
and N stills before the full render".

## Deliverables

`REFERENCES.md` (links, creators, prompts, why chosen/rejected) · `MOTION.md` · beat map ·
approved stills · `video.html` · final MP4 · `CHANGELOG.md` of review rounds.
