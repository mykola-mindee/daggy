"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Project information -----------------------------------------------------

from datetime import datetime

import {{cookiecutter.module_name}}

master_doc = "index"
project = "{{cookiecutter.project_name}}"
copyright = f"{datetime.now().year}, Mindee"
author = "Mindee"
version = release = {{cookiecutter.module_name}}.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinxemoji.sphinxemoji",  # cf. https://sphinxemojicodes.readthedocs.io/en/stable/
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_tabs.tabs",
]

napoleon_use_param = False
coverage_show_missing_items = True
# Same order as in the source instead of alphabetical
autodoc_member_order = "bysource"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"
