from __future__ import annotations

from datetime import date


project = "MedUMM"
author = "MedUMM contributors"
copyright = f"{date.today().year}, {author}"
release = "1.2.0"
version = "1.2"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinx_sitemap",
]

source_suffix = {".md": "markdown"}
master_doc = "index"
language = "zh_CN"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
suppress_warnings = ["myst.xref_missing"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "tasklist",
]
myst_heading_anchors = 3

html_theme = "sphinx_rtd_theme"
html_title = "MedUMM 文档"
html_logo = "_static/medumm-mark.svg"
html_favicon = "_static/medumm-mark.svg"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {
    "logo_only": False,
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
}
html_context = {
    "display_github": True,
    "github_user": "lixiangcog",
    "github_repo": "MedUMM-Docs",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
html_baseurl = "https://medumm-docs.readthedocs.io/"

copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

sitemap_url_scheme = "{link}"
