---
version: 1
slug: "projects-html"
primary_target: "projects.html"
related_targets: []
---

## Direction contract

THESIS: Make Projects a single rectangular blueprint board, not a styled project list. A recruiter sees all nine project subjects at once on desktop and can identify each before choosing it.

OWN-WORLD: Keep the site’s deep-blue field. Limit the blueprint grid, rulework and measured line language to Projects. Render contours derived from the existing project images as white strokes with transparent blue negative space; do not add invented engineering annotations. About and Internships use a calm, flat blue field, retaining the outlined masthead and contact/footer close.

STORY: The board is the first view and the work itself leads. Selecting a drawing zooms it into an extended, readable view containing that project’s original explanation and media. Keep the native, mutually exclusive details, direct fragments, and all nine projects in source order. The expanded reading view may scroll; the desktop overview may not. Let mobile reflow and scroll rather than make the drawings illegible.

FIRST VIEWPORT: Beneath the shared taskbar, a thin-framed blue board fills the remaining desktop viewport. Nine image-derived white-line drawings and their real project titles sit in a clear 3×3 register. No cards, duplicate lists, fabricated labels, or page scroll appear before selection.

FORM: User-pinned Blueprint experience; no concept tournament. Use an SVG edge filter on the existing thumbnail images and the native View Transitions API to morph the selected drawing into its inline detail state. Provide a no-motion/native-details fallback, keyboard access, direct-hash opening, and a clear return to the board.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
