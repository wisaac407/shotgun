#!/usr/bin/env python3

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Contributor(s): Isaac Weaver
#
# ##### END GPL LICENSE BLOCK #####

import subprocess
import requests
import os
import shutil


def main():
    # intersphinx doesn't load it properly from url so we download it here.
    if not os.path.exists('doc/blender_objects.inv'):
        r = requests.get('https://docs.blender.org/api/blender_python_api_master/objects.inv', stream=True)
        with open('doc/blender_objects.inv', 'w') as f:
            f.write(r.content)

    try:
        subprocess.run([
            'blender',
            '--factory-startup',
            '--background',
            '--python',
            'doc/export_keymaps.py'
        ], cwd='doc')

        subprocess.run([
            'sphinx-build',
            'sphinx-in',
            'dist'
        ], cwd='doc')
    finally:
        if os.path.exists('doc/sphinx-in'):
            shutil.rmtree('doc/sphinx-in')

if __name__ == '__main__':
    main()
