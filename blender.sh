#!/bin/sh

# Start blender in default mode and load shotgun. Useful for testing.
blender $1 --factory-startup --python-expr \
    "import bpy; bpy.ops.wm.keyconfig_activate(filepath='shotgun.py'); bpy.context.user_preferences.inputs.select_mouse = 'LEFT'"
