*********
Dopesheet
*********

.. km:module:: dopesheet

   


---------------
Quick Reference
---------------

+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|Hotkey                                                                                          |Operator                                              |
+================================================================================================+======================================================+
|:km:hk:`Shift-Tab <dopesheet->Shift-Tab->wm.context_toggle_enum>`                               |:func:`blender:bpy.ops.wm.context_toggle_enum`        |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Tab <dopesheet->Ctrl-Tab->wm.context_set_enum>`                                    |:func:`blender:bpy.ops.wm.context_set_enum`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-A <dopesheet->Ctrl-A->action.select_all_toggle>`                                   |:func:`blender:bpy.ops.action.select_all_toggle`      |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`O <dopesheet->O->action.clean>`                                                         |:func:`blender:bpy.ops.action.clean`                  |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`X <dopesheet->X->action.delete>`                                                        |:func:`blender:bpy.ops.action.delete`                 |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`DEL <dopesheet->DEL->action.delete>`                                                    |:func:`blender:bpy.ops.action.delete`                 |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`SELECTMOUSE <dopesheet->SELECTMOUSE->action.clickselect>`                               |:func:`blender:bpy.ops.action.clickselect`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-SELECTMOUSE <dopesheet->Alt-SELECTMOUSE->action.clickselect>`                       |:func:`blender:bpy.ops.action.clickselect`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <dopesheet->Shift-SELECTMOUSE->action.clickselect>`                   |:func:`blender:bpy.ops.action.clickselect`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-Alt-SELECTMOUSE <dopesheet->Shift-Alt-SELECTMOUSE->action.clickselect>`           |:func:`blender:bpy.ops.action.clickselect`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Alt-SELECTMOUSE <dopesheet->Ctrl-Alt-SELECTMOUSE->action.clickselect>`             |:func:`blender:bpy.ops.action.clickselect`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-SELECTMOUSE <dopesheet->Ctrl-Shift-Alt-SELECTMOUSE->action.clickselect>` |:func:`blender:bpy.ops.action.clickselect`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <dopesheet->Ctrl-SELECTMOUSE->action.select_leftright>`                |:func:`blender:bpy.ops.action.select_leftright`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-SELECTMOUSE <dopesheet->Ctrl-Shift-SELECTMOUSE->action.select_leftright>`    |:func:`blender:bpy.ops.action.select_leftright`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`LEFT_BRACKET <dopesheet->LEFT_BRACKET->action.select_leftright>`                        |:func:`blender:bpy.ops.action.select_leftright`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`RIGHT_BRACKET <dopesheet->RIGHT_BRACKET->action.select_leftright>`                      |:func:`blender:bpy.ops.action.select_leftright`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`A <dopesheet->A->action.select_all_toggle>`                                             |:func:`blender:bpy.ops.action.select_all_toggle`      |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-I <dopesheet->Ctrl-I->action.select_all_toggle>`                                   |:func:`blender:bpy.ops.action.select_all_toggle`      |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`B <dopesheet->B->action.select_border>`                                                 |:func:`blender:bpy.ops.action.select_border`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-B <dopesheet->Alt-B->action.select_border>`                                         |:func:`blender:bpy.ops.action.select_border`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-EVT_TWEAK_A <dopesheet->Ctrl-EVT_TWEAK_A->action.select_lasso>`                    |:func:`blender:bpy.ops.action.select_lasso`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-EVT_TWEAK_A <dopesheet->Ctrl-Shift-EVT_TWEAK_A->action.select_lasso>`        |:func:`blender:bpy.ops.action.select_lasso`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`C <dopesheet->C->action.select_circle>`                                                 |:func:`blender:bpy.ops.action.select_circle`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`K <dopesheet->K->action.select_column>`                                                 |:func:`blender:bpy.ops.action.select_column`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-K <dopesheet->Ctrl-K->action.select_column>`                                       |:func:`blender:bpy.ops.action.select_column`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-K <dopesheet->Shift-K->action.select_column>`                                     |:func:`blender:bpy.ops.action.select_column`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-K <dopesheet->Alt-K->action.select_column>`                                         |:func:`blender:bpy.ops.action.select_column`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <dopesheet->Ctrl-NUMPAD_PLUS->action.select_more>`                     |:func:`blender:bpy.ops.action.select_more`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <dopesheet->Ctrl-NUMPAD_MINUS->action.select_less>`                   |:func:`blender:bpy.ops.action.select_less`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`L <dopesheet->L->action.select_linked>`                                                 |:func:`blender:bpy.ops.action.select_linked`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-G <dopesheet->Ctrl-G->action.frame_jump>`                                          |:func:`blender:bpy.ops.action.frame_jump`             |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-S <dopesheet->Shift-S->action.snap>`                                              |:func:`blender:bpy.ops.action.snap`                   |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-M <dopesheet->Shift-M->action.mirror>`                                            |:func:`blender:bpy.ops.action.mirror`                 |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`V <dopesheet->V->action.handle_type>`                                                   |:func:`blender:bpy.ops.action.handle_type`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`T <dopesheet->T->action.interpolation_type>`                                            |:func:`blender:bpy.ops.action.interpolation_type`     |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-E <dopesheet->Shift-E->action.extrapolation_type>`                                |:func:`blender:bpy.ops.action.extrapolation_type`     |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`R <dopesheet->R->action.keyframe_type>`                                                 |:func:`blender:bpy.ops.action.keyframe_type`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-O <dopesheet->Shift-O->action.sample>`                                            |:func:`blender:bpy.ops.action.sample`                 |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`X <dopesheet->X->wm.call_menu>`                                                         |:func:`blender:bpy.ops.wm.call_menu`                  |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`DEL <dopesheet->DEL->wm.call_menu>`                                                     |:func:`blender:bpy.ops.wm.call_menu`                  |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-D <dopesheet->Shift-D->action.duplicate_move>`                                    |:func:`blender:bpy.ops.action.duplicate_move`         |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`I <dopesheet->I->action.keyframe_insert>`                                               |:func:`blender:bpy.ops.action.keyframe_insert`        |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-C <dopesheet->Ctrl-C->action.copy>`                                                |:func:`blender:bpy.ops.action.copy`                   |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-V <dopesheet->Ctrl-V->action.paste>`                                               |:func:`blender:bpy.ops.action.paste`                  |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-V <dopesheet->Ctrl-Shift-V->action.paste>`                                   |:func:`blender:bpy.ops.action.paste`                  |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Alt-P <dopesheet->Ctrl-Alt-P->action.previewrange_set>`                            |:func:`blender:bpy.ops.action.previewrange_set`       |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`HOME <dopesheet->HOME->action.view_all>`                                                |:func:`blender:bpy.ops.action.view_all`               |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`NDOF_BUTTON_FIT <dopesheet->NDOF_BUTTON_FIT->action.view_all>`                          |:func:`blender:bpy.ops.action.view_all`               |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`NUMPAD_PERIOD <dopesheet->NUMPAD_PERIOD->action.view_selected>`                         |:func:`blender:bpy.ops.action.view_selected`          |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`NUMPAD_0 <dopesheet->NUMPAD_0->action.view_frame>`                                      |:func:`blender:bpy.ops.action.view_frame`             |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Tab <dopesheet->Tab->anim.channels_editable_toggle>`                                    |:func:`blender:bpy.ops.anim.channels_editable_toggle` |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-F <dopesheet->Ctrl-F->anim.channels_find>`                                         |:func:`blender:bpy.ops.anim.channels_find`            |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`G <dopesheet->G->transform.transform>`                                                  |:func:`blender:bpy.ops.transform.transform`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`EVT_TWEAK_S <dopesheet->EVT_TWEAK_S->transform.transform>`                              |:func:`blender:bpy.ops.transform.transform`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`E <dopesheet->E->transform.transform>`                                                  |:func:`blender:bpy.ops.transform.transform`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`S <dopesheet->S->transform.transform>`                                                  |:func:`blender:bpy.ops.transform.transform`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-T <dopesheet->Shift-T->transform.transform>`                                      |:func:`blender:bpy.ops.transform.transform`           |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`O <dopesheet->O->wm.context_toggle>`                                                    |:func:`blender:bpy.ops.wm.context_toggle`             |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`M <dopesheet->M->marker.add>`                                                           |:func:`blender:bpy.ops.marker.add`                    |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-M <dopesheet->Ctrl-M->marker.rename>`                                              |:func:`blender:bpy.ops.marker.rename`                 |
+------------------------------------------------------------------------------------------------+------------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Shift-Tab -> wm.context_toggle_enum

   Context Toggle Values

   bpy.ops.wm.context_toggle_enum(data_path="", value_1="", value_2="")
   
   
   +-------------------+----------------+
   |Properties:        |Values:         |
   +===================+================+
   |Context Attributes |space_data.mode |
   +-------------------+----------------+
   |Value              |ACTION          |
   +-------------------+----------------+
   |Value              |DOPESHEET       |
   +-------------------+----------------+
   
   
