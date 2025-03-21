# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ncpol3sdpa'
copyright = '2025, Yann, Alain, Mathis, Nazar, Thomas'
author = 'Yann, Alain, Mathis, Nazar, Thomas'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    # 'sphinx.ext.autosny',
    # 'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = [
'.DS_Store',
]

# Mock imports that might cause issues during documentation building
autodoc_mock_imports = ['cvxpy']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
