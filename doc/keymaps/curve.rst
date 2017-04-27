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
|:km:hk:`Ctrl-A <curve->Ctrl-A->curve.select_all>`                             |:func:`blender:bpy.ops.curve.select_all`              |
+------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Alt-SELECTMOUSE <curve->Ctrl-Alt-SELECTMOUSE->curve.vertex_add>` |:func:`blender:bpy.ops.curve.vertex_add`              |
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

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> curve.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.curve.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Alt-SELECTMOUSE -> curve.vertex_add : MOUSE -> CLICK

   Add Vertex

   bpy.ops.curve.vertex_add(location=(0, 0, 0))
   
   
.. km:hotkeyd:: Shift-A -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------------+
   |Properties: |Values:                |
   +============+=======================+
   |Name        |INFO_MT_edit_curve_add |
   +------------+-----------------------+
   
   
.. km:hotkeyd:: V -> curve.handle_type_set : KEYBOARD -> PRESS

   Set Handle Type

   bpy.ops.curve.handle_type_set(type='AUTOMATIC')
   
   
.. km:hotkeyd:: Ctrl-ACTIONMOUSE -> curve.vertex_add : MOUSE -> CLICK

   Add Vertex

   bpy.ops.curve.vertex_add(location=(0, 0, 0))
   
   
.. km:hotkeyd:: Shift-ACTIONMOUSE -> curve.draw : MOUSE -> PRESS

   Draw Curve

   bpy.ops.curve.draw(error_threshold=0, fit_method='REFIT', corner_angle=1.22173, use_cyclic=True, stroke=[], wait_for_input=True)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Wait for Input |False   |
   +---------------+--------+
   
   
.. km:hotkeyd:: A -> curve.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.curve.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> curve.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.curve.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-R -> curve.select_row : KEYBOARD -> PRESS

   Select Control Point Row

   bpy.ops.curve.select_row()
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> curve.select_more : KEYBOARD -> PRESS

   Select More

   bpy.ops.curve.select_more()
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> curve.select_less : KEYBOARD -> PRESS

   Select Less

   bpy.ops.curve.select_less()
   
   
.. km:hotkeyd:: Ctrl-L -> curve.select_linked : KEYBOARD -> PRESS

   Select Linked All

   bpy.ops.curve.select_linked()
   
   
.. km:hotkeyd:: Shift-G -> curve.select_similar : KEYBOARD -> PRESS

   Select Similar

   bpy.ops.curve.select_similar(type='WEIGHT', compare='EQUAL', threshold=0.1)
   
   
.. km:hotkeyd:: L -> curve.select_linked_pick : KEYBOARD -> PRESS

   Select Linked

   bpy.ops.curve.select_linked_pick(deselect=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-L -> curve.select_linked_pick : KEYBOARD -> PRESS

   Select Linked

   bpy.ops.curve.select_linked_pick(deselect=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-SELECTMOUSE -> curve.shortest_path_pick : MOUSE -> CLICK

   Pick Shortest Path

   bpy.ops.curve.shortest_path_pick()
   
   
.. km:hotkeyd:: P -> curve.separate : KEYBOARD -> PRESS

   Separate

   bpy.ops.curve.separate()
   
   
.. km:hotkeyd:: Y -> curve.split : KEYBOARD -> PRESS

   Split

   bpy.ops.curve.split()
   
   
.. km:hotkeyd:: E -> curve.extrude_move : KEYBOARD -> PRESS

   Extrude Curve and Move

   bpy.ops.curve.extrude_move(CURVE_OT_extrude={"mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extrude     |N/A     |
   +------------+--------+
   |Translate   |N/A     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-D -> curve.duplicate_move : KEYBOARD -> PRESS

   Add Duplicate

   bpy.ops.curve.duplicate_move(CURVE_OT_duplicate={}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Duplicate Curve |N/A     |
   +----------------+--------+
   |Translate       |N/A     |
   +----------------+--------+
   
   
.. km:hotkeyd:: F -> curve.make_segment : KEYBOARD -> PRESS

   Make Segment

   bpy.ops.curve.make_segment()
   
   
.. km:hotkeyd:: Alt-C -> curve.cyclic_toggle : KEYBOARD -> PRESS

   Toggle Cyclic

   bpy.ops.curve.cyclic_toggle(direction='CYCLIC_U')
   
   
.. km:hotkeyd:: X -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+----------------------------+
   |Properties: |Values:                     |
   +============+============================+
   |Name        |VIEW3D_MT_edit_curve_delete |
   +------------+----------------------------+
   
   
.. km:hotkeyd:: DEL -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+----------------------------+
   |Properties: |Values:                     |
   +============+============================+
   |Name        |VIEW3D_MT_edit_curve_delete |
   +------------+----------------------------+
   
   
.. km:hotkeyd:: Ctrl-X -> curve.dissolve_verts : KEYBOARD -> PRESS

   Dissolve Vertices

   bpy.ops.curve.dissolve_verts()
   
   
.. km:hotkeyd:: Ctrl-DEL -> curve.dissolve_verts : KEYBOARD -> PRESS

   Dissolve Vertices

   bpy.ops.curve.dissolve_verts()
   
   
.. km:hotkeyd:: Alt-T -> curve.tilt_clear : KEYBOARD -> PRESS

   Clear Tilt

   bpy.ops.curve.tilt_clear()
   
   
.. km:hotkeyd:: Ctrl-T -> transform.tilt : KEYBOARD -> PRESS

   Tilt

   bpy.ops.transform.tilt(value=0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
   
   
.. km:hotkeyd:: Alt-S -> transform.transform : KEYBOARD -> PRESS

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+-------------------+
   |Properties: |Values:            |
   +============+===================+
   |Mode        |CURVE_SHRINKFATTEN |
   +------------+-------------------+
   
   
.. km:hotkeyd:: Alt-H -> curve.reveal : KEYBOARD -> PRESS

   Reveal Hidden

   bpy.ops.curve.reveal()
   
   
.. km:hotkeyd:: H -> curve.hide : KEYBOARD -> PRESS

   Hide Selected

   bpy.ops.curve.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> curve.hide : KEYBOARD -> PRESS

   Hide Selected

   bpy.ops.curve.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-N -> curve.normals_make_consistent : KEYBOARD -> PRESS

   Recalc Normals

   bpy.ops.curve.normals_make_consistent(calc_length=False)
   
   
.. km:hotkeyd:: Ctrl-P -> object.vertex_parent_set : KEYBOARD -> PRESS

   Make Vertex Parent

   bpy.ops.object.vertex_parent_set()
   
   
.. km:hotkeyd:: W -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------------------------+
   |Properties: |Values:                       |
   +============+==============================+
   |Name        |VIEW3D_MT_edit_curve_specials |
   +------------+------------------------------+
   
   
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
   
   
.. km:hotkeyd:: Alt-O -> wm.context_toggle_enum : KEYBOARD -> PRESS

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
   
   
