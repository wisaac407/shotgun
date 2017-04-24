*******
Console
*******

.. km:module:: console

   


---------------
Quick Reference
---------------

+----------------------------------------------------------------------------------+-----------------------------------------------+
|Hotkey                                                                            |Operator                                       |
+==================================================================================+===============================================+
|:km:hk:`Tab <console->Tab->console.autocomplete>`                                 |:func:`blender:bpy.ops.console.autocomplete`   |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-LEFT_ARROW <console->Ctrl-LEFT_ARROW->console.move>`                 |:func:`blender:bpy.ops.console.move`           |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-RIGHT_ARROW <console->Ctrl-RIGHT_ARROW->console.move>`               |:func:`blender:bpy.ops.console.move`           |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`HOME <console->HOME->console.move>`                                       |:func:`blender:bpy.ops.console.move`           |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`END <console->END->console.move>`                                         |:func:`blender:bpy.ops.console.move`           |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-WHEELUPMOUSE <console->Ctrl-WHEELUPMOUSE->wm.context_cycle_int>`     |:func:`blender:bpy.ops.wm.context_cycle_int`   |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-WHEELDOWNMOUSE <console->Ctrl-WHEELDOWNMOUSE->wm.context_cycle_int>` |:func:`blender:bpy.ops.wm.context_cycle_int`   |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <console->Ctrl-NUMPAD_PLUS->wm.context_cycle_int>`       |:func:`blender:bpy.ops.wm.context_cycle_int`   |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <console->Ctrl-NUMPAD_MINUS->wm.context_cycle_int>`     |:func:`blender:bpy.ops.wm.context_cycle_int`   |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`LEFT_ARROW <console->LEFT_ARROW->console.move>`                           |:func:`blender:bpy.ops.console.move`           |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`RIGHT_ARROW <console->RIGHT_ARROW->console.move>`                         |:func:`blender:bpy.ops.console.move`           |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`UP_ARROW <console->UP_ARROW->console.history_cycle>`                      |:func:`blender:bpy.ops.console.history_cycle`  |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`DOWN_ARROW <console->DOWN_ARROW->console.history_cycle>`                  |:func:`blender:bpy.ops.console.history_cycle`  |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`DEL <console->DEL->console.delete>`                                       |:func:`blender:bpy.ops.console.delete`         |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`BACK_SPACE <console->BACK_SPACE->console.delete>`                         |:func:`blender:bpy.ops.console.delete`         |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-BACK_SPACE <console->Shift-BACK_SPACE->console.delete>`             |:func:`blender:bpy.ops.console.delete`         |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-DEL <console->Ctrl-DEL->console.delete>`                             |:func:`blender:bpy.ops.console.delete`         |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-BACK_SPACE <console->Ctrl-BACK_SPACE->console.delete>`               |:func:`blender:bpy.ops.console.delete`         |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-RET <console->Shift-RET->console.clear_line>`                       |:func:`blender:bpy.ops.console.clear_line`     |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-NUMPAD_ENTER <console->Shift-NUMPAD_ENTER->console.clear_line>`     |:func:`blender:bpy.ops.console.clear_line`     |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`RET <console->RET->console.execute>`                                      |:func:`blender:bpy.ops.console.execute`        |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`NUMPAD_ENTER <console->NUMPAD_ENTER->console.execute>`                    |:func:`blender:bpy.ops.console.execute`        |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-SPACE <console->Ctrl-SPACE->console.autocomplete>`                   |:func:`blender:bpy.ops.console.autocomplete`   |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-Shift-C <console->Ctrl-Shift-C->console.copy_as_script>`             |:func:`blender:bpy.ops.console.copy_as_script` |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-C <console->Ctrl-C->console.copy>`                                   |:func:`blender:bpy.ops.console.copy`           |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-V <console->Ctrl-V->console.paste>`                                  |:func:`blender:bpy.ops.console.paste`          |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`LEFTMOUSE <console->LEFTMOUSE->console.select_set>`                       |:func:`blender:bpy.ops.console.select_set`     |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`LEFTMOUSE <console->LEFTMOUSE->console.select_word>`                      |:func:`blender:bpy.ops.console.select_word`    |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-Tab <console->Ctrl-Tab->console.insert>`                             |:func:`blender:bpy.ops.console.insert`         |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Tab <console->Tab->console.indent>`                                       |:func:`blender:bpy.ops.console.indent`         |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-Tab <console->Shift-Tab->console.unindent>`                         |:func:`blender:bpy.ops.console.unindent`       |
+----------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Any-TEXTINPUT <console->Any-TEXTINPUT->console.insert>`                   |:func:`blender:bpy.ops.console.insert`         |
+----------------------------------------------------------------------------------+-----------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Tab -> console.autocomplete : KEYBOARD -> PRESS

   Console Autocomplete

   bpy.ops.console.autocomplete()
   
   
.. km:hotkeyd:: Ctrl-LEFT_ARROW -> console.move : KEYBOARD -> PRESS

   Move Cursor

   bpy.ops.console.move(type='LINE_BEGIN')
   
   
   +------------+--------------+
   |Properties: |Values:       |
   +============+==============+
   |Type        |PREVIOUS_WORD |
   +------------+--------------+
   
   
.. km:hotkeyd:: Ctrl-RIGHT_ARROW -> console.move : KEYBOARD -> PRESS

   Move Cursor

   bpy.ops.console.move(type='LINE_BEGIN')
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Type        |NEXT_WORD |
   +------------+----------+
   
   
.. km:hotkeyd:: HOME -> console.move : KEYBOARD -> PRESS

   Move Cursor

   bpy.ops.console.move(type='LINE_BEGIN')
   
   
   +------------+-----------+
   |Properties: |Values:    |
   +============+===========+
   |Type        |LINE_BEGIN |
   +------------+-----------+
   
   
.. km:hotkeyd:: END -> console.move : KEYBOARD -> PRESS

   Move Cursor

   bpy.ops.console.move(type='LINE_BEGIN')
   
   
   +------------+---------+
   |Properties: |Values:  |
   +============+=========+
   |Type        |LINE_END |
   +------------+---------+
   
   
.. km:hotkeyd:: Ctrl-WHEELUPMOUSE -> wm.context_cycle_int : MOUSE -> PRESS

   Context Int Cycle

   bpy.ops.wm.context_cycle_int(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+---------------------+
   |Properties:        |Values:              |
   +===================+=====================+
   |Context Attributes |space_data.font_size |
   +-------------------+---------------------+
   |Reverse            |False                |
   +-------------------+---------------------+
   
   
.. km:hotkeyd:: Ctrl-WHEELDOWNMOUSE -> wm.context_cycle_int : MOUSE -> PRESS

   Context Int Cycle

   bpy.ops.wm.context_cycle_int(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+---------------------+
   |Properties:        |Values:              |
   +===================+=====================+
   |Context Attributes |space_data.font_size |
   +-------------------+---------------------+
   |Reverse            |True                 |
   +-------------------+---------------------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> wm.context_cycle_int : KEYBOARD -> PRESS

   Context Int Cycle

   bpy.ops.wm.context_cycle_int(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+---------------------+
   |Properties:        |Values:              |
   +===================+=====================+
   |Context Attributes |space_data.font_size |
   +-------------------+---------------------+
   |Reverse            |False                |
   +-------------------+---------------------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> wm.context_cycle_int : KEYBOARD -> PRESS

   Context Int Cycle

   bpy.ops.wm.context_cycle_int(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+---------------------+
   |Properties:        |Values:              |
   +===================+=====================+
   |Context Attributes |space_data.font_size |
   +-------------------+---------------------+
   |Reverse            |True                 |
   +-------------------+---------------------+
   
   
.. km:hotkeyd:: LEFT_ARROW -> console.move : KEYBOARD -> PRESS

   Move Cursor

   bpy.ops.console.move(type='LINE_BEGIN')
   
   
   +------------+-------------------+
   |Properties: |Values:            |
   +============+===================+
   |Type        |PREVIOUS_CHARACTER |
   +------------+-------------------+
   
   
.. km:hotkeyd:: RIGHT_ARROW -> console.move : KEYBOARD -> PRESS

   Move Cursor

   bpy.ops.console.move(type='LINE_BEGIN')
   
   
   +------------+---------------+
   |Properties: |Values:        |
   +============+===============+
   |Type        |NEXT_CHARACTER |
   +------------+---------------+
   
   
.. km:hotkeyd:: UP_ARROW -> console.history_cycle : KEYBOARD -> PRESS

   History Cycle

   bpy.ops.console.history_cycle(reverse=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Reverse     |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: DOWN_ARROW -> console.history_cycle : KEYBOARD -> PRESS

   History Cycle

   bpy.ops.console.history_cycle(reverse=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Reverse     |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: DEL -> console.delete : KEYBOARD -> PRESS

   Delete

   bpy.ops.console.delete(type='NEXT_CHARACTER')
   
   
   +------------+---------------+
   |Properties: |Values:        |
   +============+===============+
   |Type        |NEXT_CHARACTER |
   +------------+---------------+
   
   
.. km:hotkeyd:: BACK_SPACE -> console.delete : KEYBOARD -> PRESS

   Delete

   bpy.ops.console.delete(type='NEXT_CHARACTER')
   
   
   +------------+-------------------+
   |Properties: |Values:            |
   +============+===================+
   |Type        |PREVIOUS_CHARACTER |
   +------------+-------------------+
   
   
.. km:hotkeyd:: Shift-BACK_SPACE -> console.delete : KEYBOARD -> PRESS

   Delete

   bpy.ops.console.delete(type='NEXT_CHARACTER')
   
   
   +------------+-------------------+
   |Properties: |Values:            |
   +============+===================+
   |Type        |PREVIOUS_CHARACTER |
   +------------+-------------------+
   
   
.. km:hotkeyd:: Ctrl-DEL -> console.delete : KEYBOARD -> PRESS

   Delete

   bpy.ops.console.delete(type='NEXT_CHARACTER')
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Type        |NEXT_WORD |
   +------------+----------+
   
   
.. km:hotkeyd:: Ctrl-BACK_SPACE -> console.delete : KEYBOARD -> PRESS

   Delete

   bpy.ops.console.delete(type='NEXT_CHARACTER')
   
   
   +------------+--------------+
   |Properties: |Values:       |
   +============+==============+
   |Type        |PREVIOUS_WORD |
   +------------+--------------+
   
   
.. km:hotkeyd:: Shift-RET -> console.clear_line : KEYBOARD -> PRESS

   Clear Line

   bpy.ops.console.clear_line()
   
   
.. km:hotkeyd:: Shift-NUMPAD_ENTER -> console.clear_line : KEYBOARD -> PRESS

   Clear Line

   bpy.ops.console.clear_line()
   
   
.. km:hotkeyd:: RET -> console.execute : KEYBOARD -> PRESS

   Console Execute

   bpy.ops.console.execute(interactive=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |interactive |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_ENTER -> console.execute : KEYBOARD -> PRESS

   Console Execute

   bpy.ops.console.execute(interactive=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |interactive |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-SPACE -> console.autocomplete : KEYBOARD -> PRESS

   Console Autocomplete

   bpy.ops.console.autocomplete()
   
   
.. km:hotkeyd:: Ctrl-Shift-C -> console.copy_as_script : KEYBOARD -> PRESS

   Copy to Clipboard (as script)

   bpy.ops.console.copy_as_script()
   
   
.. km:hotkeyd:: Ctrl-C -> console.copy : KEYBOARD -> PRESS

   Copy to Clipboard

   bpy.ops.console.copy()
   
   
.. km:hotkeyd:: Ctrl-V -> console.paste : KEYBOARD -> PRESS

   Paste from Clipboard

   bpy.ops.console.paste()
   
   
.. km:hotkeyd:: LEFTMOUSE -> console.select_set : MOUSE -> PRESS

   Set Selection

   bpy.ops.console.select_set()
   
   
.. km:hotkeyd:: LEFTMOUSE -> console.select_word : MOUSE -> DOUBLE_CLICK

   Select Word

   bpy.ops.console.select_word()
   
   
.. km:hotkeyd:: Ctrl-Tab -> console.insert : KEYBOARD -> PRESS

   Insert

   bpy.ops.console.insert(text="")
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Text        |	       |
   +------------+--------+
   
   
.. km:hotkeyd:: Tab -> console.indent : KEYBOARD -> PRESS

   Indent

   bpy.ops.console.indent()
   
   
.. km:hotkeyd:: Shift-Tab -> console.unindent : KEYBOARD -> PRESS

   Unindent

   bpy.ops.console.unindent()
   
   
.. km:hotkeyd:: Any-TEXTINPUT -> console.insert : TEXTINPUT -> ANY

   Insert

   bpy.ops.console.insert(text="")
   
   
