*******
Lattice
*******

.. km:module:: lattice

   


---------------
Quick Reference
---------------

+-----------------------------------------------------------------------------+-------------------------------------------------+
|Hotkey                                                                       |Operator                                         |
+=============================================================================+=================================================+
|:km:hk:`Ctrl-A <lattice->Ctrl-A->lattice.select_all>`                        |:func:`blender:bpy.ops.lattice.select_all`       |
+-----------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`A <lattice->A->lattice.select_all>`                                  |:func:`blender:bpy.ops.lattice.select_all`       |
+-----------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-I <lattice->Ctrl-I->lattice.select_all>`                        |:func:`blender:bpy.ops.lattice.select_all`       |
+-----------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <lattice->Ctrl-NUMPAD_PLUS->lattice.select_more>`   |:func:`blender:bpy.ops.lattice.select_more`      |
+-----------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <lattice->Ctrl-NUMPAD_MINUS->lattice.select_less>` |:func:`blender:bpy.ops.lattice.select_less`      |
+-----------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-P <lattice->Ctrl-P->object.vertex_parent_set>`                  |:func:`blender:bpy.ops.object.vertex_parent_set` |
+-----------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-F <lattice->Ctrl-F->lattice.flip>`                              |:func:`blender:bpy.ops.lattice.flip`             |
+-----------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-H <lattice->Ctrl-H->wm.call_menu>`                              |:func:`blender:bpy.ops.wm.call_menu`             |
+-----------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-O <lattice->Shift-O->wm.context_cycle_enum>`                   |:func:`blender:bpy.ops.wm.context_cycle_enum`    |
+-----------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`O <lattice->O->wm.context_toggle_enum>`                              |:func:`blender:bpy.ops.wm.context_toggle_enum`   |
+-----------------------------------------------------------------------------+-------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> lattice.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.lattice.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: A -> lattice.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.lattice.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> lattice.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.lattice.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> lattice.select_more : KEYBOARD -> PRESS

   Select More

   bpy.ops.lattice.select_more()
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> lattice.select_less : KEYBOARD -> PRESS

   Select Less

   bpy.ops.lattice.select_less()
   
   
.. km:hotkeyd:: Ctrl-P -> object.vertex_parent_set : KEYBOARD -> PRESS

   Make Vertex Parent

   bpy.ops.object.vertex_parent_set()
   
   
.. km:hotkeyd:: Ctrl-F -> lattice.flip : KEYBOARD -> PRESS

   Flip (Distortion Free)

   bpy.ops.lattice.flip(axis='U')
   
   
.. km:hotkeyd:: Ctrl-H -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------+
   |Properties: |Values:        |
   +============+===============+
   |Name        |VIEW3D_MT_hook |
   +------------+---------------+
   
   
.. km:hotkeyd:: Shift-O -> wm.context_cycle_enum : KEYBOARD -> PRESS

   Context Enum Cycle

   bpy.ops.wm.context_cycle_enum(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+----------------------------------------+
   |Properties:        |Values:                                 |
   +===================+========================================+
   |Context Attributes |tool_settings.proportional_edit_falloff |
   +-------------------+----------------------------------------+
   |Wrap               |True                                    |
   +-------------------+----------------------------------------+
   
   
.. km:hotkeyd:: O -> wm.context_toggle_enum : KEYBOARD -> PRESS

   Context Toggle Values

   bpy.ops.wm.context_toggle_enum(data_path="", value_1="", value_2="")
   
   
   +-------------------+--------------------------------+
   |Properties:        |Values:                         |
   +===================+================================+
   |Context Attributes |tool_settings.proportional_edit |
   +-------------------+--------------------------------+
   |Value              |DISABLED                        |
   +-------------------+--------------------------------+
   |Value              |ENABLED                         |
   +-------------------+--------------------------------+
   
   
