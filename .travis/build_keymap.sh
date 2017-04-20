#!/usr/bin/env bash

# Start blender, import the keymap then export it.
# The exported keymap will have the entire keymap so blender can load it on startup.
blender --background --factory-startup --python-expr \
 "import bpy; bpy.ops.wm.keyconfig_import(filepath='shotgun.py'); bpy.ops.wm.keyconfig_export(filepath='shotgun.py')"

