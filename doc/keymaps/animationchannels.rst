******************
Animation Channels
******************

.. km:module:: animationchannels


---------------
Quick Reference
---------------

+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|Hotkey                                                                                       |Operator                                                |
+=============================================================================================+========================================================+
|:km:hk:`Ctrl-A <animationchannels->Ctrl-A->anim.channels_select_all_toggle>`                 |:func:`blender:bpy.ops.anim.channels_select_all_toggle` |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-G <animationchannels->Alt-G->anim.channels_ungroup>`                             |:func:`blender:bpy.ops.anim.channels_ungroup`           |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`V <animationchannels->V->anim.channels_visibility_set>`                              |:func:`blender:bpy.ops.anim.channels_visibility_set`    |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`LEFTMOUSE <animationchannels->LEFTMOUSE->anim.channels_click>`                       |:func:`blender:bpy.ops.anim.channels_click`             |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-LEFTMOUSE <animationchannels->Shift-LEFTMOUSE->anim.channels_click>`           |:func:`blender:bpy.ops.anim.channels_click`             |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-LEFTMOUSE <animationchannels->Ctrl-Shift-LEFTMOUSE->anim.channels_click>` |:func:`blender:bpy.ops.anim.channels_click`             |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-LEFTMOUSE <animationchannels->Ctrl-LEFTMOUSE->anim.channels_rename>`            |:func:`blender:bpy.ops.anim.channels_rename`            |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`LEFTMOUSE <animationchannels->LEFTMOUSE->anim.channels_rename>`                      |:func:`blender:bpy.ops.anim.channels_rename`            |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`LEFTMOUSE <animationchannels->LEFTMOUSE->anim.channel_select_keys>`                  |:func:`blender:bpy.ops.anim.channel_select_keys`        |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-LEFTMOUSE <animationchannels->Shift-LEFTMOUSE->anim.channel_select_keys>`      |:func:`blender:bpy.ops.anim.channel_select_keys`        |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-F <animationchannels->Ctrl-F->anim.channels_find>`                              |:func:`blender:bpy.ops.anim.channels_find`              |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`A <animationchannels->A->anim.channels_select_all_toggle>`                           |:func:`blender:bpy.ops.anim.channels_select_all_toggle` |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-I <animationchannels->Ctrl-I->anim.channels_select_all_toggle>`                 |:func:`blender:bpy.ops.anim.channels_select_all_toggle` |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`B <animationchannels->B->anim.channels_select_border>`                               |:func:`blender:bpy.ops.anim.channels_select_border`     |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`EVT_TWEAK_L <animationchannels->EVT_TWEAK_L->anim.channels_select_border>`           |:func:`blender:bpy.ops.anim.channels_select_border`     |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`X <animationchannels->X->anim.channels_delete>`                                      |:func:`blender:bpy.ops.anim.channels_delete`            |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`DEL <animationchannels->DEL->anim.channels_delete>`                                  |:func:`blender:bpy.ops.anim.channels_delete`            |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-W <animationchannels->Shift-W->anim.channels_setting_toggle>`                  |:func:`blender:bpy.ops.anim.channels_setting_toggle`    |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-W <animationchannels->Ctrl-Shift-W->anim.channels_setting_enable>`        |:func:`blender:bpy.ops.anim.channels_setting_enable`    |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-W <animationchannels->Alt-W->anim.channels_setting_disable>`                     |:func:`blender:bpy.ops.anim.channels_setting_disable`   |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Tab <animationchannels->Tab->anim.channels_editable_toggle>`                         |:func:`blender:bpy.ops.anim.channels_editable_toggle`   |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`NUMPAD_PLUS <animationchannels->NUMPAD_PLUS->anim.channels_expand>`                  |:func:`blender:bpy.ops.anim.channels_expand`            |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`NUMPAD_MINUS <animationchannels->NUMPAD_MINUS->anim.channels_collapse>`              |:func:`blender:bpy.ops.anim.channels_collapse`          |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <animationchannels->Ctrl-NUMPAD_PLUS->anim.channels_expand>`        |:func:`blender:bpy.ops.anim.channels_expand`            |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <animationchannels->Ctrl-NUMPAD_MINUS->anim.channels_collapse>`    |:func:`blender:bpy.ops.anim.channels_collapse`          |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`PAGE_UP <animationchannels->PAGE_UP->anim.channels_move>`                            |:func:`blender:bpy.ops.anim.channels_move`              |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`PAGE_DOWN <animationchannels->PAGE_DOWN->anim.channels_move>`                        |:func:`blender:bpy.ops.anim.channels_move`              |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-PAGE_UP <animationchannels->Shift-PAGE_UP->anim.channels_move>`                |:func:`blender:bpy.ops.anim.channels_move`              |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-PAGE_DOWN <animationchannels->Shift-PAGE_DOWN->anim.channels_move>`            |:func:`blender:bpy.ops.anim.channels_move`              |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-G <animationchannels->Ctrl-G->anim.channels_group>`                             |:func:`blender:bpy.ops.anim.channels_group`             |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-G <animationchannels->Alt-G->anim.channels_ungroup>`                             |:func:`blender:bpy.ops.anim.channels_ungroup`           |
+---------------------------------------------------------------------------------------------+--------------------------------------------------------+


------------------
Detailed Reference
------------------

.. km:hotkey:: Ctrl-A -> anim.channels_select_all_toggle

   Select All

   bpy.ops.anim.channels_select_all_toggle(invert=False)
   
   
.. km:hotkey:: Alt-G -> anim.channels_ungroup

   Ungroup Channels

   bpy.ops.anim.channels_ungroup()
   
   
.. km:hotkeyi:: V -> anim.channels_visibility_set

   ANIM_OT_channels_visibility_set

   
.. km:hotkey:: LEFTMOUSE -> anim.channels_click

   Mouse Click on Channels

   bpy.ops.anim.channels_click(extend=False, children_only=False)
   
   
.. km:hotkey:: Shift-LEFTMOUSE -> anim.channels_click

   Mouse Click on Channels

   bpy.ops.anim.channels_click(extend=False, children_only=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |True    |
   +--------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-LEFTMOUSE -> anim.channels_click

   Mouse Click on Channels

   bpy.ops.anim.channels_click(extend=False, children_only=False)
   
   
   +---------------------+--------+
   |Properties:          |Values: |
   +=====================+========+
   |Select Children Only |True    |
   +---------------------+--------+
   
   
.. km:hotkey:: Ctrl-LEFTMOUSE -> anim.channels_rename

   Rename Channels

   bpy.ops.anim.channels_rename()
   
   
.. km:hotkey:: LEFTMOUSE -> anim.channels_rename

   Rename Channels

   bpy.ops.anim.channels_rename()
   
   
.. km:hotkey:: LEFTMOUSE -> anim.channel_select_keys

   Select Channel keyframes

   bpy.ops.anim.channel_select_keys(extend=False)
   
   
.. km:hotkey:: Shift-LEFTMOUSE -> anim.channel_select_keys

   Select Channel keyframes

   bpy.ops.anim.channel_select_keys(extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-F -> anim.channels_find

   Find Channels

   bpy.ops.anim.channels_find(query="Query")
   
   
.. km:hotkey:: A -> anim.channels_select_all_toggle

   Select All

   bpy.ops.anim.channels_select_all_toggle(invert=False)
   
   
.. km:hotkey:: Ctrl-I -> anim.channels_select_all_toggle

   Select All

   bpy.ops.anim.channels_select_all_toggle(invert=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Invert      |True    |
   +------------+--------+
   
   
.. km:hotkey:: B -> anim.channels_select_border

   Border Select

   bpy.ops.anim.channels_select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkey:: EVT_TWEAK_L -> anim.channels_select_border

   Border Select

   bpy.ops.anim.channels_select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkey:: X -> anim.channels_delete

   Delete Channels

   bpy.ops.anim.channels_delete()
   
   
.. km:hotkey:: DEL -> anim.channels_delete

   Delete Channels

   bpy.ops.anim.channels_delete()
   
   
.. km:hotkey:: Shift-W -> anim.channels_setting_toggle

   Toggle Channel Setting

   bpy.ops.anim.channels_setting_toggle(mode='TOGGLE', type='PROTECT')
   
   
.. km:hotkey:: Ctrl-Shift-W -> anim.channels_setting_enable

   Enable Channel Setting

   bpy.ops.anim.channels_setting_enable(mode='ENABLE', type='PROTECT')
   
   
.. km:hotkey:: Alt-W -> anim.channels_setting_disable

   Disable Channel Setting

   bpy.ops.anim.channels_setting_disable(mode='DISABLE', type='PROTECT')
   
   
.. km:hotkey:: Tab -> anim.channels_editable_toggle

   Toggle Channel Editability

   bpy.ops.anim.channels_editable_toggle(mode='TOGGLE', type='PROTECT')
   
   
.. km:hotkey:: NUMPAD_PLUS -> anim.channels_expand

   Expand Channels

   bpy.ops.anim.channels_expand(all=True)
   
   
.. km:hotkey:: NUMPAD_MINUS -> anim.channels_collapse

   Collapse Channels

   bpy.ops.anim.channels_collapse(all=True)
   
   
.. km:hotkey:: Ctrl-NUMPAD_PLUS -> anim.channels_expand

   Expand Channels

   bpy.ops.anim.channels_expand(all=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |All         |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-NUMPAD_MINUS -> anim.channels_collapse

   Collapse Channels

   bpy.ops.anim.channels_collapse(all=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |All         |False   |
   +------------+--------+
   
   
.. km:hotkey:: PAGE_UP -> anim.channels_move

   Move Channels

   bpy.ops.anim.channels_move(direction='DOWN')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |UP      |
   +------------+--------+
   
   
.. km:hotkey:: PAGE_DOWN -> anim.channels_move

   Move Channels

   bpy.ops.anim.channels_move(direction='DOWN')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |DOWN    |
   +------------+--------+
   
   
.. km:hotkey:: Shift-PAGE_UP -> anim.channels_move

   Move Channels

   bpy.ops.anim.channels_move(direction='DOWN')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |TOP     |
   +------------+--------+
   
   
.. km:hotkey:: Shift-PAGE_DOWN -> anim.channels_move

   Move Channels

   bpy.ops.anim.channels_move(direction='DOWN')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |BOTTOM  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-G -> anim.channels_group

   Group Channels

   bpy.ops.anim.channels_group(name="New Group")
   
   
.. km:hotkey:: Alt-G -> anim.channels_ungroup

   Ungroup Channels

   bpy.ops.anim.channels_ungroup()
   
   
