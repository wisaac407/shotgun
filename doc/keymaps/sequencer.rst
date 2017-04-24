*********
Sequencer
*********

.. km:module:: sequencer

   


---------------
Quick Reference
---------------

+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|Hotkey                                                                                |Operator                                             |
+======================================================================================+=====================================================+
|:km:hk:`Ctrl-A <sequencer->Ctrl-A->sequencer.select_all>`                             |:func:`blender:bpy.ops.sequencer.select_all`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`RIGHTMOUSE <sequencer->RIGHTMOUSE->view2d.pan>`                               |:func:`blender:bpy.ops.view2d.pan`                   |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`A <sequencer->A->sequencer.select_all>`                                       |:func:`blender:bpy.ops.sequencer.select_all`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Ctrl-I <sequencer->Ctrl-I->sequencer.select_all>`                             |:func:`blender:bpy.ops.sequencer.select_all`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`K <sequencer->K->sequencer.cut>`                                              |:func:`blender:bpy.ops.sequencer.cut`                |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-K <sequencer->Shift-K->sequencer.cut>`                                  |:func:`blender:bpy.ops.sequencer.cut`                |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`H <sequencer->H->sequencer.mute>`                                             |:func:`blender:bpy.ops.sequencer.mute`               |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-H <sequencer->Shift-H->sequencer.mute>`                                 |:func:`blender:bpy.ops.sequencer.mute`               |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Alt-H <sequencer->Alt-H->sequencer.unmute>`                                   |:func:`blender:bpy.ops.sequencer.unmute`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-Alt-H <sequencer->Shift-Alt-H->sequencer.unmute>`                       |:func:`blender:bpy.ops.sequencer.unmute`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-L <sequencer->Shift-L->sequencer.lock>`                                 |:func:`blender:bpy.ops.sequencer.lock`               |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-Alt-L <sequencer->Shift-Alt-L->sequencer.unlock>`                       |:func:`blender:bpy.ops.sequencer.unlock`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`R <sequencer->R->sequencer.reassign_inputs>`                                  |:func:`blender:bpy.ops.sequencer.reassign_inputs`    |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Alt-R <sequencer->Alt-R->sequencer.reload>`                                   |:func:`blender:bpy.ops.sequencer.reload`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-Alt-R <sequencer->Shift-Alt-R->sequencer.reload>`                       |:func:`blender:bpy.ops.sequencer.reload`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Alt-O <sequencer->Alt-O->sequencer.offset_clear>`                             |:func:`blender:bpy.ops.sequencer.offset_clear`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-D <sequencer->Shift-D->sequencer.duplicate_move>`                       |:func:`blender:bpy.ops.sequencer.duplicate_move`     |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`X <sequencer->X->sequencer.delete>`                                           |:func:`blender:bpy.ops.sequencer.delete`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`DEL <sequencer->DEL->sequencer.delete>`                                       |:func:`blender:bpy.ops.sequencer.delete`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Ctrl-C <sequencer->Ctrl-C->sequencer.copy>`                                   |:func:`blender:bpy.ops.sequencer.copy`               |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Ctrl-V <sequencer->Ctrl-V->sequencer.paste>`                                  |:func:`blender:bpy.ops.sequencer.paste`              |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Y <sequencer->Y->sequencer.images_separate>`                                  |:func:`blender:bpy.ops.sequencer.images_separate`    |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Tab <sequencer->Tab->sequencer.meta_toggle>`                                  |:func:`blender:bpy.ops.sequencer.meta_toggle`        |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Ctrl-G <sequencer->Ctrl-G->sequencer.meta_make>`                              |:func:`blender:bpy.ops.sequencer.meta_make`          |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Alt-G <sequencer->Alt-G->sequencer.meta_separate>`                            |:func:`blender:bpy.ops.sequencer.meta_separate`      |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`HOME <sequencer->HOME->sequencer.view_all>`                                   |:func:`blender:bpy.ops.sequencer.view_all`           |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`NDOF_BUTTON_FIT <sequencer->NDOF_BUTTON_FIT->sequencer.view_all>`             |:func:`blender:bpy.ops.sequencer.view_all`           |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`NUMPAD_PERIOD <sequencer->NUMPAD_PERIOD->sequencer.view_selected>`            |:func:`blender:bpy.ops.sequencer.view_selected`      |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`NUMPAD_0 <sequencer->NUMPAD_0->sequencer.view_frame>`                         |:func:`blender:bpy.ops.sequencer.view_frame`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`PAGE_UP <sequencer->PAGE_UP->sequencer.strip_jump>`                           |:func:`blender:bpy.ops.sequencer.strip_jump`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`PAGE_DOWN <sequencer->PAGE_DOWN->sequencer.strip_jump>`                       |:func:`blender:bpy.ops.sequencer.strip_jump`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Alt-PAGE_UP <sequencer->Alt-PAGE_UP->sequencer.strip_jump>`                   |:func:`blender:bpy.ops.sequencer.strip_jump`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Alt-PAGE_DOWN <sequencer->Alt-PAGE_DOWN->sequencer.strip_jump>`               |:func:`blender:bpy.ops.sequencer.strip_jump`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Alt-LEFT_ARROW <sequencer->Alt-LEFT_ARROW->sequencer.swap>`                   |:func:`blender:bpy.ops.sequencer.swap`               |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Alt-RIGHT_ARROW <sequencer->Alt-RIGHT_ARROW->sequencer.swap>`                 |:func:`blender:bpy.ops.sequencer.swap`               |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`BACK_SPACE <sequencer->BACK_SPACE->sequencer.gap_remove>`                     |:func:`blender:bpy.ops.sequencer.gap_remove`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-BACK_SPACE <sequencer->Shift-BACK_SPACE->sequencer.gap_remove>`         |:func:`blender:bpy.ops.sequencer.gap_remove`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-EQUAL <sequencer->Shift-EQUAL->sequencer.gap_insert>`                   |:func:`blender:bpy.ops.sequencer.gap_insert`         |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-S <sequencer->Shift-S->sequencer.snap>`                                 |:func:`blender:bpy.ops.sequencer.snap`               |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Alt-S <sequencer->Alt-S->sequencer.swap_inputs>`                              |:func:`blender:bpy.ops.sequencer.swap_inputs`        |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`1 <sequencer->1->sequencer.cut_multicam>`                                     |:func:`blender:bpy.ops.sequencer.cut_multicam`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`2 <sequencer->2->sequencer.cut_multicam>`                                     |:func:`blender:bpy.ops.sequencer.cut_multicam`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`3 <sequencer->3->sequencer.cut_multicam>`                                     |:func:`blender:bpy.ops.sequencer.cut_multicam`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`4 <sequencer->4->sequencer.cut_multicam>`                                     |:func:`blender:bpy.ops.sequencer.cut_multicam`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`5 <sequencer->5->sequencer.cut_multicam>`                                     |:func:`blender:bpy.ops.sequencer.cut_multicam`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`6 <sequencer->6->sequencer.cut_multicam>`                                     |:func:`blender:bpy.ops.sequencer.cut_multicam`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`7 <sequencer->7->sequencer.cut_multicam>`                                     |:func:`blender:bpy.ops.sequencer.cut_multicam`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`8 <sequencer->8->sequencer.cut_multicam>`                                     |:func:`blender:bpy.ops.sequencer.cut_multicam`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`9 <sequencer->9->sequencer.cut_multicam>`                                     |:func:`blender:bpy.ops.sequencer.cut_multicam`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`0 <sequencer->0->sequencer.cut_multicam>`                                     |:func:`blender:bpy.ops.sequencer.cut_multicam`       |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`SELECTMOUSE <sequencer->SELECTMOUSE->sequencer.select>`                       |:func:`blender:bpy.ops.sequencer.select`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <sequencer->Shift-SELECTMOUSE->sequencer.select>`           |:func:`blender:bpy.ops.sequencer.select`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Alt-SELECTMOUSE <sequencer->Alt-SELECTMOUSE->sequencer.select>`               |:func:`blender:bpy.ops.sequencer.select`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-Alt-SELECTMOUSE <sequencer->Shift-Alt-SELECTMOUSE->sequencer.select>`   |:func:`blender:bpy.ops.sequencer.select`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <sequencer->Ctrl-SELECTMOUSE->sequencer.select>`             |:func:`blender:bpy.ops.sequencer.select`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Ctrl-Shift-SELECTMOUSE <sequencer->Ctrl-Shift-SELECTMOUSE->sequencer.select>` |:func:`blender:bpy.ops.sequencer.select`             |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <sequencer->Ctrl-NUMPAD_PLUS->sequencer.select_more>`        |:func:`blender:bpy.ops.sequencer.select_more`        |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <sequencer->Ctrl-NUMPAD_MINUS->sequencer.select_less>`      |:func:`blender:bpy.ops.sequencer.select_less`        |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`L <sequencer->L->sequencer.select_linked_pick>`                               |:func:`blender:bpy.ops.sequencer.select_linked_pick` |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-L <sequencer->Shift-L->sequencer.select_linked_pick>`                   |:func:`blender:bpy.ops.sequencer.select_linked_pick` |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Ctrl-L <sequencer->Ctrl-L->sequencer.select_linked>`                          |:func:`blender:bpy.ops.sequencer.select_linked`      |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`B <sequencer->B->sequencer.select_border>`                                    |:func:`blender:bpy.ops.sequencer.select_border`      |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-G <sequencer->Shift-G->sequencer.select_grouped>`                       |:func:`blender:bpy.ops.sequencer.select_grouped`     |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Shift-A <sequencer->Shift-A->wm.call_menu>`                                   |:func:`blender:bpy.ops.wm.call_menu`                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`C <sequencer->C->wm.call_menu>`                                               |:func:`blender:bpy.ops.wm.call_menu`                 |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`S <sequencer->S->sequencer.slip>`                                             |:func:`blender:bpy.ops.sequencer.slip`               |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`O <sequencer->O->wm.context_set_int>`                                         |:func:`blender:bpy.ops.wm.context_set_int`           |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`G <sequencer->G->transform.seq_slide>`                                        |:func:`blender:bpy.ops.transform.seq_slide`          |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`EVT_TWEAK_S <sequencer->EVT_TWEAK_S->transform.seq_slide>`                    |:func:`blender:bpy.ops.transform.seq_slide`          |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`E <sequencer->E->transform.transform>`                                        |:func:`blender:bpy.ops.transform.transform`          |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`M <sequencer->M->marker.add>`                                                 |:func:`blender:bpy.ops.marker.add`                   |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+
|:km:hk:`Ctrl-M <sequencer->Ctrl-M->marker.rename>`                                    |:func:`blender:bpy.ops.marker.rename`                |
+--------------------------------------------------------------------------------------+-----------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> sequencer.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.sequencer.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: RIGHTMOUSE -> view2d.pan : MOUSE -> PRESS

   Pan View

   bpy.ops.view2d.pan(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: A -> sequencer.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.sequencer.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> sequencer.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.sequencer.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: K -> sequencer.cut : KEYBOARD -> PRESS

   Cut Strips

   bpy.ops.sequencer.cut(frame=0, type='SOFT', side='BOTH')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Type        |SOFT    |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-K -> sequencer.cut : KEYBOARD -> PRESS

   Cut Strips

   bpy.ops.sequencer.cut(frame=0, type='SOFT', side='BOTH')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Type        |HARD    |
   +------------+--------+
   
   
.. km:hotkeyd:: H -> sequencer.mute : KEYBOARD -> PRESS

   Mute Strips

   bpy.ops.sequencer.mute(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> sequencer.mute : KEYBOARD -> PRESS

   Mute Strips

   bpy.ops.sequencer.mute(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-H -> sequencer.unmute : KEYBOARD -> PRESS

   Un-Mute Strips

   bpy.ops.sequencer.unmute(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-H -> sequencer.unmute : KEYBOARD -> PRESS

   Un-Mute Strips

   bpy.ops.sequencer.unmute(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-L -> sequencer.lock : KEYBOARD -> PRESS

   Lock Strips

   bpy.ops.sequencer.lock()
   
   
.. km:hotkeyd:: Shift-Alt-L -> sequencer.unlock : KEYBOARD -> PRESS

   UnLock Strips

   bpy.ops.sequencer.unlock()
   
   
.. km:hotkeyd:: R -> sequencer.reassign_inputs : KEYBOARD -> PRESS

   Reassign Inputs

   bpy.ops.sequencer.reassign_inputs()
   
   
.. km:hotkeyd:: Alt-R -> sequencer.reload : KEYBOARD -> PRESS

   Reload Strips

   bpy.ops.sequencer.reload(adjust_length=False)
   
   
.. km:hotkeyd:: Shift-Alt-R -> sequencer.reload : KEYBOARD -> PRESS

   Reload Strips

   bpy.ops.sequencer.reload(adjust_length=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Adjust Length |True    |
   +--------------+--------+
   
   
.. km:hotkeyd:: Alt-O -> sequencer.offset_clear : KEYBOARD -> PRESS

   Clear Strip Offset

   bpy.ops.sequencer.offset_clear()
   
   
.. km:hotkeyd:: Shift-D -> sequencer.duplicate_move : KEYBOARD -> PRESS

   Duplicate Strips

   bpy.ops.sequencer.duplicate_move(SEQUENCER_OT_duplicate={"mode":'TRANSLATION'}, TRANSFORM_OT_seq_slide={"value":(0, 0), "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False})
   
   
   +-----------------+--------+
   |Properties:      |Values: |
   +=================+========+
   |Duplicate Strips |N/A     |
   +-----------------+--------+
   |Sequence Slide   |N/A     |
   +-----------------+--------+
   
   
.. km:hotkeyd:: X -> sequencer.delete : KEYBOARD -> PRESS

   Erase Strips

   bpy.ops.sequencer.delete()
   
   
.. km:hotkeyd:: DEL -> sequencer.delete : KEYBOARD -> PRESS

   Erase Strips

   bpy.ops.sequencer.delete()
   
   
.. km:hotkeyd:: Ctrl-C -> sequencer.copy : KEYBOARD -> PRESS

   Copy

   bpy.ops.sequencer.copy()
   
   
.. km:hotkeyd:: Ctrl-V -> sequencer.paste : KEYBOARD -> PRESS

   Paste

   bpy.ops.sequencer.paste()
   
   
.. km:hotkeyd:: Y -> sequencer.images_separate : KEYBOARD -> PRESS

   Separate Images

   bpy.ops.sequencer.images_separate(length=1)
   
   
.. km:hotkeyd:: Tab -> sequencer.meta_toggle : KEYBOARD -> PRESS

   Toggle Meta Strip

   bpy.ops.sequencer.meta_toggle()
   
   
.. km:hotkeyd:: Ctrl-G -> sequencer.meta_make : KEYBOARD -> PRESS

   Make Meta Strip

   bpy.ops.sequencer.meta_make()
   
   
.. km:hotkeyd:: Alt-G -> sequencer.meta_separate : KEYBOARD -> PRESS

   UnMeta Strip

   bpy.ops.sequencer.meta_separate()
   
   
.. km:hotkeyd:: HOME -> sequencer.view_all : KEYBOARD -> PRESS

   View All

   bpy.ops.sequencer.view_all()
   
   
.. km:hotkeyd:: NDOF_BUTTON_FIT -> sequencer.view_all : NDOF -> PRESS

   View All

   bpy.ops.sequencer.view_all()
   
   
.. km:hotkeyd:: NUMPAD_PERIOD -> sequencer.view_selected : KEYBOARD -> PRESS

   View Selected

   bpy.ops.sequencer.view_selected()
   
   
.. km:hotkeyd:: NUMPAD_0 -> sequencer.view_frame : KEYBOARD -> PRESS

   View Frame

   bpy.ops.sequencer.view_frame()
   
   
.. km:hotkeyd:: PAGE_UP -> sequencer.strip_jump : KEYBOARD -> PRESS

   Jump to Strip

   bpy.ops.sequencer.strip_jump(next=True, center=True)
   
   
   +-----------------+--------+
   |Properties:      |Values: |
   +=================+========+
   |Next Strip       |True    |
   +-----------------+--------+
   |Use strip center |False   |
   +-----------------+--------+
   
   
.. km:hotkeyd:: PAGE_DOWN -> sequencer.strip_jump : KEYBOARD -> PRESS

   Jump to Strip

   bpy.ops.sequencer.strip_jump(next=True, center=True)
   
   
   +-----------------+--------+
   |Properties:      |Values: |
   +=================+========+
   |Next Strip       |False   |
   +-----------------+--------+
   |Use strip center |False   |
   +-----------------+--------+
   
   
.. km:hotkeyd:: Alt-PAGE_UP -> sequencer.strip_jump : KEYBOARD -> PRESS

   Jump to Strip

   bpy.ops.sequencer.strip_jump(next=True, center=True)
   
   
   +-----------------+--------+
   |Properties:      |Values: |
   +=================+========+
   |Next Strip       |True    |
   +-----------------+--------+
   |Use strip center |True    |
   +-----------------+--------+
   
   
.. km:hotkeyd:: Alt-PAGE_DOWN -> sequencer.strip_jump : KEYBOARD -> PRESS

   Jump to Strip

   bpy.ops.sequencer.strip_jump(next=True, center=True)
   
   
   +-----------------+--------+
   |Properties:      |Values: |
   +=================+========+
   |Next Strip       |False   |
   +-----------------+--------+
   |Use strip center |True    |
   +-----------------+--------+
   
   
.. km:hotkeyd:: Alt-LEFT_ARROW -> sequencer.swap : KEYBOARD -> PRESS

   Swap Strip

   bpy.ops.sequencer.swap(side='RIGHT')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Side        |LEFT    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-RIGHT_ARROW -> sequencer.swap : KEYBOARD -> PRESS

   Swap Strip

   bpy.ops.sequencer.swap(side='RIGHT')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Side        |RIGHT   |
   +------------+--------+
   
   
.. km:hotkeyd:: BACK_SPACE -> sequencer.gap_remove : KEYBOARD -> PRESS

   Remove Gaps

   bpy.ops.sequencer.gap_remove(all=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |All Gaps    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-BACK_SPACE -> sequencer.gap_remove : KEYBOARD -> PRESS

   Remove Gaps

   bpy.ops.sequencer.gap_remove(all=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |All Gaps    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-EQUAL -> sequencer.gap_insert : KEYBOARD -> PRESS

   Insert Gaps

   bpy.ops.sequencer.gap_insert(frames=10)
   
   
.. km:hotkeyd:: Shift-S -> sequencer.snap : KEYBOARD -> PRESS

   Snap Strips

   bpy.ops.sequencer.snap(frame=0)
   
   
.. km:hotkeyd:: Alt-S -> sequencer.swap_inputs : KEYBOARD -> PRESS

   Swap Inputs

   bpy.ops.sequencer.swap_inputs()
   
   
.. km:hotkeyd:: 1 -> sequencer.cut_multicam : KEYBOARD -> PRESS

   Cut multicam

   bpy.ops.sequencer.cut_multicam(camera=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Camera      |1       |
   +------------+--------+
   
   
.. km:hotkeyd:: 2 -> sequencer.cut_multicam : KEYBOARD -> PRESS

   Cut multicam

   bpy.ops.sequencer.cut_multicam(camera=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Camera      |2       |
   +------------+--------+
   
   
.. km:hotkeyd:: 3 -> sequencer.cut_multicam : KEYBOARD -> PRESS

   Cut multicam

   bpy.ops.sequencer.cut_multicam(camera=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Camera      |3       |
   +------------+--------+
   
   
.. km:hotkeyd:: 4 -> sequencer.cut_multicam : KEYBOARD -> PRESS

   Cut multicam

   bpy.ops.sequencer.cut_multicam(camera=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Camera      |4       |
   +------------+--------+
   
   
.. km:hotkeyd:: 5 -> sequencer.cut_multicam : KEYBOARD -> PRESS

   Cut multicam

   bpy.ops.sequencer.cut_multicam(camera=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Camera      |5       |
   +------------+--------+
   
   
.. km:hotkeyd:: 6 -> sequencer.cut_multicam : KEYBOARD -> PRESS

   Cut multicam

   bpy.ops.sequencer.cut_multicam(camera=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Camera      |6       |
   +------------+--------+
   
   
.. km:hotkeyd:: 7 -> sequencer.cut_multicam : KEYBOARD -> PRESS

   Cut multicam

   bpy.ops.sequencer.cut_multicam(camera=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Camera      |7       |
   +------------+--------+
   
   
.. km:hotkeyd:: 8 -> sequencer.cut_multicam : KEYBOARD -> PRESS

   Cut multicam

   bpy.ops.sequencer.cut_multicam(camera=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Camera      |8       |
   +------------+--------+
   
   
.. km:hotkeyd:: 9 -> sequencer.cut_multicam : KEYBOARD -> PRESS

   Cut multicam

   bpy.ops.sequencer.cut_multicam(camera=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Camera      |9       |
   +------------+--------+
   
   
.. km:hotkeyd:: 0 -> sequencer.cut_multicam : KEYBOARD -> PRESS

   Cut multicam

   bpy.ops.sequencer.cut_multicam(camera=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Camera      |10      |
   +------------+--------+
   
   
.. km:hotkeyd:: SELECTMOUSE -> sequencer.select : MOUSE -> PRESS

   Activate/Select

   bpy.ops.sequencer.select(extend=False, linked_handle=False, left_right='NONE', linked_time=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend        |False   |
   +--------------+--------+
   |Linked Handle |False   |
   +--------------+--------+
   |Left/Right    |NONE    |
   +--------------+--------+
   |Linked Time   |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Shift-SELECTMOUSE -> sequencer.select : MOUSE -> PRESS

   Activate/Select

   bpy.ops.sequencer.select(extend=False, linked_handle=False, left_right='NONE', linked_time=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend        |True    |
   +--------------+--------+
   |Linked Handle |False   |
   +--------------+--------+
   |Left/Right    |NONE    |
   +--------------+--------+
   |Linked Time   |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Alt-SELECTMOUSE -> sequencer.select : MOUSE -> PRESS

   Activate/Select

   bpy.ops.sequencer.select(extend=False, linked_handle=False, left_right='NONE', linked_time=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend        |False   |
   +--------------+--------+
   |Linked Handle |True    |
   +--------------+--------+
   |Left/Right    |NONE    |
   +--------------+--------+
   |Linked Time   |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-SELECTMOUSE -> sequencer.select : MOUSE -> PRESS

   Activate/Select

   bpy.ops.sequencer.select(extend=False, linked_handle=False, left_right='NONE', linked_time=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend        |True    |
   +--------------+--------+
   |Linked Handle |True    |
   +--------------+--------+
   |Left/Right    |NONE    |
   +--------------+--------+
   |Linked Time   |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-SELECTMOUSE -> sequencer.select : MOUSE -> PRESS

   Activate/Select

   bpy.ops.sequencer.select(extend=False, linked_handle=False, left_right='NONE', linked_time=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend        |False   |
   +--------------+--------+
   |Linked Handle |False   |
   +--------------+--------+
   |Left/Right    |MOUSE   |
   +--------------+--------+
   |Linked Time   |True    |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-SELECTMOUSE -> sequencer.select : MOUSE -> PRESS

   Activate/Select

   bpy.ops.sequencer.select(extend=False, linked_handle=False, left_right='NONE', linked_time=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend        |True    |
   +--------------+--------+
   |Linked Handle |False   |
   +--------------+--------+
   |Left/Right    |NONE    |
   +--------------+--------+
   |Linked Time   |True    |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> sequencer.select_more : KEYBOARD -> PRESS

   Select More

   bpy.ops.sequencer.select_more()
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> sequencer.select_less : KEYBOARD -> PRESS

   Select Less

   bpy.ops.sequencer.select_less()
   
   
.. km:hotkeyd:: L -> sequencer.select_linked_pick : KEYBOARD -> PRESS

   Select Pick Linked

   bpy.ops.sequencer.select_linked_pick(extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-L -> sequencer.select_linked_pick : KEYBOARD -> PRESS

   Select Pick Linked

   bpy.ops.sequencer.select_linked_pick(extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-L -> sequencer.select_linked : KEYBOARD -> PRESS

   Select Linked

   bpy.ops.sequencer.select_linked()
   
   
.. km:hotkeyd:: B -> sequencer.select_border : KEYBOARD -> PRESS

   Border Select

   bpy.ops.sequencer.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkeyd:: Shift-G -> sequencer.select_grouped : KEYBOARD -> PRESS

   Select Grouped

   bpy.ops.sequencer.select_grouped(type='TYPE', extend=False, use_active_channel=False)
   
   
.. km:hotkeyd:: Shift-A -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------+
   |Properties: |Values:          |
   +============+=================+
   |Name        |SEQUENCER_MT_add |
   +------------+-----------------+
   
   
.. km:hotkeyd:: C -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+--------------------+
   |Properties: |Values:             |
   +============+====================+
   |Name        |SEQUENCER_MT_change |
   +------------+--------------------+
   
   
.. km:hotkeyd:: S -> sequencer.slip : KEYBOARD -> PRESS

   Trim Strips

   bpy.ops.sequencer.slip(offset=0)
   
   
.. km:hotkeyd:: O -> wm.context_set_int : KEYBOARD -> PRESS

   Context Set

   bpy.ops.wm.context_set_int(data_path="", value=0, relative=False)
   
   
   +-------------------+------------------------------------+
   |Properties:        |Values:                             |
   +===================+====================================+
   |Context Attributes |scene.sequence_editor.overlay_frame |
   +-------------------+------------------------------------+
   |Value              |0                                   |
   +-------------------+------------------------------------+
   
   
.. km:hotkeyd:: G -> transform.seq_slide : KEYBOARD -> PRESS

   Sequence Slide

   bpy.ops.transform.seq_slide(value=(0, 0), snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
   
   
.. km:hotkeyd:: EVT_TWEAK_S -> transform.seq_slide : TWEAK -> ANY

   Sequence Slide

   bpy.ops.transform.seq_slide(value=(0, 0), snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
   
   
.. km:hotkeyd:: E -> transform.transform : KEYBOARD -> PRESS

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |TIME_EXTEND |
   +------------+------------+
   
   
.. km:hotkeyd:: M -> marker.add : KEYBOARD -> PRESS

   Add Time Marker

   bpy.ops.marker.add()
   
   
.. km:hotkeyd:: Ctrl-M -> marker.rename : KEYBOARD -> PRESS

   Rename Marker

   bpy.ops.marker.rename(name="RenamedMarker")
   
   
