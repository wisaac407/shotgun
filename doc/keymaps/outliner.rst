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
|:km:hk:`PAGE_DOWN <outliner->PAGE_DOWN->outliner.scroll_page>`                         |:func:`blender:bpy.ops.outliner.scroll_page`               |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+
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

.. km:hotkey:: PAGE_DOWN -> outliner.scroll_page

   Scroll Page

   bpy.ops.outliner.scroll_page(up=False)
   
   
.. km:hotkey:: Ctrl-A -> outliner.selected_toggle

   Toggle Selected

   bpy.ops.outliner.selected_toggle()
   
   
.. km:hotkey:: LEFTMOUSE -> outliner.item_rename

   Rename Item

   bpy.ops.outliner.item_rename()
   
   
.. km:hotkey:: LEFTMOUSE -> outliner.item_activate

   Activate Item

   bpy.ops.outliner.item_activate(extend=True, recursive=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Recursive   |False   |
   +------------+--------+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Shift-LEFTMOUSE -> outliner.item_activate

   Activate Item

   bpy.ops.outliner.item_activate(extend=True, recursive=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Recursive   |False   |
   +------------+--------+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-LEFTMOUSE -> outliner.item_activate

   Activate Item

   bpy.ops.outliner.item_activate(extend=True, recursive=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Recursive   |True    |
   +------------+--------+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-LEFTMOUSE -> outliner.item_activate

   Activate Item

   bpy.ops.outliner.item_activate(extend=True, recursive=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Recursive   |True    |
   +------------+--------+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: B -> outliner.select_border

   Border Select

   bpy.ops.outliner.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0)
   
   
.. km:hotkey:: RET -> outliner.item_openclose

   Open/Close Item

   bpy.ops.outliner.item_openclose(all=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |All         |False   |
   +------------+--------+
   
   
.. km:hotkey:: Shift-RET -> outliner.item_openclose

   Open/Close Item

   bpy.ops.outliner.item_openclose(all=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |All         |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-LEFTMOUSE -> outliner.item_rename

   Rename Item

   bpy.ops.outliner.item_rename()
   
   
.. km:hotkey:: RIGHTMOUSE -> outliner.operation

   Execute Operation

   bpy.ops.outliner.operation()
   
   
.. km:hotkey:: HOME -> outliner.show_hierarchy

   Show Hierarchy

   bpy.ops.outliner.show_hierarchy()
   
   
.. km:hotkey:: . -> outliner.show_active

   Show Active

   bpy.ops.outliner.show_active()
   
   
.. km:hotkey:: NUMPAD_PERIOD -> outliner.show_active

   Show Active

   bpy.ops.outliner.show_active()
   
   
.. km:hotkey:: PAGE_DOWN -> outliner.scroll_page

   Scroll Page

   bpy.ops.outliner.scroll_page(up=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Up          |False   |
   +------------+--------+
   
   
.. km:hotkey:: PAGE_UP -> outliner.scroll_page

   Scroll Page

   bpy.ops.outliner.scroll_page(up=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Up          |True    |
   +------------+--------+
   
   
.. km:hotkey:: NUMPAD_PLUS -> outliner.show_one_level

   Show/Hide One Level

   bpy.ops.outliner.show_one_level(open=True)
   
   
.. km:hotkey:: NUMPAD_MINUS -> outliner.show_one_level

   Show/Hide One Level

   bpy.ops.outliner.show_one_level(open=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Open        |False   |
   +------------+--------+
   
   
.. km:hotkey:: A -> outliner.selected_toggle

   Toggle Selected

   bpy.ops.outliner.selected_toggle()
   
   
.. km:hotkey:: Shift-A -> outliner.expanded_toggle

   Expand/Collapse All

   bpy.ops.outliner.expanded_toggle()
   
   
.. km:hotkey:: R -> outliner.renderability_toggle

   Toggle Renderability

   bpy.ops.outliner.renderability_toggle()
   
   
.. km:hotkey:: S -> outliner.selectability_toggle

   Toggle Selectability

   bpy.ops.outliner.selectability_toggle()
   
   
.. km:hotkey:: V -> outliner.visibility_toggle

   Toggle Visibility

   bpy.ops.outliner.visibility_toggle()
   
   
.. km:hotkey:: K -> outliner.keyingset_add_selected

   Keying Set Add Selected

   bpy.ops.outliner.keyingset_add_selected()
   
   
.. km:hotkey:: Alt-K -> outliner.keyingset_remove_selected

   Keying Set Remove Selected

   bpy.ops.outliner.keyingset_remove_selected()
   
   
.. km:hotkey:: I -> anim.keyframe_insert

   Insert Keyframe

   bpy.ops.anim.keyframe_insert(type='DEFAULT', confirm_success=True)
   
   
.. km:hotkey:: Alt-I -> anim.keyframe_delete

   Delete Keying-Set Keyframe

   bpy.ops.anim.keyframe_delete(type='DEFAULT', confirm_success=True)
   
   
.. km:hotkey:: D -> outliner.drivers_add_selected

   Add Drivers for Selected

   bpy.ops.outliner.drivers_add_selected()
   
   
.. km:hotkey:: Alt-D -> outliner.drivers_delete_selected

   Delete Drivers for Selected

   bpy.ops.outliner.drivers_delete_selected()
   
   
