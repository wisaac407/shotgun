*****************
File Browser Main
*****************

.. km:module:: filebrowsermain

   


---------------
Quick Reference
---------------

+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|Hotkey                                                                                      |Operator                                       |
+============================================================================================+===============================================+
|:km:hk:`Alt-LEFTMOUSE <filebrowsermain->Alt-LEFTMOUSE->file.select>`                        |:func:`blender:bpy.ops.file.select`            |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-A <filebrowsermain->Ctrl-A->file.select_all_toggle>`                           |:func:`blender:bpy.ops.file.select_all_toggle` |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`LEFTMOUSE <filebrowsermain->LEFTMOUSE->file.execute>`                               |:func:`blender:bpy.ops.file.execute`           |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`NUMPAD_PERIOD <filebrowsermain->NUMPAD_PERIOD->file.refresh>`                       |:func:`blender:bpy.ops.file.refresh`           |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`LEFTMOUSE <filebrowsermain->LEFTMOUSE->file.select>`                                |:func:`blender:bpy.ops.file.select`            |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-LEFTMOUSE <filebrowsermain->Shift-LEFTMOUSE->file.select>`                    |:func:`blender:bpy.ops.file.select`            |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-Shift-LEFTMOUSE <filebrowsermain->Ctrl-Shift-LEFTMOUSE->file.select>`          |:func:`blender:bpy.ops.file.select`            |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`RIGHTMOUSE <filebrowsermain->RIGHTMOUSE->file.select>`                              |:func:`blender:bpy.ops.file.select`            |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-RIGHTMOUSE <filebrowsermain->Shift-RIGHTMOUSE->file.select>`                  |:func:`blender:bpy.ops.file.select`            |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Alt-RIGHTMOUSE <filebrowsermain->Alt-RIGHTMOUSE->file.select>`                      |:func:`blender:bpy.ops.file.select`            |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`UP_ARROW <filebrowsermain->UP_ARROW->file.select_walk>`                             |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-UP_ARROW <filebrowsermain->Shift-UP_ARROW->file.select_walk>`                 |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-Shift-UP_ARROW <filebrowsermain->Ctrl-Shift-UP_ARROW->file.select_walk>`       |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`DOWN_ARROW <filebrowsermain->DOWN_ARROW->file.select_walk>`                         |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-DOWN_ARROW <filebrowsermain->Shift-DOWN_ARROW->file.select_walk>`             |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-Shift-DOWN_ARROW <filebrowsermain->Ctrl-Shift-DOWN_ARROW->file.select_walk>`   |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`LEFT_ARROW <filebrowsermain->LEFT_ARROW->file.select_walk>`                         |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-LEFT_ARROW <filebrowsermain->Shift-LEFT_ARROW->file.select_walk>`             |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-Shift-LEFT_ARROW <filebrowsermain->Ctrl-Shift-LEFT_ARROW->file.select_walk>`   |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`RIGHT_ARROW <filebrowsermain->RIGHT_ARROW->file.select_walk>`                       |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-RIGHT_ARROW <filebrowsermain->Shift-RIGHT_ARROW->file.select_walk>`           |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-Shift-RIGHT_ARROW <filebrowsermain->Ctrl-Shift-RIGHT_ARROW->file.select_walk>` |:func:`blender:bpy.ops.file.select_walk`       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`BUTTON4MOUSE <filebrowsermain->BUTTON4MOUSE->file.previous>`                        |:func:`blender:bpy.ops.file.previous`          |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`BUTTON5MOUSE <filebrowsermain->BUTTON5MOUSE->file.next>`                            |:func:`blender:bpy.ops.file.next`              |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`A <filebrowsermain->A->file.select_all_toggle>`                                     |:func:`blender:bpy.ops.file.select_all_toggle` |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`B <filebrowsermain->B->file.select_border>`                                         |:func:`blender:bpy.ops.file.select_border`     |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`EVT_TWEAK_L <filebrowsermain->EVT_TWEAK_L->file.select_border>`                     |:func:`blender:bpy.ops.file.select_border`     |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-LEFTMOUSE <filebrowsermain->Ctrl-LEFTMOUSE->file.rename>`                      |:func:`blender:bpy.ops.file.rename`            |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Any-MOUSEMOVE <filebrowsermain->Any-MOUSEMOVE->file.highlight>`                     |:func:`blender:bpy.ops.file.highlight`         |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`NUMPAD_PLUS <filebrowsermain->NUMPAD_PLUS->file.filenum>`                           |:func:`blender:bpy.ops.file.filenum`           |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-NUMPAD_PLUS <filebrowsermain->Shift-NUMPAD_PLUS->file.filenum>`               |:func:`blender:bpy.ops.file.filenum`           |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <filebrowsermain->Ctrl-NUMPAD_PLUS->file.filenum>`                 |:func:`blender:bpy.ops.file.filenum`           |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`NUMPAD_MINUS <filebrowsermain->NUMPAD_MINUS->file.filenum>`                         |:func:`blender:bpy.ops.file.filenum`           |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-NUMPAD_MINUS <filebrowsermain->Shift-NUMPAD_MINUS->file.filenum>`             |:func:`blender:bpy.ops.file.filenum`           |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <filebrowsermain->Ctrl-NUMPAD_MINUS->file.filenum>`               |:func:`blender:bpy.ops.file.filenum`           |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Alt-LEFTMOUSE -> file.select

   Activate/Select File

   bpy.ops.file.select(extend=False, fill=False, open=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   |Fill        |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-A -> file.select_all_toggle

   (De)select All Files

   bpy.ops.file.select_all_toggle()
   
   
.. km:hotkeyd:: LEFTMOUSE -> file.execute

   Execute File Window

   bpy.ops.file.execute(need_active=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Need Active |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_PERIOD -> file.refresh

   Refresh Filelist

   bpy.ops.file.refresh()
   
   
.. km:hotkeyd:: LEFTMOUSE -> file.select

   Activate/Select File

   bpy.ops.file.select(extend=False, fill=False, open=True)
   
   
.. km:hotkeyd:: Shift-LEFTMOUSE -> file.select

   Activate/Select File

   bpy.ops.file.select(extend=False, fill=False, open=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-LEFTMOUSE -> file.select

   Activate/Select File

   bpy.ops.file.select(extend=False, fill=False, open=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   |Fill        |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: RIGHTMOUSE -> file.select

   Activate/Select File

   bpy.ops.file.select(extend=False, fill=False, open=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Open        |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-RIGHTMOUSE -> file.select

   Activate/Select File

   bpy.ops.file.select(extend=False, fill=False, open=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   |Open        |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-RIGHTMOUSE -> file.select

   Activate/Select File

   bpy.ops.file.select(extend=False, fill=False, open=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   |Fill        |True    |
   +------------+--------+
   |Open        |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: UP_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |UP      |
   +---------------+--------+
   
   
.. km:hotkeyd:: Shift-UP_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |UP      |
   +---------------+--------+
   |Extend         |True    |
   +---------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-UP_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |UP      |
   +---------------+--------+
   |Extend         |True    |
   +---------------+--------+
   |Fill           |True    |
   +---------------+--------+
   
   
.. km:hotkeyd:: DOWN_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |DOWN    |
   +---------------+--------+
   
   
.. km:hotkeyd:: Shift-DOWN_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |DOWN    |
   +---------------+--------+
   |Extend         |True    |
   +---------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-DOWN_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |DOWN    |
   +---------------+--------+
   |Extend         |True    |
   +---------------+--------+
   |Fill           |True    |
   +---------------+--------+
   
   
.. km:hotkeyd:: LEFT_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |LEFT    |
   +---------------+--------+
   
   
.. km:hotkeyd:: Shift-LEFT_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |LEFT    |
   +---------------+--------+
   |Extend         |True    |
   +---------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-LEFT_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |LEFT    |
   +---------------+--------+
   |Extend         |True    |
   +---------------+--------+
   |Fill           |True    |
   +---------------+--------+
   
   
.. km:hotkeyd:: RIGHT_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |RIGHT   |
   +---------------+--------+
   
   
.. km:hotkeyd:: Shift-RIGHT_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |RIGHT   |
   +---------------+--------+
   |Extend         |True    |
   +---------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-RIGHT_ARROW -> file.select_walk

   Walk Select/Deselect File

   bpy.ops.file.select_walk(direction='UP', extend=False, fill=False)
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Walk Direction |RIGHT   |
   +---------------+--------+
   |Extend         |True    |
   +---------------+--------+
   |Fill           |True    |
   +---------------+--------+
   
   
.. km:hotkeyd:: BUTTON4MOUSE -> file.previous

   Previous Folder

   bpy.ops.file.previous()
   
   
.. km:hotkeyd:: BUTTON5MOUSE -> file.next

   Next Folder

   bpy.ops.file.next()
   
   
.. km:hotkeyd:: A -> file.select_all_toggle

   (De)select All Files

   bpy.ops.file.select_all_toggle()
   
   
.. km:hotkeyd:: B -> file.select_border

   Activate/Select File

   bpy.ops.file.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkeyd:: EVT_TWEAK_L -> file.select_border

   Activate/Select File

   bpy.ops.file.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkeyd:: Ctrl-LEFTMOUSE -> file.rename

   Rename File or Directory

   bpy.ops.file.rename()
   
   
.. km:hotkeyd:: Any-MOUSEMOVE -> file.highlight

   Highlight File

   bpy.ops.file.highlight()
   
   
.. km:hotkeyd:: NUMPAD_PLUS -> file.filenum

   Increment Number in Filename

   bpy.ops.file.filenum(increment=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Increment   |1       |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-NUMPAD_PLUS -> file.filenum

   Increment Number in Filename

   bpy.ops.file.filenum(increment=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Increment   |10      |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> file.filenum

   Increment Number in Filename

   bpy.ops.file.filenum(increment=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Increment   |100     |
   +------------+--------+
   
   
.. km:hotkeyd:: NUMPAD_MINUS -> file.filenum

   Increment Number in Filename

   bpy.ops.file.filenum(increment=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Increment   |-1      |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-NUMPAD_MINUS -> file.filenum

   Increment Number in Filename

   bpy.ops.file.filenum(increment=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Increment   |-10     |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> file.filenum

   Increment Number in Filename

   bpy.ops.file.filenum(increment=1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Increment   |-100    |
   +------------+--------+
   
   
