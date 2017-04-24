********
Outliner
********

.. km:module:: outliner

   


---------------
Quick Reference
---------------

+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|Hotkey                                                                                 |Operator                                                   |
+=======================================================================================+===========================================================+
|:km:hk:`Ctrl-A <outliner->Ctrl-A->outliner.selected_toggle>`                           |:func:`blender:bpy.ops.outliner.selected_toggle`           |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`LEFTMOUSE <outliner->LEFTMOUSE->outliner.item_rename>`                         |:func:`blender:bpy.ops.outliner.item_rename`               |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`LEFTMOUSE <outliner->LEFTMOUSE->outliner.item_activate>`                       |:func:`blender:bpy.ops.outliner.item_activate`             |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-LEFTMOUSE <outliner->Shift-LEFTMOUSE->outliner.item_activate>`           |:func:`blender:bpy.ops.outliner.item_activate`             |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-LEFTMOUSE <outliner->Ctrl-LEFTMOUSE->outliner.item_activate>`             |:func:`blender:bpy.ops.outliner.item_activate`             |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-Shift-LEFTMOUSE <outliner->Ctrl-Shift-LEFTMOUSE->outliner.item_activate>` |:func:`blender:bpy.ops.outliner.item_activate`             |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`B <outliner->B->outliner.select_border>`                                       |:func:`blender:bpy.ops.outliner.select_border`             |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`RET <outliner->RET->outliner.item_openclose>`                                  |:func:`blender:bpy.ops.outliner.item_openclose`            |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-RET <outliner->Shift-RET->outliner.item_openclose>`                      |:func:`blender:bpy.ops.outliner.item_openclose`            |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Ctrl-LEFTMOUSE <outliner->Ctrl-LEFTMOUSE->outliner.item_rename>`               |:func:`blender:bpy.ops.outliner.item_rename`               |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`RIGHTMOUSE <outliner->RIGHTMOUSE->outliner.operation>`                         |:func:`blender:bpy.ops.outliner.operation`                 |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`HOME <outliner->HOME->outliner.show_hierarchy>`                                |:func:`blender:bpy.ops.outliner.show_hierarchy`            |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`. <outliner->.->outliner.show_active>`                                         |:func:`blender:bpy.ops.outliner.show_active`               |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`NUMPAD_PERIOD <outliner->NUMPAD_PERIOD->outliner.show_active>`                 |:func:`blender:bpy.ops.outliner.show_active`               |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`PAGE_DOWN <outliner->PAGE_DOWN->outliner.scroll_page>`                         |:func:`blender:bpy.ops.outliner.scroll_page`               |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`PAGE_UP <outliner->PAGE_UP->outliner.scroll_page>`                             |:func:`blender:bpy.ops.outliner.scroll_page`               |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`NUMPAD_PLUS <outliner->NUMPAD_PLUS->outliner.show_one_level>`                  |:func:`blender:bpy.ops.outliner.show_one_level`            |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`NUMPAD_MINUS <outliner->NUMPAD_MINUS->outliner.show_one_level>`                |:func:`blender:bpy.ops.outliner.show_one_level`            |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`A <outliner->A->outliner.selected_toggle>`                                     |:func:`blender:bpy.ops.outliner.selected_toggle`           |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Shift-A <outliner->Shift-A->outliner.expanded_toggle>`                         |:func:`blender:bpy.ops.outliner.expanded_toggle`           |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`R <outliner->R->outliner.renderability_toggle>`                                |:func:`blender:bpy.ops.outliner.renderability_toggle`      |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`S <outliner->S->outliner.selectability_toggle>`                                |:func:`blender:bpy.ops.outliner.selectability_toggle`      |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`V <outliner->V->outliner.visibility_toggle>`                                   |:func:`blender:bpy.ops.outliner.visibility_toggle`         |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`K <outliner->K->outliner.keyingset_add_selected>`                              |:func:`blender:bpy.ops.outliner.keyingset_add_selected`    |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-K <outliner->Alt-K->outliner.keyingset_remove_selected>`                   |:func:`blender:bpy.ops.outliner.keyingset_remove_selected` |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`I <outliner->I->anim.keyframe_insert>`                                         |:func:`blender:bpy.ops.anim.keyframe_insert`               |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-I <outliner->Alt-I->anim.keyframe_delete>`                                 |:func:`blender:bpy.ops.anim.keyframe_delete`               |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`D <outliner->D->outliner.drivers_add_selected>`                                |:func:`blender:bpy.ops.outliner.drivers_add_selected`      |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
|:km:hk:`Alt-D <outliner->Alt-D->outliner.drivers_delete_selected>`                     |:func:`blender:bpy.ops.outliner.drivers_delete_selected`   |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> outliner.selected_toggle : KEYBOARD -> PRESS

   Toggle Selected

   bpy.ops.outliner.selected_toggle()
   
   
.. km:hotkeyd:: LEFTMOUSE -> outliner.item_rename : MOUSE -> DOUBLE_CLICK

   Rename Item

   bpy.ops.outliner.item_rename()
   
   
