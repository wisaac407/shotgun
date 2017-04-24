***********
Image Paint
***********

.. km:module:: imagepaint

   


---------------
Quick Reference
---------------

+----------------------------------------------------------------------------------------+------------------------------------------------+
|Hotkey                                                                                  |Operator                                        |
+========================================================================================+================================================+
|:km:hk:`R <imagepaint->R->wm.context_menu_enum>`                                        |:func:`blender:bpy.ops.wm.context_menu_enum`    |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`LEFTMOUSE <imagepaint->LEFTMOUSE->paint.image_paint>`                           |:func:`blender:bpy.ops.paint.image_paint`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-LEFTMOUSE <imagepaint->Ctrl-LEFTMOUSE->paint.image_paint>`                 |:func:`blender:bpy.ops.paint.image_paint`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`X <imagepaint->X->paint.brush_colors_flip>`                                     |:func:`blender:bpy.ops.paint.brush_colors_flip` |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`RIGHTMOUSE <imagepaint->RIGHTMOUSE->paint.grab_clone>`                          |:func:`blender:bpy.ops.paint.grab_clone`        |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`S <imagepaint->S->paint.sample_color>`                                          |:func:`blender:bpy.ops.paint.sample_color`      |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`1 <imagepaint->1->brush.active_index_set>`                                      |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`2 <imagepaint->2->brush.active_index_set>`                                      |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`3 <imagepaint->3->brush.active_index_set>`                                      |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`4 <imagepaint->4->brush.active_index_set>`                                      |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`5 <imagepaint->5->brush.active_index_set>`                                      |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`6 <imagepaint->6->brush.active_index_set>`                                      |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`7 <imagepaint->7->brush.active_index_set>`                                      |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`8 <imagepaint->8->brush.active_index_set>`                                      |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`9 <imagepaint->9->brush.active_index_set>`                                      |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`0 <imagepaint->0->brush.active_index_set>`                                      |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-1 <imagepaint->Shift-1->brush.active_index_set>`                          |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-2 <imagepaint->Shift-2->brush.active_index_set>`                          |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-3 <imagepaint->Shift-3->brush.active_index_set>`                          |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-4 <imagepaint->Shift-4->brush.active_index_set>`                          |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-5 <imagepaint->Shift-5->brush.active_index_set>`                          |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-6 <imagepaint->Shift-6->brush.active_index_set>`                          |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-7 <imagepaint->Shift-7->brush.active_index_set>`                          |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-8 <imagepaint->Shift-8->brush.active_index_set>`                          |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-9 <imagepaint->Shift-9->brush.active_index_set>`                          |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-0 <imagepaint->Shift-0->brush.active_index_set>`                          |:func:`blender:bpy.ops.brush.active_index_set`  |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`LEFT_BRACKET <imagepaint->LEFT_BRACKET->brush.scale_size>`                      |:func:`blender:bpy.ops.brush.scale_size`        |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`RIGHT_BRACKET <imagepaint->RIGHT_BRACKET->brush.scale_size>`                    |:func:`blender:bpy.ops.brush.scale_size`        |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`F <imagepaint->F->wm.radial_control>`                                           |:func:`blender:bpy.ops.wm.radial_control`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-F <imagepaint->Shift-F->wm.radial_control>`                               |:func:`blender:bpy.ops.wm.radial_control`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-F <imagepaint->Ctrl-F->wm.radial_control>`                                 |:func:`blender:bpy.ops.wm.radial_control`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-Alt-F <imagepaint->Ctrl-Alt-F->wm.radial_control>`                         |:func:`blender:bpy.ops.wm.radial_control`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`RIGHTMOUSE <imagepaint->RIGHTMOUSE->brush.stencil_control>`                     |:func:`blender:bpy.ops.brush.stencil_control`   |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-RIGHTMOUSE <imagepaint->Shift-RIGHTMOUSE->brush.stencil_control>`         |:func:`blender:bpy.ops.brush.stencil_control`   |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-RIGHTMOUSE <imagepaint->Ctrl-RIGHTMOUSE->brush.stencil_control>`           |:func:`blender:bpy.ops.brush.stencil_control`   |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Alt-RIGHTMOUSE <imagepaint->Alt-RIGHTMOUSE->brush.stencil_control>`             |:func:`blender:bpy.ops.brush.stencil_control`   |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-Alt-RIGHTMOUSE <imagepaint->Shift-Alt-RIGHTMOUSE->brush.stencil_control>` |:func:`blender:bpy.ops.brush.stencil_control`   |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-Alt-RIGHTMOUSE <imagepaint->Ctrl-Alt-RIGHTMOUSE->brush.stencil_control>`   |:func:`blender:bpy.ops.brush.stencil_control`   |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`M <imagepaint->M->wm.context_toggle>`                                           |:func:`blender:bpy.ops.wm.context_toggle`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-S <imagepaint->Shift-S->wm.context_toggle>`                               |:func:`blender:bpy.ops.wm.context_toggle`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`R <imagepaint->R->wm.call_menu>`                                                |:func:`blender:bpy.ops.wm.call_menu`            |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`E <imagepaint->E->wm.context_menu_enum>`                                        |:func:`blender:bpy.ops.wm.context_menu_enum`    |
+----------------------------------------------------------------------------------------+------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: R -> wm.context_menu_enum : KEYBOARD -> PRESS

   Context Enum Menu

   bpy.ops.wm.context_menu_enum(data_path="")
   
   
   +-------------------+------------------------------------------------------------+
   |Properties:        |Values:                                                     |
   +===================+============================================================+
   |Context Attributes |tool_settings.image_paint.brush.texture_angle_source_random |
   +-------------------+------------------------------------------------------------+
   
   
