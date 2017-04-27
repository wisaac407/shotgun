#!/bin/sh

# Prevent blender from overwrite any existing shotgun keymap
SHOTGUN=$(mktemp)
cp shotgun.py ${SHOTGUN}

# Start blender in default mode and load shotgun. Useful for testing.
blender $1 --factory-startup --python-expr \
    "import bpy; bpy.ops.wm.keyconfig_import(filepath='${SHOTGUN}'); bpy.context.user_preferences.inputs.select_mouse = 'LEFT'"

rm ${SHOTGUN}
