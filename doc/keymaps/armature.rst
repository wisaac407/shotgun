********
Armature
********

.. km:module:: armature

   


---------------
Quick Reference
---------------

+----------------------------------------------------------------------------------------+----------------------------------------------------+
|Hotkey                                                                                  |Operator                                            |
+========================================================================================+====================================================+
|:km:hk:`Ctrl-A <armature->Ctrl-A->armature.select_all>`                                 |:func:`blender:bpy.ops.armature.select_all`         |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`X <armature->X->armature.delete>`                                               |:func:`blender:bpy.ops.armature.delete`             |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`DEL <armature->DEL->armature.delete>`                                           |:func:`blender:bpy.ops.armature.delete`             |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <armature->Ctrl-SELECTMOUSE->armature.click_extrude>`          |:func:`blender:bpy.ops.armature.click_extrude`      |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-Alt-P <armature->Ctrl-Alt-P->armature.separate>`                           |:func:`blender:bpy.ops.armature.separate`           |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`X <armature->X->sketch.delete>`                                                 |:func:`blender:bpy.ops.sketch.delete`               |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`DEL <armature->DEL->sketch.delete>`                                             |:func:`blender:bpy.ops.sketch.delete`               |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`RIGHTMOUSE <armature->RIGHTMOUSE->sketch.finish_stroke>`                        |:func:`blender:bpy.ops.sketch.finish_stroke`        |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`ESC <armature->ESC->sketch.cancel_stroke>`                                      |:func:`blender:bpy.ops.sketch.cancel_stroke`        |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Shift-LEFTMOUSE <armature->Shift-LEFTMOUSE->sketch.gesture>`                    |:func:`blender:bpy.ops.sketch.gesture`              |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`LEFTMOUSE <armature->LEFTMOUSE->sketch.draw_stroke>`                            |:func:`blender:bpy.ops.sketch.draw_stroke`          |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-LEFTMOUSE <armature->Ctrl-LEFTMOUSE->sketch.draw_stroke>`                  |:func:`blender:bpy.ops.sketch.draw_stroke`          |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`MOUSEMOVE <armature->MOUSEMOVE->sketch.draw_preview>`                           |:func:`blender:bpy.ops.sketch.draw_preview`         |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-MOUSEMOVE <armature->Ctrl-MOUSEMOVE->sketch.draw_preview>`                 |:func:`blender:bpy.ops.sketch.draw_preview`         |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`H <armature->H->armature.hide>`                                                 |:func:`blender:bpy.ops.armature.hide`               |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Shift-H <armature->Shift-H->armature.hide>`                                     |:func:`blender:bpy.ops.armature.hide`               |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Alt-H <armature->Alt-H->armature.reveal>`                                       |:func:`blender:bpy.ops.armature.reveal`             |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-Alt-A <armature->Ctrl-Alt-A->armature.align>`                              |:func:`blender:bpy.ops.armature.align`              |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-N <armature->Ctrl-N->armature.calculate_roll>`                             |:func:`blender:bpy.ops.armature.calculate_roll`     |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Alt-R <armature->Alt-R->armature.roll_clear>`                                   |:func:`blender:bpy.ops.armature.roll_clear`         |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Alt-F <armature->Alt-F->armature.switch_direction>`                             |:func:`blender:bpy.ops.armature.switch_direction`   |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Shift-A <armature->Shift-A->armature.bone_primitive_add>`                       |:func:`blender:bpy.ops.armature.bone_primitive_add` |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-P <armature->Ctrl-P->armature.parent_set>`                                 |:func:`blender:bpy.ops.armature.parent_set`         |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Alt-P <armature->Alt-P->armature.parent_clear>`                                 |:func:`blender:bpy.ops.armature.parent_clear`       |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`A <armature->A->armature.select_all>`                                           |:func:`blender:bpy.ops.armature.select_all`         |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-I <armature->Ctrl-I->armature.select_all>`                                 |:func:`blender:bpy.ops.armature.select_all`         |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-Shift-M <armature->Ctrl-Shift-M->armature.select_mirror>`                  |:func:`blender:bpy.ops.armature.select_mirror`      |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`LEFT_BRACKET <armature->LEFT_BRACKET->armature.select_hierarchy>`               |:func:`blender:bpy.ops.armature.select_hierarchy`   |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Shift-LEFT_BRACKET <armature->Shift-LEFT_BRACKET->armature.select_hierarchy>`   |:func:`blender:bpy.ops.armature.select_hierarchy`   |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`RIGHT_BRACKET <armature->RIGHT_BRACKET->armature.select_hierarchy>`             |:func:`blender:bpy.ops.armature.select_hierarchy`   |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Shift-RIGHT_BRACKET <armature->Shift-RIGHT_BRACKET->armature.select_hierarchy>` |:func:`blender:bpy.ops.armature.select_hierarchy`   |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <armature->Ctrl-NUMPAD_PLUS->armature.select_more>`            |:func:`blender:bpy.ops.armature.select_more`        |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <armature->Ctrl-NUMPAD_MINUS->armature.select_less>`          |:func:`blender:bpy.ops.armature.select_less`        |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Shift-G <armature->Shift-G->armature.select_similar>`                           |:func:`blender:bpy.ops.armature.select_similar`     |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`L <armature->L->armature.select_linked>`                                        |:func:`blender:bpy.ops.armature.select_linked`      |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <armature->Ctrl-SELECTMOUSE->armature.shortest_path_pick>`     |:func:`blender:bpy.ops.armature.shortest_path_pick` |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`X <armature->X->wm.call_menu>`                                                  |:func:`blender:bpy.ops.wm.call_menu`                |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`DEL <armature->DEL->wm.call_menu>`                                              |:func:`blender:bpy.ops.wm.call_menu`                |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-X <armature->Ctrl-X->armature.dissolve>`                                   |:func:`blender:bpy.ops.armature.dissolve`           |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Shift-D <armature->Shift-D->armature.duplicate_move>`                           |:func:`blender:bpy.ops.armature.duplicate_move`     |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`E <armature->E->armature.extrude_move>`                                         |:func:`blender:bpy.ops.armature.extrude_move`       |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Shift-E <armature->Shift-E->armature.extrude_forked>`                           |:func:`blender:bpy.ops.armature.extrude_forked`     |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-ACTIONMOUSE <armature->Ctrl-ACTIONMOUSE->armature.click_extrude>`          |:func:`blender:bpy.ops.armature.click_extrude`      |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`F <armature->F->armature.fill>`                                                 |:func:`blender:bpy.ops.armature.fill`               |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Alt-M <armature->Alt-M->armature.merge>`                                        |:func:`blender:bpy.ops.armature.merge`              |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Y <armature->Y->armature.split>`                                                |:func:`blender:bpy.ops.armature.split`              |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`P <armature->P->armature.separate>`                                             |:func:`blender:bpy.ops.armature.separate`           |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Shift-W <armature->Shift-W->wm.call_menu>`                                      |:func:`blender:bpy.ops.wm.call_menu`                |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-Shift-W <armature->Ctrl-Shift-W->wm.call_menu>`                            |:func:`blender:bpy.ops.wm.call_menu`                |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Alt-W <armature->Alt-W->wm.call_menu>`                                          |:func:`blender:bpy.ops.wm.call_menu`                |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-ACCENT_GRAVE <armature->Ctrl-ACCENT_GRAVE->armature.layers_show_all>`      |:func:`blender:bpy.ops.armature.layers_show_all`    |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Shift-M <armature->Shift-M->armature.armature_layers>`                          |:func:`blender:bpy.ops.armature.armature_layers`    |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`M <armature->M->armature.bone_layers>`                                          |:func:`blender:bpy.ops.armature.bone_layers`        |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-Alt-S <armature->Ctrl-Alt-S->transform.transform>`                         |:func:`blender:bpy.ops.transform.transform`         |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Alt-S <armature->Alt-S->transform.transform>`                                   |:func:`blender:bpy.ops.transform.transform`         |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`Ctrl-R <armature->Ctrl-R->transform.transform>`                                 |:func:`blender:bpy.ops.transform.transform`         |
+----------------------------------------------------------------------------------------+----------------------------------------------------+
|:km:hk:`W <armature->W->wm.call_menu>`                                                  |:func:`blender:bpy.ops.wm.call_menu`                |
+----------------------------------------------------------------------------------------+----------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> armature.select_all

   (De)select All

   bpy.ops.armature.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: X -> armature.delete

   Delete Selected Bone(s)

   bpy.ops.armature.delete()
   
   
.. km:hotkey:: DEL -> armature.delete

   Delete Selected Bone(s)

   bpy.ops.armature.delete()
   
   
.. km:hotkey:: Ctrl-SELECTMOUSE -> armature.click_extrude

   Click-Extrude

   bpy.ops.armature.click_extrude()
   
   
.. km:hotkey:: Ctrl-Alt-P -> armature.separate

   Separate Bones

   bpy.ops.armature.separate()
   
   
.. km:hotkeyd:: X -> sketch.delete

   Delete

   bpy.ops.sketch.delete()
   
   
.. km:hotkeyd:: DEL -> sketch.delete

   Delete

   bpy.ops.sketch.delete()
   
   
.. km:hotkeyd:: RIGHTMOUSE -> sketch.finish_stroke

   End Stroke

   bpy.ops.sketch.finish_stroke()
   
   
.. km:hotkeyd:: ESC -> sketch.cancel_stroke

   Cancel Stroke

   bpy.ops.sketch.cancel_stroke()
   
   
.. km:hotkeyd:: Shift-LEFTMOUSE -> sketch.gesture

   Gesture

   bpy.ops.sketch.gesture(snap=False)
   
   
.. km:hotkeyd:: LEFTMOUSE -> sketch.draw_stroke

   Draw Stroke

   bpy.ops.sketch.draw_stroke(snap=False)
   
   
.. km:hotkeyd:: Ctrl-LEFTMOUSE -> sketch.draw_stroke

   Draw Stroke

   bpy.ops.sketch.draw_stroke(snap=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Snap        |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: MOUSEMOVE -> sketch.draw_preview

   Draw Preview

   bpy.ops.sketch.draw_preview(snap=False)
   
   
.. km:hotkeyd:: Ctrl-MOUSEMOVE -> sketch.draw_preview

   Draw Preview

   bpy.ops.sketch.draw_preview(snap=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Snap        |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: H -> armature.hide

   Hide Selected Bones

   bpy.ops.armature.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> armature.hide

   Hide Selected Bones

   bpy.ops.armature.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-H -> armature.reveal

   Reveal Bones

   bpy.ops.armature.reveal()
   
   
.. km:hotkeyd:: Ctrl-Alt-A -> armature.align

   Align Bones

   bpy.ops.armature.align()
   
   
.. km:hotkeyd:: Ctrl-N -> armature.calculate_roll

   Recalculate Roll

   bpy.ops.armature.calculate_roll(type='POS_X', axis_flip=False, axis_only=False)
   
   
.. km:hotkeyd:: Alt-R -> armature.roll_clear

   Clear Roll

   bpy.ops.armature.roll_clear(roll=0)
   
   
.. km:hotkeyd:: Alt-F -> armature.switch_direction

   Switch Direction

   bpy.ops.armature.switch_direction()
   
   
.. km:hotkeyd:: Shift-A -> armature.bone_primitive_add

   Add Bone

   bpy.ops.armature.bone_primitive_add(name="Bone")
   
   
.. km:hotkeyd:: Ctrl-P -> armature.parent_set

   Make Parent

   bpy.ops.armature.parent_set(type='CONNECTED')
   
   
.. km:hotkeyd:: Alt-P -> armature.parent_clear

   Clear Parent

   bpy.ops.armature.parent_clear(type='CLEAR')
   
   
.. km:hotkeyd:: A -> armature.select_all

   (De)select All

   bpy.ops.armature.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> armature.select_all

   (De)select All

   bpy.ops.armature.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-M -> armature.select_mirror

   Flip Active/Selected Bone

   bpy.ops.armature.select_mirror(only_active=False, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: LEFT_BRACKET -> armature.select_hierarchy

   Select Hierarchy

   bpy.ops.armature.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |PARENT  |
   +------------+--------+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-LEFT_BRACKET -> armature.select_hierarchy

   Select Hierarchy

   bpy.ops.armature.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |PARENT  |
   +------------+--------+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: RIGHT_BRACKET -> armature.select_hierarchy

   Select Hierarchy

   bpy.ops.armature.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |CHILD   |
   +------------+--------+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-RIGHT_BRACKET -> armature.select_hierarchy

   Select Hierarchy

   bpy.ops.armature.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |CHILD   |
   +------------+--------+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> armature.select_more

   Select More

   bpy.ops.armature.select_more()
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> armature.select_less

   Select Less

   bpy.ops.armature.select_less()
   
   
.. km:hotkeyd:: Shift-G -> armature.select_similar

   Select Similar

   bpy.ops.armature.select_similar(type='LENGTH', threshold=0.1)
   
   
.. km:hotkeyd:: L -> armature.select_linked

   Select Connected

   bpy.ops.armature.select_linked(extend=False)
   
   
.. km:hotkeyd:: Ctrl-SELECTMOUSE -> armature.shortest_path_pick

   Pick Shortest Path

   bpy.ops.armature.shortest_path_pick()
   
   
.. km:hotkeyd:: X -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-------------------------------+
   |Properties: |Values:                        |
   +============+===============================+
   |Name        |VIEW3D_MT_edit_armature_delete |
   +------------+-------------------------------+
   
   
.. km:hotkeyd:: DEL -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-------------------------------+
   |Properties: |Values:                        |
   +============+===============================+
   |Name        |VIEW3D_MT_edit_armature_delete |
   +------------+-------------------------------+
   
   
.. km:hotkeyd:: Ctrl-X -> armature.dissolve

   Dissolve Selected Bone(s)

   bpy.ops.armature.dissolve()
   
   
.. km:hotkeyd:: Shift-D -> armature.duplicate_move

   Duplicate

   bpy.ops.armature.duplicate_move(ARMATURE_OT_duplicate={}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +---------------------------+--------+
   |Properties:                |Values: |
   +===========================+========+
   |Duplicate Selected Bone(s) |N/A     |
   +---------------------------+--------+
   |Translate                  |N/A     |
   +---------------------------+--------+
   
   
.. km:hotkeyd:: E -> armature.extrude_move

   Extrude

   bpy.ops.armature.extrude_move(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extrude     |N/A     |
   +------------+--------+
   |Translate   |N/A     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-E -> armature.extrude_forked

   Extrude Forked

   bpy.ops.armature.extrude_forked(ARMATURE_OT_extrude={"forked":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extrude     |N/A     |
   +------------+--------+
   |Translate   |N/A     |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-ACTIONMOUSE -> armature.click_extrude

   Click-Extrude

   bpy.ops.armature.click_extrude()
   
   
.. km:hotkeyd:: F -> armature.fill

   Fill Between Joints

   bpy.ops.armature.fill()
   
   
.. km:hotkeyd:: Alt-M -> armature.merge

   Merge Bones

   bpy.ops.armature.merge(type='WITHIN_CHAIN')
   
   
.. km:hotkeyd:: Y -> armature.split

   Split

   bpy.ops.armature.split()
   
   
.. km:hotkeyd:: P -> armature.separate

   Separate Bones

   bpy.ops.armature.separate()
   
   
.. km:hotkeyd:: Shift-W -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------------------------+
   |Properties: |Values:                       |
   +============+==============================+
   |Name        |VIEW3D_MT_bone_options_toggle |
   +------------+------------------------------+
   
   
.. km:hotkeyd:: Ctrl-Shift-W -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------------------------+
   |Properties: |Values:                       |
   +============+==============================+
   |Name        |VIEW3D_MT_bone_options_enable |
   +------------+------------------------------+
   
   
.. km:hotkeyd:: Alt-W -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-------------------------------+
   |Properties: |Values:                        |
   +============+===============================+
   |Name        |VIEW3D_MT_bone_options_disable |
   +------------+-------------------------------+
   
   
.. km:hotkeyd:: Ctrl-ACCENT_GRAVE -> armature.layers_show_all

   Show All Layers

   bpy.ops.armature.layers_show_all(all=True)
   
   
.. km:hotkeyd:: Shift-M -> armature.armature_layers

   Change Armature Layers

   bpy.ops.armature.armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   
   
.. km:hotkeyd:: M -> armature.bone_layers

   Change Bone Layers

   bpy.ops.armature.bone_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   
   
.. km:hotkeyd:: Ctrl-Alt-S -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Mode        |BONE_SIZE |
   +------------+----------+
   
   
.. km:hotkeyd:: Alt-S -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+--------------+
   |Properties: |Values:       |
   +============+==============+
   |Mode        |BONE_ENVELOPE |
   +------------+--------------+
   
   
.. km:hotkeyd:: Ctrl-R -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Mode        |BONE_ROLL |
   +------------+----------+
   
   
.. km:hotkeyd:: W -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+----------------------------+
   |Properties: |Values:                     |
   +============+============================+
   |Name        |VIEW3D_MT_armature_specials |
   +------------+----------------------------+
   
   
