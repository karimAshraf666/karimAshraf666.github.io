# Renderer, brief and iteration notes

Read when selecting a coded-video renderer, drafting its build contract or exploring a
logo sting. This extends the existing motion workflow; the brand, references and approved
stills remain the creative authority.

## Video source and useful lessons

Source: Tyler Mommsen, [YouTube video 2moKxAZjwCE](https://www.youtube.com/watch?v=2moKxAZjwCE).
Reviewed from the complete English auto-caption transcript on 2026-11-02. Captions can
misname models and products; the timestamps below locate ideas, not verified API facts.
These are original notes, not the creator's prompt pack or a transcript reproduction.

| Source segment | Lesson retained in this workflow |
| --- | --- |
| [0:53–1:56](https://www.youtube.com/watch?v=2moKxAZjwCE&t=53s) | Coded motion needs a rendering/export mechanism. Specify it rather than leaving the agent to improvise an exporter. The tutorial discourages custom code; our existing deterministic HTML route remains valid when its capture pipeline is established. |
| [1:57–3:05](https://www.youtube.com/watch?v=2moKxAZjwCE&t=117s) | Generated imagery/footage is a separate optional source of assets. A logo/UI animation does not inherently need a paid generation connector. |
| [3:26–4:23](https://www.youtube.com/watch?v=2moKxAZjwCE&t=206s) | Specify product, story, format, look, motion, sound and quality checks. An agent may draft the brief, but decisions and facts still come from the user/brand. |
| [4:49–5:59](https://www.youtube.com/watch?v=2moKxAZjwCE&t=289s) | Revise a specific detail and watch again. The examples do not establish a one-prompt quality guarantee or a reliable production time/cost. |
| [6:00–7:15](https://www.youtube.com/watch?v=2moKxAZjwCE&t=360s) | Logo-motion alternatives can reveal a direction before commitment. Here, explore with beats/key poses before producing the selected animation. |
| [7:18–7:49](https://www.youtube.com/watch?v=2moKxAZjwCE&t=438s) | Style vocabulary broadens exploration. A style name still needs a visual reference and brand-specific translation. The transcript does not name the displayed styles; do not invent that list. |

Do not adopt the tutorial's model name, effort setting, subscription recommendation,
fictional-app styling, auto-install suggestion, or claim that the frameworks are equivalent
and universally free. They are source claims/examples, not standing defaults.

## Checked framework facts

Primary documentation checked 2026-11-02. Recheck APIs and licensing for the installed
release when using a framework; the links track current upstream documentation.

- **Remotion:** React compositions derive their image from a frame number. Use
  `useCurrentFrame()` and the composition fps; frame indices start at zero, and nested
  sequences can return local frame time. Use native still/preview/render facilities rather
  than wrapping the project in a separate screenshot exporter.
  [Core idea](https://www.remotion.dev/docs/idea),
  [frame API](https://www.remotion.dev/docs/use-current-frame),
  [still CLI](https://www.remotion.dev/docs/cli/still),
  [render CLI](https://www.remotion.dev/docs/cli/render).
- **HyperFrames:** HeyGen's official repository describes HTML, CSS, media and seekable
  animation rendered to video. Its GSAP contract uses a paused timeline registered in
  `window.__timelines` under the matching `data-composition-id`; explicit tween positions
  and `fromTo()` endpoints support backward/random seeking. Its documented local check
  loop is `lint`, `check`, then `render`; browser checks supplement visual review.
  [Official project](https://github.com/heygen-com/hyperframes),
  [GSAP contract](https://github.com/heygen-com/hyperframes/blob/main/docs/guides/gsap-animation.mdx),
  [render/check guide](https://github.com/heygen-com/hyperframes/blob/main/docs/guides/rendering.mdx).
- **Costs:** Remotion has eligibility-dependent licensing; HyperFrames' repository is
  Apache-2.0. Neither fact promises free cloud rendering, generated assets or third-party
  services. Check the selected release/use case instead of repeating the video's blanket
  cost claim.
  [Remotion license](https://github.com/remotion-dev/remotion/blob/main/packages/core/LICENSE.md),
  [HyperFrames license](https://github.com/heygen-com/hyperframes/blob/main/LICENSE).

## Practical adaptation

1. Keep the requested/established renderer. If undecided, choose for the existing project:
   HTML/canvas with the working Playwright/ffmpeg exporter; Remotion for React/frame-based
   composition; HyperFrames for HTML/seekable timelines. Explain the fit before changing
   stack. This reference is not an installation instruction.
2. Put renderer, source assets, fps, dimensions, duration, export format and acceptance
   checks in the brief. Separate creative rules in `MOTION.md` from version-specific APIs.
3. After the existing still approval, test a representative moving range. Seek to the same
   frame from different directions and compare the visible result; wait for required
   fonts/media before measuring or capturing. Resolve technical failures before full export.
4. Iterate against scene/time-specific notes with a keep-list. Inspect the changed range,
   adjoining transitions and audio, then watch the final exported file before delivery.

This is Karim's adaptation of the video's workflow, checked against the linked docs; it
does not claim that the tutorial itself used still approval or this exact validation loop.
