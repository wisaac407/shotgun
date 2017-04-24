*********
Face Mask
*********

.. km:module:: facemask

   


---------------
Quick Reference
---------------

+--------------------------------------------------------------------+------------------------------------------------------+
|Hotkey                                                              |Operator                                              |
+====================================================================+======================================================+
|:km:hk:`Ctrl-A <facemask->Ctrl-A->paint.face_select_all>`           |:func:`blender:bpy.ops.paint.face_select_all`         |
+--------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`A <facemask->A->paint.face_select_all>`                     |:func:`blender:bpy.ops.paint.face_select_all`         |
+--------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-I <facemask->Ctrl-I->paint.face_select_all>`           |:func:`blender:bpy.ops.paint.face_select_all`         |
+--------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`H <facemask->H->paint.face_select_hide>`                    |:func:`blender:bpy.ops.paint.face_select_hide`        |
+--------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-H <facemask->Shift-H->paint.face_select_hide>`        |:func:`blender:bpy.ops.paint.face_select_hide`        |
+--------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Alt-H <facemask->Alt-H->paint.face_select_reveal>`          |:func:`blender:bpy.ops.paint.face_select_reveal`      |
+--------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Ctrl-L <facemask->Ctrl-L->paint.face_select_linked>`        |:func:`blender:bpy.ops.paint.face_select_linked`      |
+--------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`L <facemask->L->paint.face_select_linked_pick>`             |:func:`blender:bpy.ops.paint.face_select_linked_pick` |
+--------------------------------------------------------------------+------------------------------------------------------+
|:km:hk:`Shift-L <facemask->Shift-L->paint.face_select_linked_pick>` |:func:`blender:bpy.ops.paint.face_select_linked_pick` |
+--------------------------------------------------------------------+------------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> paint.face_select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.paint.face_select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: A -> paint.face_select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.paint.face_select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> paint.face_select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.paint.face_select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: H -> paint.face_select_hide : KEYBOARD -> PRESS

   Face Select Hide

   bpy.ops.paint.face_select_hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> paint.face_select_hide : KEYBOARD -> PRESS

   Face Select Hide

   bpy.ops.paint.face_select_hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-H -> paint.face_select_reveal : KEYBOARD -> PRESS

   Face Select Reveal

   bpy.ops.paint.face_select_reveal(unselected=False)
   
   
.. km:hotkeyd:: Ctrl-L -> paint.face_select_linked : KEYBOARD -> PRESS

   Select Linked

   bpy.ops.paint.face_select_linked()
   
   
.. km:hotkeyd:: L -> paint.face_select_linked_pick : KEYBOARD -> PRESS

   Select Linked Pick

   bpy.ops.paint.face_select_linked_pick(deselect=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-L -> paint.face_select_linked_pick : KEYBOARD -> PRESS

   Select Linked Pick

   bpy.ops.paint.face_select_linked_pick(deselect=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
