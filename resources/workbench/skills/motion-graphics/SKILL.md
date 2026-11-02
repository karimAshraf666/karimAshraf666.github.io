---
name: motion-graphics
description: >
  Make premium coded motion graphics: product promos, launch films, UI motion
  loops, kinetic type, explainers, animated social posts. References first, a motion design
  system, still boards approved before video production, then a deterministic build
  using HTML/canvas, Remotion or HyperFrames, refined one note at a time. Use for "motion graphics",
  "promo video", "launch film", "animate this", "kinetic type", "product video", "explainer",
  "make a video of my site/app", writing a Claude/Codex motion brief or prompt, or any
  code-rendered video.
  For AI-generated live-action/character films (Seedance, Higgsfield) use ai-film-pipeline.
---

# Motion Graphics

## Applying this workflow in Codex

Select this workflow automatically for coded motion and its creative briefs. Use the
available Codex browser, rendering and media tools; Claude-specific names in the source
describe the original tutorial, not a required application. For a prompt-only request,
deliver the structured brief below without starting production. Preserve existing user
answers, brand, model and tool choices; ask only for missing inputs that affect the result.
Naming a framework or generator in a tutorial does not authorize installing it, connecting
an account or spending credits. Generated footage/assets are optional inputs; route actual
AI film production to `ai-film-pipeline` within the user's authorized scope.

Sources: Duncan Rogoff, "Turn Claude Into a Motion Design GENIUS" (youtu.be/Wkf2IjZrRt4) and
its 5-prompt guide; build method distilled from top prompts on prompt-motion.com
(e.g. @rossaxbt's Ora 2 launch film and white-ball UI loop).
Tyler Mommsen's [renderer, brief and iteration tutorial](https://www.youtube.com/watch?v=2moKxAZjwCE)
adds stack selection and a more explicit brief/check contract. Read
[the source notes and checked renderer guidance](references/renderer-brief-iteration.md)
when choosing a renderer, writing its build instructions or exploring logo-motion concepts.

**Why first tries fail:** Without references, an agent guesses your taste, and a guess looks
like everyone else's video (square, silent, copy you'd never say). References, a design system
and approved stills give it taste before anything renders.

## Step 1: References (never skip)

- Start with the user's supplied reference and the client's world. If direction is missing,
  find 2 favourites on **prompt-motion.com** or comparable sources, then a few supporting
  references for colour and mood only if needed. An approved reference need not be
  rediscovered; a short sting does not need a launch film's research set.
- For each, save: link, creator, available prompt/stack link, concise structural notes and
  a few useful frames. Choose one dominant direction; report meaningful rejections and why.
- **Detailed prompts carry style; one-liners leave gaps the agent fills with guesses.** Prefer
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
- **Signature moves** appropriate to the piece; one can be enough for a logo sting
- **Motion rules**: easing, minimum fade (≥0.3s; 0.05s reads as a pop), camera behaviour
  (e.g. continuous drift, never reset zoom on a handoff), cut timing (on beats/phrases)
- **Layout menu**: the scene types actually needed; a larger library suits a recurring series
- **Banned list**: e.g. hard cuts, glows, particle bursts, gradient text, highlight boxes,
  white flashes, small text under big headlines, pill labels/buttons that look AI-made
- **Defaults**: every scene fills the frame; nothing overlaps; safe margins
- Say **where each rule came from** (brand, reference, user note)

If a client DNA skill exists (design-dna), it is the source for look/type; MOTION.md adds motion.
Every later fix is written back here, **replacing** the old rule, never adding a duplicate.

## Step 4: Stills before any video

- Write a **beat map** first (scene, time range, what moves, audio cue).
- Build **still boards** as web pages for important scene types (title, product UI, proof/
  review, grid of work, CTA/end card...), saved as full-size images. Real screenshots, logos and
  words from the client only. A short sting may need only its opening, key pose and final
  hold; expand the board set when the piece has more distinct compositions.
- Inspect every still yourself: overlaps, edge crowding, contrast (e.g. dark logos on dark bg),
  duplicates (logo twice), readability at final size. Fix stills before rendering; a render
  costs 10-20 minutes, a still costs seconds.
- Show the user the stills (contact sheet) and get approval. Only then build the video, with a
  scene-by-scene plan written first.
- Reuse approved stills and decisions. A timing revision does not reopen visual approval;
  material changes to the agreed look or content need updated boards.

