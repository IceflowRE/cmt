import sys
from pathlib import Path

import sphinx_rtd_theme

sys.path.insert(0, str(Path('../../').resolve()))

from cmt import static_data

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
]
autodoc_mock_imports = [
    "bpy",
    "bpy_extras",
]
source_suffix = '.rst'
master_doc = 'index'

project = 'Celaria Map Toolkit'
author = 'Iceflower S'
copyright = '2019-present, Iceflower S'
title = project + ' Documentation'
version = static_data.VERSION
release = '0.2.0'

language = None  # english
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'includehidden': True,
}
man_pages = [
    (master_doc, project, title,
     [author], 1)
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'packaging': ('https://packaging.pypa.io/en/latest/', None),
}
