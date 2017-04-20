************
Graph Editor
************

.. km:module:: grapheditor


---------------
Quick Reference
---------------

+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|Hotkey                                                                                           |Operator                                              |
+=================================================================================================+======================================================+
|:km:hk:`Ctrl-Tab <grapheditor->Ctrl-Tab->wm.context_set_enum>`                                   |:func:`blender:bpy.ops.wm.context_set_enum`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`SELECTMOUSE <grapheditor->SELECTMOUSE->graph.cursor_set>`                                |:func:`blender:bpy.ops.graph.cursor_set`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-SELECTMOUSE <grapheditor->Alt-SELECTMOUSE->graph.select_leftright>`                  |:func:`blender:bpy.ops.graph.select_leftright`        |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-Alt-SELECTMOUSE <grapheditor->Shift-Alt-SELECTMOUSE->graph.select_leftright>`      |:func:`blender:bpy.ops.graph.select_leftright`        |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-A <grapheditor->Ctrl-A->graph.select_all_toggle>`                                   |:func:`blender:bpy.ops.graph.select_all_toggle`       |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-EVT_TWEAK_S <grapheditor->Ctrl-EVT_TWEAK_S->graph.select_lasso>`                    |:func:`blender:bpy.ops.graph.select_lasso`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-EVT_TWEAK_S <grapheditor->Ctrl-Shift-EVT_TWEAK_S->graph.select_lasso>`        |:func:`blender:bpy.ops.graph.select_lasso`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`O <grapheditor->O->graph.clean>`                                                         |:func:`blender:bpy.ops.graph.clean`                   |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`X <grapheditor->X->graph.delete>`                                                        |:func:`blender:bpy.ops.graph.delete`                  |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`DEL <grapheditor->DEL->graph.delete>`                                                    |:func:`blender:bpy.ops.graph.delete`                  |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <grapheditor->Ctrl-SELECTMOUSE->graph.click_insert>`                    |:func:`blender:bpy.ops.graph.click_insert`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`NDOF_BUTTON_FIT <grapheditor->NDOF_BUTTON_FIT->graph.view_all>`                          |:func:`blender:bpy.ops.graph.view_all`                |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-M <grapheditor->Ctrl-M->marker.rename>`                                             |:func:`blender:bpy.ops.marker.rename`                 |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-H <grapheditor->Ctrl-H->wm.context_toggle>`                                         |:func:`blender:bpy.ops.wm.context_toggle`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`ACTIONMOUSE <grapheditor->ACTIONMOUSE->graph.cursor_set>`                                |:func:`blender:bpy.ops.graph.cursor_set`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`SELECTMOUSE <grapheditor->SELECTMOUSE->graph.clickselect>`                               |:func:`blender:bpy.ops.graph.clickselect`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-SELECTMOUSE <grapheditor->Alt-SELECTMOUSE->graph.clickselect>`                       |:func:`blender:bpy.ops.graph.clickselect`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <grapheditor->Shift-SELECTMOUSE->graph.clickselect>`                   |:func:`blender:bpy.ops.graph.clickselect`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-Alt-SELECTMOUSE <grapheditor->Shift-Alt-SELECTMOUSE->graph.clickselect>`           |:func:`blender:bpy.ops.graph.clickselect`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Alt-SELECTMOUSE <grapheditor->Ctrl-Alt-SELECTMOUSE->graph.clickselect>`             |:func:`blender:bpy.ops.graph.clickselect`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-SELECTMOUSE <grapheditor->Ctrl-Shift-Alt-SELECTMOUSE->graph.clickselect>` |:func:`blender:bpy.ops.graph.clickselect`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <grapheditor->Ctrl-SELECTMOUSE->graph.select_leftright>`                |:func:`blender:bpy.ops.graph.select_leftright`        |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-SELECTMOUSE <grapheditor->Ctrl-Shift-SELECTMOUSE->graph.select_leftright>`    |:func:`blender:bpy.ops.graph.select_leftright`        |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`LEFT_BRACKET <grapheditor->LEFT_BRACKET->graph.select_leftright>`                        |:func:`blender:bpy.ops.graph.select_leftright`        |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`RIGHT_BRACKET <grapheditor->RIGHT_BRACKET->graph.select_leftright>`                      |:func:`blender:bpy.ops.graph.select_leftright`        |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`A <grapheditor->A->graph.select_all_toggle>`                                             |:func:`blender:bpy.ops.graph.select_all_toggle`       |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-I <grapheditor->Ctrl-I->graph.select_all_toggle>`                                   |:func:`blender:bpy.ops.graph.select_all_toggle`       |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`B <grapheditor->B->graph.select_border>`                                                 |:func:`blender:bpy.ops.graph.select_border`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-B <grapheditor->Alt-B->graph.select_border>`                                         |:func:`blender:bpy.ops.graph.select_border`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-B <grapheditor->Ctrl-B->graph.select_border>`                                       |:func:`blender:bpy.ops.graph.select_border`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Alt-B <grapheditor->Ctrl-Alt-B->graph.select_border>`                               |:func:`blender:bpy.ops.graph.select_border`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-EVT_TWEAK_A <grapheditor->Ctrl-EVT_TWEAK_A->graph.select_lasso>`                    |:func:`blender:bpy.ops.graph.select_lasso`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-EVT_TWEAK_A <grapheditor->Ctrl-Shift-EVT_TWEAK_A->graph.select_lasso>`        |:func:`blender:bpy.ops.graph.select_lasso`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`C <grapheditor->C->graph.select_circle>`                                                 |:func:`blender:bpy.ops.graph.select_circle`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`K <grapheditor->K->graph.select_column>`                                                 |:func:`blender:bpy.ops.graph.select_column`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-K <grapheditor->Ctrl-K->graph.select_column>`                                       |:func:`blender:bpy.ops.graph.select_column`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-K <grapheditor->Shift-K->graph.select_column>`                                     |:func:`blender:bpy.ops.graph.select_column`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-K <grapheditor->Alt-K->graph.select_column>`                                         |:func:`blender:bpy.ops.graph.select_column`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <grapheditor->Ctrl-NUMPAD_PLUS->graph.select_more>`                     |:func:`blender:bpy.ops.graph.select_more`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <grapheditor->Ctrl-NUMPAD_MINUS->graph.select_less>`                   |:func:`blender:bpy.ops.graph.select_less`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`L <grapheditor->L->graph.select_linked>`                                                 |:func:`blender:bpy.ops.graph.select_linked`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-G <grapheditor->Ctrl-G->graph.frame_jump>`                                          |:func:`blender:bpy.ops.graph.frame_jump`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-S <grapheditor->Shift-S->graph.snap>`                                              |:func:`blender:bpy.ops.graph.snap`                    |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-M <grapheditor->Shift-M->graph.mirror>`                                            |:func:`blender:bpy.ops.graph.mirror`                  |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`V <grapheditor->V->graph.handle_type>`                                                   |:func:`blender:bpy.ops.graph.handle_type`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`T <grapheditor->T->graph.interpolation_type>`                                            |:func:`blender:bpy.ops.graph.interpolation_type`      |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-E <grapheditor->Ctrl-E->graph.easing_type>`                                         |:func:`blender:bpy.ops.graph.easing_type`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-O <grapheditor->Alt-O->graph.smooth>`                                                |:func:`blender:bpy.ops.graph.smooth`                  |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-O <grapheditor->Shift-O->graph.sample>`                                            |:func:`blender:bpy.ops.graph.sample`                  |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-C <grapheditor->Alt-C->graph.bake>`                                                  |:func:`blender:bpy.ops.graph.bake`                    |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`X <grapheditor->X->wm.call_menu>`                                                        |:func:`blender:bpy.ops.wm.call_menu`                  |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`DEL <grapheditor->DEL->wm.call_menu>`                                                    |:func:`blender:bpy.ops.wm.call_menu`                  |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-D <grapheditor->Shift-D->graph.duplicate_move>`                                    |:func:`blender:bpy.ops.graph.duplicate_move`          |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`I <grapheditor->I->graph.keyframe_insert>`                                               |:func:`blender:bpy.ops.graph.keyframe_insert`         |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-ACTIONMOUSE <grapheditor->Ctrl-ACTIONMOUSE->graph.click_insert>`                    |:func:`blender:bpy.ops.graph.click_insert`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-ACTIONMOUSE <grapheditor->Ctrl-Shift-ACTIONMOUSE->graph.click_insert>`        |:func:`blender:bpy.ops.graph.click_insert`            |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-C <grapheditor->Ctrl-C->graph.copy>`                                                |:func:`blender:bpy.ops.graph.copy`                    |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-V <grapheditor->Ctrl-V->graph.paste>`                                               |:func:`blender:bpy.ops.graph.paste`                   |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-V <grapheditor->Ctrl-Shift-V->graph.paste>`                                   |:func:`blender:bpy.ops.graph.paste`                   |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Alt-P <grapheditor->Ctrl-Alt-P->graph.previewrange_set>`                            |:func:`blender:bpy.ops.graph.previewrange_set`        |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`HOME <grapheditor->HOME->graph.view_all>`                                                |:func:`blender:bpy.ops.graph.view_all`                |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`NDOF_BUTTON_FIT <grapheditor->NDOF_BUTTON_FIT->graph.view_all>`                          |:func:`blender:bpy.ops.graph.view_all`                |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`NUMPAD_PERIOD <grapheditor->NUMPAD_PERIOD->graph.view_selected>`                         |:func:`blender:bpy.ops.graph.view_selected`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`NUMPAD_0 <grapheditor->NUMPAD_0->graph.view_frame>`                                      |:func:`blender:bpy.ops.graph.view_frame`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-Shift-M <grapheditor->Ctrl-Shift-M->graph.fmodifier_add>`                           |:func:`blender:bpy.ops.graph.fmodifier_add`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Tab <grapheditor->Tab->anim.channels_editable_toggle>`                                   |:func:`blender:bpy.ops.anim.channels_editable_toggle` |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`G <grapheditor->G->transform.translate>`                                                 |:func:`blender:bpy.ops.transform.translate`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`EVT_TWEAK_S <grapheditor->EVT_TWEAK_S->transform.translate>`                             |:func:`blender:bpy.ops.transform.translate`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`E <grapheditor->E->transform.transform>`                                                 |:func:`blender:bpy.ops.transform.transform`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`R <grapheditor->R->transform.rotate>`                                                    |:func:`blender:bpy.ops.transform.rotate`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`S <grapheditor->S->transform.resize>`                                                    |:func:`blender:bpy.ops.transform.resize`              |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`O <grapheditor->O->wm.context_toggle>`                                                   |:func:`blender:bpy.ops.wm.context_toggle`             |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`, <grapheditor->,->wm.context_set_enum>`                                                 |:func:`blender:bpy.ops.wm.context_set_enum`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`. <grapheditor->.->wm.context_set_enum>`                                                 |:func:`blender:bpy.ops.wm.context_set_enum`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-. <grapheditor->Ctrl-.->wm.context_set_enum>`                                       |:func:`blender:bpy.ops.wm.context_set_enum`           |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`M <grapheditor->M->marker.add>`                                                          |:func:`blender:bpy.ops.marker.add`                    |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-M <grapheditor->Ctrl-M->marker.rename>`                                             |:func:`blender:bpy.ops.marker.rename`                 |
+-------------------------------------------------------------------------------------------------+------------------------------------------------------+


