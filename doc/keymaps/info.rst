****
Info
****

.. km:module:: info

   


---------------
Quick Reference
---------------

+-----------------------------------------------------------+-----------------------------------------------+
|Hotkey                                                     |Operator                                       |
+===========================================================+===============================================+
|:km:hk:`Ctrl-A <info->Ctrl-A->info.select_all_toggle>`     |:func:`blender:bpy.ops.info.select_all_toggle` |
+-----------------------------------------------------------+-----------------------------------------------+
|:km:hk:`SELECTMOUSE <info->SELECTMOUSE->info.select_pick>` |:func:`blender:bpy.ops.info.select_pick`       |
+-----------------------------------------------------------+-----------------------------------------------+
|:km:hk:`A <info->A->info.select_all_toggle>`               |:func:`blender:bpy.ops.info.select_all_toggle` |
+-----------------------------------------------------------+-----------------------------------------------+
|:km:hk:`B <info->B->info.select_border>`                   |:func:`blender:bpy.ops.info.select_border`     |
+-----------------------------------------------------------+-----------------------------------------------+
|:km:hk:`R <info->R->info.report_replay>`                   |:func:`blender:bpy.ops.info.report_replay`     |
+-----------------------------------------------------------+-----------------------------------------------+
|:km:hk:`X <info->X->info.report_delete>`                   |:func:`blender:bpy.ops.info.report_delete`     |
+-----------------------------------------------------------+-----------------------------------------------+
|:km:hk:`DEL <info->DEL->info.report_delete>`               |:func:`blender:bpy.ops.info.report_delete`     |
+-----------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-C <info->Ctrl-C->info.report_copy>`           |:func:`blender:bpy.ops.info.report_copy`       |
+-----------------------------------------------------------+-----------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> info.select_all_toggle : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.info.select_all_toggle()
   
   
.. km:hotkeyd:: SELECTMOUSE -> info.select_pick : MOUSE -> PRESS

   Select Report

   bpy.ops.info.select_pick(report_index=0)
   
   
.. km:hotkeyd:: A -> info.select_all_toggle : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.info.select_all_toggle()
   
   
.. km:hotkeyd:: B -> info.select_border : KEYBOARD -> PRESS

   Border Select

   bpy.ops.info.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkeyd:: R -> info.report_replay : KEYBOARD -> PRESS

   Replay Operators

   bpy.ops.info.report_replay()
   
   
.. km:hotkeyd:: X -> info.report_delete : KEYBOARD -> PRESS

   Delete Reports

   bpy.ops.info.report_delete()
   
   
.. km:hotkeyd:: DEL -> info.report_delete : KEYBOARD -> PRESS

   Delete Reports

   bpy.ops.info.report_delete()
   
   
.. km:hotkeyd:: Ctrl-C -> info.report_copy : KEYBOARD -> PRESS

   Copy Reports to Clipboard

   bpy.ops.info.report_copy()
   
   
