*****
Curve
*****

.. km:module:: curve


---------------
Quick Reference
---------------

+------------------------------------------------------------------------------+------------------------------------------------------+
|Hotkey                                                                        |Operator                                              |
+==============================================================================+======================================================+
|:km:hk:`Ctrl-SELECTMOUSE <curve->Ctrl-SELECTMOUSE->curve.vertex_add>`         |:func:`blender:bpy.ops.curve.vertex_add`              |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-A <curve->Ctrl-A->curve.select_all>`                             |:func:`blender:bpy.ops.curve.select_all`              |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`X <curve->X->curve.delete>`                                           |:func:`blender:bpy.ops.curve.delete`                  |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`DEL <curve->DEL->curve.delete>`                                       |:func:`blender:bpy.ops.curve.delete`                  |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-O <curve->Shift-O->wm.context_cycle_enum>`                      |:func:`blender:bpy.ops.wm.context_cycle_enum`         |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-A <curve->Shift-A->wm.call_menu>`                               |:func:`blender:bpy.ops.wm.call_menu`                  |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`V <curve->V->curve.handle_type_set>`                                  |:func:`blender:bpy.ops.curve.handle_type_set`         |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-ACTIONMOUSE <curve->Ctrl-ACTIONMOUSE->curve.vertex_add>`         |:func:`blender:bpy.ops.curve.vertex_add`              |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-ACTIONMOUSE <curve->Shift-ACTIONMOUSE->curve.draw>`             |:func:`blender:bpy.ops.curve.draw`                    |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`A <curve->A->curve.select_all>`                                       |:func:`blender:bpy.ops.curve.select_all`              |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-I <curve->Ctrl-I->curve.select_all>`                             |:func:`blender:bpy.ops.curve.select_all`              |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-R <curve->Shift-R->curve.select_row>`                           |:func:`blender:bpy.ops.curve.select_row`              |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <curve->Ctrl-NUMPAD_PLUS->curve.select_more>`        |:func:`blender:bpy.ops.curve.select_more`             |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <curve->Ctrl-NUMPAD_MINUS->curve.select_less>`      |:func:`blender:bpy.ops.curve.select_less`             |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-L <curve->Ctrl-L->curve.select_linked>`                          |:func:`blender:bpy.ops.curve.select_linked`           |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-G <curve->Shift-G->curve.select_similar>`                       |:func:`blender:bpy.ops.curve.select_similar`          |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`L <curve->L->curve.select_linked_pick>`                               |:func:`blender:bpy.ops.curve.select_linked_pick`      |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-L <curve->Shift-L->curve.select_linked_pick>`                   |:func:`blender:bpy.ops.curve.select_linked_pick`      |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <curve->Ctrl-SELECTMOUSE->curve.shortest_path_pick>` |:func:`blender:bpy.ops.curve.shortest_path_pick`      |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`P <curve->P->curve.separate>`                                         |:func:`blender:bpy.ops.curve.separate`                |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Y <curve->Y->curve.split>`                                            |:func:`blender:bpy.ops.curve.split`                   |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`E <curve->E->curve.extrude_move>`                                     |:func:`blender:bpy.ops.curve.extrude_move`            |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-D <curve->Shift-D->curve.duplicate_move>`                       |:func:`blender:bpy.ops.curve.duplicate_move`          |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`F <curve->F->curve.make_segment>`                                     |:func:`blender:bpy.ops.curve.make_segment`            |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-C <curve->Alt-C->curve.cyclic_toggle>`                            |:func:`blender:bpy.ops.curve.cyclic_toggle`           |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`X <curve->X->wm.call_menu>`                                           |:func:`blender:bpy.ops.wm.call_menu`                  |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`DEL <curve->DEL->wm.call_menu>`                                       |:func:`blender:bpy.ops.wm.call_menu`                  |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-X <curve->Ctrl-X->curve.dissolve_verts>`                         |:func:`blender:bpy.ops.curve.dissolve_verts`          |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-DEL <curve->Ctrl-DEL->curve.dissolve_verts>`                     |:func:`blender:bpy.ops.curve.dissolve_verts`          |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-T <curve->Alt-T->curve.tilt_clear>`                               |:func:`blender:bpy.ops.curve.tilt_clear`              |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-T <curve->Ctrl-T->transform.tilt>`                               |:func:`blender:bpy.ops.transform.tilt`                |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-S <curve->Alt-S->transform.transform>`                            |:func:`blender:bpy.ops.transform.transform`           |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-H <curve->Alt-H->curve.reveal>`                                   |:func:`blender:bpy.ops.curve.reveal`                  |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`H <curve->H->curve.hide>`                                             |:func:`blender:bpy.ops.curve.hide`                    |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-H <curve->Shift-H->curve.hide>`                                 |:func:`blender:bpy.ops.curve.hide`                    |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-N <curve->Ctrl-N->curve.normals_make_consistent>`                |:func:`blender:bpy.ops.curve.normals_make_consistent` |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-P <curve->Ctrl-P->object.vertex_parent_set>`                     |:func:`blender:bpy.ops.object.vertex_parent_set`      |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`W <curve->W->wm.call_menu>`                                           |:func:`blender:bpy.ops.wm.call_menu`                  |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-H <curve->Ctrl-H->wm.call_menu>`                                 |:func:`blender:bpy.ops.wm.call_menu`                  |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-O <curve->Shift-O->wm.context_cycle_enum>`                      |:func:`blender:bpy.ops.wm.context_cycle_enum`         |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`O <curve->O->wm.context_toggle_enum>`                                 |:func:`blender:bpy.ops.wm.context_toggle_enum`        |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-O <curve->Alt-O->wm.context_toggle_enum>`                         |:func:`blender:bpy.ops.wm.context_toggle_enum`        |
+------------------------------------------------------------------------------+------------------------------------------------------+


