# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Add the project root directory to Python's path
import os
import sys

# Configure paths and do imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import generate_docs

sys.path.insert(0, os.path.abspath("../../"))
sys.path.insert(0, os.path.abspath("../../src/"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ncpol3sdpa"
copyright = "2025, Alain, Mathis, Nazar, Thomas, Yann"
author = "Alain, Mathis, Nazar, Thomas, Yann"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",  # Support for Google/NumPy style docstrings
    "sphinx.ext.viewcode",  # Link documentation to source code
    "sphinx.ext.intersphinx",  # Link to other documentation
    "sphinx.ext.mathjax",  # For math notation
]

# Configure autodoc
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

# Generate API documentation automatically
autosummary_generate = True
autodoc_member_order = "bysource"

# Create a directory for autosummary generated templates
if not os.path.exists(os.path.join(os.path.dirname(__file__), "api")):
    os.makedirs(os.path.join(os.path.dirname(__file__), "api"))

templates_path = ["_templates"]
exclude_patterns = [
    ".DS_Store",
]

# Mock imports that might cause issues during documentation building
autodoc_mock_imports = [
    "cvxpy",
    "mosek",
    "sympy",
    "numpy",
    "numpy.typing",
    "typing",
    "scipy",
    "scipy.sparse",
    "scipy._lib",
    "scipy._lib._pep440",
]

# Intersphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "sympy": ("https://docs.sympy.org/latest/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Use sphinx-rtd-theme

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
    "titles_only": False,
}

html_title = f"{project} {release} Documentation"
html_show_sourcelink = True

# -- Options for LaTeX output ------------------------------------------------


# -- Script to generate the documentation -----------------------------------

print("Generating documentation...")

# Run the generate_docs.py script to create RST files for modules
generate_docs.generate_RST_files()
print(".rst files generated")
