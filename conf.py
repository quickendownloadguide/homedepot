import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Home Depot Credit Card Login'
copyright = '2025, The Home Depot'
author = 'The Home Depot, Inc.'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']

# -- HTML output -------------------------------------------------------------

html_theme = 'furo'
html_logo = 'logo.png'
html_favicon = 'favicon.ico'
html_title = "HomeDepot.com/mycard – Manage Your Home Depot Credit Card Online"
html_short_title = "Home Depot Card Login"
html_show_sourcelink = False

html_theme_options = {
    "light_logo": "logo.png",
    "dark_logo": "logo.png",
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "footer_icons": [],
    "source_repository": None,
    "source_branch": None,
    "source_directory": None,
    'show_powered_by': False,
}

html_css_files = ['custom.css']