.. km:hotkeyd:: LEFTMOUSE -> outliner.item_activate : MOUSE -> CLICK

   Activate Item

   bpy.ops.outliner.item_activate(extend=True, recursive=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Recursive   |False   |
   +------------+--------+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-LEFTMOUSE -> outliner.item_activate : MOUSE -> CLICK

   Activate Item

   bpy.ops.outliner.item_activate(extend=True, recursive=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Recursive   |False   |
   +------------+--------+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-LEFTMOUSE -> outliner.item_activate : MOUSE -> CLICK

   Activate Item

   bpy.ops.outliner.item_activate(extend=True, recursive=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Recursive   |True    |
   +------------+--------+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-LEFTMOUSE -> outliner.item_activate : MOUSE -> CLICK

   Activate Item

   bpy.ops.outliner.item_activate(extend=True, recursive=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Recursive   |True    |
   +------------+--------+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: B -> outliner.select_border : KEYBOARD -> PRESS

   Border Select

   bpy.ops.outliner.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0)
   
   
.. km:hotkeyd:: RET -> outliner.item_openclose : KEYBOARD -> PRESS

   Open/Close Item

   bpy.ops.outliner.item_openclose(all=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |All         |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-RET -> outliner.item_openclose : KEYBOARD -> PRESS

   Open/Close Item

   bpy.ops.outliner.item_openclose(all=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |All         |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-LEFTMOUSE -> outliner.item_rename : MOUSE -> PRESS

   Rename Item

   bpy.ops.outliner.item_rename()
   
   
.. km:hotkeyd:: RIGHTMOUSE -> outliner.operation : MOUSE -> PRESS

   Execute Operation

   bpy.ops.outliner.operation()
   
   
.. km:hotkeyd:: HOME -> outliner.show_hierarchy : KEYBOARD -> PRESS

   Show Hierarchy

   bpy.ops.outliner.show_hierarchy()
   
   
.. km:hotkeyd:: . -> outliner.show_active : KEYBOARD -> PRESS

   Show Active

   bpy.ops.outliner.show_active()
   
   
.. km:hotkeyd:: NUMPAD_PERIOD -> outliner.show_active : KEYBOARD -> PRESS

   Show Active

   bpy.ops.outliner.show_active()
   
   
.. km:hotkeyd:: PAGE_DOWN -> outliner.scroll_page : KEYBOARD -> PRESS

   Scroll Page

   bpy.ops.outliner.scroll_page(up=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Up          |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: PAGE_UP -> outliner.scroll_page : KEYBOARD -> PRESS

   Scroll Page

   bpy.ops.outliner.scroll_page(up=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Up          |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_PLUS -> outliner.show_one_level : KEYBOARD -> PRESS

   Show/Hide One Level

   bpy.ops.outliner.show_one_level(open=True)
   
   
.. km:hotkeyd:: NUMPAD_MINUS -> outliner.show_one_level : KEYBOARD -> PRESS

   Show/Hide One Level

   bpy.ops.outliner.show_one_level(open=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Open        |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: A -> outliner.selected_toggle : KEYBOARD -> PRESS

   Toggle Selected

   bpy.ops.outliner.selected_toggle()
   
   
.. km:hotkeyd:: Shift-A -> outliner.expanded_toggle : KEYBOARD -> PRESS

   Expand/Collapse All

   bpy.ops.outliner.expanded_toggle()
   
   
.. km:hotkeyd:: R -> outliner.renderability_toggle : KEYBOARD -> PRESS

   Toggle Renderability

   bpy.ops.outliner.renderability_toggle()
   
   
.. km:hotkeyd:: S -> outliner.selectability_toggle : KEYBOARD -> PRESS

   Toggle Selectability

   bpy.ops.outliner.selectability_toggle()
   
   
.. km:hotkeyd:: V -> outliner.visibility_toggle : KEYBOARD -> PRESS

   Toggle Visibility

   bpy.ops.outliner.visibility_toggle()
   
   
.. km:hotkeyd:: K -> outliner.keyingset_add_selected : KEYBOARD -> PRESS

   Keying Set Add Selected

   bpy.ops.outliner.keyingset_add_selected()
   
   
.. km:hotkeyd:: Alt-K -> outliner.keyingset_remove_selected : KEYBOARD -> PRESS

   Keying Set Remove Selected

   bpy.ops.outliner.keyingset_remove_selected()
   
   
.. km:hotkeyd:: I -> anim.keyframe_insert : KEYBOARD -> PRESS

   Insert Keyframe

   bpy.ops.anim.keyframe_insert(type='DEFAULT', confirm_success=True)
   
   
.. km:hotkeyd:: Alt-I -> anim.keyframe_delete : KEYBOARD -> PRESS

   Delete Keying-Set Keyframe

   bpy.ops.anim.keyframe_delete(type='DEFAULT', confirm_success=True)
   
   
.. km:hotkeyd:: D -> outliner.drivers_add_selected : KEYBOARD -> PRESS

   Add Drivers for Selected

   bpy.ops.outliner.drivers_add_selected()
   
   
.. km:hotkeyd:: Alt-D -> outliner.drivers_delete_selected : KEYBOARD -> PRESS

   Delete Drivers for Selected

   bpy.ops.outliner.drivers_delete_selected()
   
   
