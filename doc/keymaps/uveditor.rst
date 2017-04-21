*********
UV Editor
*********

.. km:module:: uveditor

   


---------------
Quick Reference
---------------

+------------------------------------------------------------------------------------+-------------------------------------------------+
|Hotkey                                                                              |Operator                                         |
+====================================================================================+=================================================+
|:km:hk:`Shift-B <uveditor->Shift-B->uv.select_border>`                              |:func:`blender:bpy.ops.uv.select_border`         |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-EVT_TWEAK_S <uveditor->Ctrl-EVT_TWEAK_S->uv.select_lasso>`             |:func:`blender:bpy.ops.uv.select_lasso`          |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-Shift-EVT_TWEAK_S <uveditor->Ctrl-Shift-EVT_TWEAK_S->uv.select_lasso>` |:func:`blender:bpy.ops.uv.select_lasso`          |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-A <uveditor->Ctrl-A->uv.select_all>`                                   |:func:`blender:bpy.ops.uv.select_all`            |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-ACTIONMOUSE <uveditor->Ctrl-ACTIONMOUSE->uv.cursor_set>`               |:func:`blender:bpy.ops.uv.cursor_set`            |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-O <uveditor->Shift-O->wm.context_cycle_enum>`                         |:func:`blender:bpy.ops.wm.context_cycle_enum`    |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-Shift-Tab <uveditor->Ctrl-Shift-Tab->wm.context_menu_enum>`            |:func:`blender:bpy.ops.wm.context_menu_enum`     |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Q <uveditor->Q->wm.context_toggle>`                                         |:func:`blender:bpy.ops.wm.context_toggle`        |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-E <uveditor->Ctrl-E->uv.mark_seam>`                                    |:func:`blender:bpy.ops.uv.mark_seam`             |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`SELECTMOUSE <uveditor->SELECTMOUSE->uv.select>`                             |:func:`blender:bpy.ops.uv.select`                |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <uveditor->Shift-SELECTMOUSE->uv.select>`                 |:func:`blender:bpy.ops.uv.select`                |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Alt-SELECTMOUSE <uveditor->Alt-SELECTMOUSE->uv.select_loop>`                |:func:`blender:bpy.ops.uv.select_loop`           |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-Alt-SELECTMOUSE <uveditor->Shift-Alt-SELECTMOUSE->uv.select_loop>`    |:func:`blender:bpy.ops.uv.select_loop`           |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Y <uveditor->Y->uv.select_split>`                                           |:func:`blender:bpy.ops.uv.select_split`          |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`B <uveditor->B->uv.select_border>`                                          |:func:`blender:bpy.ops.uv.select_border`         |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-B <uveditor->Ctrl-B->uv.select_border>`                                |:func:`blender:bpy.ops.uv.select_border`         |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`C <uveditor->C->uv.circle_select>`                                          |:func:`blender:bpy.ops.uv.circle_select`         |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-EVT_TWEAK_A <uveditor->Ctrl-EVT_TWEAK_A->uv.select_lasso>`             |:func:`blender:bpy.ops.uv.select_lasso`          |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-Shift-EVT_TWEAK_A <uveditor->Ctrl-Shift-EVT_TWEAK_A->uv.select_lasso>` |:func:`blender:bpy.ops.uv.select_lasso`          |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-L <uveditor->Ctrl-L->uv.select_linked>`                                |:func:`blender:bpy.ops.uv.select_linked`         |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`L <uveditor->L->uv.select_linked_pick>`                                     |:func:`blender:bpy.ops.uv.select_linked_pick`    |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-Shift-L <uveditor->Ctrl-Shift-L->uv.select_linked>`                    |:func:`blender:bpy.ops.uv.select_linked`         |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-L <uveditor->Shift-L->uv.select_linked_pick>`                         |:func:`blender:bpy.ops.uv.select_linked_pick`    |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <uveditor->Ctrl-NUMPAD_PLUS->uv.select_more>`              |:func:`blender:bpy.ops.uv.select_more`           |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <uveditor->Ctrl-NUMPAD_MINUS->uv.select_less>`            |:func:`blender:bpy.ops.uv.select_less`           |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`A <uveditor->A->uv.select_all>`                                             |:func:`blender:bpy.ops.uv.select_all`            |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-I <uveditor->Ctrl-I->uv.select_all>`                                   |:func:`blender:bpy.ops.uv.select_all`            |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-P <uveditor->Shift-P->uv.select_pinned>`                              |:func:`blender:bpy.ops.uv.select_pinned`         |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`W <uveditor->W->wm.call_menu>`                                              |:func:`blender:bpy.ops.wm.call_menu`             |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`V <uveditor->V->uv.stitch>`                                                 |:func:`blender:bpy.ops.uv.stitch`                |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`P <uveditor->P->uv.pin>`                                                    |:func:`blender:bpy.ops.uv.pin`                   |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Alt-P <uveditor->Alt-P->uv.pin>`                                            |:func:`blender:bpy.ops.uv.pin`                   |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`E <uveditor->E->uv.unwrap>`                                                 |:func:`blender:bpy.ops.uv.unwrap`                |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-V <uveditor->Ctrl-V->uv.minimize_stretch>`                             |:func:`blender:bpy.ops.uv.minimize_stretch`      |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-P <uveditor->Ctrl-P->uv.pack_islands>`                                 |:func:`blender:bpy.ops.uv.pack_islands`          |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-A <uveditor->Ctrl-A->uv.average_islands_scale>`                        |:func:`blender:bpy.ops.uv.average_islands_scale` |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`H <uveditor->H->uv.hide>`                                                   |:func:`blender:bpy.ops.uv.hide`                  |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-H <uveditor->Shift-H->uv.hide>`                                       |:func:`blender:bpy.ops.uv.hide`                  |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Alt-H <uveditor->Alt-H->uv.reveal>`                                         |:func:`blender:bpy.ops.uv.reveal`                |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`ACTIONMOUSE <uveditor->ACTIONMOUSE->uv.cursor_set>`                         |:func:`blender:bpy.ops.uv.cursor_set`            |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-ACTIONMOUSE <uveditor->Shift-ACTIONMOUSE->uv.tile_set>`               |:func:`blender:bpy.ops.uv.tile_set`              |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-S <uveditor->Shift-S->wm.call_menu>`                                  |:func:`blender:bpy.ops.wm.call_menu`             |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-Tab <uveditor->Ctrl-Tab->wm.call_menu>`                                |:func:`blender:bpy.ops.wm.call_menu`             |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-O <uveditor->Shift-O->wm.context_cycle_enum>`                         |:func:`blender:bpy.ops.wm.context_cycle_enum`    |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`O <uveditor->O->wm.context_toggle_enum>`                                    |:func:`blender:bpy.ops.wm.context_toggle_enum`   |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`G <uveditor->G->transform.translate>`                                       |:func:`blender:bpy.ops.transform.translate`      |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`EVT_TWEAK_S <uveditor->EVT_TWEAK_S->transform.translate>`                   |:func:`blender:bpy.ops.transform.translate`      |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`R <uveditor->R->transform.rotate>`                                          |:func:`blender:bpy.ops.transform.rotate`         |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`S <uveditor->S->transform.resize>`                                          |:func:`blender:bpy.ops.transform.resize`         |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-S <uveditor->Ctrl-Shift-Alt-S->transform.shear>`             |:func:`blender:bpy.ops.transform.shear`          |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-M <uveditor->Ctrl-M->transform.mirror>`                                |:func:`blender:bpy.ops.transform.mirror`         |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-Tab <uveditor->Shift-Tab->wm.context_toggle>`                         |:func:`blender:bpy.ops.wm.context_toggle`        |
+------------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-Shift-Tab <uveditor->Ctrl-Shift-Tab->wm.context_menu_enum>`            |:func:`blender:bpy.ops.wm.context_menu_enum`     |
+------------------------------------------------------------------------------------+-------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Shift-B -> uv.select_border

   Border Select

   bpy.ops.uv.select_border(pinned=False, gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Pinned      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-EVT_TWEAK_S -> uv.select_lasso

   Lasso Select UV

   bpy.ops.uv.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-EVT_TWEAK_S -> uv.select_lasso

   Lasso Select UV

   bpy.ops.uv.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-A -> uv.select_all

   (De)select All

   bpy.ops.uv.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-ACTIONMOUSE -> uv.cursor_set

   Set 2D Cursor

   bpy.ops.uv.cursor_set(location=(0, 0))
   
   
.. km:hotkeyd:: Shift-O -> wm.context_cycle_enum

   Context Enum Cycle

   bpy.ops.wm.context_cycle_enum(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+----------------------------------------+
   |Properties:        |Values:                                 |
   +===================+========================================+
   |Context Attributes |tool_settings.proportional_edit_falloff |
   +-------------------+----------------------------------------+
   
   
.. km:hotkeyd:: Ctrl-Shift-Tab -> wm.context_menu_enum

   Context Enum Menu

   bpy.ops.wm.context_menu_enum(data_path="")
   
   
   +-------------------+------------------------------+
   |Properties:        |Values:                       |
   +===================+==============================+
   |Context Attributes |tool_settings.snap_uv_element |
   +-------------------+------------------------------+
   
   
.. km:hotkeyd:: Q -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+----------------------------+
   |Properties:        |Values:                     |
   +===================+============================+
   |Context Attributes |tool_settings.use_uv_sculpt |
   +-------------------+----------------------------+
   
   
.. km:hotkeyd:: Ctrl-E -> uv.mark_seam

   Mark Seam

   bpy.ops.uv.mark_seam(clear=False)
   
   
.. km:hotkeyd:: SELECTMOUSE -> uv.select

   Select

   bpy.ops.uv.select(extend=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-SELECTMOUSE -> uv.select

   Select

   bpy.ops.uv.select(extend=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-SELECTMOUSE -> uv.select_loop

   Loop Select

   bpy.ops.uv.select_loop(extend=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-SELECTMOUSE -> uv.select_loop

   Loop Select

   bpy.ops.uv.select_loop(extend=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Y -> uv.select_split

   Select Split

   bpy.ops.uv.select_split()
   
   
.. km:hotkeyd:: B -> uv.select_border

   Border Select

   bpy.ops.uv.select_border(pinned=False, gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Pinned      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-B -> uv.select_border

   Border Select

   bpy.ops.uv.select_border(pinned=False, gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Pinned      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: C -> uv.circle_select

   Circle Select

   bpy.ops.uv.circle_select(x=0, y=0, radius=1, gesture_mode=0)
   
   
.. km:hotkeyd:: Ctrl-EVT_TWEAK_A -> uv.select_lasso

   Lasso Select UV

   bpy.ops.uv.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-EVT_TWEAK_A -> uv.select_lasso

   Lasso Select UV

   bpy.ops.uv.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-L -> uv.select_linked

   Select Linked

   bpy.ops.uv.select_linked(extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: L -> uv.select_linked_pick

   Select Linked Pick

   bpy.ops.uv.select_linked_pick(extend=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-L -> uv.select_linked

   Select Linked

   bpy.ops.uv.select_linked(extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-L -> uv.select_linked_pick

   Select Linked Pick

   bpy.ops.uv.select_linked_pick(extend=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> uv.select_more

   Select More

   bpy.ops.uv.select_more()
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> uv.select_less

   Select Less

   bpy.ops.uv.select_less()
   
   
.. km:hotkeyd:: A -> uv.select_all

   (De)select All

   bpy.ops.uv.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> uv.select_all

   (De)select All

   bpy.ops.uv.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-P -> uv.select_pinned

   Selected Pinned

   bpy.ops.uv.select_pinned()
   
   
.. km:hotkeyd:: W -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------------+
   |Properties: |Values:                |
   +============+=======================+
   |Name        |IMAGE_MT_uvs_weldalign |
   +------------+-----------------------+
   
   
.. km:hotkeyd:: V -> uv.stitch

   Stitch

   bpy.ops.uv.stitch(use_limit=False, snap_islands=True, limit=0.01, static_island=0, midpoint_snap=False, clear_seams=True, mode='VERTEX', stored_mode='VERTEX', selection=[])
   
   
.. km:hotkeyd:: P -> uv.pin

   Pin

   bpy.ops.uv.pin(clear=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Clear       |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-P -> uv.pin

   Pin

   bpy.ops.uv.pin(clear=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Clear       |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: E -> uv.unwrap

   Unwrap

   bpy.ops.uv.unwrap(method='ANGLE_BASED', fill_holes=True, correct_aspect=True, use_subsurf_data=False, margin=0.001)
   
   
.. km:hotkeyd:: Ctrl-V -> uv.minimize_stretch

   Minimize Stretch

   bpy.ops.uv.minimize_stretch(fill_holes=True, blend=0, iterations=0)
   
   
.. km:hotkeyd:: Ctrl-P -> uv.pack_islands

   Pack Islands

   bpy.ops.uv.pack_islands(rotate=True, margin=0.001)
   
   
.. km:hotkeyd:: Ctrl-A -> uv.average_islands_scale

   Average Islands Scale

   bpy.ops.uv.average_islands_scale()
   
   
.. km:hotkeyd:: H -> uv.hide

   Hide Selected

   bpy.ops.uv.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> uv.hide

   Hide Selected

   bpy.ops.uv.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-H -> uv.reveal

   Reveal Hidden

   bpy.ops.uv.reveal()
   
   
.. km:hotkeyd:: ACTIONMOUSE -> uv.cursor_set

   Set 2D Cursor

   bpy.ops.uv.cursor_set(location=(0, 0))
   
   
.. km:hotkeyd:: Shift-ACTIONMOUSE -> uv.tile_set

   Set Tile

   bpy.ops.uv.tile_set(tile=(0, 0))
   
   
.. km:hotkeyd:: Shift-S -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------------+
   |Properties: |Values:           |
   +============+==================+
   |Name        |IMAGE_MT_uvs_snap |
   +------------+------------------+
   
   
.. km:hotkeyd:: Ctrl-Tab -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-------------------------+
   |Properties: |Values:                  |
   +============+=========================+
   |Name        |IMAGE_MT_uvs_select_mode |
   +------------+-------------------------+
   
   
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
   
   
.. km:hotkeyd:: G -> transform.translate

   Translate

   bpy.ops.transform.translate(value=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
.. km:hotkeyd:: EVT_TWEAK_S -> transform.translate

   Translate

   bpy.ops.transform.translate(value=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
.. km:hotkeyd:: R -> transform.rotate

   Rotate

   bpy.ops.transform.rotate(value=0, axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
.. km:hotkeyd:: S -> transform.resize

   Resize

   bpy.ops.transform.resize(value=(1, 1, 1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
.. km:hotkeyd:: Ctrl-Shift-Alt-S -> transform.shear

   Shear

   bpy.ops.transform.shear(value=0, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
.. km:hotkeyd:: Ctrl-M -> transform.mirror

   Mirror

   bpy.ops.transform.mirror(constraint_axis=(False, False, False), constraint_orientation='GLOBAL', proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, gpencil_strokes=False, release_confirm=False)
   
   
.. km:hotkeyd:: Shift-Tab -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |tool_settings.use_snap |
   +-------------------+-----------------------+
   
   
.. km:hotkeyd:: Ctrl-Shift-Tab -> wm.context_menu_enum

   Context Enum Menu

   bpy.ops.wm.context_menu_enum(data_path="")
   
   
   +-------------------+------------------------------+
   |Properties:        |Values:                       |
   +===================+==============================+
   |Context Attributes |tool_settings.snap_uv_element |
   +-------------------+------------------------------+
   
   