------------------
Detailed Reference
------------------

.. km:hotkey:: Ctrl-SELECTMOUSE -> curve.vertex_add

   Add Vertex

   bpy.ops.curve.vertex_add(location=(0, 0, 0))
   
   
.. km:hotkey:: Ctrl-A -> curve.select_all

   (De)select All

   bpy.ops.curve.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: X -> curve.delete

   Delete

   bpy.ops.curve.delete(type='VERT')
   
   
.. km:hotkey:: DEL -> curve.delete

   Delete

   bpy.ops.curve.delete(type='VERT')
   
   
.. km:hotkey:: Shift-O -> wm.context_cycle_enum

   Context Enum Cycle

   bpy.ops.wm.context_cycle_enum(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+----------------------------------------+
   |Properties:        |Values:                                 |
   +===================+========================================+
   |Context Attributes |tool_settings.proportional_edit_falloff |
   +-------------------+----------------------------------------+
   
   
.. km:hotkey:: Shift-A -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------------+
   |Properties: |Values:                |
   +============+=======================+
   |Name        |INFO_MT_edit_curve_add |
   +------------+-----------------------+
   
   
.. km:hotkey:: V -> curve.handle_type_set

   Set Handle Type

   bpy.ops.curve.handle_type_set(type='AUTOMATIC')
   
   
.. km:hotkey:: Ctrl-ACTIONMOUSE -> curve.vertex_add

   Add Vertex

   bpy.ops.curve.vertex_add(location=(0, 0, 0))
   
   
.. km:hotkey:: Shift-ACTIONMOUSE -> curve.draw

   Draw Curve

   bpy.ops.curve.draw(error_threshold=0, fit_method='REFIT', corner_angle=1.22173, use_cyclic=True, stroke=[], wait_for_input=True)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Wait for Input |False   |
   +---------------+--------+
   
   
.. km:hotkey:: A -> curve.select_all

   (De)select All

   bpy.ops.curve.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-I -> curve.select_all

   (De)select All

   bpy.ops.curve.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkey:: Shift-R -> curve.select_row

   Select Control Point Row

   bpy.ops.curve.select_row()
   
   
.. km:hotkey:: Ctrl-NUMPAD_PLUS -> curve.select_more

   Select More

   bpy.ops.curve.select_more()
   
   
.. km:hotkey:: Ctrl-NUMPAD_MINUS -> curve.select_less

   Select Less

   bpy.ops.curve.select_less()
   
   
.. km:hotkey:: Ctrl-L -> curve.select_linked

   Select Linked All

   bpy.ops.curve.select_linked()
   
   
.. km:hotkey:: Shift-G -> curve.select_similar

   Select Similar

   bpy.ops.curve.select_similar(type='WEIGHT', compare='EQUAL', threshold=0.1)
   
   
.. km:hotkey:: L -> curve.select_linked_pick

   Select Linked

   bpy.ops.curve.select_linked_pick(deselect=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkey:: Shift-L -> curve.select_linked_pick

   Select Linked

   bpy.ops.curve.select_linked_pick(deselect=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-SELECTMOUSE -> curve.shortest_path_pick

   Pick Shortest Path

   bpy.ops.curve.shortest_path_pick()
   
   
.. km:hotkey:: P -> curve.separate

   Separate

   bpy.ops.curve.separate()
   
   
.. km:hotkey:: Y -> curve.split

   Split

   bpy.ops.curve.split()
   
   
.. km:hotkey:: E -> curve.extrude_move

   Extrude Curve and Move

   bpy.ops.curve.extrude_move(CURVE_OT_extrude={"mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extrude     |N/A     |
   +------------+--------+
   |Translate   |N/A     |
   +------------+--------+
   
   
.. km:hotkey:: Shift-D -> curve.duplicate_move

   Add Duplicate

   bpy.ops.curve.duplicate_move(CURVE_OT_duplicate={}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Duplicate Curve |N/A     |
   +----------------+--------+
   |Translate       |N/A     |
   +----------------+--------+
   
   
.. km:hotkey:: F -> curve.make_segment

   Make Segment

   bpy.ops.curve.make_segment()
   
   
.. km:hotkey:: Alt-C -> curve.cyclic_toggle

   Toggle Cyclic

   bpy.ops.curve.cyclic_toggle(direction='CYCLIC_U')
   
   
.. km:hotkey:: X -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+----------------------------+
   |Properties: |Values:                     |
   +============+============================+
   |Name        |VIEW3D_MT_edit_curve_delete |
   +------------+----------------------------+
   
   
.. km:hotkey:: DEL -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+----------------------------+
   |Properties: |Values:                     |
   +============+============================+
   |Name        |VIEW3D_MT_edit_curve_delete |
   +------------+----------------------------+
   
   
.. km:hotkey:: Ctrl-X -> curve.dissolve_verts

   Dissolve Vertices

   bpy.ops.curve.dissolve_verts()
   
   
.. km:hotkey:: Ctrl-DEL -> curve.dissolve_verts

   Dissolve Vertices

   bpy.ops.curve.dissolve_verts()
   
   
.. km:hotkey:: Alt-T -> curve.tilt_clear

   Clear Tilt

   bpy.ops.curve.tilt_clear()
   
   
.. km:hotkey:: Ctrl-T -> transform.tilt

   Tilt

   bpy.ops.transform.tilt(value=0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
   
   
.. km:hotkey:: Alt-S -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+-------------------+
   |Properties: |Values:            |
   +============+===================+
   |Mode        |CURVE_SHRINKFATTEN |
   +------------+-------------------+
   
   
.. km:hotkey:: Alt-H -> curve.reveal

   Reveal Hidden

   bpy.ops.curve.reveal()
   
   
.. km:hotkey:: H -> curve.hide

   Hide Selected

   bpy.ops.curve.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkey:: Shift-H -> curve.hide

   Hide Selected

   bpy.ops.curve.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-N -> curve.normals_make_consistent

   Recalc Normals

   bpy.ops.curve.normals_make_consistent(calc_length=False)
   
   
.. km:hotkey:: Ctrl-P -> object.vertex_parent_set

   Make Vertex Parent

   bpy.ops.object.vertex_parent_set()
   
   
.. km:hotkey:: W -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------------------------+
   |Properties: |Values:                       |
   +============+==============================+
   |Name        |VIEW3D_MT_edit_curve_specials |
   +------------+------------------------------+
   
   
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
   
   
.. km:hotkey:: Alt-O -> wm.context_toggle_enum

   Context Toggle Values

   bpy.ops.wm.context_toggle_enum(data_path="", value_1="", value_2="")
   
   
   +-------------------+--------------------------------+
   |Properties:        |Values:                         |
   +===================+================================+
   |Context Attributes |tool_settings.proportional_edit |
   +-------------------+--------------------------------+
   |Value              |DISABLED                        |
   +-------------------+--------------------------------+
   |Value              |CONNECTED                       |
   +-------------------+--------------------------------+
   
   
