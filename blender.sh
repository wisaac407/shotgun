#!/bin/sh
# Start blender in default mode and load shotgun. Useful for testing.
blender --factory-startup --python-expr \
    "import bpy; bpy.ops.wm.keyconfig_import(filepath='shotgun.py'); bpy.context.user_preferences.inputs.select_mouse = 'LEFT'"
