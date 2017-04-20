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
|:km:hk:`F <imagepaint->F->wm.radial_control>`                                           |:func:`blender:bpy.ops.wm.radial_control`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Shift-F <imagepaint->Shift-F->wm.radial_control>`                               |:func:`blender:bpy.ops.wm.radial_control`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-F <imagepaint->Ctrl-F->wm.radial_control>`                                 |:func:`blender:bpy.ops.wm.radial_control`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-Alt-F <imagepaint->Ctrl-Alt-F->wm.radial_control>`                         |:func:`blender:bpy.ops.wm.radial_control`       |
+----------------------------------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Alt-RIGHTMOUSE <imagepaint->Alt-RIGHTMOUSE->brush.stencil_control>`             |:func:`blender:bpy.ops.brush.stencil_control`   |
+----------------------------------------------------------------------------------------+------------------------------------------------+
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

.. km:hotkey:: F -> wm.radial_control

   Radial Control

   bpy.ops.wm.radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)
   
   
   +--------------------+--------------------------------------------------------+
   |Properties:         |Values:                                                 |
   +====================+========================================================+
   |Primary Data Path   |tool_settings.image_paint.brush.size                    |
   +--------------------+--------------------------------------------------------+
   |Secondary Data Path |tool_settings.unified_paint_settings.size               |
   +--------------------+--------------------------------------------------------+
   |Use Secondary       |tool_settings.unified_paint_settings.use_unified_size   |
   +--------------------+--------------------------------------------------------+
   |Rotation Path       |tool_settings.image_paint.brush.mask_texture_slot.angle |
   +--------------------+--------------------------------------------------------+
   |Color Path          |tool_settings.image_paint.brush.cursor_color_add        |
   +--------------------+--------------------------------------------------------+
   |Fill Color Path     |tool_settings.image_paint.brush.color                   |
   +--------------------+--------------------------------------------------------+
   |Zoom Path           |space_data.zoom                                         |
   +--------------------+--------------------------------------------------------+
   |Image ID            |tool_settings.image_paint.brush                         |
   +--------------------+--------------------------------------------------------+
   |Secondary Texture   |True                                                    |
   +--------------------+--------------------------------------------------------+
   
   
.. km:hotkey:: Shift-F -> wm.radial_control

   Radial Control

   bpy.ops.wm.radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)
   
   
   +--------------------+----------------------------------------------------------+
   |Properties:         |Values:                                                   |
   +====================+==========================================================+
   |Primary Data Path   |tool_settings.image_paint.brush.strength                  |
   +--------------------+----------------------------------------------------------+
   |Secondary Data Path |tool_settings.unified_paint_settings.strength             |
   +--------------------+----------------------------------------------------------+
   |Use Secondary       |tool_settings.unified_paint_settings.use_unified_strength |
   +--------------------+----------------------------------------------------------+
   |Rotation Path       |tool_settings.image_paint.brush.mask_texture_slot.angle   |
   +--------------------+----------------------------------------------------------+
   |Color Path          |tool_settings.image_paint.brush.cursor_color_add          |
   +--------------------+----------------------------------------------------------+
   |Fill Color Path     |tool_settings.image_paint.brush.color                     |
   +--------------------+----------------------------------------------------------+
   |Zoom Path           |                                                          |
   +--------------------+----------------------------------------------------------+
   |Image ID            |tool_settings.image_paint.brush                           |
   +--------------------+----------------------------------------------------------+
   |Secondary Texture   |True                                                      |
   +--------------------+----------------------------------------------------------+
   
   
.. km:hotkey:: Ctrl-F -> wm.radial_control

   Radial Control

   bpy.ops.wm.radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)
   
   
   +--------------------+---------------------------------------------------+
   |Properties:         |Values:                                            |
   +====================+===================================================+
   |Primary Data Path   |tool_settings.image_paint.brush.texture_slot.angle |
   +--------------------+---------------------------------------------------+
   |Secondary Data Path |                                                   |
   +--------------------+---------------------------------------------------+
   |Use Secondary       |                                                   |
   +--------------------+---------------------------------------------------+
   |Rotation Path       |tool_settings.image_paint.brush.texture_slot.angle |
   +--------------------+---------------------------------------------------+
   |Color Path          |tool_settings.image_paint.brush.cursor_color_add   |
   +--------------------+---------------------------------------------------+
   |Fill Color Path     |tool_settings.image_paint.brush.color              |
   +--------------------+---------------------------------------------------+
   |Zoom Path           |                                                   |
   +--------------------+---------------------------------------------------+
   |Image ID            |tool_settings.image_paint.brush                    |
   +--------------------+---------------------------------------------------+
   |Secondary Texture   |False                                              |
   +--------------------+---------------------------------------------------+
   
   
