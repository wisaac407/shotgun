*****************************
Weight Paint Vertex Selection
*****************************

.. km:module:: weightpaintvertexselection

   


---------------
Quick Reference
---------------

+----------------------------------------------------------------------------------------------------------+----------------------------------------------+
|Hotkey                                                                                                    |Operator                                      |
+==========================================================================================================+==============================================+
|:km:hk:`Ctrl-A <weightpaintvertexselection->Ctrl-A->paint.vert_select_all>`                               |:func:`blender:bpy.ops.paint.vert_select_all` |
+----------------------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-EVT_TWEAK_S <weightpaintvertexselection->Ctrl-EVT_TWEAK_S->view3d.select_lasso>`             |:func:`blender:bpy.ops.view3d.select_lasso`   |
+----------------------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-Shift-EVT_TWEAK_S <weightpaintvertexselection->Ctrl-Shift-EVT_TWEAK_S->view3d.select_lasso>` |:func:`blender:bpy.ops.view3d.select_lasso`   |
+----------------------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`A <weightpaintvertexselection->A->paint.vert_select_all>`                                         |:func:`blender:bpy.ops.paint.vert_select_all` |
+----------------------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-I <weightpaintvertexselection->Ctrl-I->paint.vert_select_all>`                               |:func:`blender:bpy.ops.paint.vert_select_all` |
+----------------------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`B <weightpaintvertexselection->B->view3d.select_border>`                                          |:func:`blender:bpy.ops.view3d.select_border`  |
+----------------------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-EVT_TWEAK_A <weightpaintvertexselection->Ctrl-EVT_TWEAK_A->view3d.select_lasso>`             |:func:`blender:bpy.ops.view3d.select_lasso`   |
+----------------------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`Ctrl-Shift-EVT_TWEAK_A <weightpaintvertexselection->Ctrl-Shift-EVT_TWEAK_A->view3d.select_lasso>` |:func:`blender:bpy.ops.view3d.select_lasso`   |
+----------------------------------------------------------------------------------------------------------+----------------------------------------------+
|:km:hk:`C <weightpaintvertexselection->C->view3d.select_circle>`                                          |:func:`blender:bpy.ops.view3d.select_circle`  |
+----------------------------------------------------------------------------------------------------------+----------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> paint.vert_select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.paint.vert_select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-EVT_TWEAK_S -> view3d.select_lasso : TWEAK -> ANY

   Lasso Select

   bpy.ops.view3d.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-EVT_TWEAK_S -> view3d.select_lasso : TWEAK -> ANY

   Lasso Select

   bpy.ops.view3d.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: A -> paint.vert_select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.paint.vert_select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> paint.vert_select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.paint.vert_select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: B -> view3d.select_border : KEYBOARD -> PRESS

   Border Select

   bpy.ops.view3d.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkeyd:: Ctrl-EVT_TWEAK_A -> view3d.select_lasso : TWEAK -> ANY

   Lasso Select

   bpy.ops.view3d.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-EVT_TWEAK_A -> view3d.select_lasso : TWEAK -> ANY

   Lasso Select

   bpy.ops.view3d.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: C -> view3d.select_circle : KEYBOARD -> PRESS

   Circle Select

   bpy.ops.view3d.select_circle(x=0, y=0, radius=1, gesture_mode=0)
   
   