## Step 5: Build (deterministic, reviewable)

Record the renderer, reason, installed version, dimensions, duration and delivery fps before
coding. Preserve the user's chosen stack and inspect the existing project first. Remotion
uses React and a frame-based API; HyperFrames uses HTML and seekable timelines. They are
options with different authoring contracts, not interchangeable dependencies. Keep the
existing HTML/canvas route when it fits; do not replace it just because a framework appears
in a reference. Read the linked renderer guidance for the selected route only.

For the HTML/canvas route:

1. **One HTML file** (DOM/SVG or canvas) at the agreed target size (e.g. 1920x1080 16:9,
   1080x1920 9:16, 1440x1440 square) and fps; 60fps is an option, not a universal requirement.
2. **Every frame is a pure function of time inside `seek(t)`.** No CSS transitions, timers or
   state carried between frames, so any frame renders independently and stills match the video.
3. One world + **one camera transform** (position + log-space zoom) when scenes should flow
   like a continuous shot. Closed-form springs for landings; small overshoots only.
4. Sync to measured beats: cuts on phrase starts, the music drop on the key line. If there's
   voiceover, build a word-timing table and type captions to it.
5. Render with **Playwright** (headless Chrome) frame by frame at the agreed fps (optionally 4-8
   motion-blur subframes), encode with **ffmpeg** (H.264, yuv420p; loudnorm to -14 LUFS if audio).
6. Before showing anything: contact sheet of stills, scan frame differences for single-frame
   pops, check the loop boundary (first = last frame) if looping, check voice vs music levels.

For any route, retain the same time/frame determinism and stills-first rule using that
renderer’s native API; Remotion does not require a literal `seek(t)` function. After still
approval, test one representative transition and seek backwards/forwards before a long
export. Run available renderer checks, inspect frames and watch the exported file with
sound. A successful render command alone does not establish visual quality.

**Setup check** (once): inspect installed Node, the chosen renderer/browser and ffmpeg.
Surface missing dependencies before changing setup; prompt-only work needs no installation.
Audio is optional: music (e.g. Pixabay), SFX (e.g. Mixkit), voice (ElevenLabs or Fish Audio,
keys in `.env` only); verify the selected asset's usage terms.

## Step 6: Review like a designer (one round at a time)

- Ask for (or give) notes in plain words: what works, what doesn't, how to fix. Never accept
  "make it better" as a note; name the scene or the feeling and what's wrong.
- Good notes: "too much copy", "one big headline, no small text under it", "the buttons look
  like AI slop", "flow like one continuous camera shot". Praise matters: it says what to keep.
- One note → one revision → watch → next note. Name the scene/timestamp, intended change and
  what must stay. Preview the affected range first, then check neighbouring transitions and
  audio sync. Write reusable rules into MOTION.md and the specific revision into CHANGELOG.md.
- For an open-ended logo sting, propose a small set of distinct motion ideas as beat
  descriptions/key poses, then develop the chosen concept through the same still approval
  gate. Variants are an exploration tool, not a requirement to rerender the full film.
- If it's fundamentally wrong ("not premium, not flashy"), polish won't fix it: **change the
  input** (better references, different product angle) and restart from Step 1.

## Prompt shape for a full brief (reusable)

Write briefs in this block structure (it's how the best prompt-motion.com prompts work):
`<inputs>` product, audience, goal, verified copy/assets and missing decisions → `<direction>`
dominant reference, format, size, duration, look, motion rules and bans → `<structure>` story
and scenes with timing → `<sound>` (optional, including sync cues) → `<build>` chosen renderer,
existing project constraints, editable source and export settings → `<checks>` factual
accuracy, readability, timing, transition continuity, sound and final-file inspection →
`<gotchas>` known failure modes → `<start>` "ask only for missing inputs, show beat map and
stills before video production". State assumptions; derive style from this brand and its
references, not the tutorial's fictional app. Prompt-only requests end with the brief.

## Deliverables

`REFERENCES.md` (links, creators, prompt/stack sources, why chosen/rejected) · `MOTION.md` ·
beat map · approved stills · editable renderer source (`video.html` for the HTML route) ·
final MP4 or agreed format · `CHANGELOG.md` of review rounds. Scale these to the deliverable;
prompt-only work delivers the brief, not a production package.
