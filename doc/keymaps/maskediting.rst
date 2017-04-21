************
Mask Editing
************

.. km:module:: maskediting

   


---------------
Quick Reference
---------------

+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|Hotkey                                                                                           |Operator                                              |
+=================================================================================================+======================================================+
|:km:hk:`Shift-O <maskediting->Shift-O->wm.context_cycle_enum>`                                   |:func:`blender:bpy.ops.wm.context_cycle_enum`         |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <maskediting->Ctrl-SELECTMOUSE->mask.add_vertex_slide>`                 |:func:`blender:bpy.ops.mask.add_vertex_slide`         |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-A <maskediting->Ctrl-A->mask.select_all>`                                           |:func:`blender:bpy.ops.mask.select_all`               |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Alt-EVT_TWEAK_S <maskediting->Ctrl-Alt-EVT_TWEAK_S->mask.select_lasso>`             |:func:`blender:bpy.ops.mask.select_lasso`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-EVT_TWEAK_S <maskediting->Ctrl-Shift-Alt-EVT_TWEAK_S->mask.select_lasso>` |:func:`blender:bpy.ops.mask.select_lasso`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`SELECTMOUSE <maskediting->SELECTMOUSE->mask.slide_point>`                                |:func:`blender:bpy.ops.mask.slide_point`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`SELECTMOUSE <maskediting->SELECTMOUSE->mask.slide_spline_curvature>`                     |:func:`blender:bpy.ops.mask.slide_spline_curvature`   |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-ACTIONMOUSE <maskediting->Ctrl-ACTIONMOUSE->uv.cursor_set>`                         |:func:`blender:bpy.ops.uv.cursor_set`                 |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-N <maskediting->Alt-N->mask.new>`                                                    |:func:`blender:bpy.ops.mask.new`                      |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-A <maskediting->Shift-A->wm.call_menu>`                                            |:func:`blender:bpy.ops.wm.call_menu`                  |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-O <maskediting->Shift-O->wm.context_cycle_enum>`                                   |:func:`blender:bpy.ops.wm.context_cycle_enum`         |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`O <maskediting->O->wm.context_toggle>`                                                   |:func:`blender:bpy.ops.wm.context_toggle`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-ACTIONMOUSE <maskediting->Ctrl-ACTIONMOUSE->mask.add_vertex_slide>`                 |:func:`blender:bpy.ops.mask.add_vertex_slide`         |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-ACTIONMOUSE <maskediting->Shift-ACTIONMOUSE->mask.add_feather_vertex_slide>`       |:func:`blender:bpy.ops.mask.add_feather_vertex_slide` |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`X <maskediting->X->mask.delete>`                                                         |:func:`blender:bpy.ops.mask.delete`                   |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`DEL <maskediting->DEL->mask.delete>`                                                     |:func:`blender:bpy.ops.mask.delete`                   |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`SELECTMOUSE <maskediting->SELECTMOUSE->mask.select>`                                     |:func:`blender:bpy.ops.mask.select`                   |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <maskediting->Shift-SELECTMOUSE->mask.select>`                         |:func:`blender:bpy.ops.mask.select`                   |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`A <maskediting->A->mask.select_all>`                                                     |:func:`blender:bpy.ops.mask.select_all`               |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-I <maskediting->Ctrl-I->mask.select_all>`                                           |:func:`blender:bpy.ops.mask.select_all`               |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-L <maskediting->Ctrl-L->mask.select_linked>`                                        |:func:`blender:bpy.ops.mask.select_linked`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`L <maskediting->L->mask.select_linked_pick>`                                             |:func:`blender:bpy.ops.mask.select_linked_pick`       |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-L <maskediting->Shift-L->mask.select_linked_pick>`                                 |:func:`blender:bpy.ops.mask.select_linked_pick`       |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`B <maskediting->B->mask.select_border>`                                                  |:func:`blender:bpy.ops.mask.select_border`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`C <maskediting->C->mask.select_circle>`                                                  |:func:`blender:bpy.ops.mask.select_circle`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Alt-EVT_TWEAK_A <maskediting->Ctrl-Alt-EVT_TWEAK_A->mask.select_lasso>`             |:func:`blender:bpy.ops.mask.select_lasso`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-EVT_TWEAK_A <maskediting->Ctrl-Shift-Alt-EVT_TWEAK_A->mask.select_lasso>` |:func:`blender:bpy.ops.mask.select_lasso`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <maskediting->Ctrl-NUMPAD_PLUS->mask.select_more>`                      |:func:`blender:bpy.ops.mask.select_more`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <maskediting->Ctrl-NUMPAD_MINUS->mask.select_less>`                    |:func:`blender:bpy.ops.mask.select_less`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-H <maskediting->Alt-H->mask.hide_view_clear>`                                        |:func:`blender:bpy.ops.mask.hide_view_clear`          |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`H <maskediting->H->mask.hide_view_set>`                                                  |:func:`blender:bpy.ops.mask.hide_view_set`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-H <maskediting->Shift-H->mask.hide_view_set>`                                      |:func:`blender:bpy.ops.mask.hide_view_set`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <maskediting->Ctrl-SELECTMOUSE->clip.select>`                           |:func:`blender:bpy.ops.clip.select`                   |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-C <maskediting->Alt-C->mask.cyclic_toggle>`                                          |:func:`blender:bpy.ops.mask.cyclic_toggle`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`ACTIONMOUSE <maskediting->ACTIONMOUSE->mask.slide_point>`                                |:func:`blender:bpy.ops.mask.slide_point`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`ACTIONMOUSE <maskediting->ACTIONMOUSE->mask.slide_spline_curvature>`                     |:func:`blender:bpy.ops.mask.slide_spline_curvature`   |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`V <maskediting->V->mask.handle_type_set>`                                                |:func:`blender:bpy.ops.mask.handle_type_set`          |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-N <maskediting->Ctrl-N->mask.normals_make_consistent>`                              |:func:`blender:bpy.ops.mask.normals_make_consistent`  |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-P <maskediting->Ctrl-P->mask.parent_set>`                                           |:func:`blender:bpy.ops.mask.parent_set`               |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-P <maskediting->Alt-P->mask.parent_clear>`                                           |:func:`blender:bpy.ops.mask.parent_clear`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`I <maskediting->I->mask.shape_key_insert>`                                               |:func:`blender:bpy.ops.mask.shape_key_insert`         |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-I <maskediting->Alt-I->mask.shape_key_clear>`                                        |:func:`blender:bpy.ops.mask.shape_key_clear`          |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-D <maskediting->Shift-D->mask.duplicate_move>`                                     |:func:`blender:bpy.ops.mask.duplicate_move`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-C <maskediting->Ctrl-C->mask.copy_splines>`                                         |:func:`blender:bpy.ops.mask.copy_splines`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-V <maskediting->Ctrl-V->mask.paste_splines>`                                        |:func:`blender:bpy.ops.mask.paste_splines`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`ACTIONMOUSE <maskediting->ACTIONMOUSE->uv.cursor_set>`                                   |:func:`blender:bpy.ops.uv.cursor_set`                 |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`G <maskediting->G->transform.translate>`                                                 |:func:`blender:bpy.ops.transform.translate`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`EVT_TWEAK_S <maskediting->EVT_TWEAK_S->transform.translate>`                             |:func:`blender:bpy.ops.transform.translate`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`S <maskediting->S->transform.resize>`                                                    |:func:`blender:bpy.ops.transform.resize`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`R <maskediting->R->transform.rotate>`                                                    |:func:`blender:bpy.ops.transform.rotate`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-S <maskediting->Alt-S->transform.transform>`                                         |:func:`blender:bpy.ops.transform.transform`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+


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
   
   
.. km:hotkey:: Ctrl-SELECTMOUSE -> mask.add_vertex_slide

   Add Vertex and Slide

   bpy.ops.mask.add_vertex_slide(MASK_OT_add_vertex={"location":(0, 0)}, MASK_OT_slide_point={"slide_feather":False, "is_new_point":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Add Vertex  |N/A     |
   +------------+--------+
   |Slide Point |N/A     |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-A -> mask.select_all

   (De)select All

   bpy.ops.mask.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Alt-EVT_TWEAK_S -> mask.select_lasso

   Lasso Select

   bpy.ops.mask.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-Alt-EVT_TWEAK_S -> mask.select_lasso

   Lasso Select

   bpy.ops.mask.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkey:: SELECTMOUSE -> mask.slide_spline_curvature

   Slide Spline Curvature

   bpy.ops.mask.slide_spline_curvature()
   
   
.. km:hotkey:: Ctrl-ACTIONMOUSE -> uv.cursor_set

   Set 2D Cursor

   bpy.ops.uv.cursor_set(location=(0, 0))
   
   
.. km:hotkeyd:: Alt-N -> mask.new

   New Mask

   bpy.ops.mask.new(name="")
   
   
.. km:hotkeyd:: Shift-A -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Name        |MASK_MT_add |
   +------------+------------+
   
   
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
   
   
   +-------------------+-----------------------------------------+
   |Properties:        |Values:                                  |
   +===================+=========================================+
   |Context Attributes |tool_settings.use_proportional_edit_mask |
   +-------------------+-----------------------------------------+
   
   
.. km:hotkeyd:: Ctrl-ACTIONMOUSE -> mask.add_vertex_slide

   Add Vertex and Slide

   bpy.ops.mask.add_vertex_slide(MASK_OT_add_vertex={"location":(0, 0)}, MASK_OT_slide_point={"slide_feather":False, "is_new_point":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Add Vertex  |N/A     |
   +------------+--------+
   |Slide Point |N/A     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-ACTIONMOUSE -> mask.add_feather_vertex_slide

   Add Feather Vertex and Slide

   bpy.ops.mask.add_feather_vertex_slide(MASK_OT_add_feather_vertex={"location":(0, 0)}, MASK_OT_slide_point={"slide_feather":False, "is_new_point":False})
   
   
   +-------------------+--------+
   |Properties:        |Values: |
   +===================+========+
   |Add Feather Vertex |N/A     |
   +-------------------+--------+
   |Slide Point        |N/A     |
   +-------------------+--------+
   
   
.. km:hotkeyd:: X -> mask.delete

   Delete

   bpy.ops.mask.delete()
   
   
.. km:hotkeyd:: DEL -> mask.delete

   Delete

   bpy.ops.mask.delete()
   
   
.. km:hotkeyd:: SELECTMOUSE -> mask.select

   Select

   bpy.ops.mask.select(extend=False, deselect=False, toggle=False, location=(0, 0))
   
   
   +-----------------+--------+
   |Properties:      |Values: |
   +=================+========+
   |Extend           |False   |
   +-----------------+--------+
   |Deselect         |False   |
   +-----------------+--------+
   |Toggle Selection |False   |
   +-----------------+--------+
   
   
.. km:hotkeyd:: Shift-SELECTMOUSE -> mask.select

   Select

   bpy.ops.mask.select(extend=False, deselect=False, toggle=False, location=(0, 0))
   
   
   +-----------------+--------+
   |Properties:      |Values: |
   +=================+========+
   |Extend           |False   |
   +-----------------+--------+
   |Deselect         |False   |
   +-----------------+--------+
   |Toggle Selection |True    |
   +-----------------+--------+
   
   
.. km:hotkeyd:: A -> mask.select_all

   (De)select All

   bpy.ops.mask.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> mask.select_all

   (De)select All

   bpy.ops.mask.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-L -> mask.select_linked

   Select Linked All

   bpy.ops.mask.select_linked()
   
   
.. km:hotkeyd:: L -> mask.select_linked_pick

   Select Linked

   bpy.ops.mask.select_linked_pick(deselect=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-L -> mask.select_linked_pick

   Select Linked

   bpy.ops.mask.select_linked_pick(deselect=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: B -> mask.select_border

   Border Select

   bpy.ops.mask.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkeyd:: C -> mask.select_circle

   Circle Select

   bpy.ops.mask.select_circle(x=0, y=0, radius=1, gesture_mode=0)
   
   
.. km:hotkeyd:: Ctrl-Alt-EVT_TWEAK_A -> mask.select_lasso

   Lasso Select

   bpy.ops.mask.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-Alt-EVT_TWEAK_A -> mask.select_lasso

   Lasso Select

   bpy.ops.mask.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> mask.select_more

   Select More

   bpy.ops.mask.select_more()
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> mask.select_less

   Select Less

   bpy.ops.mask.select_less()
   
   
.. km:hotkeyd:: Alt-H -> mask.hide_view_clear

   Clear Restrict View

   bpy.ops.mask.hide_view_clear()
   
   
.. km:hotkeyd:: H -> mask.hide_view_set

   Set Restrict View

   bpy.ops.mask.hide_view_set(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> mask.hide_view_set

   Set Restrict View

   bpy.ops.mask.hide_view_set(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-SELECTMOUSE -> clip.select

   Select

   bpy.ops.clip.select(extend=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-C -> mask.cyclic_toggle

   Toggle Cyclic

   bpy.ops.mask.cyclic_toggle()
   
   
.. km:hotkeyd:: ACTIONMOUSE -> mask.slide_point

   Slide Point

   bpy.ops.mask.slide_point(slide_feather=False, is_new_point=False)
   
   
.. km:hotkeyd:: ACTIONMOUSE -> mask.slide_spline_curvature

   Slide Spline Curvature

   bpy.ops.mask.slide_spline_curvature()
   
   
.. km:hotkeyd:: V -> mask.handle_type_set

   Set Handle Type

   bpy.ops.mask.handle_type_set(type='AUTO')
   
   
.. km:hotkeyd:: Ctrl-N -> mask.normals_make_consistent

   Recalc Normals

   bpy.ops.mask.normals_make_consistent()
   
   
.. km:hotkeyd:: Ctrl-P -> mask.parent_set

   Make Parent

   bpy.ops.mask.parent_set()
   
   
.. km:hotkeyd:: Alt-P -> mask.parent_clear

   Clear Parent

   bpy.ops.mask.parent_clear()
   
   
.. km:hotkeyd:: I -> mask.shape_key_insert

   Insert Shape Key

   bpy.ops.mask.shape_key_insert()
   
   
.. km:hotkeyd:: Alt-I -> mask.shape_key_clear

   Clear Shape Key

   bpy.ops.mask.shape_key_clear()
   
   
.. km:hotkeyd:: Shift-D -> mask.duplicate_move

   Add Duplicate

   bpy.ops.mask.duplicate_move(MASK_OT_duplicate={}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Duplicate Mask |N/A     |
   +---------------+--------+
   |Translate      |N/A     |
   +---------------+--------+
   
   
.. km:hotkeyd:: Ctrl-C -> mask.copy_splines

   Copy Splines

   bpy.ops.mask.copy_splines()
   
   
.. km:hotkeyd:: Ctrl-V -> mask.paste_splines

   Paste Splines

   bpy.ops.mask.paste_splines()
   
   
.. km:hotkeyd:: ACTIONMOUSE -> uv.cursor_set

   Set 2D Cursor

   bpy.ops.uv.cursor_set(location=(0, 0))
   
   
.. km:hotkeyd:: G -> transform.translate

   Translate

   bpy.ops.transform.translate(value=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
.. km:hotkeyd:: EVT_TWEAK_S -> transform.translate

   Translate

   bpy.ops.transform.translate(value=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
.. km:hotkeyd:: S -> transform.resize

   Resize

   bpy.ops.transform.resize(value=(1, 1, 1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
.. km:hotkeyd:: R -> transform.rotate

   Rotate

   bpy.ops.transform.rotate(value=0, axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
.. km:hotkeyd:: Alt-S -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+------------------+
   |Properties: |Values:           |
   +============+==================+
   |Mode        |MASK_SHRINKFATTEN |
   +------------+------------------+
   
   
