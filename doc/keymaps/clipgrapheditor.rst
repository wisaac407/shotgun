*****************
Clip Graph Editor
*****************

.. km:module:: clipgrapheditor

   


---------------
Quick Reference
---------------

+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|Hotkey                                                                                   |Operator                                                |
+=========================================================================================+========================================================+
|:km:hk:`Ctrl-SELECTMOUSE <clipgrapheditor->Ctrl-SELECTMOUSE->clip.change_frame>`         |:func:`blender:bpy.ops.clip.change_frame`               |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-A <clipgrapheditor->Ctrl-A->clip.graph_select_all_markers>`                 |:func:`blender:bpy.ops.clip.graph_select_all_markers`   |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Any-EVT_TWEAK_L <clipgrapheditor->Any-EVT_TWEAK_L->clip.graph_select_border>`    |:func:`blender:bpy.ops.clip.graph_select_border`        |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`ACTIONMOUSE <clipgrapheditor->ACTIONMOUSE->clip.change_frame>`                   |:func:`blender:bpy.ops.clip.change_frame`               |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`SELECTMOUSE <clipgrapheditor->SELECTMOUSE->clip.graph_select>`                   |:func:`blender:bpy.ops.clip.graph_select`               |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <clipgrapheditor->Shift-SELECTMOUSE->clip.graph_select>`       |:func:`blender:bpy.ops.clip.graph_select`               |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`A <clipgrapheditor->A->clip.graph_select_all_markers>`                           |:func:`blender:bpy.ops.clip.graph_select_all_markers`   |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-I <clipgrapheditor->Ctrl-I->clip.graph_select_all_markers>`                 |:func:`blender:bpy.ops.clip.graph_select_all_markers`   |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`B <clipgrapheditor->B->clip.graph_select_border>`                                |:func:`blender:bpy.ops.clip.graph_select_border`        |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`DEL <clipgrapheditor->DEL->clip.graph_delete_curve>`                             |:func:`blender:bpy.ops.clip.graph_delete_curve`         |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`X <clipgrapheditor->X->clip.graph_delete_curve>`                                 |:func:`blender:bpy.ops.clip.graph_delete_curve`         |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-DEL <clipgrapheditor->Shift-DEL->clip.graph_delete_knot>`                  |:func:`blender:bpy.ops.clip.graph_delete_knot`          |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-X <clipgrapheditor->Shift-X->clip.graph_delete_knot>`                      |:func:`blender:bpy.ops.clip.graph_delete_knot`          |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`HOME <clipgrapheditor->HOME->clip.graph_view_all>`                               |:func:`blender:bpy.ops.clip.graph_view_all`             |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`NDOF_BUTTON_FIT <clipgrapheditor->NDOF_BUTTON_FIT->clip.graph_view_all>`         |:func:`blender:bpy.ops.clip.graph_view_all`             |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`NUMPAD_PERIOD <clipgrapheditor->NUMPAD_PERIOD->clip.graph_center_current_frame>` |:func:`blender:bpy.ops.clip.graph_center_current_frame` |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`L <clipgrapheditor->L->wm.context_toggle>`                                       |:func:`blender:bpy.ops.wm.context_toggle`               |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-T <clipgrapheditor->Alt-T->clip.clear_track_path>`                           |:func:`blender:bpy.ops.clip.clear_track_path`           |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-T <clipgrapheditor->Shift-T->clip.clear_track_path>`                       |:func:`blender:bpy.ops.clip.clear_track_path`           |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-Alt-T <clipgrapheditor->Shift-Alt-T->clip.clear_track_path>`               |:func:`blender:bpy.ops.clip.clear_track_path`           |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-D <clipgrapheditor->Shift-D->clip.graph_disable_markers>`                  |:func:`blender:bpy.ops.clip.graph_disable_markers`      |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`G <clipgrapheditor->G->transform.translate>`                                     |:func:`blender:bpy.ops.transform.translate`             |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`EVT_TWEAK_S <clipgrapheditor->EVT_TWEAK_S->transform.translate>`                 |:func:`blender:bpy.ops.transform.translate`             |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`S <clipgrapheditor->S->transform.resize>`                                        |:func:`blender:bpy.ops.transform.resize`                |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`R <clipgrapheditor->R->transform.rotate>`                                        |:func:`blender:bpy.ops.transform.rotate`                |
+-----------------------------------------------------------------------------------------+--------------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-SELECTMOUSE -> clip.change_frame

   Change Frame

   bpy.ops.clip.change_frame(frame=0)
   
   
