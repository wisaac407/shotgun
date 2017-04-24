**********
NLA Editor
**********

.. km:module:: nlaeditor

   


---------------
Quick Reference
---------------

+------------------------------------------------------------------------------------------+----------------------------------------------+
|Hotkey                                                                                    |Operator                                      |
+==========================================================================================+==============================================+
|:km:hk:`Ctrl-A <nlaeditor->Ctrl-A->nla.select_all_toggle>`                                |:func:`blender:bpy.ops.nla.select_all_toggle` |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`A <nlaeditor->A->nla.apply_scale>`                                                |:func:`blender:bpy.ops.nla.apply_scale`       |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`SELECTMOUSE <nlaeditor->SELECTMOUSE->nla.click_select>`                           |:func:`blender:bpy.ops.nla.click_select`      |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <nlaeditor->Shift-SELECTMOUSE->nla.click_select>`               |:func:`blender:bpy.ops.nla.click_select`      |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <nlaeditor->Ctrl-SELECTMOUSE->nla.select_leftright>`             |:func:`blender:bpy.ops.nla.select_leftright`  |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-Shift-SELECTMOUSE <nlaeditor->Ctrl-Shift-SELECTMOUSE->nla.select_leftright>` |:func:`blender:bpy.ops.nla.select_leftright`  |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`LEFT_BRACKET <nlaeditor->LEFT_BRACKET->nla.select_leftright>`                     |:func:`blender:bpy.ops.nla.select_leftright`  |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`RIGHT_BRACKET <nlaeditor->RIGHT_BRACKET->nla.select_leftright>`                   |:func:`blender:bpy.ops.nla.select_leftright`  |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`A <nlaeditor->A->nla.select_all_toggle>`                                          |:func:`blender:bpy.ops.nla.select_all_toggle` |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-I <nlaeditor->Ctrl-I->nla.select_all_toggle>`                                |:func:`blender:bpy.ops.nla.select_all_toggle` |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`B <nlaeditor->B->nla.select_border>`                                              |:func:`blender:bpy.ops.nla.select_border`     |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Alt-B <nlaeditor->Alt-B->nla.select_border>`                                      |:func:`blender:bpy.ops.nla.select_border`     |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-Alt-P <nlaeditor->Ctrl-Alt-P->nla.previewrange_set>`                         |:func:`blender:bpy.ops.nla.previewrange_set`  |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`HOME <nlaeditor->HOME->nla.view_all>`                                             |:func:`blender:bpy.ops.nla.view_all`          |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`NDOF_BUTTON_FIT <nlaeditor->NDOF_BUTTON_FIT->nla.view_all>`                       |:func:`blender:bpy.ops.nla.view_all`          |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`NUMPAD_PERIOD <nlaeditor->NUMPAD_PERIOD->nla.view_selected>`                      |:func:`blender:bpy.ops.nla.view_selected`     |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`NUMPAD_0 <nlaeditor->NUMPAD_0->nla.view_frame>`                                   |:func:`blender:bpy.ops.nla.view_frame`        |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Shift-A <nlaeditor->Shift-A->nla.actionclip_add>`                                 |:func:`blender:bpy.ops.nla.actionclip_add`    |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Shift-T <nlaeditor->Shift-T->nla.transition_add>`                                 |:func:`blender:bpy.ops.nla.transition_add`    |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Shift-K <nlaeditor->Shift-K->nla.soundclip_add>`                                  |:func:`blender:bpy.ops.nla.soundclip_add`     |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Shift-G <nlaeditor->Shift-G->nla.meta_add>`                                       |:func:`blender:bpy.ops.nla.meta_add`          |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Alt-G <nlaeditor->Alt-G->nla.meta_remove>`                                        |:func:`blender:bpy.ops.nla.meta_remove`       |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Shift-D <nlaeditor->Shift-D->nla.duplicate>`                                      |:func:`blender:bpy.ops.nla.duplicate`         |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Alt-D <nlaeditor->Alt-D->nla.duplicate>`                                          |:func:`blender:bpy.ops.nla.duplicate`         |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`U <nlaeditor->U->nla.make_single_user>`                                           |:func:`blender:bpy.ops.nla.make_single_user`  |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`X <nlaeditor->X->nla.delete>`                                                     |:func:`blender:bpy.ops.nla.delete`            |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`DEL <nlaeditor->DEL->nla.delete>`                                                 |:func:`blender:bpy.ops.nla.delete`            |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Y <nlaeditor->Y->nla.split>`                                                      |:func:`blender:bpy.ops.nla.split`             |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`H <nlaeditor->H->nla.mute_toggle>`                                                |:func:`blender:bpy.ops.nla.mute_toggle`       |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Alt-F <nlaeditor->Alt-F->nla.swap>`                                               |:func:`blender:bpy.ops.nla.swap`              |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`PAGE_UP <nlaeditor->PAGE_UP->nla.move_up>`                                        |:func:`blender:bpy.ops.nla.move_up`           |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`PAGE_DOWN <nlaeditor->PAGE_DOWN->nla.move_down>`                                  |:func:`blender:bpy.ops.nla.move_down`         |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-A <nlaeditor->Ctrl-A->nla.apply_scale>`                                      |:func:`blender:bpy.ops.nla.apply_scale`       |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Alt-S <nlaeditor->Alt-S->nla.clear_scale>`                                        |:func:`blender:bpy.ops.nla.clear_scale`       |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Shift-S <nlaeditor->Shift-S->nla.snap>`                                           |:func:`blender:bpy.ops.nla.snap`              |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-Shift-M <nlaeditor->Ctrl-Shift-M->nla.fmodifier_add>`                        |:func:`blender:bpy.ops.nla.fmodifier_add`     |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`G <nlaeditor->G->transform.transform>`                                            |:func:`blender:bpy.ops.transform.transform`   |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`EVT_TWEAK_S <nlaeditor->EVT_TWEAK_S->transform.transform>`                        |:func:`blender:bpy.ops.transform.transform`   |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`E <nlaeditor->E->transform.transform>`                                            |:func:`blender:bpy.ops.transform.transform`   |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`S <nlaeditor->S->transform.transform>`                                            |:func:`blender:bpy.ops.transform.transform`   |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`M <nlaeditor->M->marker.add>`                                                     |:func:`blender:bpy.ops.marker.add`            |
+------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-M <nlaeditor->Ctrl-M->marker.rename>`                                        |:func:`blender:bpy.ops.marker.rename`         |
+------------------------------------------------------------------------------------------+----------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> nla.select_all_toggle : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.nla.select_all_toggle(invert=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Invert      |False   |
   +------------+--------+
   
   
.. km:hotkey:: A -> nla.apply_scale : KEYBOARD -> PRESS

   Apply Scale

   bpy.ops.nla.apply_scale()
   
   
.. km:hotkeyd:: SELECTMOUSE -> nla.click_select : MOUSE -> PRESS

   Mouse Select

   bpy.ops.nla.click_select(extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Shift-SELECTMOUSE -> nla.click_select : MOUSE -> PRESS

   Mouse Select

   bpy.ops.nla.click_select(extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-SELECTMOUSE -> nla.select_leftright : MOUSE -> PRESS

   Select Left/Right

   bpy.ops.nla.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Mode          |CHECK   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-SELECTMOUSE -> nla.select_leftright : MOUSE -> PRESS

   Select Left/Right

   bpy.ops.nla.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   |Mode          |CHECK   |
   +--------------+--------+
   
   
.. km:hotkeyd:: LEFT_BRACKET -> nla.select_leftright : KEYBOARD -> PRESS

   Select Left/Right

   bpy.ops.nla.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Mode          |LEFT    |
   +--------------+--------+
   
   
.. km:hotkeyd:: RIGHT_BRACKET -> nla.select_leftright : KEYBOARD -> PRESS

   Select Left/Right

   bpy.ops.nla.select_leftright(mode='CHECK', extend=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Mode          |RIGHT   |
   +--------------+--------+
   
   
.. km:hotkeyd:: A -> nla.select_all_toggle : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.nla.select_all_toggle(invert=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Invert      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> nla.select_all_toggle : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.nla.select_all_toggle(invert=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Invert      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: B -> nla.select_border : KEYBOARD -> PRESS

   Border Select

   bpy.ops.nla.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Axis Range  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-B -> nla.select_border : KEYBOARD -> PRESS

   Border Select

   bpy.ops.nla.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, axis_range=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Axis Range  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Alt-P -> nla.previewrange_set : KEYBOARD -> PRESS

   Auto-Set Preview Range

   bpy.ops.nla.previewrange_set()
   
   
.. km:hotkeyd:: HOME -> nla.view_all : KEYBOARD -> PRESS

   View All

   bpy.ops.nla.view_all()
   
   
.. km:hotkeyd:: NDOF_BUTTON_FIT -> nla.view_all : NDOF -> PRESS

   View All

   bpy.ops.nla.view_all()
   
   
.. km:hotkeyd:: NUMPAD_PERIOD -> nla.view_selected : KEYBOARD -> PRESS

   View Selected

   bpy.ops.nla.view_selected()
   
   
.. km:hotkeyd:: NUMPAD_0 -> nla.view_frame : KEYBOARD -> PRESS

   View Frame

   bpy.ops.nla.view_frame()
   
   
.. km:hotkeyd:: Shift-A -> nla.actionclip_add : KEYBOARD -> PRESS

   Add Action Strip

   bpy.ops.nla.actionclip_add(action='<UNKNOWN ENUM>')
   
   
.. km:hotkeyd:: Shift-T -> nla.transition_add : KEYBOARD -> PRESS

   Add Transition

   bpy.ops.nla.transition_add()
   
   
.. km:hotkeyd:: Shift-K -> nla.soundclip_add : KEYBOARD -> PRESS

   Add Sound Clip

   bpy.ops.nla.soundclip_add()
   
   
.. km:hotkeyd:: Shift-G -> nla.meta_add : KEYBOARD -> PRESS

   Add Meta-Strips

   bpy.ops.nla.meta_add()
   
   
.. km:hotkeyd:: Alt-G -> nla.meta_remove : KEYBOARD -> PRESS

   Remove Meta-Strips

   bpy.ops.nla.meta_remove()
   
   
.. km:hotkeyd:: Shift-D -> nla.duplicate : KEYBOARD -> PRESS

   Duplicate Strips

   bpy.ops.nla.duplicate(linked=False, mode='TRANSLATION')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Linked      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-D -> nla.duplicate : KEYBOARD -> PRESS

   Duplicate Strips

   bpy.ops.nla.duplicate(linked=False, mode='TRANSLATION')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Linked      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: U -> nla.make_single_user : KEYBOARD -> PRESS

   Make Single User

   bpy.ops.nla.make_single_user()
   
   
.. km:hotkeyd:: X -> nla.delete : KEYBOARD -> PRESS

   Delete Strips

   bpy.ops.nla.delete()
   
   
.. km:hotkeyd:: DEL -> nla.delete : KEYBOARD -> PRESS

   Delete Strips

   bpy.ops.nla.delete()
   
   
.. km:hotkeyd:: Y -> nla.split : KEYBOARD -> PRESS

   Split Strips

   bpy.ops.nla.split()
   
   
.. km:hotkeyd:: H -> nla.mute_toggle : KEYBOARD -> PRESS

   Toggle Muting

   bpy.ops.nla.mute_toggle()
   
   
.. km:hotkeyd:: Alt-F -> nla.swap : KEYBOARD -> PRESS

   Swap Strips

   bpy.ops.nla.swap()
   
   
.. km:hotkeyd:: PAGE_UP -> nla.move_up : KEYBOARD -> PRESS

   Move Strips Up

   bpy.ops.nla.move_up()
   
   
.. km:hotkeyd:: PAGE_DOWN -> nla.move_down : KEYBOARD -> PRESS

   Move Strips Down

   bpy.ops.nla.move_down()
   
   
.. km:hotkeyd:: Ctrl-A -> nla.apply_scale : KEYBOARD -> PRESS

   Apply Scale

   bpy.ops.nla.apply_scale()
   
   
.. km:hotkeyd:: Alt-S -> nla.clear_scale : KEYBOARD -> PRESS

   Clear Scale

   bpy.ops.nla.clear_scale()
   
   
.. km:hotkeyd:: Shift-S -> nla.snap : KEYBOARD -> PRESS

   Snap Strips

   bpy.ops.nla.snap(type='CFRA')
   
   
.. km:hotkeyd:: Ctrl-Shift-M -> nla.fmodifier_add : KEYBOARD -> PRESS

   Add F-Modifier

   bpy.ops.nla.fmodifier_add(type='NULL', only_active=True)
   
   
.. km:hotkeyd:: G -> transform.transform : KEYBOARD -> PRESS

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |TRANSLATION |
   +------------+------------+
   
   
.. km:hotkeyd:: EVT_TWEAK_S -> transform.transform : TWEAK -> ANY

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |TRANSLATION |
   +------------+------------+
   
   
.. km:hotkeyd:: E -> transform.transform : KEYBOARD -> PRESS

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Mode        |TIME_EXTEND |
   +------------+------------+
   
   
.. km:hotkeyd:: S -> transform.transform : KEYBOARD -> PRESS

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+-----------+
   |Properties: |Values:    |
   +============+===========+
   |Mode        |TIME_SCALE |
   +------------+-----------+
   
   
.. km:hotkeyd:: M -> marker.add : KEYBOARD -> PRESS

   Add Time Marker

   bpy.ops.marker.add()
   
   
.. km:hotkeyd:: Ctrl-M -> marker.rename : KEYBOARD -> PRESS

   Rename Marker

   bpy.ops.marker.rename(name="RenamedMarker")
   
   
