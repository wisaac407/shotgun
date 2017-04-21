********
Particle
********

.. km:module:: particle

   


---------------
Quick Reference
---------------

+-------------------------------------------------------------------------------+-----------------------------------------------+
|Hotkey                                                                         |Operator                                       |
+===============================================================================+===============================================+
|:km:hk:`Ctrl-A <particle->Ctrl-A->particle.select_all>`                        |:func:`blender:bpy.ops.particle.select_all`    |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Any-LEFTMOUSE <particle->Any-LEFTMOUSE->view3d.manipulator>`           |:func:`blender:bpy.ops.view3d.manipulator`     |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-O <particle->Shift-O->wm.context_cycle_enum>`                    |:func:`blender:bpy.ops.wm.context_cycle_enum`  |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`A <particle->A->particle.select_all>`                                  |:func:`blender:bpy.ops.particle.select_all`    |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-I <particle->Ctrl-I->particle.select_all>`                        |:func:`blender:bpy.ops.particle.select_all`    |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <particle->Ctrl-NUMPAD_PLUS->particle.select_more>`   |:func:`blender:bpy.ops.particle.select_more`   |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <particle->Ctrl-NUMPAD_MINUS->particle.select_less>` |:func:`blender:bpy.ops.particle.select_less`   |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`L <particle->L->particle.select_linked>`                               |:func:`blender:bpy.ops.particle.select_linked` |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-L <particle->Shift-L->particle.select_linked>`                   |:func:`blender:bpy.ops.particle.select_linked` |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`X <particle->X->particle.delete>`                                      |:func:`blender:bpy.ops.particle.delete`        |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`DEL <particle->DEL->particle.delete>`                                  |:func:`blender:bpy.ops.particle.delete`        |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Alt-H <particle->Alt-H->particle.reveal>`                              |:func:`blender:bpy.ops.particle.reveal`        |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`H <particle->H->particle.hide>`                                        |:func:`blender:bpy.ops.particle.hide`          |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-H <particle->Shift-H->particle.hide>`                            |:func:`blender:bpy.ops.particle.hide`          |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Any-LEFTMOUSE <particle->Any-LEFTMOUSE->view3d.manipulator>`           |:func:`blender:bpy.ops.view3d.manipulator`     |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`LEFTMOUSE <particle->LEFTMOUSE->particle.brush_edit>`                  |:func:`blender:bpy.ops.particle.brush_edit`    |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-LEFTMOUSE <particle->Shift-LEFTMOUSE->particle.brush_edit>`      |:func:`blender:bpy.ops.particle.brush_edit`    |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`F <particle->F->wm.radial_control>`                                    |:func:`blender:bpy.ops.wm.radial_control`      |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-F <particle->Shift-F->wm.radial_control>`                        |:func:`blender:bpy.ops.wm.radial_control`      |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`W <particle->W->wm.call_menu>`                                         |:func:`blender:bpy.ops.wm.call_menu`           |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-K <particle->Shift-K->particle.weight_set>`                      |:func:`blender:bpy.ops.particle.weight_set`    |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-O <particle->Shift-O->wm.context_cycle_enum>`                    |:func:`blender:bpy.ops.wm.context_cycle_enum`  |
+-------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`O <particle->O->wm.context_toggle_enum>`                               |:func:`blender:bpy.ops.wm.context_toggle_enum` |
+-------------------------------------------------------------------------------+-----------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> particle.select_all

   (De)select All

   bpy.ops.particle.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Any-LEFTMOUSE -> view3d.manipulator

   3D Manipulator

   bpy.ops.view3d.manipulator(constraint_axis=(False, False, False), constraint_orientation='GLOBAL', release_confirm=False)
   
   
   +-------------------+--------+
   |Properties:        |Values: |
   +===================+========+
   |Confirm on Release |True    |
   +-------------------+--------+
   
   
.. km:hotkeyd:: Shift-O -> wm.context_cycle_enum

   Context Enum Cycle

   bpy.ops.wm.context_cycle_enum(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+----------------------------------------+
   |Properties:        |Values:                                 |
   +===================+========================================+
   |Context Attributes |tool_settings.proportional_edit_falloff |
   +-------------------+----------------------------------------+
   
   
.. km:hotkeyd:: A -> particle.select_all

   (De)select All

   bpy.ops.particle.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> particle.select_all

   (De)select All

   bpy.ops.particle.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> particle.select_more

   Select More

   bpy.ops.particle.select_more()
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> particle.select_less

   Select Less

   bpy.ops.particle.select_less()
   
   
.. km:hotkeyd:: L -> particle.select_linked

   Select Linked

   bpy.ops.particle.select_linked(deselect=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-L -> particle.select_linked

   Select Linked

   bpy.ops.particle.select_linked(deselect=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: X -> particle.delete

   Delete

   bpy.ops.particle.delete(type='PARTICLE')
   
   
.. km:hotkeyd:: DEL -> particle.delete

   Delete

   bpy.ops.particle.delete(type='PARTICLE')
   
   
.. km:hotkeyd:: Alt-H -> particle.reveal

   Reveal

   bpy.ops.particle.reveal()
   
   
.. km:hotkeyd:: H -> particle.hide

   Hide Selected

   bpy.ops.particle.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> particle.hide

   Hide Selected

   bpy.ops.particle.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Any-LEFTMOUSE -> view3d.manipulator

   3D Manipulator

   bpy.ops.view3d.manipulator(constraint_axis=(False, False, False), constraint_orientation='GLOBAL', release_confirm=False)
   
   
   +-------------------+--------+
   |Properties:        |Values: |
   +===================+========+
   |Confirm on Release |True    |
   +-------------------+--------+
   
   
.. km:hotkeyd:: LEFTMOUSE -> particle.brush_edit

   Brush Edit

   bpy.ops.particle.brush_edit(stroke=[])
   
   
.. km:hotkeyd:: Shift-LEFTMOUSE -> particle.brush_edit

   Brush Edit

   bpy.ops.particle.brush_edit(stroke=[])
   
   
.. km:hotkeyd:: F -> wm.radial_control

   Radial Control

   bpy.ops.wm.radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)
   
   
   +------------------+---------------------------------------+
   |Properties:       |Values:                                |
   +==================+=======================================+
   |Primary Data Path |tool_settings.particle_edit.brush.size |
   +------------------+---------------------------------------+
   
   
.. km:hotkeyd:: Shift-F -> wm.radial_control

   Radial Control

   bpy.ops.wm.radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)
   
   
   +------------------+-------------------------------------------+
   |Properties:       |Values:                                    |
   +==================+===========================================+
   |Primary Data Path |tool_settings.particle_edit.brush.strength |
   +------------------+-------------------------------------------+
   
   
.. km:hotkeyd:: W -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+----------------------------+
   |Properties: |Values:                     |
   +============+============================+
   |Name        |VIEW3D_MT_particle_specials |
   +------------+----------------------------+
   
   
.. km:hotkeyd:: Shift-K -> particle.weight_set

   Weight Set

   bpy.ops.particle.weight_set(factor=1)
   
   
.. km:hotkeyd:: Shift-O -> wm.context_cycle_enum

   Context Enum Cycle

   bpy.ops.wm.context_cycle_enum(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+----------------------------------------+
   |Properties:        |Values:                                 |
   +===================+========================================+
   |Context Attributes |tool_settings.proportional_edit_falloff |
   +-------------------+----------------------------------------+
   |Wrap               |True                                    |
   +-------------------+----------------------------------------+
   
   
.. km:hotkeyd:: O -> wm.context_toggle_enum

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
   
   
