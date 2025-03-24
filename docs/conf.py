# Configuration file for the Sphinx documentation builder
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Literal, Optional, Tuple, Union

# Add project root to path using Path for better path handling
project_root = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(project_root))

# -- MyST Compatibility Layer ------------------------------------------------
# Handle MyST compatibility with newer Sphinx versions (8.x+)
suppress_warnings = ["myst.footnote"]
myst_footnote_transition = True
myst_dmath_double_inline = True

# -- Project information -----------------------------------------------------
project = "Eidosian Type Forge"
copyright = f"{datetime.now().year}, Lloyd Handyside"
author = "Lloyd Handyside"
version = "0.1.0"  # Will be replaced with type_forge.__version__
release = "Beta"  # Will be replaced with type_forge.__version__

# -- General configuration ---------------------------------------------------
extensions: List[str] = [
    # Core Sphinx extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.duration",
    "sphinx.ext.githubpages",
    "sphinx.ext.graphviz",
    "sphinx.ext.ifconfig",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # Markdown support
    "myst_parser",
    "myst_nb",
    # Auto API documentation
    "autoapi.extension",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.autodoc_pydantic",
    # Additional neat features
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinxext.opengraph",
    "sphinxcontrib.mermaid",
    # Add autosectionlabel for internal links
    "sphinx.ext.autosectionlabel",
]

# -- Markdown Configuration --------------------------------------------------
source_suffix: Dict[str, str] = {
    ".rst": "restructuredtext",
    ".md": "markdown",
    ".ipynb": "myst-nb",
}

# MyST markdown parser settings
myst_enable_extensions: List[str] = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_heading_anchors: int = 4  # Generate anchors for h1-h4

# -- Napoleon Configuration --------------------------------------------------
napoleon_google_docstring: bool = True
napoleon_numpy_docstring: bool = True
napoleon_include_init_with_doc: bool = True
napoleon_include_private_with_doc: bool = False
napoleon_include_special_with_doc: bool = True
napoleon_use_admonition_for_examples: bool = True
napoleon_use_admonition_for_notes: bool = True
napoleon_use_admonition_for_references: bool = True
napoleon_use_ivar: bool = True
napoleon_use_param: bool = True
napoleon_use_rtype: bool = True
napoleon_use_keyword: bool = True
napoleon_custom_sections: List[str] = ["Attributes", "Methods", "Examples"]

# -- AutoAPI Configuration ---------------------------------------------------
autoapi_dirs: List[str] = ["../type_forge"]
autoapi_template_dir: str = "_templates/autoapi"
autoapi_options: List[str] = [
    "members",
    "undoc-members",
    "private-members",
    "special-members",
    "inherited-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]
autoapi_python_class_content: str = "both"
autoapi_member_order: str = "groupwise"
autoapi_keep_files: bool = True
autoapi_add_toctree_entry: bool = True

# -- HTML output configuration ------------------------------------------------
html_theme: str = "furo"
html_favicon: str = "_static/favicon.ico"
html_logo: str = "_static/logo.png"
html_static_path: List[str] = ["_static"]
html_css_files: List[str] = ["custom.css"]
html_theme_options: Dict[
    str,
    Union[bool, str, Dict[str, str], List[Dict[str, str]]],
] = {
    "sidebar_hide_name": False,
    "light_css_variables": {
        "color-brand-primary": "#8A2BE2",  # Purple matching Eidosian theme
        "color-brand-content": "#8A2BE2",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Ace1928/type_forge",
            "html": '<i class="fab fa-github fa-2x"></i>',
            "class": "",
        },
    ],
    "navigation_with_keys": True,
    "announcement": "Type Forge is currently in beta",
}

# -- Additional configuration ------------------------------------------------
# Generate internal links to headers
autosectionlabel_prefix_document: bool = True
autosectionlabel_maxdepth: int = 3

# Show typehints in documentation
autodoc_typehints: Literal["description", "signature", "none"] = "description"
autodoc_typehints_format: Literal["short", "fully-qualified"] = "short"
typehints_fully_qualified: bool = False
typehints_document_rtype: bool = True

# Pydantic model documentation
autodoc_pydantic_model_show_json: bool = True
autodoc_pydantic_field_list_validators: bool = True

# Add any paths that contain templates
templates_path: List[str] = ["_templates"]
exclude_patterns: List[str] = ["_build", "Thumbs.db", ".DS_Store"]

# Enable todo notes in documentation
todo_include_todos: bool = True

# Set up intersphinx mapping for external references
intersphinx_mapping: Dict[str, Tuple[str, Optional[str]]] = {
    "python": ("https://docs.python.org/3", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

# Enable linkcheck builder
linkcheck_ignore: List[str] = []
