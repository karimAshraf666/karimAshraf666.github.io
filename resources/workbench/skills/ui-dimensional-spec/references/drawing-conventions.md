# Drawing conventions

Use only the codes the component needs:

| Code | Meaning |
| --- | --- |
| S1… | Spacing/padding/gap; name semantic role |
| H1… / W1… | Height/width; specify fixed, minimum or maximum |
| Z1… / I1… | Square control size / icon bounds |
| B1… / R1… | Border thickness / radius |
| Y1, BL1, SP1, E1 | Shadow offset, blur, spread, elevation role |
| V1, MH1 / T1 | Viewport, maximum height / interactive target |

Each row: code | role | value/unit or rule | provenance | status. Provenance is token path, Figma node/property, source file:line or measurement environment. Status is declared, computed, observed or TBD. Raster pixels and font metrics are not automatically CSS geometry.

Place dimension lines outside objects with extension lines and readable labels. Use a zoomed detail instead of overlapping annotations. Show layer stacks only when they clarify borders, shadows, hit targets or nested surfaces.

Prefer relationships to duplicated numbers. A symmetric fixed-height row may use min-height = 2*S1 + H3; wrapping may require an inequality. R2 = R1 - B1 - S6 applies only to concentric inset geometry and must remain nonnegative. Verify assumptions.

Screenshot-only example: S1 | top inset | approximately 16 raster px | supplied screenshot, scale unverified | observed. The CSS/token value remains TBD. Resolve it before calling an implementation-dependent spec ready.

Acceptance: every code resolves once; every value has provenance; formulas compute correctly; labels do not collide; HUG/FILL behavior is explicit; tested viewports are listed; untested breakpoints and unknowns remain visible.