.. km:hotkey:: Ctrl-Alt-F -> wm.radial_control

   Radial Control

   bpy.ops.wm.radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False)
   
   
   +--------------------+--------------------------------------------------------+
   |Properties:         |Values:                                                 |
   +====================+========================================================+
   |Primary Data Path   |tool_settings.image_paint.brush.mask_texture_slot.angle |
   +--------------------+--------------------------------------------------------+
   |Secondary Data Path |                                                        |
   +--------------------+--------------------------------------------------------+
   |Use Secondary       |                                                        |
   +--------------------+--------------------------------------------------------+
   |Rotation Path       |tool_settings.image_paint.brush.mask_texture_slot.angle |
   +--------------------+--------------------------------------------------------+
   |Color Path          |tool_settings.image_paint.brush.cursor_color_add        |
   +--------------------+--------------------------------------------------------+
   |Fill Color Path     |tool_settings.image_paint.brush.color                   |
   +--------------------+--------------------------------------------------------+
   |Zoom Path           |                                                        |
   +--------------------+--------------------------------------------------------+
   |Image ID            |tool_settings.image_paint.brush                         |
   +--------------------+--------------------------------------------------------+
   |Secondary Texture   |True                                                    |
   +--------------------+--------------------------------------------------------+
   
   
.. km:hotkey:: Alt-RIGHTMOUSE -> brush.stencil_control

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Tool        |TRANSLATION |
   +------------+------------+
   
   
.. km:hotkey:: R -> wm.context_menu_enum

   Context Enum Menu

   bpy.ops.wm.context_menu_enum(data_path="")
   
   
   +-------------------+------------------------------------------------------------+
   |Properties:        |Values:                                                     |
   +===================+============================================================+
   |Context Attributes |tool_settings.image_paint.brush.texture_angle_source_random |
   +-------------------+------------------------------------------------------------+
   
   
.. km:hotkey:: LEFTMOUSE -> paint.image_paint

   Image Paint

   bpy.ops.paint.image_paint(stroke=[], mode='NORMAL')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Stroke Mode |NORMAL  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-LEFTMOUSE -> paint.image_paint

   Image Paint

   bpy.ops.paint.image_paint(stroke=[], mode='NORMAL')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Stroke Mode |INVERT  |
   +------------+--------+
   
   
.. km:hotkey:: X -> paint.brush_colors_flip

   Brush Colors Flip

   bpy.ops.paint.brush_colors_flip()
   
   
.. km:hotkey:: RIGHTMOUSE -> paint.grab_clone

   Grab Clone

   bpy.ops.paint.grab_clone(delta=(0, 0))
   
   
.. km:hotkey:: S -> paint.sample_color

   Sample Color

   bpy.ops.paint.sample_color(location=(0, 0), merged=False, palette=False)
   
   
.. km:hotkey:: 1 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |0           |
   +------------+------------+
   
   
.. km:hotkey:: 2 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |1           |
   +------------+------------+
   
   
.. km:hotkey:: 3 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |2           |
   +------------+------------+
   
   
.. km:hotkey:: 4 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |3           |
   +------------+------------+
   
   
.. km:hotkey:: 5 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |4           |
   +------------+------------+
   
   
.. km:hotkey:: 6 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |5           |
   +------------+------------+
   
   
.. km:hotkey:: 7 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |6           |
   +------------+------------+
   
   
.. km:hotkey:: 8 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |7           |
   +------------+------------+
   
   
.. km:hotkey:: 9 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |8           |
   +------------+------------+
   
   
.. km:hotkey:: 0 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |9           |
   +------------+------------+
   
   
.. km:hotkey:: Shift-1 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |10          |
   +------------+------------+
   
   
.. km:hotkey:: Shift-2 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |11          |
   +------------+------------+
   
   
