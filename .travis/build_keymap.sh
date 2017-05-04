#!/usr/bin/env bash

# Start blender, import the keymap then export it.
# The exported keymap will have the entire keymap so blender can load it on startup.
blender --background --factory-startup --python-expr \
 "import bpy; bpy.ops.wm.keyconfig_import(filepath='shotgun.py'); bpy.ops.wm.keyconfig_export(filepath='temp.py')"

BANNER="# Shotgun keymap. More info at http://shotgun.readthedocs.io
VERSION = '$(git describe --abbrev=0)'

"

printf "${BANNER}" | cat - temp.py > shotgun.py
rm temp.py
