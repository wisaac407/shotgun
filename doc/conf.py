
#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

extensions = [
    'keymap_domain'
]

master_doc = 'index'

project = 'Shotgun'
copyright = '2017, Isaac Weaver'
author = 'Isaac Weaver'

version = 'show
0.1
0.1.1 78c6e19'
release = 'show
0.1
0.1.1 78c6e19'

intersphinx_mapping = {
    'blender': ('http://docs.blender.org/api/blender_python_api_master/', '../blender_objects.inv')
}
