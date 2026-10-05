const projects = document.querySelector(".projects-section");
const page = projects?.closest(".projects-page");
const index = projects?.querySelector(".project-index");
const panels = [...(projects?.querySelectorAll(".project-panel") ?? [])];
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

function projectFor(hash) {
  return panels.find((panel) => `#${panel.id}` === hash);
}

function indexLinkFor(panel) {
  return index?.querySelector(`a[href="#${panel.id}"]`);
}

function focusImageFor(panel) {
  let image = panel.querySelector(".project-focus-image");
  if (!image) {
    image = indexLinkFor(panel)?.querySelector("img")?.cloneNode();
    if (!image) return null;
    image.className = "project-focus-image";
    image.alt = "";
    image.loading = "eager";
    panel.querySelector("summary").prepend(image);
  }
  return image;
}

function reveal(panel) {
  panel.open = true;
  projects.classList.add("is-reading");
  page.classList.add("is-reading");
}

function closeProjects() {
  panels.forEach((panel) => { panel.open = false; });
  projects.classList.remove("is-reading");
  page.classList.remove("is-reading");
}

function transitionArt(from, to, update) {
  page.classList.add("is-opening");
  from.style.viewTransitionName = "project-art";
  const transition = document.startViewTransition(() => {
    from.style.viewTransitionName = "none";
    to.style.viewTransitionName = "project-art";
    update();
  });
  return transition.finished.catch(() => {}).then(() => {
    from.style.removeProperty("view-transition-name");
    to.style.removeProperty("view-transition-name");
    page.classList.remove("is-opening");
  });
}

function syncLocation() {
  if (!projects) return;
  const panel = projectFor(window.location.hash);
  if (panel) {
    focusImageFor(panel);
    reveal(panel);
    requestAnimationFrame(() => panel.querySelector("summary").scrollIntoView({ block: "start" }));
  } else {
    closeProjects();
  }
}

document.addEventListener("click", async (event) => {
  const link = event.target.closest('.project-index a[href^="#project-"]');
  if (link) {
    const panel = projectFor(link.hash);
    if (!panel) return;
    const image = focusImageFor(panel);
    if (document.startViewTransition && !reducedMotion.matches && image) {
      event.preventDefault();
      await image.decode().catch(() => {});
      const source = link.querySelector("img");
      await transitionArt(source, image, () => {
        reveal(panel);
        history.pushState(null, "", link.hash);
      });
      panel.querySelector("summary").focus({ preventScroll: true });
    } else {
      reveal(panel);
    }
    return;
  }

  const back = event.target.closest(".project-back");
  if (!back) return;
  const panel = panels.find((candidate) => candidate.open);
  const linkBackTo = panel && indexLinkFor(panel);
  if (!panel) return;
  if (document.startViewTransition && !reducedMotion.matches && linkBackTo) {
    event.preventDefault();
    const source = focusImageFor(panel);
    const destination = linkBackTo.querySelector("img");
    await transitionArt(source, destination, () => {
      closeProjects();
      history.pushState(null, "", back.hash);
    });
    linkBackTo.focus({ preventScroll: true });
    index.scrollIntoView({ behavior: "smooth", block: "start" });
  } else {
    closeProjects();
  }
});

panels.forEach((panel) => panel.addEventListener("toggle", () => {
  if (panel.open) {
    projects.classList.add("is-reading");
    page.classList.add("is-reading");
    if (window.location.hash !== `#${panel.id}`) history.replaceState(null, "", `#${panel.id}`);
  } else if (!panels.some((candidate) => candidate.open)) {
    projects.classList.remove("is-reading");
    page.classList.remove("is-reading");
    if (window.location.hash === `#${panel.id}`) history.replaceState(null, "", "#project-index");
    indexLinkFor(panel)?.focus({ preventScroll: true });
  }
}));

window.addEventListener("hashchange", syncLocation);
window.addEventListener("popstate", syncLocation);
if (window.location.hash) syncLocation();
