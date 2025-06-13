# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Home Depot Credit Card Login'
copyright = '2025, The Home Depot'
author = 'The Home Depot, Inc.'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "HomeDepot.com/mycard – Manage Your Home Depot Credit Card Online"

# Optional short title (e.g., for nav bar)
html_short_title = "Home Depot MyCard"

# Favicon (must be placed inside _static or root directory)
html_favicon = 'favicon.ico'

# Theme (use Furo or uncomment another theme like ReadTheDocs if needed)
html_theme = 'furo'

# Hide "View page source" links
html_show_sourcelink = False

# Allow raw HTML in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,  # Furo ignores this, but safe to keep
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
}

# Paths to templates and static files
templates_path = ['_templates']
html_static_path = ['_static']  # Include only if you have favicon, CSS, etc.

# Add extra files like Google verification HTML if needed
# html_extra_path = ['google12345abcde.html']

# Files or directories to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