.. km:hotkeyd:: LEFTMOUSE -> paint.image_paint : MOUSE -> PRESS

   Image Paint

   bpy.ops.paint.image_paint(stroke=[], mode='NORMAL')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Stroke Mode |NORMAL  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-LEFTMOUSE -> paint.image_paint : MOUSE -> PRESS

   Image Paint

   bpy.ops.paint.image_paint(stroke=[], mode='NORMAL')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Stroke Mode |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: X -> paint.brush_colors_flip : KEYBOARD -> PRESS

   Brush Colors Flip

   bpy.ops.paint.brush_colors_flip()
   
   
.. km:hotkeyd:: RIGHTMOUSE -> paint.grab_clone : MOUSE -> PRESS

   Grab Clone

   bpy.ops.paint.grab_clone(delta=(0, 0))
   
   
.. km:hotkeyd:: S -> paint.sample_color : KEYBOARD -> PRESS

   Sample Color

   bpy.ops.paint.sample_color(location=(0, 0), merged=False, palette=False)
   
   
.. km:hotkeyd:: 1 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |0           |
   +------------+------------+
   
   
.. km:hotkeyd:: 2 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |1           |
   +------------+------------+
   
   
.. km:hotkeyd:: 3 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |2           |
   +------------+------------+
   
   
.. km:hotkeyd:: 4 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |3           |
   +------------+------------+
   
   
.. km:hotkeyd:: 5 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |4           |
   +------------+------------+
   
   
.. km:hotkeyd:: 6 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |5           |
   +------------+------------+
   
   
.. km:hotkeyd:: 7 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |6           |
   +------------+------------+
   
   
.. km:hotkeyd:: 8 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |7           |
   +------------+------------+
   
   
.. km:hotkeyd:: 9 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |8           |
   +------------+------------+
   
   
.. km:hotkeyd:: 0 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |9           |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-1 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |10          |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-2 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |11          |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-3 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |12          |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-4 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |13          |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-5 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |14          |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-6 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |15          |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-7 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |16          |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-8 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |17          |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-9 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |18          |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-0 -> brush.active_index_set : KEYBOARD -> PRESS

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |19          |
   +------------+------------+
   
   
.. km:hotkeyd:: LEFT_BRACKET -> brush.scale_size : KEYBOARD -> PRESS

   Scale Sculpt/Paint Brush Size

   bpy.ops.brush.scale_size(scalar=1)
   
   
   +------------+-------------------+
   |Properties: |Values:            |
   +============+===================+
   |Scalar      |0.8999999761581421 |
   +------------+-------------------+
   
   
.. km:hotkeyd:: RIGHT_BRACKET -> brush.scale_size : KEYBOARD -> PRESS

   Scale Sculpt/Paint Brush Size

   bpy.ops.brush.scale_size(scalar=1)
   
   
   +------------+-------------------+
   |Properties: |Values:            |
   +============+===================+
   |Scalar      |1.1111111640930176 |
   +------------+-------------------+
   
   