------------------
Detailed Reference
------------------

.. km:hotkey:: Ctrl-Tab -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-----------------+
   |Properties:        |Values:          |
   +===================+=================+
   |Context Attributes |area.type        |
   +-------------------+-----------------+
   |Value              |DOPESHEET_EDITOR |
   +-------------------+-----------------+
   
   
.. km:hotkey:: SELECTMOUSE -> graph.cursor_set

   Set Cursor

   bpy.ops.graph.cursor_set(frame=0, value=0)
   
   
.. km:hotkey:: Alt-SELECTMOUSE -> graph.select_leftright

   Select Left/Right

   bpy.ops.graph.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Mode          |CHECK   |
   +--------------+--------+
   |Extend Select |False   |
   +--------------+--------+
   
   
.. km:hotkey:: Shift-Alt-SELECTMOUSE -> graph.select_leftright

   Select Left/Right

   bpy.ops.graph.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Mode          |CHECK   |
   +--------------+--------+
   |Extend Select |True    |
   +--------------+--------+
   
   
.. km:hotkey:: Ctrl-A -> graph.select_all_toggle

   Select All

   bpy.ops.graph.select_all_toggle(invert=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Invert      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-EVT_TWEAK_S -> graph.select_lasso

   Lasso Select

   bpy.ops.graph.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-EVT_TWEAK_S -> graph.select_lasso

   Lasso Select

   bpy.ops.graph.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkey:: O -> graph.clean

   Clean Keyframes

   bpy.ops.graph.clean(threshold=0.001, channels=False)
   
   
.. km:hotkey:: X -> graph.delete

   Delete Keyframes

   bpy.ops.graph.delete()
   
   
.. km:hotkey:: DEL -> graph.delete

   Delete Keyframes

   bpy.ops.graph.delete()
   
   
.. km:hotkey:: Ctrl-SELECTMOUSE -> graph.click_insert

   Click-Insert Keyframes

   bpy.ops.graph.click_insert(frame=1, value=1, extend=False)
   
   
.. km:hotkey:: NDOF_BUTTON_FIT -> graph.view_all

   View All

   bpy.ops.graph.view_all(include_handles=True)
   
   
.. km:hotkey:: Ctrl-M -> marker.rename

   Rename Marker

   bpy.ops.marker.rename(name="RenamedMarker")
   
   
.. km:hotkey:: Ctrl-H -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+------------------------+
   |Properties:        |Values:                 |
   +===================+========================+
   |Context Attributes |space_data.show_handles |
   +-------------------+------------------------+
   
   
.. km:hotkey:: ACTIONMOUSE -> graph.cursor_set

   Set Cursor

   bpy.ops.graph.cursor_set(frame=0, value=0)
   
   
.. km:hotkey:: SELECTMOUSE -> graph.clickselect

   Mouse Select Keys

   bpy.ops.graph.clickselect(extend=False, column=False, curves=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Only Curves   |False   |
   +--------------+--------+
   |Column Select |False   |
   +--------------+--------+
   
   
.. km:hotkey:: Alt-SELECTMOUSE -> graph.clickselect

   Mouse Select Keys

   bpy.ops.graph.clickselect(extend=False, column=False, curves=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Only Curves   |False   |
   +--------------+--------+
   |Column Select |True    |
   +--------------+--------+
   
   
.. km:hotkey:: Shift-SELECTMOUSE -> graph.clickselect

   Mouse Select Keys

   bpy.ops.graph.clickselect(extend=False, column=False, curves=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   |Only Curves   |False   |
   +--------------+--------+
   |Column Select |False   |
   +--------------+--------+
   
   
.. km:hotkey:: Shift-Alt-SELECTMOUSE -> graph.clickselect

   Mouse Select Keys

   bpy.ops.graph.clickselect(extend=False, column=False, curves=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   |Only Curves   |False   |
   +--------------+--------+
   |Column Select |True    |
   +--------------+--------+
   
   
.. km:hotkey:: Ctrl-Alt-SELECTMOUSE -> graph.clickselect

   Mouse Select Keys

   bpy.ops.graph.clickselect(extend=False, column=False, curves=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Only Curves   |True    |
   +--------------+--------+
   |Column Select |False   |
   +--------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-Alt-SELECTMOUSE -> graph.clickselect

   Mouse Select Keys

   bpy.ops.graph.clickselect(extend=False, column=False, curves=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   |Only Curves   |True    |
   +--------------+--------+
   |Column Select |False   |
   +--------------+--------+
   
   
.. km:hotkey:: Ctrl-SELECTMOUSE -> graph.select_leftright

   Select Left/Right

   bpy.ops.graph.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Mode          |CHECK   |
   +--------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-SELECTMOUSE -> graph.select_leftright

   Select Left/Right

   bpy.ops.graph.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   |Mode          |CHECK   |
   +--------------+--------+
   
   
.. km:hotkey:: LEFT_BRACKET -> graph.select_leftright

   Select Left/Right

   bpy.ops.graph.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Mode          |LEFT    |
   +--------------+--------+
   
   
.. km:hotkey:: RIGHT_BRACKET -> graph.select_leftright

   Select Left/Right

   bpy.ops.graph.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Mode          |RIGHT   |
   +--------------+--------+
   
   
.. km:hotkey:: A -> graph.select_all_toggle

   Select All

   bpy.ops.graph.select_all_toggle(invert=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Invert      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-I -> graph.select_all_toggle

   Select All

   bpy.ops.graph.select_all_toggle(invert=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Invert      |True    |
   +------------+--------+
   
   
.. km:hotkey:: B -> graph.select_border

   Border Select

   bpy.ops.graph.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False, include_handles=False)
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Axis Range      |False   |
   +----------------+--------+
   |Include Handles |False   |
   +----------------+--------+
   
   
.. km:hotkey:: Alt-B -> graph.select_border

   Border Select

   bpy.ops.graph.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False, include_handles=False)
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Axis Range      |True    |
   +----------------+--------+
   |Include Handles |False   |
   +----------------+--------+
   
   
.. km:hotkey:: Ctrl-B -> graph.select_border

   Border Select

   bpy.ops.graph.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False, include_handles=False)
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Axis Range      |False   |
   +----------------+--------+
   |Include Handles |True    |
   +----------------+--------+
   
   
.. km:hotkey:: Ctrl-Alt-B -> graph.select_border

   Border Select

   bpy.ops.graph.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False, include_handles=False)
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Axis Range      |True    |
   +----------------+--------+
   |Include Handles |True    |
   +----------------+--------+
   
   
.. km:hotkey:: Ctrl-EVT_TWEAK_A -> graph.select_lasso

   Lasso Select

   bpy.ops.graph.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-EVT_TWEAK_A -> graph.select_lasso

   Lasso Select

   bpy.ops.graph.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkey:: C -> graph.select_circle

   Circle Select

   bpy.ops.graph.select_circle(x=0, y=0, radius=1, gesture_mode=0)
   
   
.. km:hotkey:: K -> graph.select_column

   Select All

   bpy.ops.graph.select_column(mode='KEYS')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Mode        |KEYS    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-K -> graph.select_column

   Select All

   bpy.ops.graph.select_column(mode='KEYS')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Mode        |CFRA    |
   +------------+--------+
   
   
.. km:hotkey:: Shift-K -> graph.select_column

   Select All

   bpy.ops.graph.select_column(mode='KEYS')
   
   
   +------------+---------------+
   |Properties: |Values:        |
   +============+===============+
   |Mode        |MARKERS_COLUMN |
   +------------+---------------+
   
   
.. km:hotkey:: Alt-K -> graph.select_column

   Select All

   bpy.ops.graph.select_column(mode='KEYS')
   
   
   +------------+----------------+
   |Properties: |Values:         |
   +============+================+
   |Mode        |MARKERS_BETWEEN |
   +------------+----------------+
   
   
.. km:hotkey:: Ctrl-NUMPAD_PLUS -> graph.select_more

   Select More

   bpy.ops.graph.select_more()
   
   
.. km:hotkey:: Ctrl-NUMPAD_MINUS -> graph.select_less

   Select Less

   bpy.ops.graph.select_less()
   
   
.. km:hotkey:: L -> graph.select_linked

   Select Linked

   bpy.ops.graph.select_linked()
   
   
.. km:hotkey:: Ctrl-G -> graph.frame_jump

   Jump to Keyframes

   bpy.ops.graph.frame_jump()
   
   
.. km:hotkey:: Shift-S -> graph.snap

   Snap Keys

   bpy.ops.graph.snap(type='CFRA')
   
   
.. km:hotkey:: Shift-M -> graph.mirror

   Mirror Keys

   bpy.ops.graph.mirror(type='CFRA')
   
   
.. km:hotkey:: V -> graph.handle_type

   Set Keyframe Handle Type

   bpy.ops.graph.handle_type(type='FREE')
   
   
.. km:hotkey:: T -> graph.interpolation_type

   Set Keyframe Interpolation

   bpy.ops.graph.interpolation_type(type='CONSTANT')
   
   
.. km:hotkey:: Ctrl-E -> graph.easing_type

   Set Keyframe Easing Type

   bpy.ops.graph.easing_type(type='AUTO')
   
   
.. km:hotkey:: Alt-O -> graph.smooth

   Smooth Keys

   bpy.ops.graph.smooth()
   
   
.. km:hotkey:: Shift-O -> graph.sample

   Sample Keyframes

   bpy.ops.graph.sample()
   
   
.. km:hotkey:: Alt-C -> graph.bake

   Bake Curve

   bpy.ops.graph.bake()
   
   
.. km:hotkey:: X -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+----------------+
   |Properties: |Values:         |
   +============+================+
   |Name        |GRAPH_MT_delete |
   +------------+----------------+
   
   
.. km:hotkey:: DEL -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+----------------+
   |Properties: |Values:         |
   +============+================+
   |Name        |GRAPH_MT_delete |
   +------------+----------------+
   
   
.. km:hotkey:: Shift-D -> graph.duplicate_move

   Duplicate

   bpy.ops.graph.duplicate_move(GRAPH_OT_duplicate={"mode":'TRANSLATION'}, TRANSFORM_OT_transform={"mode":'TRANSLATION', "value":(0, 0, 0, 0), "axis":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "release_confirm":False})
   
   
   +--------------------+--------+
   |Properties:         |Values: |
   +====================+========+
   |Duplicate Keyframes |N/A     |
   +--------------------+--------+
   |Transform           |N/A     |
   +--------------------+--------+
   
   
.. km:hotkey:: I -> graph.keyframe_insert

   Insert Keyframes

   bpy.ops.graph.keyframe_insert(type='ALL')
   
   
.. km:hotkey:: Ctrl-ACTIONMOUSE -> graph.click_insert

   Click-Insert Keyframes

   bpy.ops.graph.click_insert(frame=1, value=1, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-ACTIONMOUSE -> graph.click_insert

   Click-Insert Keyframes

   bpy.ops.graph.click_insert(frame=1, value=1, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-C -> graph.copy

   Copy Keyframes

   bpy.ops.graph.copy()
   
   
.. km:hotkey:: Ctrl-V -> graph.paste

   Paste Keyframes

   bpy.ops.graph.paste(offset='START', merge='MIX', flipped=False)
   
   
.. km:hotkey:: Ctrl-Shift-V -> graph.paste

   Paste Keyframes

   bpy.ops.graph.paste(offset='START', merge='MIX', flipped=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Flipped     |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Alt-P -> graph.previewrange_set

   Auto-Set Preview Range

   bpy.ops.graph.previewrange_set()
   
   
.. km:hotkey:: HOME -> graph.view_all

   View All

   bpy.ops.graph.view_all(include_handles=True)
   
   
.. km:hotkey:: NDOF_BUTTON_FIT -> graph.view_all

   View All

   bpy.ops.graph.view_all(include_handles=True)
   
   
.. km:hotkey:: NUMPAD_PERIOD -> graph.view_selected

   View Selected

   bpy.ops.graph.view_selected(include_handles=True)
   
   
.. km:hotkey:: NUMPAD_0 -> graph.view_frame

   View Frame

   bpy.ops.graph.view_frame()
   
   
.. km:hotkey:: Ctrl-Shift-M -> graph.fmodifier_add

   Add F-Curve Modifier

   bpy.ops.graph.fmodifier_add(type='NULL', only_active=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Only Active |False   |
   +------------+--------+
   
   
.. km:hotkey:: Tab -> anim.channels_editable_toggle

   Toggle Channel Editability

   bpy.ops.anim.channels_editable_toggle(mode='TOGGLE', type='PROTECT')
   
   
.. km:hotkey:: G -> transform.translate

   Translate

   bpy.ops.transform.translate(value=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
.. km:hotkey:: EVT_TWEAK_S -> transform.translate

   Translate

   bpy.ops.transform.translate(value=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
.. km:hotkey:: E -> transform.transform

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |TIME_EXTEND |
   +------------+------------+
   
   
.. km:hotkey:: R -> transform.rotate

   Rotate

   bpy.ops.transform.rotate(value=0, axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
.. km:hotkey:: S -> transform.resize

   Resize

   bpy.ops.transform.resize(value=(1, 1, 1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
.. km:hotkey:: O -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+--------------------------------------+
   |Properties:        |Values:                               |
   +===================+======================================+
   |Context Attributes |tool_settings.use_proportional_fcurve |
   +-------------------+--------------------------------------+
   
   
.. km:hotkey:: , -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |space_data.pivot_point |
   +-------------------+-----------------------+
   |Value              |BOUNDING_BOX_CENTER    |
   +-------------------+-----------------------+
   
   
.. km:hotkey:: . -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |space_data.pivot_point |
   +-------------------+-----------------------+
   |Value              |CURSOR                 |
   +-------------------+-----------------------+
   
   
.. km:hotkey:: Ctrl-. -> wm.context_set_enum

   Context Set Enum

   bpy.ops.wm.context_set_enum(data_path="", value="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |space_data.pivot_point |
   +-------------------+-----------------------+
   |Value              |INDIVIDUAL_ORIGINS     |
   +-------------------+-----------------------+
   
   
.. km:hotkey:: M -> marker.add

   Add Time Marker

   bpy.ops.marker.add()
   
   
.. km:hotkey:: Ctrl-M -> marker.rename

   Rename Marker

   bpy.ops.marker.rename(name="RenamedMarker")
   
   
