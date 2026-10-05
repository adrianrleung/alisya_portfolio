---
name: "Alisya Sofiyuddin — Technical Editorial Portfolio"
description: "A concise three-route engineering portfolio for recruiter scanning."
colors:
  canvas: "#F3F6F8"
  surface: "#FFFFFF"
  ink: "#172735"
  muted: "#4B5E6D"
  rule: "#D4DDE5"
  cobalt: "#2857E8"
  cobalt-soft: "#E3EBF8"
typography:
  display:
    fontFamily: "Sora, sans-serif"
    fontSize: "clamp(3.2rem, 7vw, 6rem)"
    fontWeight: 600
    lineHeight: 0.98
    letterSpacing: "-0.04em"
  title:
    fontFamily: "Sora, sans-serif"
    fontSize: "clamp(1.15rem, 2vw, 1.55rem)"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.02em"
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
  label:
    fontFamily: "Atkinson Hyperlegible, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 700
    lineHeight: 1.2
spacing:
  compact: "0.7rem"
  base: "1rem"
  inset: "1.5rem"
  section: "3rem"
  wide: "2.5rem"
components:
  resume-action:
    backgroundColor: "{colors.cobalt}"
    textColor: "{colors.surface}"
    typography: "{typography.label}"
    padding: "0.55rem 0.9rem"
  linkedin-action:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    padding: "0.55rem 0.9rem"
  site-navigation:
    typography: "{typography.label}"
    padding: "0.6rem 0"
  hero-path:
    typography: "{typography.title}"
    padding: "0.7rem 0"
  project-index-tile:
    backgroundColor: "{colors.surface}"
    typography: "{typography.title}"
    padding: "0.65rem 0.8rem"
  project-panel:
    backgroundColor: "{colors.canvas}"
    typography: "{typography.title}"
    padding: "1rem 0.5rem"
  internship-panel:
    backgroundColor: "{colors.canvas}"
    typography: "{typography.body}"
    padding: "1.2rem 0"
---

# Design System: Technical Editorial Portfolio

## Overview

**Creative North Star: "Three Routes, One Technical Story"**

This portfolio behaves like a concise engineering folio: identity and contact form a fast entry, project and internship evidence have separate routes, and project write-ups unfold only when selected. Editorial scale and a compact navigation system make the material easy to scan without hiding the source explanations.

Cool neutral surfaces, a restrained cobalt accent and fine rules keep attention on Alisya’s original project photography, drawings and plots. Motion is brief and limited to the landing introduction; the visitor controls when project details open.

**Key Characteristics:**
- Three short routes: About, Projects and Internships.
- Sora display type paired with Atkinson Hyperlegible reading text.
- Original engineering images carry the strongest colors and technical proof.
- Cobalt marks primary actions, focus and the current route.

## Colors

The palette is cool and light, with graphite text and one cobalt accent; the dark contact panel provides a clear close to the landing page.

### Primary
- **Cobalt:** the Resume PDF action, current-route marker, keyboard focus and selected name emphasis.
- **Cobalt tint:** a quiet backing field behind the portrait.

### Neutral
- **Canvas:** the cool page ground.
- **Surface:** image tiles and high-contrast text surfaces.
- **Ink:** headings, body text and the landing contact panel.
- **Muted:** supporting degree, date and project metadata.
- **Rule:** fine dividers between navigation, entries and disclosure panels.

### Named Rules
**The One Blue Rule.** Reserve cobalt for actions, focus and current-route state; let project imagery supply the rest of the page’s color.

**The Cool Ground Rule.** Keep the page on a cool near-white ground. Do not drift back to warm paper or pastel panel stacks.

## Typography

**Display Font:** Sora (with a sans-serif fallback)  
**Body Font:** Atkinson Hyperlegible (with a sans-serif fallback)  
**Label/Mono Font:** Atkinson Hyperlegible Bold; no mono face is used.

**Character:** Sora gives names and project titles a crisp geometric silhouette; Atkinson Hyperlegible keeps the long engineering explanations readable. Use display weight for short labels, not paragraphs.

### Hierarchy
- **Display:** Alisya’s name and route headings.
- **Title:** project and internship names, plus project-index labels.
- **Body:** degree and navigation text.
- **Reading:** biography, project write-ups and internship details; keep sustained copy near a 70ch measure.
- **Label:** actions, dates and compact metadata.

### Named Rules
**The Two-Voice Rule.** Use Sora for brief display text and Atkinson Hyperlegible for sustained reading; do not set project paragraphs in the display face.

## Layout

The shared masthead keeps the wordmark, three route links, LinkedIn and Resume PDF together within a centered content width capped at 1280px. The About route pairs the source portrait with Alisya’s name, degree and full source biography, then gives direct paths to Projects and Internships; contact and social details close the landing page.

Projects uses an image-led index above a compact list of native disclosure panels. Index links open and jump to the corresponding project, and only one project panel stays open at a time. Internships keeps the three source roles visible in a readable list. At narrow widths, the hero and project index stack, while the masthead becomes a two-row navigation.

**The Three-Route Rule.** Keep identity/contact, project evidence and work history on their own route; do not recombine them into one long scroll.

## Elevation & Depth

The interface is flat: it uses no box shadows, gradients or glass effects. Depth comes from space, fine rules, a cool tint behind the portrait and the dark contact panel. The one entrance motion is a short vertical arrival for the landing copy and portrait; the rest of the site stays still until the visitor opens a project.

**The One Entrance Rule.** Keep motion to the landing arrival and short control-state transitions; do not add scroll-triggered reveals, parallax or staged page entrances.

## Shapes

Large surfaces remain rectangular with fine neutral rules. The project disclosure indicator is the one recurring circular detail. Photo and engineering-media frames stay rectangular, without masks or decorative borders heavier than the content.

## Components

### Buttons
Resume PDF is the filled primary action; LinkedIn is the outlined secondary action. Both use clear text labels and direct links.
- **Resume PDF:** cobalt fill, white text and a square silhouette.
- **LinkedIn:** transparent ground, ink text and a fine neutral outline.
- **Hover / Focus:** hover inverts to ink; keyboard focus uses a visible cobalt outline.

### Cards / Containers
Project-index tiles pair original images with a short title strip. Their desktop spans vary; on mobile they become a single compact list. Project details use the browser’s native disclosure control: summaries remain visible, the full source explanation opens on request, and named panels are mutually exclusive. Paired project images stay side by side on desktop and stack only on narrow screens. Detail figures stay at or below their source resolution, are centered, and are capped to a readable width and viewport height so small originals are not enlarged to fill the page.
- **Background:** surface for image tiles; canvas for project and internship reading areas.
- **Border:** fine neutral rules, without card shadows.
- **Internships:** source company marks align beside the original role and visible details.

### Navigation
The shared sticky masthead marks the current route with a cobalt underline. About, Projects and Internships are direct page links; LinkedIn opens Alisya’s profile. Resume PDF stays visible in the masthead, while email and GitHub remain on the About page.

## Do's and Don'ts

### Do:
- **Do** keep the About, Projects and Internships routes distinct and quick to reach.
- **Do** use cobalt for primary action, focus and current-route state.
- **Do** let original project photographs and engineering media provide visual texture.
- **Do** keep project details user-controlled and preserve reduced-motion preferences.

### Don't:
- **Don't** return to warm-paper grounds, pastel panel stacks or comic display lettering.
- **Don't** add parallax, scroll-driven reveals, long page transitions or autoplay.
- **Don't** substitute gradients, shadows or fabricated diagrams for real project media.
