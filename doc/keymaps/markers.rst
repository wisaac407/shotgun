*******
Markers
*******

.. km:module:: markers

   


---------------
Quick Reference
---------------

+---------------------------------------------------------------------------------+---------------------------------------------+
|Hotkey                                                                           |Operator                                     |
+=================================================================================+=============================================+
|:km:hk:`Alt-EVT_TWEAK_S <markers->Alt-EVT_TWEAK_S->marker.move>`                 |:func:`blender:bpy.ops.marker.move`          |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`Ctrl-A <markers->Ctrl-A->marker.select_all>`                             |:func:`blender:bpy.ops.marker.select_all`    |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`M <markers->M->marker.add>`                                              |:func:`blender:bpy.ops.marker.add`           |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`EVT_TWEAK_S <markers->EVT_TWEAK_S->marker.move>`                         |:func:`blender:bpy.ops.marker.move`          |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`Shift-D <markers->Shift-D->marker.duplicate>`                            |:func:`blender:bpy.ops.marker.duplicate`     |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`SELECTMOUSE <markers->SELECTMOUSE->marker.select>`                       |:func:`blender:bpy.ops.marker.select`        |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <markers->Shift-SELECTMOUSE->marker.select>`           |:func:`blender:bpy.ops.marker.select`        |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <markers->Ctrl-SELECTMOUSE->marker.select>`             |:func:`blender:bpy.ops.marker.select`        |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`Ctrl-Shift-SELECTMOUSE <markers->Ctrl-Shift-SELECTMOUSE->marker.select>` |:func:`blender:bpy.ops.marker.select`        |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`B <markers->B->marker.select_border>`                                    |:func:`blender:bpy.ops.marker.select_border` |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`A <markers->A->marker.select_all>`                                       |:func:`blender:bpy.ops.marker.select_all`    |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`X <markers->X->marker.delete>`                                           |:func:`blender:bpy.ops.marker.delete`        |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`DEL <markers->DEL->marker.delete>`                                       |:func:`blender:bpy.ops.marker.delete`        |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`Ctrl-M <markers->Ctrl-M->marker.rename>`                                 |:func:`blender:bpy.ops.marker.rename`        |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`G <markers->G->marker.move>`                                             |:func:`blender:bpy.ops.marker.move`          |
+---------------------------------------------------------------------------------+---------------------------------------------+
|:km:hk:`Ctrl-B <markers->Ctrl-B->marker.camera_bind>`                            |:func:`blender:bpy.ops.marker.camera_bind`   |
+---------------------------------------------------------------------------------+---------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Alt-EVT_TWEAK_S -> marker.move

   Move Time Marker

   bpy.ops.marker.move(frames=0)
   
   
.. km:hotkey:: Ctrl-A -> marker.select_all

   (De)select all Markers

   bpy.ops.marker.select_all(action='TOGGLE')
   
   
.. km:hotkeyd:: M -> marker.add

   Add Time Marker

   bpy.ops.marker.add()
   
   
.. km:hotkeyd:: EVT_TWEAK_S -> marker.move

   Move Time Marker

   bpy.ops.marker.move(frames=0)
   
   
.. km:hotkeyd:: Shift-D -> marker.duplicate

   Duplicate Time Marker

   bpy.ops.marker.duplicate(frames=0)
   
   
.. km:hotkeyd:: SELECTMOUSE -> marker.select

   Select Time Marker

   bpy.ops.marker.select(extend=False, camera=False)
   
   
.. km:hotkeyd:: Shift-SELECTMOUSE -> marker.select

   Select Time Marker

   bpy.ops.marker.select(extend=False, camera=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-SELECTMOUSE -> marker.select

   Select Time Marker

   bpy.ops.marker.select(extend=False, camera=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   |Camera      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-SELECTMOUSE -> marker.select

   Select Time Marker

   bpy.ops.marker.select(extend=False, camera=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   |Camera      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: B -> marker.select_border

   Marker Border Select

   bpy.ops.marker.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkeyd:: A -> marker.select_all

   (De)select all Markers

   bpy.ops.marker.select_all(action='TOGGLE')
   
   
.. km:hotkeyd:: X -> marker.delete

   Delete Markers

   bpy.ops.marker.delete()
   
   
.. km:hotkeyd:: DEL -> marker.delete

   Delete Markers

   bpy.ops.marker.delete()
   
   
.. km:hotkeyd:: Ctrl-M -> marker.rename

   Rename Marker

   bpy.ops.marker.rename(name="RenamedMarker")
   
   
.. km:hotkeyd:: G -> marker.move

   Move Time Marker

   bpy.ops.marker.move(frames=0)
   
   
.. km:hotkeyd:: Ctrl-B -> marker.camera_bind

   Bind Camera to Markers

   bpy.ops.marker.camera_bind()
   
   