.. km:hotkeyd:: F -> wm.radial_control : KEYBOARD -> PRESS

   Radial Control

   bpy.ops.wm.radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)
   
   
   +-------------------------+--------------------------------------------------------+
   |Properties:              |Values:                                                 |
   +=========================+========================================================+
   |Primary Data Path        |tool_settings.image_paint.brush.size                    |
   +-------------------------+--------------------------------------------------------+
   |Use Secondary            |tool_settings.unified_paint_settings.use_unified_size   |
   +-------------------------+--------------------------------------------------------+
   |Secondary Data Path      |tool_settings.unified_paint_settings.size               |
   +-------------------------+--------------------------------------------------------+
   |Color Path               |tool_settings.image_paint.brush.cursor_color_add        |
   +-------------------------+--------------------------------------------------------+
   |Rotation Path            |tool_settings.image_paint.brush.mask_texture_slot.angle |
   +-------------------------+--------------------------------------------------------+
   |Image ID                 |tool_settings.image_paint.brush                         |
   +-------------------------+--------------------------------------------------------+
   |Fill Color Path          |tool_settings.image_paint.brush.color                   |
   +-------------------------+--------------------------------------------------------+
   |Fill Color Override Path |tool_settings.unified_paint_settings.color              |
   +-------------------------+--------------------------------------------------------+
   |Fill Color Override Test |tool_settings.unified_paint_settings.use_unified_color  |
   +-------------------------+--------------------------------------------------------+
   |Zoom Path                |space_data.zoom                                         |
   +-------------------------+--------------------------------------------------------+
   |Secondary Texture        |True                                                    |
   +-------------------------+--------------------------------------------------------+
   
   
.. km:hotkeyd:: Shift-F -> wm.radial_control : KEYBOARD -> PRESS

   Radial Control

   bpy.ops.wm.radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)
   
   
   +-------------------------+----------------------------------------------------------+
   |Properties:              |Values:                                                   |
   +=========================+==========================================================+
   |Primary Data Path        |tool_settings.image_paint.brush.strength                  |
   +-------------------------+----------------------------------------------------------+
   |Use Secondary            |tool_settings.unified_paint_settings.use_unified_strength |
   +-------------------------+----------------------------------------------------------+
   |Secondary Data Path      |tool_settings.unified_paint_settings.strength             |
   +-------------------------+----------------------------------------------------------+
   |Color Path               |tool_settings.image_paint.brush.cursor_color_add          |
   +-------------------------+----------------------------------------------------------+
   |Rotation Path            |tool_settings.image_paint.brush.mask_texture_slot.angle   |
   +-------------------------+----------------------------------------------------------+
   |Image ID                 |tool_settings.image_paint.brush                           |
   +-------------------------+----------------------------------------------------------+
   |Fill Color Path          |tool_settings.image_paint.brush.color                     |
   +-------------------------+----------------------------------------------------------+
   |Fill Color Override Path |tool_settings.unified_paint_settings.color                |
   +-------------------------+----------------------------------------------------------+
   |Fill Color Override Test |tool_settings.unified_paint_settings.use_unified_color    |
   +-------------------------+----------------------------------------------------------+
   |Zoom Path                |                                                          |
   +-------------------------+----------------------------------------------------------+
   |Secondary Texture        |True                                                      |
   +-------------------------+----------------------------------------------------------+
   
   
.. km:hotkeyd:: Ctrl-F -> wm.radial_control : KEYBOARD -> PRESS

   Radial Control

   bpy.ops.wm.radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)
   
   
   +-------------------------+-------------------------------------------------------+
   |Properties:              |Values:                                                |
   +=========================+=======================================================+
   |Primary Data Path        |tool_settings.image_paint.brush.texture_slot.angle     |
   +-------------------------+-------------------------------------------------------+
   |Use Secondary            |                                                       |
   +-------------------------+-------------------------------------------------------+
   |Secondary Data Path      |                                                       |
   +-------------------------+-------------------------------------------------------+
   |Color Path               |tool_settings.image_paint.brush.cursor_color_add       |
   +-------------------------+-------------------------------------------------------+
   |Rotation Path            |tool_settings.image_paint.brush.texture_slot.angle     |
   +-------------------------+-------------------------------------------------------+
   |Image ID                 |tool_settings.image_paint.brush                        |
   +-------------------------+-------------------------------------------------------+
   |Fill Color Path          |tool_settings.image_paint.brush.color                  |
   +-------------------------+-------------------------------------------------------+
   |Fill Color Override Path |tool_settings.unified_paint_settings.color             |
   +-------------------------+-------------------------------------------------------+
   |Fill Color Override Test |tool_settings.unified_paint_settings.use_unified_color |
   +-------------------------+-------------------------------------------------------+
   |Zoom Path                |                                                       |
   +-------------------------+-------------------------------------------------------+
   |Secondary Texture        |False                                                  |
   +-------------------------+-------------------------------------------------------+
   
   
