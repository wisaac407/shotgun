***********
Object Mode
***********

.. km:module:: objectmode

   


---------------
Quick Reference
---------------

+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|Hotkey                                                                                  |Operator                                                   |
+========================================================================================+===========================================================+
|:km:hk:`Shift-O <objectmode->Shift-O->wm.context_cycle_enum>`                           |:func:`blender:bpy.ops.wm.context_cycle_enum`              |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-A <objectmode->Ctrl-A->object.select_all>`                                 |:func:`blender:bpy.ops.object.select_all`                  |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-G <objectmode->Alt-G->object.location_clear>`                               |:func:`blender:bpy.ops.object.location_clear`              |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-R <objectmode->Alt-R->object.rotation_clear>`                               |:func:`blender:bpy.ops.object.rotation_clear`              |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-S <objectmode->Alt-S->object.scale_clear>`                                  |:func:`blender:bpy.ops.object.scale_clear`                 |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`A <objectmode->A->wm.call_menu>`                                                |:func:`blender:bpy.ops.wm.call_menu`                       |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-O <objectmode->Shift-O->wm.context_cycle_enum>`                           |:func:`blender:bpy.ops.wm.context_cycle_enum`              |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`O <objectmode->O->wm.context_toggle>`                                           |:func:`blender:bpy.ops.wm.context_toggle`                  |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`P <objectmode->P->view3d.game_start>`                                           |:func:`blender:bpy.ops.view3d.game_start`                  |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`A <objectmode->A->object.select_all>`                                           |:func:`blender:bpy.ops.object.select_all`                  |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-I <objectmode->Ctrl-I->object.select_all>`                                 |:func:`blender:bpy.ops.object.select_all`                  |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <objectmode->Ctrl-NUMPAD_PLUS->object.select_more>`            |:func:`blender:bpy.ops.object.select_more`                 |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <objectmode->Ctrl-NUMPAD_MINUS->object.select_less>`          |:func:`blender:bpy.ops.object.select_less`                 |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-L <objectmode->Shift-L->object.select_linked>`                            |:func:`blender:bpy.ops.object.select_linked`               |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-G <objectmode->Shift-G->object.select_grouped>`                           |:func:`blender:bpy.ops.object.select_grouped`              |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Shift-M <objectmode->Ctrl-Shift-M->object.select_mirror>`                  |:func:`blender:bpy.ops.object.select_mirror`               |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`LEFT_BRACKET <objectmode->LEFT_BRACKET->object.select_hierarchy>`               |:func:`blender:bpy.ops.object.select_hierarchy`            |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-LEFT_BRACKET <objectmode->Shift-LEFT_BRACKET->object.select_hierarchy>`   |:func:`blender:bpy.ops.object.select_hierarchy`            |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`RIGHT_BRACKET <objectmode->RIGHT_BRACKET->object.select_hierarchy>`             |:func:`blender:bpy.ops.object.select_hierarchy`            |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-RIGHT_BRACKET <objectmode->Shift-RIGHT_BRACKET->object.select_hierarchy>` |:func:`blender:bpy.ops.object.select_hierarchy`            |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-P <objectmode->Ctrl-P->object.parent_set>`                                 |:func:`blender:bpy.ops.object.parent_set`                  |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Shift-P <objectmode->Ctrl-Shift-P->object.parent_no_inverse_set>`          |:func:`blender:bpy.ops.object.parent_no_inverse_set`       |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-P <objectmode->Alt-P->object.parent_clear>`                                 |:func:`blender:bpy.ops.object.parent_clear`                |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-T <objectmode->Ctrl-T->object.track_set>`                                  |:func:`blender:bpy.ops.object.track_set`                   |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-T <objectmode->Alt-T->object.track_clear>`                                  |:func:`blender:bpy.ops.object.track_clear`                 |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Shift-C <objectmode->Ctrl-Shift-C->object.constraint_add_with_targets>`    |:func:`blender:bpy.ops.object.constraint_add_with_targets` |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Alt-C <objectmode->Ctrl-Alt-C->object.constraints_clear>`                  |:func:`blender:bpy.ops.object.constraints_clear`           |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-G <objectmode->Alt-G->object.location_clear>`                               |:func:`blender:bpy.ops.object.location_clear`              |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-R <objectmode->Alt-R->object.rotation_clear>`                               |:func:`blender:bpy.ops.object.rotation_clear`              |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-S <objectmode->Alt-S->object.scale_clear>`                                  |:func:`blender:bpy.ops.object.scale_clear`                 |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-Alt-G <objectmode->Shift-Alt-G->object.location_clear>`                   |:func:`blender:bpy.ops.object.location_clear`              |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-Alt-R <objectmode->Shift-Alt-R->object.rotation_clear>`                   |:func:`blender:bpy.ops.object.rotation_clear`              |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-Alt-S <objectmode->Shift-Alt-S->object.scale_clear>`                      |:func:`blender:bpy.ops.object.scale_clear`                 |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-O <objectmode->Alt-O->object.origin_clear>`                                 |:func:`blender:bpy.ops.object.origin_clear`                |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-H <objectmode->Alt-H->object.hide_view_clear>`                              |:func:`blender:bpy.ops.object.hide_view_clear`             |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`H <objectmode->H->object.hide_view_set>`                                        |:func:`blender:bpy.ops.object.hide_view_set`               |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-H <objectmode->Shift-H->object.hide_view_set>`                            |:func:`blender:bpy.ops.object.hide_view_set`               |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Alt-H <objectmode->Ctrl-Alt-H->object.hide_render_clear>`                  |:func:`blender:bpy.ops.object.hide_render_clear`           |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-H <objectmode->Ctrl-H->object.hide_render_set>`                            |:func:`blender:bpy.ops.object.hide_render_set`             |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`M <objectmode->M->object.move_to_layer>`                                        |:func:`blender:bpy.ops.object.move_to_layer`               |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`X <objectmode->X->object.delete>`                                               |:func:`blender:bpy.ops.object.delete`                      |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-X <objectmode->Shift-X->object.delete>`                                   |:func:`blender:bpy.ops.object.delete`                      |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`DEL <objectmode->DEL->object.delete>`                                           |:func:`blender:bpy.ops.object.delete`                      |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-DEL <objectmode->Shift-DEL->object.delete>`                               |:func:`blender:bpy.ops.object.delete`                      |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-A <objectmode->Shift-A->wm.call_menu>`                                    |:func:`blender:bpy.ops.wm.call_menu`                       |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Shift-A <objectmode->Ctrl-Shift-A->object.duplicates_make_real>`           |:func:`blender:bpy.ops.object.duplicates_make_real`        |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-A <objectmode->Ctrl-A->wm.call_menu>`                                      |:func:`blender:bpy.ops.wm.call_menu`                       |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`U <objectmode->U->wm.call_menu>`                                                |:func:`blender:bpy.ops.wm.call_menu`                       |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-L <objectmode->Ctrl-L->wm.call_menu>`                                      |:func:`blender:bpy.ops.wm.call_menu`                       |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-D <objectmode->Shift-D->object.duplicate_move>`                           |:func:`blender:bpy.ops.object.duplicate_move`              |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-D <objectmode->Alt-D->object.duplicate_move_linked>`                        |:func:`blender:bpy.ops.object.duplicate_move_linked`       |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-J <objectmode->Ctrl-J->object.join>`                                       |:func:`blender:bpy.ops.object.join`                        |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-C <objectmode->Alt-C->object.convert>`                                      |:func:`blender:bpy.ops.object.convert`                     |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Alt-P <objectmode->Ctrl-Alt-P->object.proxy_make>`                         |:func:`blender:bpy.ops.object.proxy_make`                  |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`L <objectmode->L->object.make_local>`                                           |:func:`blender:bpy.ops.object.make_local`                  |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`I <objectmode->I->anim.keyframe_insert_menu>`                                   |:func:`blender:bpy.ops.anim.keyframe_insert_menu`          |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-I <objectmode->Alt-I->anim.keyframe_delete_v3d>`                            |:func:`blender:bpy.ops.anim.keyframe_delete_v3d`           |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-I <objectmode->Ctrl-Shift-Alt-I->anim.keying_set_active_set>`    |:func:`blender:bpy.ops.anim.keying_set_active_set`         |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-G <objectmode->Ctrl-G->group.create>`                                      |:func:`blender:bpy.ops.group.create`                       |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Alt-G <objectmode->Ctrl-Alt-G->group.objects_remove>`                      |:func:`blender:bpy.ops.group.objects_remove`               |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-G <objectmode->Ctrl-Shift-Alt-G->group.objects_remove_all>`      |:func:`blender:bpy.ops.group.objects_remove_all`           |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Shift-G <objectmode->Ctrl-Shift-G->group.objects_add_active>`              |:func:`blender:bpy.ops.group.objects_add_active`           |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-Alt-G <objectmode->Shift-Alt-G->group.objects_remove_active>`             |:func:`blender:bpy.ops.group.objects_remove_active`        |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`W <objectmode->W->wm.call_menu>`                                                |:func:`blender:bpy.ops.wm.call_menu`                       |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Shift-T <objectmode->Ctrl-Shift-T->object.data_transfer>`                  |:func:`blender:bpy.ops.object.data_transfer`               |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-0 <objectmode->Ctrl-0->object.subdivision_set>`                            |:func:`blender:bpy.ops.object.subdivision_set`             |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-1 <objectmode->Ctrl-1->object.subdivision_set>`                            |:func:`blender:bpy.ops.object.subdivision_set`             |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-2 <objectmode->Ctrl-2->object.subdivision_set>`                            |:func:`blender:bpy.ops.object.subdivision_set`             |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-3 <objectmode->Ctrl-3->object.subdivision_set>`                            |:func:`blender:bpy.ops.object.subdivision_set`             |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-4 <objectmode->Ctrl-4->object.subdivision_set>`                            |:func:`blender:bpy.ops.object.subdivision_set`             |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-5 <objectmode->Ctrl-5->object.subdivision_set>`                            |:func:`blender:bpy.ops.object.subdivision_set`             |
+----------------------------------------------------------------------------------------+-----------------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkeyd:: Shift-O -> wm.context_cycle_enum

   Context Enum Cycle

   bpy.ops.wm.context_cycle_enum(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+----------------------------------------+
   |Properties:        |Values:                                 |
   +===================+========================================+
   |Context Attributes |tool_settings.proportional_edit_falloff |
   +-------------------+----------------------------------------+
   
   
.. km:hotkey:: Ctrl-A -> object.select_all

   (De)select All

   bpy.ops.object.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-G -> object.location_clear

   Clear Location

   bpy.ops.object.location_clear(clear_delta=False)
   
   
.. km:hotkeyd:: Alt-R -> object.rotation_clear

   Clear Rotation

   bpy.ops.object.rotation_clear(clear_delta=False)
   
   
.. km:hotkeyd:: Alt-S -> object.scale_clear

   Clear Scale

   bpy.ops.object.scale_clear(clear_delta=False)
   
   
.. km:hotkey:: A -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------------+
   |Properties: |Values:                |
   +============+=======================+
   |Name        |VIEW3D_MT_object_apply |
   +------------+-----------------------+
   
   
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
   
   
.. km:hotkeyd:: O -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+--------------------------------------------+
   |Properties:        |Values:                                     |
   +===================+============================================+
   |Context Attributes |tool_settings.use_proportional_edit_objects |
   +-------------------+--------------------------------------------+
   
   
.. km:hotkeyd:: P -> view3d.game_start

   Start Game Engine

   bpy.ops.view3d.game_start()
   
   
.. km:hotkeyd:: A -> object.select_all

   (De)select All

   bpy.ops.object.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> object.select_all

   (De)select All

   bpy.ops.object.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> object.select_more

   Select More

   bpy.ops.object.select_more()
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> object.select_less

   Select Less

   bpy.ops.object.select_less()
   
   
.. km:hotkeyd:: Shift-L -> object.select_linked

   Select Linked

   bpy.ops.object.select_linked(extend=False, type='OBDATA')
   
   
.. km:hotkeyd:: Shift-G -> object.select_grouped

   Select Grouped

   bpy.ops.object.select_grouped(extend=False, type='CHILDREN_RECURSIVE')
   
   
.. km:hotkeyd:: Ctrl-Shift-M -> object.select_mirror

   Select Mirror

   bpy.ops.object.select_mirror(extend=False)
   
   
.. km:hotkeyd:: LEFT_BRACKET -> object.select_hierarchy

   Select Hierarchy

   bpy.ops.object.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |PARENT  |
   +------------+--------+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-LEFT_BRACKET -> object.select_hierarchy

   Select Hierarchy

   bpy.ops.object.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |PARENT  |
   +------------+--------+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: RIGHT_BRACKET -> object.select_hierarchy

   Select Hierarchy

   bpy.ops.object.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |CHILD   |
   +------------+--------+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-RIGHT_BRACKET -> object.select_hierarchy

   Select Hierarchy

   bpy.ops.object.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |CHILD   |
   +------------+--------+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-P -> object.parent_set

   Make Parent

   bpy.ops.object.parent_set(type='OBJECT', xmirror=False, keep_transform=False)
   
   
.. km:hotkeyd:: Ctrl-Shift-P -> object.parent_no_inverse_set

   Make Parent without Inverse

   bpy.ops.object.parent_no_inverse_set()
   
   
.. km:hotkeyd:: Alt-P -> object.parent_clear

   Clear Parent

   bpy.ops.object.parent_clear(type='CLEAR')
   
   
.. km:hotkeyd:: Ctrl-T -> object.track_set

   Make Track

   bpy.ops.object.track_set(type='DAMPTRACK')
   
   
.. km:hotkeyd:: Alt-T -> object.track_clear

   Clear Track

   bpy.ops.object.track_clear(type='CLEAR')
   
   
.. km:hotkeyd:: Ctrl-Shift-C -> object.constraint_add_with_targets

   Add Constraint (with Targets)

   bpy.ops.object.constraint_add_with_targets(type='<UNKNOWN ENUM>')
   
   
.. km:hotkeyd:: Ctrl-Alt-C -> object.constraints_clear

   Clear Object Constraints

   bpy.ops.object.constraints_clear()
   
   
.. km:hotkeyd:: Alt-G -> object.location_clear

   Clear Location

   bpy.ops.object.location_clear(clear_delta=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Clear Delta |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-R -> object.rotation_clear

   Clear Rotation

   bpy.ops.object.rotation_clear(clear_delta=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Clear Delta |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-S -> object.scale_clear

   Clear Scale

   bpy.ops.object.scale_clear(clear_delta=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Clear Delta |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-G -> object.location_clear

   Clear Location

   bpy.ops.object.location_clear(clear_delta=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Clear Delta |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-R -> object.rotation_clear

   Clear Rotation

   bpy.ops.object.rotation_clear(clear_delta=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Clear Delta |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-S -> object.scale_clear

   Clear Scale

   bpy.ops.object.scale_clear(clear_delta=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Clear Delta |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-O -> object.origin_clear

   Clear Origin

   bpy.ops.object.origin_clear()
   
   
.. km:hotkeyd:: Alt-H -> object.hide_view_clear

   Clear Restrict View

   bpy.ops.object.hide_view_clear()
   
   
.. km:hotkeyd:: H -> object.hide_view_set

   Set Restrict View

   bpy.ops.object.hide_view_set(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> object.hide_view_set

   Set Restrict View

   bpy.ops.object.hide_view_set(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Alt-H -> object.hide_render_clear

   Clear Restrict Render

   bpy.ops.object.hide_render_clear()
   
   
.. km:hotkeyd:: Ctrl-H -> object.hide_render_set

   Set Restrict Render

   bpy.ops.object.hide_render_set(unselected=False)
   
   
.. km:hotkeyd:: M -> object.move_to_layer

   Move to Layer

   bpy.ops.object.move_to_layer(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   
   
.. km:hotkeyd:: X -> object.delete

   Delete

   bpy.ops.object.delete(use_global=False)
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Delete Globally |False   |
   +----------------+--------+
   
   
.. km:hotkeyd:: Shift-X -> object.delete

   Delete

   bpy.ops.object.delete(use_global=False)
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Delete Globally |True    |
   +----------------+--------+
   
   
.. km:hotkeyd:: DEL -> object.delete

   Delete

   bpy.ops.object.delete(use_global=False)
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Delete Globally |False   |
   +----------------+--------+
   
   
.. km:hotkeyd:: Shift-DEL -> object.delete

   Delete

   bpy.ops.object.delete(use_global=False)
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Delete Globally |True    |
   +----------------+--------+
   
   
.. km:hotkeyd:: Shift-A -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Name        |INFO_MT_add |
   +------------+------------+
   
   
.. km:hotkeyd:: Ctrl-Shift-A -> object.duplicates_make_real

   Make Duplicates Real

   bpy.ops.object.duplicates_make_real(use_base_parent=False, use_hierarchy=False)
   
   
.. km:hotkeyd:: Ctrl-A -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------------+
   |Properties: |Values:                |
   +============+=======================+
   |Name        |VIEW3D_MT_object_apply |
   +------------+-----------------------+
   
   
.. km:hotkeyd:: U -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------------------+
   |Properties: |Values:                    |
   +============+===========================+
   |Name        |VIEW3D_MT_make_single_user |
   +------------+---------------------------+
   
   
.. km:hotkeyd:: Ctrl-L -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------------+
   |Properties: |Values:              |
   +============+=====================+
   |Name        |VIEW3D_MT_make_links |
   +------------+---------------------+
   
   
.. km:hotkeyd:: Shift-D -> object.duplicate_move

   Duplicate Objects

   bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +------------------+--------+
   |Properties:       |Values: |
   +==================+========+
   |Duplicate Objects |N/A     |
   +------------------+--------+
   |Translate         |N/A     |
   +------------------+--------+
   
   
.. km:hotkeyd:: Alt-D -> object.duplicate_move_linked

   Duplicate Linked

   bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +------------------+--------+
   |Properties:       |Values: |
   +==================+========+
   |Duplicate Objects |N/A     |
   +------------------+--------+
   |Translate         |N/A     |
   +------------------+--------+
   
   
.. km:hotkeyd:: Ctrl-J -> object.join

   Join

   bpy.ops.object.join()
   
   
.. km:hotkeyd:: Alt-C -> object.convert

   Convert to

   bpy.ops.object.convert(target='MESH', keep_original=False)
   
   
.. km:hotkeyd:: Ctrl-Alt-P -> object.proxy_make

   Make Proxy

   bpy.ops.object.proxy_make(object='DEFAULT')
   
   
.. km:hotkeyd:: L -> object.make_local

   Make Local

   bpy.ops.object.make_local(type='SELECT_OBJECT')
   
   
.. km:hotkeyd:: I -> anim.keyframe_insert_menu

   Insert Keyframe Menu

   bpy.ops.anim.keyframe_insert_menu(type='DEFAULT', confirm_success=False, always_prompt=False)
   
   
.. km:hotkeyd:: Alt-I -> anim.keyframe_delete_v3d

   Delete Keyframe

   bpy.ops.anim.keyframe_delete_v3d()
   
   
.. km:hotkeyd:: Ctrl-Shift-Alt-I -> anim.keying_set_active_set

   Set Active Keying Set

   bpy.ops.anim.keying_set_active_set(type='DEFAULT')
   
   
.. km:hotkeyd:: Ctrl-G -> group.create

   Create New Group

   bpy.ops.group.create(name="Group")
   
   
.. km:hotkeyd:: Ctrl-Alt-G -> group.objects_remove

   Remove From Group

   bpy.ops.group.objects_remove(group='<UNKNOWN ENUM>')
   
   
.. km:hotkeyd:: Ctrl-Shift-Alt-G -> group.objects_remove_all

   Remove From All Groups

   bpy.ops.group.objects_remove_all()
   
   
.. km:hotkeyd:: Ctrl-Shift-G -> group.objects_add_active

   Add Selected To Active Group

   bpy.ops.group.objects_add_active(group='<UNKNOWN ENUM>')
   
   
.. km:hotkeyd:: Shift-Alt-G -> group.objects_remove_active

   Remove Selected From Active Group

   bpy.ops.group.objects_remove_active(group='<UNKNOWN ENUM>')
   
   
.. km:hotkeyd:: W -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+--------------------------+
   |Properties: |Values:                   |
   +============+==========================+
   |Name        |VIEW3D_MT_object_specials |
   +------------+--------------------------+
   
   
.. km:hotkeyd:: Ctrl-Shift-T -> object.data_transfer

   Transfer Mesh Data

   bpy.ops.object.data_transfer(use_reverse_transfer=False, use_freeze=False, data_type='<UNKNOWN ENUM>', use_create=True, vert_mapping='NEAREST', edge_mapping='NEAREST', loop_mapping='NEAREST_POLYNOR', poly_mapping='NEAREST', use_auto_transform=False, use_object_transform=True, use_max_distance=False, max_distance=1, ray_radius=0, islands_precision=0.1, layers_select_src='ACTIVE', layers_select_dst='ACTIVE', mix_mode='REPLACE', mix_factor=1)
   
   
.. km:hotkeyd:: Ctrl-0 -> object.subdivision_set

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |0       |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-1 -> object.subdivision_set

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |1       |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-2 -> object.subdivision_set

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |2       |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-3 -> object.subdivision_set

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |3       |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-4 -> object.subdivision_set

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |4       |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-5 -> object.subdivision_set

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |5       |
   +------------+--------+
   
   
