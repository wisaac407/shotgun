***********
Clip Editor
***********

.. km:module:: clipeditor

   


---------------
Quick Reference
---------------

+------------------------------------------------------------------------------------------------+------------------------------------------------+
|Hotkey                                                                                          |Operator                                        |
+================================================================================================+================================================+
|:km:hk:`ACTIONMOUSE <clipeditor->ACTIONMOUSE->clip.view_pan>`                                   |:func:`blender:bpy.ops.clip.view_pan`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-A <clipeditor->Ctrl-A->clip.select_all>`                                           |:func:`blender:bpy.ops.clip.select_all`         |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-Alt-EVT_TWEAK_S <clipeditor->Ctrl-Alt-EVT_TWEAK_S->clip.select_lasso>`             |:func:`blender:bpy.ops.clip.select_lasso`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-EVT_TWEAK_S <clipeditor->Ctrl-Shift-Alt-EVT_TWEAK_S->clip.select_lasso>` |:func:`blender:bpy.ops.clip.select_lasso`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-ACTIONMOUSE <clipeditor->Ctrl-ACTIONMOUSE->clip.cursor_set>`                       |:func:`blender:bpy.ops.clip.cursor_set`         |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`MIDDLEMOUSE <clipeditor->MIDDLEMOUSE->clip.view_pan>`                                   |:func:`blender:bpy.ops.clip.view_pan`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-MIDDLEMOUSE <clipeditor->Shift-MIDDLEMOUSE->clip.view_pan>`                       |:func:`blender:bpy.ops.clip.view_pan`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`TRACKPADPAN <clipeditor->TRACKPADPAN->clip.view_pan>`                                   |:func:`blender:bpy.ops.clip.view_pan`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-MIDDLEMOUSE <clipeditor->Ctrl-MIDDLEMOUSE->clip.view_zoom>`                        |:func:`blender:bpy.ops.clip.view_zoom`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`TRACKPADZOOM <clipeditor->TRACKPADZOOM->clip.view_zoom>`                                |:func:`blender:bpy.ops.clip.view_zoom`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-TRACKPADPAN <clipeditor->Ctrl-TRACKPADPAN->clip.view_zoom>`                        |:func:`blender:bpy.ops.clip.view_zoom`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`WHEELINMOUSE <clipeditor->WHEELINMOUSE->clip.view_zoom_in>`                             |:func:`blender:bpy.ops.clip.view_zoom_in`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`WHEELOUTMOUSE <clipeditor->WHEELOUTMOUSE->clip.view_zoom_out>`                          |:func:`blender:bpy.ops.clip.view_zoom_out`      |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`NUMPAD_PLUS <clipeditor->NUMPAD_PLUS->clip.view_zoom_in>`                               |:func:`blender:bpy.ops.clip.view_zoom_in`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`NUMPAD_MINUS <clipeditor->NUMPAD_MINUS->clip.view_zoom_out>`                            |:func:`blender:bpy.ops.clip.view_zoom_out`      |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_8 <clipeditor->Ctrl-NUMPAD_8->clip.view_zoom_ratio>`                        |:func:`blender:bpy.ops.clip.view_zoom_ratio`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_4 <clipeditor->Ctrl-NUMPAD_4->clip.view_zoom_ratio>`                        |:func:`blender:bpy.ops.clip.view_zoom_ratio`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_2 <clipeditor->Ctrl-NUMPAD_2->clip.view_zoom_ratio>`                        |:func:`blender:bpy.ops.clip.view_zoom_ratio`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-NUMPAD_8 <clipeditor->Shift-NUMPAD_8->clip.view_zoom_ratio>`                      |:func:`blender:bpy.ops.clip.view_zoom_ratio`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-NUMPAD_4 <clipeditor->Shift-NUMPAD_4->clip.view_zoom_ratio>`                      |:func:`blender:bpy.ops.clip.view_zoom_ratio`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-NUMPAD_2 <clipeditor->Shift-NUMPAD_2->clip.view_zoom_ratio>`                      |:func:`blender:bpy.ops.clip.view_zoom_ratio`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`NUMPAD_1 <clipeditor->NUMPAD_1->clip.view_zoom_ratio>`                                  |:func:`blender:bpy.ops.clip.view_zoom_ratio`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`NUMPAD_2 <clipeditor->NUMPAD_2->clip.view_zoom_ratio>`                                  |:func:`blender:bpy.ops.clip.view_zoom_ratio`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`NUMPAD_4 <clipeditor->NUMPAD_4->clip.view_zoom_ratio>`                                  |:func:`blender:bpy.ops.clip.view_zoom_ratio`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`NUMPAD_8 <clipeditor->NUMPAD_8->clip.view_zoom_ratio>`                                  |:func:`blender:bpy.ops.clip.view_zoom_ratio`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`HOME <clipeditor->HOME->clip.view_all>`                                                 |:func:`blender:bpy.ops.clip.view_all`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`F <clipeditor->F->clip.view_all>`                                                       |:func:`blender:bpy.ops.clip.view_all`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`NUMPAD_PERIOD <clipeditor->NUMPAD_PERIOD->clip.view_selected>`                          |:func:`blender:bpy.ops.clip.view_selected`      |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`NDOF_BUTTON_FIT <clipeditor->NDOF_BUTTON_FIT->clip.view_all>`                           |:func:`blender:bpy.ops.clip.view_all`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`NDOF_MOTION <clipeditor->NDOF_MOTION->clip.view_ndof>`                                  |:func:`blender:bpy.ops.clip.view_ndof`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-Shift-LEFT_ARROW <clipeditor->Ctrl-Shift-LEFT_ARROW->clip.frame_jump>`             |:func:`blender:bpy.ops.clip.frame_jump`         |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-Shift-RIGHT_ARROW <clipeditor->Ctrl-Shift-RIGHT_ARROW->clip.frame_jump>`           |:func:`blender:bpy.ops.clip.frame_jump`         |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-Alt-LEFT_ARROW <clipeditor->Shift-Alt-LEFT_ARROW->clip.frame_jump>`               |:func:`blender:bpy.ops.clip.frame_jump`         |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-Alt-RIGHT_ARROW <clipeditor->Shift-Alt-RIGHT_ARROW->clip.frame_jump>`             |:func:`blender:bpy.ops.clip.frame_jump`         |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`LEFTMOUSE <clipeditor->LEFTMOUSE->clip.change_frame>`                                   |:func:`blender:bpy.ops.clip.change_frame`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`SELECTMOUSE <clipeditor->SELECTMOUSE->clip.select>`                                     |:func:`blender:bpy.ops.clip.select`             |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <clipeditor->Shift-SELECTMOUSE->clip.select>`                         |:func:`blender:bpy.ops.clip.select`             |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`A <clipeditor->A->clip.select_all>`                                                     |:func:`blender:bpy.ops.clip.select_all`         |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-I <clipeditor->Ctrl-I->clip.select_all>`                                           |:func:`blender:bpy.ops.clip.select_all`         |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`B <clipeditor->B->clip.select_border>`                                                  |:func:`blender:bpy.ops.clip.select_border`      |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`C <clipeditor->C->clip.select_circle>`                                                  |:func:`blender:bpy.ops.clip.select_circle`      |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-G <clipeditor->Shift-G->wm.call_menu>`                                            |:func:`blender:bpy.ops.wm.call_menu`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-Alt-EVT_TWEAK_A <clipeditor->Ctrl-Alt-EVT_TWEAK_A->clip.select_lasso>`             |:func:`blender:bpy.ops.clip.select_lasso`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-EVT_TWEAK_A <clipeditor->Ctrl-Shift-Alt-EVT_TWEAK_A->clip.select_lasso>` |:func:`blender:bpy.ops.clip.select_lasso`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-LEFTMOUSE <clipeditor->Ctrl-LEFTMOUSE->clip.add_marker_slide>`                     |:func:`blender:bpy.ops.clip.add_marker_slide`   |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-DEL <clipeditor->Shift-DEL->clip.delete_marker>`                                  |:func:`blender:bpy.ops.clip.delete_marker`      |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-X <clipeditor->Shift-X->clip.delete_marker>`                                      |:func:`blender:bpy.ops.clip.delete_marker`      |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`LEFTMOUSE <clipeditor->LEFTMOUSE->clip.slide_marker>`                                   |:func:`blender:bpy.ops.clip.slide_marker`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-D <clipeditor->Shift-D->clip.disable_markers>`                                    |:func:`blender:bpy.ops.clip.disable_markers`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`DEL <clipeditor->DEL->clip.delete_track>`                                               |:func:`blender:bpy.ops.clip.delete_track`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`X <clipeditor->X->clip.delete_track>`                                                   |:func:`blender:bpy.ops.clip.delete_track`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-L <clipeditor->Ctrl-L->clip.lock_tracks>`                                          |:func:`blender:bpy.ops.clip.lock_tracks`        |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Alt-L <clipeditor->Alt-L->clip.lock_tracks>`                                            |:func:`blender:bpy.ops.clip.lock_tracks`        |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`H <clipeditor->H->clip.hide_tracks>`                                                    |:func:`blender:bpy.ops.clip.hide_tracks`        |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-H <clipeditor->Shift-H->clip.hide_tracks>`                                        |:func:`blender:bpy.ops.clip.hide_tracks`        |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Alt-H <clipeditor->Alt-H->clip.hide_tracks_clear>`                                      |:func:`blender:bpy.ops.clip.hide_tracks_clear`  |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`ACTIONMOUSE <clipeditor->ACTIONMOUSE->clip.slide_plane_marker>`                         |:func:`blender:bpy.ops.clip.slide_plane_marker` |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`I <clipeditor->I->clip.keyframe_insert>`                                                |:func:`blender:bpy.ops.clip.keyframe_insert`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Alt-I <clipeditor->Alt-I->clip.keyframe_delete>`                                        |:func:`blender:bpy.ops.clip.keyframe_delete`    |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-J <clipeditor->Ctrl-J->clip.join_tracks>`                                          |:func:`blender:bpy.ops.clip.join_tracks`        |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`W <clipeditor->W->wm.call_menu>`                                                        |:func:`blender:bpy.ops.wm.call_menu`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`L <clipeditor->L->wm.context_toggle>`                                                   |:func:`blender:bpy.ops.wm.context_toggle`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Alt-D <clipeditor->Alt-D->wm.context_toggle>`                                           |:func:`blender:bpy.ops.wm.context_toggle`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Alt-S <clipeditor->Alt-S->wm.context_toggle>`                                           |:func:`blender:bpy.ops.wm.context_toggle`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`M <clipeditor->M->wm.context_toggle>`                                                   |:func:`blender:bpy.ops.wm.context_toggle`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`G <clipeditor->G->transform.translate>`                                                 |:func:`blender:bpy.ops.transform.translate`     |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`EVT_TWEAK_S <clipeditor->EVT_TWEAK_S->transform.translate>`                             |:func:`blender:bpy.ops.transform.translate`     |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`S <clipeditor->S->transform.resize>`                                                    |:func:`blender:bpy.ops.transform.resize`        |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`R <clipeditor->R->transform.rotate>`                                                    |:func:`blender:bpy.ops.transform.rotate`        |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Alt-T <clipeditor->Alt-T->clip.clear_track_path>`                                       |:func:`blender:bpy.ops.clip.clear_track_path`   |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-T <clipeditor->Shift-T->clip.clear_track_path>`                                   |:func:`blender:bpy.ops.clip.clear_track_path`   |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-Alt-T <clipeditor->Shift-Alt-T->clip.clear_track_path>`                           |:func:`blender:bpy.ops.clip.clear_track_path`   |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`ACTIONMOUSE <clipeditor->ACTIONMOUSE->clip.cursor_set>`                                 |:func:`blender:bpy.ops.clip.cursor_set`         |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`, <clipeditor->,->wm.context_set_enum>`                                                 |:func:`blender:bpy.ops.wm.context_set_enum`     |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-, <clipeditor->Ctrl-,->wm.context_set_enum>`                                       |:func:`blender:bpy.ops.wm.context_set_enum`     |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`. <clipeditor->.->wm.context_set_enum>`                                                 |:func:`blender:bpy.ops.wm.context_set_enum`     |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-. <clipeditor->Ctrl-.->wm.context_set_enum>`                                       |:func:`blender:bpy.ops.wm.context_set_enum`     |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-C <clipeditor->Ctrl-C->clip.copy_tracks>`                                          |:func:`blender:bpy.ops.clip.copy_tracks`        |
+------------------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-V <clipeditor->Ctrl-V->clip.paste_tracks>`                                         |:func:`blender:bpy.ops.clip.paste_tracks`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: ACTIONMOUSE -> clip.view_pan

   View Pan

   bpy.ops.clip.view_pan(offset=(0, 0))
   
   
.. km:hotkey:: Ctrl-A -> clip.select_all

   (De)select All

   bpy.ops.clip.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Alt-EVT_TWEAK_S -> clip.select_lasso

   Lasso Select

   bpy.ops.clip.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-Alt-EVT_TWEAK_S -> clip.select_lasso

   Lasso Select

   bpy.ops.clip.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-ACTIONMOUSE -> clip.cursor_set

   Set 2D Cursor

   bpy.ops.clip.cursor_set(location=(0, 0))
   
   
.. km:hotkeyd:: MIDDLEMOUSE -> clip.view_pan

   View Pan

   bpy.ops.clip.view_pan(offset=(0, 0))
   
   
.. km:hotkeyd:: Shift-MIDDLEMOUSE -> clip.view_pan

   View Pan

   bpy.ops.clip.view_pan(offset=(0, 0))
   
   
.. km:hotkeyd:: TRACKPADPAN -> clip.view_pan

   View Pan

   bpy.ops.clip.view_pan(offset=(0, 0))
   
   
.. km:hotkeyd:: Ctrl-MIDDLEMOUSE -> clip.view_zoom

   View Zoom

   bpy.ops.clip.view_zoom(factor=0)
   
   
.. km:hotkeyd:: TRACKPADZOOM -> clip.view_zoom

   View Zoom

   bpy.ops.clip.view_zoom(factor=0)
   
   
.. km:hotkeyd:: Ctrl-TRACKPADPAN -> clip.view_zoom

   View Zoom

   bpy.ops.clip.view_zoom(factor=0)
   
   
.. km:hotkeyd:: WHEELINMOUSE -> clip.view_zoom_in

   View Zoom In

   bpy.ops.clip.view_zoom_in(location=(0, 0))
   
   
.. km:hotkeyd:: WHEELOUTMOUSE -> clip.view_zoom_out

   View Zoom Out

   bpy.ops.clip.view_zoom_out(location=(0, 0))
   
   
.. km:hotkeyd:: NUMPAD_PLUS -> clip.view_zoom_in

   View Zoom In

   bpy.ops.clip.view_zoom_in(location=(0, 0))
   
   
.. km:hotkeyd:: NUMPAD_MINUS -> clip.view_zoom_out

   View Zoom Out

   bpy.ops.clip.view_zoom_out(location=(0, 0))
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_8 -> clip.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.clip.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |8.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_4 -> clip.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.clip.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |4.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_2 -> clip.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.clip.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |2.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-NUMPAD_8 -> clip.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.clip.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |8.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-NUMPAD_4 -> clip.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.clip.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |4.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-NUMPAD_2 -> clip.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.clip.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |2.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_1 -> clip.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.clip.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |1.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_2 -> clip.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.clip.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |0.5     |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_4 -> clip.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.clip.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |0.25    |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_8 -> clip.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.clip.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |0.125   |
   +------------+--------+
   
   
.. km:hotkeyd:: HOME -> clip.view_all

   View All

   bpy.ops.clip.view_all(fit_view=False)
   
   
.. km:hotkeyd:: F -> clip.view_all

   View All

   bpy.ops.clip.view_all(fit_view=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Fit View    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_PERIOD -> clip.view_selected

   View Selected

   bpy.ops.clip.view_selected()
   
   
.. km:hotkeyd:: NDOF_BUTTON_FIT -> clip.view_all

   View All

   bpy.ops.clip.view_all(fit_view=False)
   
   
.. km:hotkeyd:: NDOF_MOTION -> clip.view_ndof

   NDOF Pan/Zoom

   bpy.ops.clip.view_ndof()
   
   
.. km:hotkeyd:: Ctrl-Shift-LEFT_ARROW -> clip.frame_jump

   Jump to Frame

   bpy.ops.clip.frame_jump(position='PATHSTART')
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Position    |PATHSTART |
   +------------+----------+
   
   
.. km:hotkeyd:: Ctrl-Shift-RIGHT_ARROW -> clip.frame_jump

   Jump to Frame

   bpy.ops.clip.frame_jump(position='PATHSTART')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Position    |PATHEND |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-LEFT_ARROW -> clip.frame_jump

   Jump to Frame

   bpy.ops.clip.frame_jump(position='PATHSTART')
   
   
   +------------+-----------+
   |Properties: |Values:    |
   +============+===========+
   |Position    |FAILEDPREV |
   +------------+-----------+
   
   
.. km:hotkeyd:: Shift-Alt-RIGHT_ARROW -> clip.frame_jump

   Jump to Frame

   bpy.ops.clip.frame_jump(position='PATHSTART')
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Position    |PATHSTART |
   +------------+----------+
   
   
.. km:hotkeyd:: LEFTMOUSE -> clip.change_frame

   Change Frame

   bpy.ops.clip.change_frame(frame=0)
   
   
.. km:hotkeyd:: SELECTMOUSE -> clip.select

   Select

   bpy.ops.clip.select(extend=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-SELECTMOUSE -> clip.select

   Select

   bpy.ops.clip.select(extend=False, location=(0, 0))
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: A -> clip.select_all

   (De)select All

   bpy.ops.clip.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> clip.select_all

   (De)select All

   bpy.ops.clip.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: B -> clip.select_border

   Border Select

   bpy.ops.clip.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkeyd:: C -> clip.select_circle

   Circle Select

   bpy.ops.clip.select_circle(x=0, y=0, radius=1, gesture_mode=0)
   
   
.. km:hotkeyd:: Shift-G -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------------+
   |Properties: |Values:                |
   +============+=======================+
   |Name        |CLIP_MT_select_grouped |
   +------------+-----------------------+
   
   
.. km:hotkeyd:: Ctrl-Alt-EVT_TWEAK_A -> clip.select_lasso

   Lasso Select

   bpy.ops.clip.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-Alt-EVT_TWEAK_A -> clip.select_lasso

   Lasso Select

   bpy.ops.clip.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-LEFTMOUSE -> clip.add_marker_slide

   Add Marker and Slide

   bpy.ops.clip.add_marker_slide(CLIP_OT_add_marker={"location":(0, 0)}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Add Marker  |N/A     |
   +------------+--------+
   |Translate   |N/A     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-DEL -> clip.delete_marker

   Delete Marker

   bpy.ops.clip.delete_marker()
   
   
.. km:hotkeyd:: Shift-X -> clip.delete_marker

   Delete Marker

   bpy.ops.clip.delete_marker()
   
   
.. km:hotkeyd:: LEFTMOUSE -> clip.slide_marker

   Slide Marker

   bpy.ops.clip.slide_marker(offset=(0, 0))
   
   
.. km:hotkeyd:: Shift-D -> clip.disable_markers

   Disable Markers

   bpy.ops.clip.disable_markers(action='DISABLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: DEL -> clip.delete_track

   Delete Track

   bpy.ops.clip.delete_track()
   
   
.. km:hotkeyd:: X -> clip.delete_track

   Delete Track

   bpy.ops.clip.delete_track()
   
   
.. km:hotkeyd:: Ctrl-L -> clip.lock_tracks

   Lock Tracks

   bpy.ops.clip.lock_tracks(action='LOCK')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |LOCK    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-L -> clip.lock_tracks

   Lock Tracks

   bpy.ops.clip.lock_tracks(action='LOCK')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |UNLOCK  |
   +------------+--------+
   
   
.. km:hotkeyd:: H -> clip.hide_tracks

   Hide Tracks

   bpy.ops.clip.hide_tracks(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> clip.hide_tracks

   Hide Tracks

   bpy.ops.clip.hide_tracks(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-H -> clip.hide_tracks_clear

   Hide Tracks Clear

   bpy.ops.clip.hide_tracks_clear()
   
   
.. km:hotkeyd:: ACTIONMOUSE -> clip.slide_plane_marker

   Slide Plane Marker

   bpy.ops.clip.slide_plane_marker()
   
   
.. km:hotkeyd:: I -> clip.keyframe_insert

   Insert keyframe

   bpy.ops.clip.keyframe_insert()
   
   
.. km:hotkeyd:: Alt-I -> clip.keyframe_delete

   Delete keyframe

   bpy.ops.clip.keyframe_delete()
   
   
.. km:hotkeyd:: Ctrl-J -> clip.join_tracks

   Join Tracks

   bpy.ops.clip.join_tracks()
   
   
.. km:hotkeyd:: W -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+--------------------------+
   |Properties: |Values:                   |
   +============+==========================+
   |Name        |CLIP_MT_tracking_specials |
   +------------+--------------------------+
   
   
.. km:hotkeyd:: L -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+--------------------------+
   |Properties:        |Values:                   |
   +===================+==========================+
   |Context Attributes |space_data.lock_selection |
   +-------------------+--------------------------+
   
   
.. km:hotkeyd:: Alt-D -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+-------------------------+
   |Properties:        |Values:                  |
   +===================+=========================+
   |Context Attributes |space_data.show_disabled |
   +-------------------+-------------------------+
   
   
.. km:hotkeyd:: Alt-S -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+------------------------------+
   |Properties:        |Values:                       |
   +===================+==============================+
   |Context Attributes |space_data.show_marker_search |
   +-------------------+------------------------------+
   
   
.. km:hotkeyd:: M -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+----------------------------+
   |Properties:        |Values:                     |
   +===================+============================+
   |Context Attributes |space_data.use_mute_footage |
   +-------------------+----------------------------+
   
   
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
   
   
.. km:hotkeyd:: Alt-T -> clip.clear_track_path

   Clear Track Path

   bpy.ops.clip.clear_track_path(action='REMAINED', clear_active=False)
   
   
   +-------------+---------+
   |Properties:  |Values:  |
   +=============+=========+
   |Action       |REMAINED |
   +-------------+---------+
   |Clear Active |False    |
   +-------------+---------+
   
   
.. km:hotkeyd:: Shift-T -> clip.clear_track_path

   Clear Track Path

   bpy.ops.clip.clear_track_path(action='REMAINED', clear_active=False)
   
   
   +-------------+--------+
   |Properties:  |Values: |
   +=============+========+
   |Action       |UPTO    |
   +-------------+--------+
   |Clear Active |False   |
   +-------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-T -> clip.clear_track_path

   Clear Track Path

   bpy.ops.clip.clear_track_path(action='REMAINED', clear_active=False)
   
   
   +-------------+--------+
   |Properties:  |Values: |
   +=============+========+
   |Action       |ALL     |
   +-------------+--------+
   |Clear Active |False   |
   +-------------+--------+
   
   
.. km:hotkeyd:: ACTIONMOUSE -> clip.cursor_set

   Set 2D Cursor

   bpy.ops.clip.cursor_set(location=(0, 0))
   
   
.. km:hotkeyd:: , -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |space_data.pivot_point |
   +-------------------+-----------------------+
   |Value              |BOUNDING_BOX_CENTER    |
   +-------------------+-----------------------+
   
   
.. km:hotkeyd:: Ctrl-, -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |space_data.pivot_point |
   +-------------------+-----------------------+
   |Value              |MEDIAN_POINT           |
   +-------------------+-----------------------+
   
   
.. km:hotkeyd:: . -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |space_data.pivot_point |
   +-------------------+-----------------------+
   |Value              |CURSOR                 |
   +-------------------+-----------------------+
   
   
.. km:hotkeyd:: Ctrl-. -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |space_data.pivot_point |
   +-------------------+-----------------------+
   |Value              |INDIVIDUAL_ORIGINS     |
   +-------------------+-----------------------+
   
   
.. km:hotkeyd:: Ctrl-C -> clip.copy_tracks

   Copy Tracks

   bpy.ops.clip.copy_tracks()
   
   
.. km:hotkeyd:: Ctrl-V -> clip.paste_tracks

   Paste Tracks

   bpy.ops.clip.paste_tracks()
   
   
