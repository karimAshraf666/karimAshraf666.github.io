# Platforms & Tools Referenced

Every platform mentioned across the three videos, their descriptions and linked pages,
with what it's used for. **Source** = who mentioned it. Items marked *(added)* weren't in
the videos; I added them as useful equivalents.


## Design inspiration & reference research

| Platform | URL | Use it for | Source | Cost / access |
|---|---|---|---|---|
| **Savee** | savee.com | Finding beautiful reference designs (posters, graphics, layouts) to feed design-loop. Save or screenshot the piece. | Jack Roberts | Free account |
| **Refero** | refero.design | 2,000+ AI-readable design systems / styles, 120k+ real product screens and user flows. Grab a style URL and give it to Claude. Also has an **MCP server** (`https://api.refero.design/mcp`) and a **skill** (`referodesign/refero_skill`). | Jack Roberts | Browsing free; MCP needs a paid plan |
| **Mobbin** *(added)* | mobbin.com | Real app/web screen patterns, alternative to Refero screens | n/a | Freemium |
| Example sites used as gold standards | duolingo.com, mercury.com, Vox YouTube explainers | Jack's level 2 (Duolingo-style site) and level 3 (Vox-style motion) references; Mercury praised on Refero | Jack Roberts | n/a |

## Image, video & audio generation

| Platform | URL | Use it for | Source | Cost / access |
|---|---|---|---|---|
| **Higgsfield** | higgsfield.ai | One account for many image + video models. Connect to Claude via **MCP or CLI** so Claude generates custom graphics, characters, animated backgrounds during builds. | Jack Roberts | Paid credits |
| **kie.ai** | kie.ai | "OpenRouter for image/video models", one API key for many models. ScrollCraft uses it (`KIE_AI_API_KEY`) to generate images, turn them into video and stitch them. Logs show every generation. | Nate Herk | Paid credits; optional (own photos = free) |
| **Fish Audio** | fish.audio | Voiceover / narration: ~3-7x cheaper than alternatives, huge voice library, **emotion tags + auto-tag**, S2.1 model, sound effects. Connect via API key (Developer → API keys) for Claude to generate narration. | Jack Roberts | Paid; free tier |

## Claude, agents & build tooling

| Platform | URL | Use it for | Source |
|---|---|---|---|
| **Claude / Claude Code (desktop)** | claude.ai | Building everything; skills invoked with `/skill-name`; subagents for critic loops | All |
| **Claude Design** | claude.ai | Claude's design surface; "added design-system constraints within 2 months of launch" | Jack, Cassie |
| **GitHub: nateherkai/scroll-craft** | github.com/nateherkai/scroll-craft | ScrollCraft skill (MIT). Needs Node 18+, full ffmpeg, playwright-core + Chrome | Nate Herk |
| **Playwright + Chrome** | playwright.dev | Headless screenshots for visual verification of builds | Nate Herk (ScrollCraft) |
| **ffmpeg** (full build) | ffmpeg.org | Video encoding for scroll-scrubbed video | Nate Herk (ScrollCraft) |
| **Figma / Figma Make** | figma.com | Component-level design stays on the canvas; Figma Make for prototyping states | Cassie Groos |
| **Storybook** | storybook.js.org | Documents the component API (dev-owned), so the CRD doesn't duplicate it | Cassie Groos |
| **MCP servers / CLIs for design systems** | n/a | Next step for making a system queryable by agents | Cassie Groos |
| **Vercel** | vercel.com | Cited as building on components (context); also your deploy target | Cassie Groos |
| **Hostinger VPS** | hostinger.com | Hosting Claude Code on a VPS | Nate Herk |
| **Glaido** | glaido.com | Voice-to-text dictation for prompting faster | Jack Roberts & Nate Herk |

## Knowledge, communities & learning

| Platform | URL | What's there | Source | Access |
|---|---|---|---|---|
| **Notion: Design DNA page** | app.notion.com/p/Design-DNA-…3bee8d6b… | Full Design DNA method + prompt (rebuilt here as the `design-dna` skill) | Jack Roberts | Public |
| **Skool: AI Automation Vault** | skool.com/ai-automation-vault | Jack's free community: **design-loop skill original**, Claude Code / Cowork / AntiGravity / design resources | Jack Roberts | Free, needs a Skool account |
| **Skool: AI Automations by Jack** | skool.com/aiautomationsbyjack | Paid: Claude Code OS, "design OS", website design system skill, anti-slop copy system, Claude design system course | Jack Roberts | $87/mo |
| **Skool: AI Automation Society** | skool.com/ai-automation-society | Nate's free community: ScrollCraft post + all his free YouTube resources (classroom → All YouTube resources → AI skills) | Nate Herk | Free, needs account |
| **Design Systems Collective** (Medium) | designsystemscollective.com | Cassie's CRD article "Probabilistic isn't a dirty word" (Aug 2026) | Cassie Groos | Free |
| **Hatch Conference** | hatchconference.com | Design leadership conference, Berlin (Sept 2027 at Tempelhof); invite-only | Cassie Groos | Apply |
| **The Question podcast** (Ben Callahan) | n/a | Ep. 075: Cassie on the design system identity crisis | search result | Free |
| **Wikipedia: Signs of AI writing** | en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | Basis of the humanizer skill / anti-slop copy | Jack (as a principle) | Free |
| **blader/humanizer** | github.com/blader/humanizer | Anti-AI-writing skill (MIT), 29+ patterns | *(added, matches Jack's description)* | Free |
| People cited for design system thinking | Brad Frost, Nathan Curtis, Alla Kholmatova, TJ Pitre (Figma) | Definitions and the "AI gets you 80-85%" figure | Cassie Groos | n/a |
