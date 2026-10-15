---
component: <Name>
lifecycle: requested   # requested | backlog | active | built | deprecated
status:
  requirements: draft  # empty | draft | complete
  design_notes: empty
  pre_dev_research: empty
  usage: empty
owners: { pm: , design: , dev: }
precedents: [ ]        # sibling CRDs read before writing, e.g. MenuRow, Card
---

<!-- AMENDMENT (only while a shipped component is being changed; delete once folded in)
> **Under revision (YYYY-MM-DD):** what is changing and why. Requirements below may be superseded by: …
-->

# <Name>

## 1. Requirements

**Purpose:** why this component exists, in one or two sentences.

**Scope:** what it covers.

**Anatomy:** container · label · leading icon · … (statements below use only these nouns)

### Functional
- **F1** …
### States
- **S1** …
### Behaviour
- **B1** …
### Content
- **C1** …
### Accessibility
- **A1** …
- **A2** [review] …
### Integration
- **I1** …

### Open
- [open] … (build agents stop here and ask)

### Out of scope
- … (belongs to <OtherComponent>)

### Ruled out
- … (who, date, why)

## 2. Design notes
<!-- Written back by design while working. Variant/state changes go into section 1. Do not repeat spacing/visual spec from Figma/tokens. Link the Figma frame. -->

## 3. Pre-dev research
<!-- How the codebase + sibling CRDs already handle this, standards checked, implementation decisions, questions. -->

## 4. Usage guidance
- **Use when:** …
- **Don't use when:** … use <Alternative> instead.

## Decision log
- YYYY-MM-DD: decision. Why.
