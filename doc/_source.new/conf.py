
#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'keymap_domain'
]

# templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'Shotgun'
copyright = '2017, Isaac Weaver'
author = 'Isaac Weaver'

version = '1.0.0'
release = '1.0.0'

language = None

exclude_patterns = []

pygments_style = 'sphinx'

todo_include_todos = True

# html_static_path = ['_static']

htmlhelp_basename = 'Shotgundoc'

latex_elements = {

}

latex_documents = [
    (master_doc, 'Shotgun.tex', 'Shotgun Documentation',
     'Isaac Weaver', 'manual'),
]

man_pages = [
    (master_doc, 'shotgun', 'Shotgun Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'Shotgun', 'Shotgun Documentation',
     author, 'Shotgun', 'One line description of project.',
     'Miscellaneous'),
]

intersphinx_mapping = {
    'blender': ('http://docs.blender.org/api/blender_python_api_master/', '../blender_objects.inv')
}
