# Karim Ashraf Portfolio | V2

A standalone, responsive static portfolio. No framework, paid service, database, tracking, or external product data. Nothing is published; this runs locally only.

## Structure

- `index.html` is the home page: hero, Selected work, About, Résumé, AI in the practice, Writing, Contact. Sections are numbered 01 to 06 and must stay sequential.
- Four case studies: `money-fellows.html`, `bluworks.html`, `sharwa.html`, `one-more-thing.html`.
- `styles.css` holds the whole visual system. `script.js` holds the shared nav and footer year behaviour.
- `docs/EVIDENCE-INVENTORY.md` is the source of truth for what is claimed and how it was verified. Read it before changing any copy that carries a number.

## Local preview

```
python -m http.server 4173
```

Then open `http://localhost:4173`. There is no build step.

## Evidence rules

- **The CV is the source of record for numbers.** `Karim_Ashraf_Product_Designer_Resume_2026.pdf`. CV, LinkedIn and portfolio must agree. Verified 2026-08-20.
- **Never add the cumulative "200+ research" claim.** The documented figure is 70+ interviews.
- **Money Fellows shows no product screens.** Business case study and technical work only; screens and flows to be added later once cleared, asset by asset. The 12 files in `assets/money-fellows/` stay unused until then.
- **UXcel-published work is cleared.** Every project on `app.uxcel.com/ux/karimashraf` may appear here the same way Bluworks does. Cite the specific showcase URL on the page.
- **Attribute company facts.** Public product facts (for example Money Fellows circle sizes and regulation) are labelled as the company's own published material, not as Karim's results.
- **Check attribution before adding a project.** Prime Talent Management Hub is AIESEC work, not 1MORETHING. The Jumlaty showcase credits NOMU Group while the CV places JumlatyPro under 1MORETHING, and the page states both.
- **No em dashes anywhere.**

## Before changing anything

Run the checks that have caught real defects here:

```
python -c "import html5lib,io,glob;[print(f,len(html5lib.HTMLParser(strict=False).parse(io.open(f,encoding='utf-8').read()) and 0 or 0)) for f in glob.glob('*.html')]"
```

More practically, after any edit confirm: all five pages parse with zero `html5lib` errors, no horizontal overflow at 1280px and 375px, every `assets/` reference resolves, and no em dashes. New SVG diagrams need a `min-width` and a scrolling container, or their text becomes illegible on a phone.

## Publishing

Not published. Create a repository and publish only after Karim explicitly approves it.
