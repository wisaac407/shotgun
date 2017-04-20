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
|:km:hk:`Shift-O <lattice->Shift-O->wm.context_cycle_enum>`                   |:func:`blender:bpy.ops.wm.context_cycle_enum`    |
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

.. km:hotkey:: Ctrl-A -> lattice.select_all

   (De)select All

   bpy.ops.lattice.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Shift-O -> wm.context_cycle_enum

   Context Enum Cycle

   bpy.ops.wm.context_cycle_enum(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+----------------------------------------+
   |Properties:        |Values:                                 |
   +===================+========================================+
   |Context Attributes |tool_settings.proportional_edit_falloff |
   +-------------------+----------------------------------------+
   
   
.. km:hotkey:: A -> lattice.select_all

   (De)select All

   bpy.ops.lattice.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-I -> lattice.select_all

   (De)select All

   bpy.ops.lattice.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-NUMPAD_PLUS -> lattice.select_more

   Select More

   bpy.ops.lattice.select_more()
   
   
.. km:hotkey:: Ctrl-NUMPAD_MINUS -> lattice.select_less

   Select Less

   bpy.ops.lattice.select_less()
   
   
.. km:hotkey:: Ctrl-P -> object.vertex_parent_set

   Make Vertex Parent

   bpy.ops.object.vertex_parent_set()
   
   
.. km:hotkey:: Ctrl-F -> lattice.flip

   Flip (Distortion Free)

   bpy.ops.lattice.flip(axis='U')
   
   
.. km:hotkey:: Ctrl-H -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------+
   |Properties: |Values:        |
   +============+===============+
   |Name        |VIEW3D_MT_hook |
   +------------+---------------+
   
   
.. km:hotkey:: Shift-O -> wm.context_cycle_enum

   Context Enum Cycle

   bpy.ops.wm.context_cycle_enum(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+----------------------------------------+
   |Properties:        |Values:                                 |
   +===================+========================================+
   |Context Attributes |tool_settings.proportional_edit_falloff |
   +-------------------+----------------------------------------+
   |Wrap               |True                                    |
   +-------------------+----------------------------------------+
   
   
.. km:hotkey:: O -> wm.context_toggle_enum

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
   
   
