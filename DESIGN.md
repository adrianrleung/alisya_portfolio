---
name: "Alisya Sofiyuddin — Blueprint Projects Portfolio"
description: "A recruiter-friendly portfolio with a blueprint drawing board for project selection."
colors:
  canvas: "#081D2E"
  surface: "#102C42"
  ink: "#EDF4F8"
  muted: "#B4C6D4"
  rule: "rgba(143, 181, 204, 0.32)"
  blue: "#1F659A"
  blue-soft: "#103655"
  reading-surface: "#F1F5F7"
typography:
  display:
    fontFamily: "Sora, sans-serif"
    fontWeight: 600
    lineHeight: 0.98
    letterSpacing: "-0.04em"
  body:
    fontFamily: "Atkinson Hyperlegible, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  reading:
    fontFamily: "Atkinson Hyperlegible, sans-serif"
    fontSize: "1.04rem"
    fontWeight: 400
    lineHeight: 1.72
components:
  taskbar:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.rule}"
  project-board:
    backgroundColor: "{colors.canvas}"
    columns: 3
    rows: 3
    desktopScroll: false
  project-drawing:
    source: "existing project thumbnail"
    treatment: "white image contours; transparent blue negative space"
  project-reading:
    backgroundColor: "{colors.reading-surface}"
    interaction: "native, exclusive details"
  contact-close:
    backgroundColor: "#0C2A41"
    border: "1px solid {colors.rule}"
---

# Design System: Blueprint Projects Portfolio

## Overview

**Creative North Star: “A Blueprint Board That Opens Into the Work.”**

The site has three direct routes: About, Projects and Internships. About and Internships use a calm, flat deep-blue field. Projects alone carries the blueprint grid and drawing language. Keep the shared taskbar and outlined contact close visible, and preserve the original copy, links, media and order.

## Colors and type

The canvas is deep navy, with pale text and fine blue-gray rules. The Projects board uses a subtle grid over the same blue field. Existing project thumbnails are edge-filtered into white contours; the transparent areas reveal the board beneath. Do not add diagram labels, specifications or other invented engineering content.

Use Sora for headings and short titles. Use Atkinson Hyperlegible for navigation, metadata and sustained reading. Expanded project copy uses a light surface for contrast.

## Layout

On desktop, the Projects route shows one framed, 3×3 board containing all nine projects in their original order. Each drawing and real title is an equally clear link. The overview fits without page scrolling. Do not add a second list, separate cards or a large hero above the board.

Selecting a drawing uses the browser’s View Transitions API to move its image into the expanded project view. That view reveals the unchanged project title, dates, explanation and original media; it may scroll. A single return link brings visitors back to the board. Native `details` keeps the panels exclusive and supports direct project fragments. Under reduced motion or without View Transitions, open the same content without the animation.

Mobile keeps the drawings legible in a two-column board and permits vertical scrolling. Expanded reading content remains scrollable at every size.

## Surfaces and behavior

- **About:** flat blue field, existing biography and portrait, direct paths to Projects and Internships. The contact panel remains outlined; no blueprint grid.
- **Internships:** flat blue field with the existing three roles and their original details and logos. Keep the taskbar and entry separators; no blueprint grid.
- **Taskbar:** retain all route, LinkedIn and résumé links, current-page state, focus visibility and responsive behavior.
- **Media:** keep all original image assets and alt text; drawings in the board are decorative because each link’s visible project title names its destination.
- **Motion:** the drawing-to-reading transition is optional, brief and disabled for `prefers-reduced-motion`.

## Do / don’t

- **Do** keep all nine projects, their order, actual titles and full write-ups.
- **Do** use only existing images as drawing sources and keep their negative space transparent.
- **Do** preserve keyboard access, direct fragments, mobile scrolling and all contact targets.
- **Don’t** add dependencies, fabricated annotations, new claims, duplicate project lists or blueprint treatment to About and Internships.