.. km:hotkeyd:: Ctrl-Alt-F -> wm.radial_control : KEYBOARD -> PRESS

   Radial Control

   bpy.ops.wm.radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)
   
   
   +-------------------------+--------------------------------------------------------+
   |Properties:              |Values:                                                 |
   +=========================+========================================================+
   |Primary Data Path        |tool_settings.image_paint.brush.mask_texture_slot.angle |
   +-------------------------+--------------------------------------------------------+
   |Use Secondary            |                                                        |
   +-------------------------+--------------------------------------------------------+
   |Secondary Data Path      |                                                        |
   +-------------------------+--------------------------------------------------------+
   |Color Path               |tool_settings.image_paint.brush.cursor_color_add        |
   +-------------------------+--------------------------------------------------------+
   |Rotation Path            |tool_settings.image_paint.brush.mask_texture_slot.angle |
   +-------------------------+--------------------------------------------------------+
   |Image ID                 |tool_settings.image_paint.brush                         |
   +-------------------------+--------------------------------------------------------+
   |Fill Color Path          |tool_settings.image_paint.brush.color                   |
   +-------------------------+--------------------------------------------------------+
   |Fill Color Override Path |tool_settings.unified_paint_settings.color              |
   +-------------------------+--------------------------------------------------------+
   |Fill Color Override Test |tool_settings.unified_paint_settings.use_unified_color  |
   +-------------------------+--------------------------------------------------------+
   |Zoom Path                |                                                        |
   +-------------------------+--------------------------------------------------------+
   |Secondary Texture        |True                                                    |
   +-------------------------+--------------------------------------------------------+
   
   
.. km:hotkeyd:: RIGHTMOUSE -> brush.stencil_control : MOUSE -> PRESS

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Tool        |TRANSLATION |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-RIGHTMOUSE -> brush.stencil_control : MOUSE -> PRESS

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Tool        |SCALE   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-RIGHTMOUSE -> brush.stencil_control : MOUSE -> PRESS

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+---------+
   |Properties: |Values:  |
   +============+=========+
   |Tool        |ROTATION |
   +------------+---------+
   
   
.. km:hotkeyd:: Alt-RIGHTMOUSE -> brush.stencil_control : MOUSE -> PRESS

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Tool        |TRANSLATION |
   +------------+------------+
   |Tool        |SECONDARY   |
   +------------+------------+
   
   
.. km:hotkeyd:: Shift-Alt-RIGHTMOUSE -> brush.stencil_control : MOUSE -> PRESS

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Tool        |SECONDARY |
   +------------+----------+
   |Tool        |SCALE     |
   +------------+----------+
   
   
.. km:hotkeyd:: Ctrl-Alt-RIGHTMOUSE -> brush.stencil_control : MOUSE -> PRESS

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Tool        |SECONDARY |
   +------------+----------+
   |Tool        |ROTATION  |
   +------------+----------+
   
   
.. km:hotkeyd:: M -> wm.context_toggle : KEYBOARD -> PRESS

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+---------------------------------------+
   |Properties:        |Values:                                |
   +===================+=======================================+
   |Context Attributes |image_paint_object.data.use_paint_mask |
   +-------------------+---------------------------------------+
   
   
.. km:hotkeyd:: Shift-S -> wm.context_toggle : KEYBOARD -> PRESS

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+--------------------------------------------------+
   |Properties:        |Values:                                           |
   +===================+==================================================+
   |Context Attributes |tool_settings.image_paint.brush.use_smooth_stroke |
   +-------------------+--------------------------------------------------+
   
   
.. km:hotkeyd:: R -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------------------+
   |Properties: |Values:                 |
   +============+========================+
   |Name        |VIEW3D_MT_angle_control |
   +------------+------------------------+
   
   
.. km:hotkeyd:: E -> wm.context_menu_enum : KEYBOARD -> PRESS

   Context Enum Menu

   bpy.ops.wm.context_menu_enum(data_path="")
   
   
   +-------------------+----------------------------------------------+
   |Properties:        |Values:                                       |
   +===================+==============================================+
   |Context Attributes |tool_settings.image_paint.brush.stroke_method |
   +-------------------+----------------------------------------------+
   
   
