from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import subprocess

ROOT = Path(__file__).parent
PAGES = ("index.html", "projects.html", "internships.html")


class Site(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.refs, self.project_links = [], [], []
        self.project_panels, self.internship_panels, self.current_pages = [], [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for name in ("href", "src"):
            if attrs.get(name):
                self.refs.append((name, attrs[name]))
        if tag == "a" and "index-tile" in attrs.get("class", "").split() and attrs.get("href", "").startswith("#project-"):
            self.project_links.append(attrs["href"][1:])
        if tag == "details" and "project-panel" in attrs.get("class", ""):
            self.project_panels.append(attrs)
        if tag == "details" and "internship-panel" in attrs.get("class", ""):
            self.internship_panels.append(attrs)
        if tag == "a" and attrs.get("aria-current") == "page":
            self.current_pages.append(attrs.get("href"))


def parse(path):
    parser = Site()
    parser.feed(path.read_text())
    assert len(parser.ids) == len(set(parser.ids)), f"duplicate IDs in {path.name}"
    return parser


sites = {name: parse(ROOT / name) for name in PAGES}

for name, site in sites.items():
    for kind, ref in site.refs:
        if ref.startswith(("https://", "http://", "mailto:", "tel:")):
            continue
        parsed = urlsplit(ref)
        target = ROOT / parsed.path if parsed.path else ROOT / name
        assert target.is_file(), f"missing local file in {name}: {ref}"
        if parsed.fragment:
            target_site = sites.get(target.name) or parse(target)
            assert parsed.fragment in target_site.ids, f"missing anchor in {name}: {ref}"

projects = sites["projects.html"]
assert len(projects.project_links) == 9, "project index must link all nine projects"
assert len(set(projects.project_links)) == 9, "project index links must be unique"
assert len(projects.project_panels) == 9, "all nine project details must be present"
assert all("open" not in panel for panel in projects.project_panels), "projects should start collapsed"
assert all(panel.get("name") == "projects" for panel in projects.project_panels), "project panels should open one at a time"
assert set(projects.project_links) == {panel["id"] for panel in projects.project_panels}
project_html = (ROOT / "projects.html").read_text()
assert "Conveyor Belt Drivetrain" in project_html, "use the authorized corrected title"
assert "Conveyor Belt Drivtrain" not in project_html, "do not publish the source typo"
predistortion_pair = project_html.split('class="media-grid predistortion-images">', 1)[1].split("</div>", 1)[0]
assert "591247_e87820e6a8484298b628c5db6a3cf3fc~mv2.png" in predistortion_pair
assert "591247_30bb774ff5f74f79b20e94f578534f69~mv2.png" in predistortion_pair
assert project_html.index("Photosensitive Resin") > project_html.index("591247_30bb774ff5f74f79b20e94f578534f69~mv2.png")
assert len(sites["internships.html"].internship_panels) == 3, "all internship details must be present"
assert all("open" in panel for panel in sites["internships.html"].internship_panels), "internship details should be immediately visible"

for name, site in sites.items():
    assert site.current_pages, f"missing current-page navigation state in {name}"
    assert any(ref == "./projects.html" for kind, ref in site.refs if kind == "href"), f"missing projects route in {name}"
    assert any(ref == "./internships.html" for kind, ref in site.refs if kind == "href"), f"missing internships route in {name}"
    assert any(ref == "https://www.linkedin.com/in/nawal-alisya-mohd-sofiyuddin-039b1524b" for kind, ref in site.refs if kind == "href"), f"missing LinkedIn action in {name}"

home = (ROOT / "index.html").read_text()
assert "alisya.sofiyuddin23@imperial.ac.uk" in home
assert "github.com/n-sya?tab=repositories" in home
assert "linkedin.com/in/nawal-alisya-mohd-sofiyuddin-039b1524b" in home

images = {
    ref.removeprefix("./")
    for site in sites.values()
    for kind, ref in site.refs
    if kind == "src" and ref.startswith("./assets/images/")
}
manifest = set(json.loads((ROOT / "assets/source-media.json").read_text())["assets"])
assert images == manifest, "every sourced image should be used"
subprocess.run(["node", "--check", str(ROOT / "assets/main.js")], check=True)
print(f"OK: {len(images)} source images, 9 project accordions, 3 internship entries, and all local links")