.. km:hotkey:: Ctrl-A -> clip.graph_select_all_markers

   (De)select All Markers

   bpy.ops.clip.graph_select_all_markers(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Any-EVT_TWEAK_L -> clip.graph_select_border

   Border Select

   bpy.ops.clip.graph_select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkeyd:: ACTIONMOUSE -> clip.change_frame

   Change Frame

   bpy.ops.clip.change_frame(frame=0)
   
   
.. km:hotkeyd:: SELECTMOUSE -> clip.graph_select

   Select

   bpy.ops.clip.graph_select(location=(0, 0), extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-SELECTMOUSE -> clip.graph_select

   Select

   bpy.ops.clip.graph_select(location=(0, 0), extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: A -> clip.graph_select_all_markers

   (De)select All Markers

   bpy.ops.clip.graph_select_all_markers(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> clip.graph_select_all_markers

   (De)select All Markers

   bpy.ops.clip.graph_select_all_markers(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: B -> clip.graph_select_border

   Border Select

   bpy.ops.clip.graph_select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkeyd:: DEL -> clip.graph_delete_curve

   Delete Curve

   bpy.ops.clip.graph_delete_curve()
   
   
.. km:hotkeyd:: X -> clip.graph_delete_curve

   Delete Curve

   bpy.ops.clip.graph_delete_curve()
   
   
.. km:hotkeyd:: Shift-DEL -> clip.graph_delete_knot

   Delete Knot

   bpy.ops.clip.graph_delete_knot()
   
   
.. km:hotkeyd:: Shift-X -> clip.graph_delete_knot

   Delete Knot

   bpy.ops.clip.graph_delete_knot()
   
   
.. km:hotkeyd:: HOME -> clip.graph_view_all

   View All

   bpy.ops.clip.graph_view_all()
   
   
.. km:hotkeyd:: NDOF_BUTTON_FIT -> clip.graph_view_all

   View All

   bpy.ops.clip.graph_view_all()
   
   
.. km:hotkeyd:: NUMPAD_PERIOD -> clip.graph_center_current_frame

   Center Current Frame

   bpy.ops.clip.graph_center_current_frame()
   
   
.. km:hotkeyd:: L -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+----------------------------+
   |Properties:        |Values:                     |
   +===================+============================+
   |Context Attributes |space_data.lock_time_cursor |
   +-------------------+----------------------------+
   
   
.. km:hotkeyd:: Alt-T -> clip.clear_track_path

   Clear Track Path

   bpy.ops.clip.clear_track_path(action='REMAINED', clear_active=False)
   
   
   +-------------+---------+
   |Properties:  |Values:  |
   +=============+=========+
   |Action       |REMAINED |
   +-------------+---------+
   |Clear Active |True     |
   +-------------+---------+
   
   
.. km:hotkeyd:: Shift-T -> clip.clear_track_path

   Clear Track Path

   bpy.ops.clip.clear_track_path(action='REMAINED', clear_active=False)
   
   
   +-------------+--------+
   |Properties:  |Values: |
   +=============+========+
   |Action       |UPTO    |
   +-------------+--------+
   |Clear Active |True    |
   +-------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-T -> clip.clear_track_path

   Clear Track Path

   bpy.ops.clip.clear_track_path(action='REMAINED', clear_active=False)
   
   
   +-------------+--------+
   |Properties:  |Values: |
   +=============+========+
   |Action       |ALL     |
   +-------------+--------+
   |Clear Active |True    |
   +-------------+--------+
   
   
.. km:hotkeyd:: Shift-D -> clip.graph_disable_markers

   Disable Markers

   bpy.ops.clip.graph_disable_markers(action='DISABLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
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
   
   
