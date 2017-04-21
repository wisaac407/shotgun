*****
Image
*****

.. km:module:: image

   


---------------
Quick Reference
---------------

+------------------------------------------------------------------------------+--------------------------------------------------+
|Hotkey                                                                        |Operator                                          |
+==============================================================================+==================================================+
|:km:hk:`F <image->F->image.view_all>`                                         |:func:`blender:bpy.ops.image.view_all`            |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`ACTIONMOUSE <image->ACTIONMOUSE->image.view_pan>`                     |:func:`blender:bpy.ops.image.view_pan`            |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`SELECTMOUSE <image->SELECTMOUSE->image.sample>`                       |:func:`blender:bpy.ops.image.sample`              |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Tab <image->Tab->object.mode_set>`                                    |:func:`blender:bpy.ops.object.mode_set`           |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`1 <image->1->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`2 <image->2->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`3 <image->3->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`4 <image->4->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`5 <image->5->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`6 <image->6->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`7 <image->7->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`8 <image->8->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`9 <image->9->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`HOME <image->HOME->image.view_all>`                                   |:func:`blender:bpy.ops.image.view_all`            |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Shift-HOME <image->Shift-HOME->image.view_all>`                       |:func:`blender:bpy.ops.image.view_all`            |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`NUMPAD_PERIOD <image->NUMPAD_PERIOD->image.view_selected>`            |:func:`blender:bpy.ops.image.view_selected`       |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`MIDDLEMOUSE <image->MIDDLEMOUSE->image.view_pan>`                     |:func:`blender:bpy.ops.image.view_pan`            |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Shift-MIDDLEMOUSE <image->Shift-MIDDLEMOUSE->image.view_pan>`         |:func:`blender:bpy.ops.image.view_pan`            |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`TRACKPADPAN <image->TRACKPADPAN->image.view_pan>`                     |:func:`blender:bpy.ops.image.view_pan`            |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`NDOF_BUTTON_FIT <image->NDOF_BUTTON_FIT->image.view_all>`             |:func:`blender:bpy.ops.image.view_all`            |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`NDOF_MOTION <image->NDOF_MOTION->image.view_ndof>`                    |:func:`blender:bpy.ops.image.view_ndof`           |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`WHEELINMOUSE <image->WHEELINMOUSE->image.view_zoom_in>`               |:func:`blender:bpy.ops.image.view_zoom_in`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`WHEELOUTMOUSE <image->WHEELOUTMOUSE->image.view_zoom_out>`            |:func:`blender:bpy.ops.image.view_zoom_out`       |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`NUMPAD_PLUS <image->NUMPAD_PLUS->image.view_zoom_in>`                 |:func:`blender:bpy.ops.image.view_zoom_in`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`NUMPAD_MINUS <image->NUMPAD_MINUS->image.view_zoom_out>`              |:func:`blender:bpy.ops.image.view_zoom_out`       |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Ctrl-MIDDLEMOUSE <image->Ctrl-MIDDLEMOUSE->image.view_zoom>`          |:func:`blender:bpy.ops.image.view_zoom`           |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`TRACKPADZOOM <image->TRACKPADZOOM->image.view_zoom>`                  |:func:`blender:bpy.ops.image.view_zoom`           |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Ctrl-TRACKPADPAN <image->Ctrl-TRACKPADPAN->image.view_zoom>`          |:func:`blender:bpy.ops.image.view_zoom`           |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Shift-B <image->Shift-B->image.view_zoom_border>`                     |:func:`blender:bpy.ops.image.view_zoom_border`    |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_8 <image->Ctrl-NUMPAD_8->image.view_zoom_ratio>`          |:func:`blender:bpy.ops.image.view_zoom_ratio`     |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_4 <image->Ctrl-NUMPAD_4->image.view_zoom_ratio>`          |:func:`blender:bpy.ops.image.view_zoom_ratio`     |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_2 <image->Ctrl-NUMPAD_2->image.view_zoom_ratio>`          |:func:`blender:bpy.ops.image.view_zoom_ratio`     |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Shift-NUMPAD_8 <image->Shift-NUMPAD_8->image.view_zoom_ratio>`        |:func:`blender:bpy.ops.image.view_zoom_ratio`     |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Shift-NUMPAD_4 <image->Shift-NUMPAD_4->image.view_zoom_ratio>`        |:func:`blender:bpy.ops.image.view_zoom_ratio`     |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Shift-NUMPAD_2 <image->Shift-NUMPAD_2->image.view_zoom_ratio>`        |:func:`blender:bpy.ops.image.view_zoom_ratio`     |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`NUMPAD_1 <image->NUMPAD_1->image.view_zoom_ratio>`                    |:func:`blender:bpy.ops.image.view_zoom_ratio`     |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`NUMPAD_2 <image->NUMPAD_2->image.view_zoom_ratio>`                    |:func:`blender:bpy.ops.image.view_zoom_ratio`     |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`NUMPAD_4 <image->NUMPAD_4->image.view_zoom_ratio>`                    |:func:`blender:bpy.ops.image.view_zoom_ratio`     |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`NUMPAD_8 <image->NUMPAD_8->image.view_zoom_ratio>`                    |:func:`blender:bpy.ops.image.view_zoom_ratio`     |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`LEFTMOUSE <image->LEFTMOUSE->image.change_frame>`                     |:func:`blender:bpy.ops.image.change_frame`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`ACTIONMOUSE <image->ACTIONMOUSE->image.sample>`                       |:func:`blender:bpy.ops.image.sample`              |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Ctrl-ACTIONMOUSE <image->Ctrl-ACTIONMOUSE->image.curves_point_set>`   |:func:`blender:bpy.ops.image.curves_point_set`    |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Shift-ACTIONMOUSE <image->Shift-ACTIONMOUSE->image.curves_point_set>` |:func:`blender:bpy.ops.image.curves_point_set`    |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Tab <image->Tab->object.mode_set>`                                    |:func:`blender:bpy.ops.object.mode_set`           |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`1 <image->1->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`2 <image->2->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`3 <image->3->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`4 <image->4->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`5 <image->5->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`6 <image->6->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`7 <image->7->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`8 <image->8->wm.context_set_int>`                                     |:func:`blender:bpy.ops.wm.context_set_int`        |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`, <image->,->wm.context_set_enum>`                                    |:func:`blender:bpy.ops.wm.context_set_enum`       |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Ctrl-, <image->Ctrl-,->wm.context_set_enum>`                          |:func:`blender:bpy.ops.wm.context_set_enum`       |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`. <image->.->wm.context_set_enum>`                                    |:func:`blender:bpy.ops.wm.context_set_enum`       |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Ctrl-B <image->Ctrl-B->image.render_border>`                          |:func:`blender:bpy.ops.image.render_border`       |
+------------------------------------------------------------------------------+--------------------------------------------------+
|:km:hk:`Ctrl-Alt-B <image->Ctrl-Alt-B->image.clear_render_border>`            |:func:`blender:bpy.ops.image.clear_render_border` |
+------------------------------------------------------------------------------+--------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: F -> image.view_all

   View All

   bpy.ops.image.view_all(fit_view=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Fit View    |True    |
   +------------+--------+
   
   
.. km:hotkey:: ACTIONMOUSE -> image.view_pan

   View Pan

   bpy.ops.image.view_pan(offset=(0, 0))
   
   
.. km:hotkey:: SELECTMOUSE -> image.sample

   Sample Color

   bpy.ops.image.sample()
   
   
.. km:hotkey:: Tab -> object.mode_set

   Set Object Mode

   bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Mode        |OBJECT  |
   +------------+--------+
   |Toggle      |True    |
   +------------+--------+
   
   
.. km:hotkey:: 1 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-----------------------------+
   |Properties:        |Values:                      |
   +===================+=============================+
   |Context Attributes |space_data.image.render_slot |
   +-------------------+-----------------------------+
   |Value              |0                            |
   +-------------------+-----------------------------+
   
   
.. km:hotkey:: 2 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-----------------------------+
   |Properties:        |Values:                      |
   +===================+=============================+
   |Context Attributes |space_data.image.render_slot |
   +-------------------+-----------------------------+
   |Value              |1                            |
   +-------------------+-----------------------------+
   
   
.. km:hotkey:: 3 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-----------------------------+
   |Properties:        |Values:                      |
   +===================+=============================+
   |Context Attributes |space_data.image.render_slot |
   +-------------------+-----------------------------+
   |Value              |2                            |
   +-------------------+-----------------------------+
   
   
.. km:hotkey:: 4 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-----------------------------+
   |Properties:        |Values:                      |
   +===================+=============================+
   |Context Attributes |space_data.image.render_slot |
   +-------------------+-----------------------------+
   |Value              |3                            |
   +-------------------+-----------------------------+
   
   
.. km:hotkey:: 5 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-----------------------------+
   |Properties:        |Values:                      |
   +===================+=============================+
   |Context Attributes |space_data.image.render_slot |
   +-------------------+-----------------------------+
   |Value              |4                            |
   +-------------------+-----------------------------+
   
   
.. km:hotkey:: 6 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-----------------------------+
   |Properties:        |Values:                      |
   +===================+=============================+
   |Context Attributes |space_data.image.render_slot |
   +-------------------+-----------------------------+
   |Value              |5                            |
   +-------------------+-----------------------------+
   
   
.. km:hotkey:: 7 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-----------------------------+
   |Properties:        |Values:                      |
   +===================+=============================+
   |Context Attributes |space_data.image.render_slot |
   +-------------------+-----------------------------+
   |Value              |6                            |
   +-------------------+-----------------------------+
   
   
.. km:hotkey:: 8 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-----------------------------+
   |Properties:        |Values:                      |
   +===================+=============================+
   |Context Attributes |space_data.image.render_slot |
   +-------------------+-----------------------------+
   |Value              |7                            |
   +-------------------+-----------------------------+
   
   
.. km:hotkey:: 9 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-----------------------------+
   |Properties:        |Values:                      |
   +===================+=============================+
   |Context Attributes |space_data.image.render_slot |
   +-------------------+-----------------------------+
   |Value              |8                            |
   +-------------------+-----------------------------+
   
   
.. km:hotkeyd:: HOME -> image.view_all

   View All

   bpy.ops.image.view_all(fit_view=False)
   
   
.. km:hotkeyd:: Shift-HOME -> image.view_all

   View All

   bpy.ops.image.view_all(fit_view=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Fit View    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_PERIOD -> image.view_selected

   View Center

   bpy.ops.image.view_selected()
   
   
.. km:hotkeyd:: MIDDLEMOUSE -> image.view_pan

   View Pan

   bpy.ops.image.view_pan(offset=(0, 0))
   
   
.. km:hotkeyd:: Shift-MIDDLEMOUSE -> image.view_pan

   View Pan

   bpy.ops.image.view_pan(offset=(0, 0))
   
   
.. km:hotkeyd:: TRACKPADPAN -> image.view_pan

   View Pan

   bpy.ops.image.view_pan(offset=(0, 0))
   
   
.. km:hotkeyd:: NDOF_BUTTON_FIT -> image.view_all

   View All

   bpy.ops.image.view_all(fit_view=False)
   
   
.. km:hotkeyd:: NDOF_MOTION -> image.view_ndof

   NDOF Pan/Zoom

   bpy.ops.image.view_ndof()
   
   
.. km:hotkeyd:: WHEELINMOUSE -> image.view_zoom_in

   View Zoom In

   bpy.ops.image.view_zoom_in(location=(0, 0))
   
   
.. km:hotkeyd:: WHEELOUTMOUSE -> image.view_zoom_out

   View Zoom Out

   bpy.ops.image.view_zoom_out(location=(0, 0))
   
   
.. km:hotkeyd:: NUMPAD_PLUS -> image.view_zoom_in

   View Zoom In

   bpy.ops.image.view_zoom_in(location=(0, 0))
   
   
.. km:hotkeyd:: NUMPAD_MINUS -> image.view_zoom_out

   View Zoom Out

   bpy.ops.image.view_zoom_out(location=(0, 0))
   
   
.. km:hotkeyd:: Ctrl-MIDDLEMOUSE -> image.view_zoom

   View Zoom

   bpy.ops.image.view_zoom(factor=0)
   
   
.. km:hotkeyd:: TRACKPADZOOM -> image.view_zoom

   View Zoom

   bpy.ops.image.view_zoom(factor=0)
   
   
.. km:hotkeyd:: Ctrl-TRACKPADPAN -> image.view_zoom

   View Zoom

   bpy.ops.image.view_zoom(factor=0)
   
   
.. km:hotkeyd:: Shift-B -> image.view_zoom_border

   Zoom to Border

   bpy.ops.image.view_zoom_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0)
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_8 -> image.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.image.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |8.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_4 -> image.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.image.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |4.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_2 -> image.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.image.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |2.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-NUMPAD_8 -> image.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.image.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |8.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-NUMPAD_4 -> image.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.image.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |4.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-NUMPAD_2 -> image.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.image.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |2.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_1 -> image.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.image.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |1.0     |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_2 -> image.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.image.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |0.5     |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_4 -> image.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.image.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |0.25    |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_8 -> image.view_zoom_ratio

   View Zoom Ratio

   bpy.ops.image.view_zoom_ratio(ratio=0)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Ratio       |0.125   |
   +------------+--------+
   
   
.. km:hotkeyd:: LEFTMOUSE -> image.change_frame

   Change Frame

   bpy.ops.image.change_frame(frame=0)
   
   
.. km:hotkeyd:: ACTIONMOUSE -> image.sample

   Sample Color

   bpy.ops.image.sample()
   
   
.. km:hotkeyd:: Ctrl-ACTIONMOUSE -> image.curves_point_set

   Set Curves Point

   bpy.ops.image.curves_point_set(point='BLACK_POINT')
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Point       |BLACK_POINT |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-ACTIONMOUSE -> image.curves_point_set

   Set Curves Point

   bpy.ops.image.curves_point_set(point='BLACK_POINT')
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Point       |WHITE_POINT |
   +------------+------------+
   
   
.. km:hotkeyd:: Tab -> object.mode_set

   Set Object Mode

   bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Mode        |EDIT    |
   +------------+--------+
   |Toggle      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: 1 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-------------------------------------------+
   |Properties:        |Values:                                    |
   +===================+===========================================+
   |Context Attributes |space_data.image.render_slots.active_index |
   +-------------------+-------------------------------------------+
   |Value              |0                                          |
   +-------------------+-------------------------------------------+
   
   
.. km:hotkeyd:: 2 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-------------------------------------------+
   |Properties:        |Values:                                    |
   +===================+===========================================+
   |Context Attributes |space_data.image.render_slots.active_index |
   +-------------------+-------------------------------------------+
   |Value              |1                                          |
   +-------------------+-------------------------------------------+
   
   
.. km:hotkeyd:: 3 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-------------------------------------------+
   |Properties:        |Values:                                    |
   +===================+===========================================+
   |Context Attributes |space_data.image.render_slots.active_index |
   +-------------------+-------------------------------------------+
   |Value              |2                                          |
   +-------------------+-------------------------------------------+
   
   
.. km:hotkeyd:: 4 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-------------------------------------------+
   |Properties:        |Values:                                    |
   +===================+===========================================+
   |Context Attributes |space_data.image.render_slots.active_index |
   +-------------------+-------------------------------------------+
   |Value              |3                                          |
   +-------------------+-------------------------------------------+
   
   
.. km:hotkeyd:: 5 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-------------------------------------------+
   |Properties:        |Values:                                    |
   +===================+===========================================+
   |Context Attributes |space_data.image.render_slots.active_index |
   +-------------------+-------------------------------------------+
   |Value              |4                                          |
   +-------------------+-------------------------------------------+
   
   
.. km:hotkeyd:: 6 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-------------------------------------------+
   |Properties:        |Values:                                    |
   +===================+===========================================+
   |Context Attributes |space_data.image.render_slots.active_index |
   +-------------------+-------------------------------------------+
   |Value              |5                                          |
   +-------------------+-------------------------------------------+
   
   
.. km:hotkeyd:: 7 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-------------------------------------------+
   |Properties:        |Values:                                    |
   +===================+===========================================+
   |Context Attributes |space_data.image.render_slots.active_index |
   +-------------------+-------------------------------------------+
   |Value              |6                                          |
   +-------------------+-------------------------------------------+
   
   
.. km:hotkeyd:: 8 -> wm.context_set_int

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+-------------------------------------------+
   |Properties:        |Values:                                    |
   +===================+===========================================+
   |Context Attributes |space_data.image.render_slots.active_index |
   +-------------------+-------------------------------------------+
   |Value              |7                                          |
   +-------------------+-------------------------------------------+
   
   
.. km:hotkeyd:: , -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |space_data.pivot_point |
   +-------------------+-----------------------+
   |Value              |CENTER                 |
   +-------------------+-----------------------+
   
   
.. km:hotkeyd:: Ctrl-, -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |space_data.pivot_point |
   +-------------------+-----------------------+
   |Value              |MEDIAN                 |
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
   
   
.. km:hotkeyd:: Ctrl-B -> image.render_border

   Render Border

   bpy.ops.image.render_border(xmin=0, xmax=0, ymin=0, ymax=0)
   
   
.. km:hotkeyd:: Ctrl-Alt-B -> image.clear_render_border

   Clear Render Border

   bpy.ops.image.clear_render_border()
   
   