.. km:hotkey:: Shift-3 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |12          |
   +------------+------------+
   
   
.. km:hotkey:: Shift-4 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |13          |
   +------------+------------+
   
   
.. km:hotkey:: Shift-5 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |14          |
   +------------+------------+
   
   
.. km:hotkey:: Shift-6 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |15          |
   +------------+------------+
   
   
.. km:hotkey:: Shift-7 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |16          |
   +------------+------------+
   
   
.. km:hotkey:: Shift-8 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |17          |
   +------------+------------+
   
   
.. km:hotkey:: Shift-9 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |18          |
   +------------+------------+
   
   
.. km:hotkey:: Shift-0 -> brush.active_index_set

   Set Brush Number

   bpy.ops.brush.active_index_set(mode="", index=0)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |image_paint |
   +------------+------------+
   |Number      |19          |
   +------------+------------+
   
   
.. km:hotkey:: LEFT_BRACKET -> brush.scale_size

   Scale Sculpt/Paint Brush Size

   bpy.ops.brush.scale_size(scalar=1)
   
   
   +------------+-------------------+
   |Properties: |Values:            |
   +============+===================+
   |Scalar      |0.8999999761581421 |
   +------------+-------------------+
   
   
.. km:hotkey:: RIGHT_BRACKET -> brush.scale_size

   Scale Sculpt/Paint Brush Size

   bpy.ops.brush.scale_size(scalar=1)
   
   
   +------------+-------------------+
   |Properties: |Values:            |
   +============+===================+
   |Scalar      |1.1111111640930176 |
   +------------+-------------------+
   
   
.. km:hotkey:: F -> wm.radial_control

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
   
   
.. km:hotkey:: Shift-F -> wm.radial_control

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
   
   
.. km:hotkey:: Ctrl-F -> wm.radial_control

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
   
   
.. km:hotkey:: Ctrl-Alt-F -> wm.radial_control

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
   
   
.. km:hotkey:: RIGHTMOUSE -> brush.stencil_control

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Tool        |TRANSLATION |
   +------------+------------+
   
   
.. km:hotkey:: Shift-RIGHTMOUSE -> brush.stencil_control

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Tool        |SCALE   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-RIGHTMOUSE -> brush.stencil_control

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+---------+
   |Properties: |Values:  |
   +============+=========+
   |Tool        |ROTATION |
   +------------+---------+
   
   
.. km:hotkey:: Alt-RIGHTMOUSE -> brush.stencil_control

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Tool        |TRANSLATION |
   +------------+------------+
   |Tool        |SECONDARY   |
   +------------+------------+
   
   
.. km:hotkey:: Shift-Alt-RIGHTMOUSE -> brush.stencil_control

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Tool        |SECONDARY |
   +------------+----------+
   |Tool        |SCALE     |
   +------------+----------+
   
   
.. km:hotkey:: Ctrl-Alt-RIGHTMOUSE -> brush.stencil_control

   Stencil Brush Control

   bpy.ops.brush.stencil_control(mode='TRANSLATION', texmode='PRIMARY')
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Tool        |SECONDARY |
   +------------+----------+
   |Tool        |ROTATION  |
   +------------+----------+
   
   
.. km:hotkey:: M -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+---------------------------------------+
   |Properties:        |Values:                                |
   +===================+=======================================+
   |Context Attributes |image_paint_object.data.use_paint_mask |
   +-------------------+---------------------------------------+
   
   
.. km:hotkey:: Shift-S -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+--------------------------------------------------+
   |Properties:        |Values:                                           |
   +===================+==================================================+
   |Context Attributes |tool_settings.image_paint.brush.use_smooth_stroke |
   +-------------------+--------------------------------------------------+
   
   
.. km:hotkey:: R -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------------------+
   |Properties: |Values:                 |
   +============+========================+
   |Name        |VIEW3D_MT_angle_control |
   +------------+------------------------+
   
   
.. km:hotkey:: E -> wm.context_menu_enum

   Context Enum Menu

   bpy.ops.wm.context_menu_enum(data_path="")
   
   
   +-------------------+----------------------------------------------+
   |Properties:        |Values:                                       |
   +===================+==============================================+
   |Context Attributes |tool_settings.image_paint.brush.stroke_method |
   +-------------------+----------------------------------------------+
   
   
