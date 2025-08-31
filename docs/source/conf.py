# conf.py for Metatranscriptomics Workshop

from datetime import datetime

# -- Project info -------------------------------------------------------------
project = "Metatranscriptomics Workshop"
author = "Javad Sadeghi"

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_copybutton',  # adds copy buttons to code blocks
]

# Source file type
source_suffix = ".rst"

# Paths to templates and static files
templates_path = ["_templates"]
html_static_path = ["_static"]

# Exclude build files
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML output -------------------------------------------------------------
html_theme = "sphinx_book_theme"
html_title = project
html_last_updated_fmt = "%b %d, %Y"

# Theme options
html_theme_options = {
    "repository_url": "https://github.com/USERNAME/Metatranscriptomics_Workshop",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "show_toc_level": 2,  # controls how deep the sidebar TOC goes
}
