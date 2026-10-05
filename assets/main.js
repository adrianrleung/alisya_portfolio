function openProject(hash) {
  const panel = document.querySelector(hash);
  if (panel instanceof HTMLDetailsElement && panel.classList.contains("project-panel")) {
    panel.open = true;
  }
}

document.addEventListener("click", (event) => {
  const link = event.target.closest('.project-index a[href^="#project-"]');
  if (link) openProject(link.hash);
});

window.addEventListener("hashchange", () => openProject(window.location.hash));
if (window.location.hash.startsWith("#project-")) openProject(window.location.hash);
