---
name: ai-film-pipeline
description: >
  Run an AI-generated film, ad, music video, skit or character series end to end with
  image/video models (Higgsfield Cinema Studio, Seedance 2.0/2.5, Genjutsu, Nano Banana Pro,
  Soul, Seedream): world bible, locked characters, scene plates, shot prompts, cheap draft pass,
  final render, sound and finishing. Orchestrates story-bible-builder → castkit-v1 →
  scenecraft-v1 → shotcaller-v1 / motiondojo-v1 in the right order. Use for "AI video", "AI film",
  "Seedance", "Higgsfield", "short film", "spec ad", "music video", "consistent characters",
  "character series", "video generation prompt", or when shots/characters drift between gens.
  For code-rendered motion graphics (promos, UI motion, kinetic type) use motion-graphics.
---

# AI Film Pipeline

Source: Joey (@joeysnoisygroup), "4 free Claude skills and how to use them so you stop wasting
credits" (youtu.be/LOUEH3DzLro) and his Higgsfield post "All My Claude Skills for Better
Prompting". Joey's four/five skills are installed separately; this skill sets the order and the
production rules around them.

**Core idea: build the world first.** The boring skills at the front decide whether the
expensive generations at the end work. Most people jump straight to Shotcaller and burn credits.

## The order (don't skip ahead)

| # | Stage | Skill | Output | Gate |
|---|---|---|---|---|
| 1 | World | `story-bible-builder` | An installable story-bible SKILL.md for this world (premise, thesis, timeline, factions, locations, rules, characters with voice/movement/stillness locks, relationships) | Only for a **world/series**. Skip for a one-off mini doc or single ad. |
| 2 | Cast | `castkit-v1` | Face lock → (additions) → outfit → 3-panel character sheet | Outfit needs a locked face; sheet needs an approved outfit |
| 3 | Places | `scenecraft-v1` | Scene plates (environment, people-in-scene first frames, coverage angles) | Plates agree on geometry and light |
| 4 | Shots | `shotcaller-v1` (Seedance) or `motiondojo-v1` (Genjutsu motion transfer) | Numbered reference list, titled prompt, one paste-ready code block per shot | Version and runtime cap chosen first |

Install the story bible as its own skill (personal `~/.claude/skills/<world>-bible/`, or the
client repo `.claude/skills/`) so every later chat knows the world. Don't spend memory slots on it.

## Production rules (from the video, not in the skill files)

- **Characters are text-first.** Show Claude visual inspiration, but write the character as a
  text prompt; don't feed internet reference photos into the image model. Higgsfield **Soul**
  for distinctive cinematic faces, then **Nano Banana Pro** for a clean chest-up canon plate.
- **Flat 18% gray, shadowless** reference plates: no baked lighting; the scene lights the
  character later. White backgrounds blow out edges and read plastic.
- For the 3-panel sheet's face panel, attach the **canon face plate** as bone/face structure
  reference, not the small face from the outfit image.
- Scene prompts describe **only what's visible in frame**. Leave camera brand/stock name-dropping out.
  Add **atmospheric depth** (distant things slightly faded) to avoid the plastic look.
- **Seedance version:** 2.0 = 9 references, 15s, native 4K. 2.5 = 50 references, 30s, 1080p,
  best colour, but may add background music (strip it with **Moises.ai**). Splits anything
  longer than the cap into separate prompts.
- **Dialogue:** paste the script with speaker labels; one mouth speaks at a time; the delivery is
  written separately from the words. Expect ~90-95% accuracy, not 100%.
- **Draft at 480p first** to check framing, action and dialogue; re-send the approved prompt at
  1080p. Never iterate at full resolution.
- **Finishing:** 1080p renders can be scaled 200% in the edit with added grain instead of AI
  upscaling (Joey's approach; judge per delivery spec).
- Keep one project space per world (characters, plates, logos, assets) in the generation tool.
- Turn off old/duplicate skill versions instead of keeping two that compete.

## Budget and log (every project)

Keep `PRODUCTION-LOG.md`: shot, model/version, resolution, credits, keep/kill, note. Reference
point: a ~40-second spec skit with a 480p draft pass cost ~750 Higgsfield credits (~$30) in
October 2026. Tell the user the estimated credits before the full-res pass.

## Ethics and rights

Original characters only, never a real person's likeness or voice without consent. Garment
and look references inspire; don't reproduce a brand's logo or trademarked design. Disclose
sponsored tools when publishing for a client.

## Hand-offs

- Brand/product spots that need on-screen UI, kinetic type or data → `motion-graphics`
  (coded) and cut together.
- Narration/voice → Fish Audio or ElevenLabs; music → licensed or royalty-free only.
- Approved look for a series → `design-dna` to codify the visual style.