.. km:hotkey:: Ctrl-Tab -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-------------+
   |Properties:        |Values:      |
   +===================+=============+
   |Context Attributes |area.type    |
   +-------------------+-------------+
   |Value              |GRAPH_EDITOR |
   +-------------------+-------------+
   
   
.. km:hotkey:: Ctrl-A -> action.select_all_toggle

   Select All

   bpy.ops.action.select_all_toggle(invert=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Invert      |False   |
   +------------+--------+
   
   
.. km:hotkey:: O -> action.clean

   Clean Keyframes

   bpy.ops.action.clean(threshold=0.001, channels=False)
   
   
.. km:hotkey:: X -> action.delete

   Delete Keyframes

   bpy.ops.action.delete()
   
   
.. km:hotkey:: DEL -> action.delete

   Delete Keyframes

   bpy.ops.action.delete()
   
   
.. km:hotkeyd:: SELECTMOUSE -> action.clickselect

   Mouse Select Keys

   bpy.ops.action.clickselect(extend=False, column=False, channel=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Column Select |False   |
   +--------------+--------+
   |Only Channel  |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Alt-SELECTMOUSE -> action.clickselect

   Mouse Select Keys

   bpy.ops.action.clickselect(extend=False, column=False, channel=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Column Select |True    |
   +--------------+--------+
   |Only Channel  |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Shift-SELECTMOUSE -> action.clickselect

   Mouse Select Keys

   bpy.ops.action.clickselect(extend=False, column=False, channel=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   |Column Select |False   |
   +--------------+--------+
   |Only Channel  |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-SELECTMOUSE -> action.clickselect

   Mouse Select Keys

   bpy.ops.action.clickselect(extend=False, column=False, channel=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   |Column Select |True    |
   +--------------+--------+
   |Only Channel  |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Alt-SELECTMOUSE -> action.clickselect

   Mouse Select Keys

   bpy.ops.action.clickselect(extend=False, column=False, channel=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Column Select |False   |
   +--------------+--------+
   |Only Channel  |True    |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-Alt-SELECTMOUSE -> action.clickselect

   Mouse Select Keys

   bpy.ops.action.clickselect(extend=False, column=False, channel=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   |Column Select |False   |
   +--------------+--------+
   |Only Channel  |True    |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-SELECTMOUSE -> action.select_leftright

   Select Left/Right

   bpy.ops.action.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Mode          |CHECK   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-SELECTMOUSE -> action.select_leftright

   Select Left/Right

   bpy.ops.action.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   |Mode          |CHECK   |
   +--------------+--------+
   
   
.. km:hotkeyd:: LEFT_BRACKET -> action.select_leftright

   Select Left/Right

   bpy.ops.action.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Mode          |LEFT    |
   +--------------+--------+
   
   
.. km:hotkeyd:: RIGHT_BRACKET -> action.select_leftright

   Select Left/Right

   bpy.ops.action.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Mode          |RIGHT   |
   +--------------+--------+
   
   
.. km:hotkeyd:: A -> action.select_all_toggle

   Select All

   bpy.ops.action.select_all_toggle(invert=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Invert      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> action.select_all_toggle

   Select All

   bpy.ops.action.select_all_toggle(invert=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Invert      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: B -> action.select_border

   Border Select

   bpy.ops.action.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Axis Range  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-B -> action.select_border

   Border Select

   bpy.ops.action.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Axis Range  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-EVT_TWEAK_A -> action.select_lasso

   Lasso Select

   bpy.ops.action.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-EVT_TWEAK_A -> action.select_lasso

   Lasso Select

   bpy.ops.action.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: C -> action.select_circle

   Circle Select

   bpy.ops.action.select_circle(x=0, y=0, radius=1, gesture_mode=0)
   
   
.. km:hotkeyd:: K -> action.select_column

   Select All

   bpy.ops.action.select_column(mode='KEYS')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Mode        |KEYS    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-K -> action.select_column

   Select All

   bpy.ops.action.select_column(mode='KEYS')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Mode        |CFRA    |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-K -> action.select_column

   Select All

   bpy.ops.action.select_column(mode='KEYS')
   
   
   +------------+---------------+
   |Properties: |Values:        |
   +============+===============+
   |Mode        |MARKERS_COLUMN |
   +------------+---------------+
   
   
.. km:hotkeyd:: Alt-K -> action.select_column

   Select All

   bpy.ops.action.select_column(mode='KEYS')
   
   
   +------------+----------------+
   |Properties: |Values:         |
   +============+================+
   |Mode        |MARKERS_BETWEEN |
   +------------+----------------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> action.select_more

   Select More

   bpy.ops.action.select_more()
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> action.select_less

   Select Less

   bpy.ops.action.select_less()
   
   
.. km:hotkeyd:: L -> action.select_linked

   Select Linked

   bpy.ops.action.select_linked()
   
   
.. km:hotkeyd:: Ctrl-G -> action.frame_jump

   Jump to Keyframes

   bpy.ops.action.frame_jump()
   
   
.. km:hotkeyd:: Shift-S -> action.snap

   Snap Keys

   bpy.ops.action.snap(type='CFRA')
   
   
.. km:hotkeyd:: Shift-M -> action.mirror

   Mirror Keys

   bpy.ops.action.mirror(type='CFRA')
   
   
.. km:hotkeyd:: V -> action.handle_type

   Set Keyframe Handle Type

   bpy.ops.action.handle_type(type='FREE')
   
   
.. km:hotkeyd:: T -> action.interpolation_type

   Set Keyframe Interpolation

   bpy.ops.action.interpolation_type(type='CONSTANT')
   
   
.. km:hotkeyd:: Shift-E -> action.extrapolation_type

   Set Keyframe Extrapolation

   bpy.ops.action.extrapolation_type(type='CONSTANT')
   
   
.. km:hotkeyd:: R -> action.keyframe_type

   Set Keyframe Type

   bpy.ops.action.keyframe_type(type='KEYFRAME')
   
   
.. km:hotkeyd:: Shift-O -> action.sample

   Sample Keyframes

   bpy.ops.action.sample()
   
   
.. km:hotkeyd:: X -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+--------------------+
   |Properties: |Values:             |
   +============+====================+
   |Name        |DOPESHEET_MT_delete |
   +------------+--------------------+
   
   
.. km:hotkeyd:: DEL -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+--------------------+
   |Properties: |Values:             |
   +============+====================+
   |Name        |DOPESHEET_MT_delete |
   +------------+--------------------+
   
   
.. km:hotkeyd:: Shift-D -> action.duplicate_move

   Duplicate

   bpy.ops.action.duplicate_move(ACTION_OT_duplicate={}, TRANSFORM_OT_transform={"mode":'TRANSLATION', "value":(0, 0, 0, 0), "axis":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "release_confirm":False})
   
   
   +--------------------+--------+
   |Properties:         |Values: |
   +====================+========+
   |Duplicate Keyframes |N/A     |
   +--------------------+--------+
   |Transform           |N/A     |
   +--------------------+--------+
   
   
.. km:hotkeyd:: I -> action.keyframe_insert

   Insert Keyframes

   bpy.ops.action.keyframe_insert(type='ALL')
   
   
.. km:hotkeyd:: Ctrl-C -> action.copy

   Copy Keyframes

   bpy.ops.action.copy()
   
   
.. km:hotkeyd:: Ctrl-V -> action.paste

   Paste Keyframes

   bpy.ops.action.paste(offset='START', merge='MIX', flipped=False)
   
   
.. km:hotkeyd:: Ctrl-Shift-V -> action.paste

   Paste Keyframes

   bpy.ops.action.paste(offset='START', merge='MIX', flipped=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Flipped     |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Alt-P -> action.previewrange_set

   Auto-Set Preview Range

   bpy.ops.action.previewrange_set()
   
   
.. km:hotkeyd:: HOME -> action.view_all

   View All

   bpy.ops.action.view_all()
   
   
.. km:hotkeyd:: NDOF_BUTTON_FIT -> action.view_all

   View All

   bpy.ops.action.view_all()
   
   
.. km:hotkeyd:: NUMPAD_PERIOD -> action.view_selected

   View Selected

   bpy.ops.action.view_selected()
   
   
.. km:hotkeyd:: NUMPAD_0 -> action.view_frame

   View Frame

   bpy.ops.action.view_frame()
   
   
.. km:hotkeyd:: Tab -> anim.channels_editable_toggle

   Toggle Channel Editability

   bpy.ops.anim.channels_editable_toggle(mode='TOGGLE', type='PROTECT')
   
   
.. km:hotkeyd:: Ctrl-F -> anim.channels_find

   Find Channels

   bpy.ops.anim.channels_find(query="Query")
   
   
.. km:hotkeyd:: G -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+---------------+
   |Properties: |Values:        |
   +============+===============+
   |Mode        |TIME_TRANSLATE |
   +------------+---------------+
   
   
.. km:hotkeyd:: EVT_TWEAK_S -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+---------------+
   |Properties: |Values:        |
   +============+===============+
   |Mode        |TIME_TRANSLATE |
   +------------+---------------+
   
   
.. km:hotkeyd:: E -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |TIME_EXTEND |
   +------------+------------+
   
   
.. km:hotkeyd:: S -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+-----------+
   |Properties: |Values:    |
   +============+===========+
   |Mode        |TIME_SCALE |
   +------------+-----------+
   
   
.. km:hotkeyd:: Shift-T -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+-----------+
   |Properties: |Values:    |
   +============+===========+
   |Mode        |TIME_SLIDE |
   +------------+-----------+
   
   
.. km:hotkeyd:: O -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+--------------------------------------+
   |Properties:        |Values:                               |
   +===================+======================================+
   |Context Attributes |tool_settings.use_proportional_action |
   +-------------------+--------------------------------------+
   
   
.. km:hotkeyd:: M -> marker.add

   Add Time Marker

   bpy.ops.marker.add()
   
   
.. km:hotkeyd:: Ctrl-M -> marker.rename

   Rename Marker

   bpy.ops.marker.rename(name="RenamedMarker")
   
   
