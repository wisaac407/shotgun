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
import sys
import shutil
import argparse


def download_inv():
    with open('doc/blender_objects.inv', 'wb') as f:
        print('Downloading inventory file:')
        r = requests.get('https://docs.blender.org/api/blender_python_api_master/objects.inv', stream=True)
        for data in r.iter_content(chunk_size=4096):
            f.write(data)
            print('.', end='', flush=True)
        print('Done')


def parse_args(args):
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--clean', help='Clean generated files', action='store_true')
    parser.add_argument('-f', '--full-clean',
                        help='Same as "--clean" except it removes the bpy doc inventory', action='store_true')
    parser.add_argument('-r', '--rebuild', help='Fresh rebuild of all docs', action='store_true')
    parser.add_argument('-d', '--download', help='Re-download bpy doc inventory', action='store_true')
    parser.add_argument('--keep-source', help='Keep the generated .rst files', action='store_true')
    parser.add_argument('--skip-export', help='Skip exporting the keymaps from blender', action='store_true')
    parser.add_argument('--skip-sphinx', help='Skip generating the final html documents', action='store_true')

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])

    if args.clean or args.rebuild or args.full_clean:
        # Clean generated output files
        if os.path.exists('doc/dist'):
            shutil.rmtree('doc/dist')

    if args.clean or args.full_clean:
        if os.path.exists('doc/_source'):
            shutil.rmtree('doc/_source')

    if args.full_clean:
        if os.path.exists('doc/blender_objects.inv'):
            os.remove('doc/blender_objects.inv')
        sys.exit(0)

    if args.clean:
        sys.exit(0)

    # intersphinx doesn't load it properly from url so we download it here.
    if not os.path.exists('doc/blender_objects.inv') or args.download:
        download_inv()

    try:
        if not args.skip_export:
            subprocess.run([
                'blender',
                '--factory-startup',
                '--background',
                '--python',
                'doc/export_keymaps.py'
            ], cwd='doc')

        if not args.skip_sphinx:
            subprocess.run([
                'sphinx-build',
                '_source',
                'dist'
            ], cwd='doc')
    finally:
        # Don't delete the source if we're not running sphinx or if --keep-source flag is active
        if not (args.keep_source or args.skip_sphinx) and os.path.exists('doc/_source'):
            shutil.rmtree('doc/_source')

if __name__ == '__main__':
    main()
