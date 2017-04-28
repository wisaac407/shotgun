
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

version = ' - efc8e98'
release = ' - efc8e98'

intersphinx_mapping = {
    'blender': ('http://docs.blender.org/api/blender_python_api_master/', None)
}
