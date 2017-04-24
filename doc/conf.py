
#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

extensions = [
    'sphinx.ext.intersphinx',
    'keymap_domain'
]

master_doc = 'index'

project = 'Shotgun'
copyright = '2017, Isaac Weaver'
author = 'Isaac Weaver'

version = ' - 5ad28c0'
release = ' - 5ad28c0'

intersphinx_mapping = {
    'blender': ('http://docs.blender.org/api/blender_python_api_master/', '../blender_objects.inv')
}
