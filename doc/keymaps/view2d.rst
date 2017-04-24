******
View2D
******

.. km:module:: view2d

   


---------------
Quick Reference
---------------

+---------------------------------------------------------------------------------+-------------------------------------------------+
|Hotkey                                                                           |Operator                                         |
+=================================================================================+=================================================+
|:km:hk:`MIDDLEMOUSE <view2d->MIDDLEMOUSE->view2d.pan>`                           |:func:`blender:bpy.ops.view2d.pan`               |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`ACTIONMOUSE <view2d->ACTIONMOUSE->view2d.pan>`                           |:func:`blender:bpy.ops.view2d.pan`               |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`LEFTMOUSE <view2d->LEFTMOUSE->view2d.scroller_activate>`                 |:func:`blender:bpy.ops.view2d.scroller_activate` |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`MIDDLEMOUSE <view2d->MIDDLEMOUSE->view2d.scroller_activate>`             |:func:`blender:bpy.ops.view2d.scroller_activate` |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`MIDDLEMOUSE <view2d->MIDDLEMOUSE->view2d.pan>`                           |:func:`blender:bpy.ops.view2d.pan`               |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-MIDDLEMOUSE <view2d->Shift-MIDDLEMOUSE->view2d.pan>`               |:func:`blender:bpy.ops.view2d.pan`               |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`TRACKPADPAN <view2d->TRACKPADPAN->view2d.pan>`                           |:func:`blender:bpy.ops.view2d.pan`               |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-WHEELDOWNMOUSE <view2d->Ctrl-WHEELDOWNMOUSE->view2d.scroll_right>`  |:func:`blender:bpy.ops.view2d.scroll_right`      |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-WHEELUPMOUSE <view2d->Ctrl-WHEELUPMOUSE->view2d.scroll_left>`       |:func:`blender:bpy.ops.view2d.scroll_left`       |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-WHEELDOWNMOUSE <view2d->Shift-WHEELDOWNMOUSE->view2d.scroll_down>` |:func:`blender:bpy.ops.view2d.scroll_down`       |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-WHEELUPMOUSE <view2d->Shift-WHEELUPMOUSE->view2d.scroll_up>`       |:func:`blender:bpy.ops.view2d.scroll_up`         |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`NDOF_MOTION <view2d->NDOF_MOTION->view2d.ndof>`                          |:func:`blender:bpy.ops.view2d.ndof`              |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`WHEELOUTMOUSE <view2d->WHEELOUTMOUSE->view2d.zoom_out>`                  |:func:`blender:bpy.ops.view2d.zoom_out`          |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`WHEELINMOUSE <view2d->WHEELINMOUSE->view2d.zoom_in>`                     |:func:`blender:bpy.ops.view2d.zoom_in`           |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`NUMPAD_MINUS <view2d->NUMPAD_MINUS->view2d.zoom_out>`                    |:func:`blender:bpy.ops.view2d.zoom_out`          |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`NUMPAD_PLUS <view2d->NUMPAD_PLUS->view2d.zoom_in>`                       |:func:`blender:bpy.ops.view2d.zoom_in`           |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-TRACKPADPAN <view2d->Ctrl-TRACKPADPAN->view2d.zoom>`                |:func:`blender:bpy.ops.view2d.zoom`              |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Any-TIMER1 <view2d->Any-TIMER1->view2d.smoothview>`                      |:func:`blender:bpy.ops.view2d.smoothview`        |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`WHEELDOWNMOUSE <view2d->WHEELDOWNMOUSE->view2d.scroll_down>`             |:func:`blender:bpy.ops.view2d.scroll_down`       |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`WHEELUPMOUSE <view2d->WHEELUPMOUSE->view2d.scroll_up>`                   |:func:`blender:bpy.ops.view2d.scroll_up`         |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`WHEELDOWNMOUSE <view2d->WHEELDOWNMOUSE->view2d.scroll_right>`            |:func:`blender:bpy.ops.view2d.scroll_right`      |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`WHEELUPMOUSE <view2d->WHEELUPMOUSE->view2d.scroll_left>`                 |:func:`blender:bpy.ops.view2d.scroll_left`       |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Ctrl-MIDDLEMOUSE <view2d->Ctrl-MIDDLEMOUSE->view2d.zoom>`                |:func:`blender:bpy.ops.view2d.zoom`              |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`TRACKPADZOOM <view2d->TRACKPADZOOM->view2d.zoom>`                        |:func:`blender:bpy.ops.view2d.zoom`              |
+---------------------------------------------------------------------------------+-------------------------------------------------+
|:km:hk:`Shift-B <view2d->Shift-B->view2d.zoom_border>`                           |:func:`blender:bpy.ops.view2d.zoom_border`       |
+---------------------------------------------------------------------------------+-------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: MIDDLEMOUSE -> view2d.pan : MOUSE -> ANY

   Pan View

   bpy.ops.view2d.pan(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: LEFTMOUSE -> view2d.scroller_activate : MOUSE -> PRESS

   Scroller Activate

   bpy.ops.view2d.scroller_activate()
   
   
.. km:hotkeyd:: MIDDLEMOUSE -> view2d.scroller_activate : MOUSE -> PRESS

   Scroller Activate

   bpy.ops.view2d.scroller_activate()
   
   
.. km:hotkeyd:: MIDDLEMOUSE -> view2d.pan : MOUSE -> PRESS

   Pan View

   bpy.ops.view2d.pan(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: Shift-MIDDLEMOUSE -> view2d.pan : MOUSE -> PRESS

   Pan View

   bpy.ops.view2d.pan(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: TRACKPADPAN -> view2d.pan : MOUSE -> ANY

   Pan View

   bpy.ops.view2d.pan(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: Ctrl-WHEELDOWNMOUSE -> view2d.scroll_right : MOUSE -> PRESS

   Scroll Right

   bpy.ops.view2d.scroll_right(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: Ctrl-WHEELUPMOUSE -> view2d.scroll_left : MOUSE -> PRESS

   Scroll Left

   bpy.ops.view2d.scroll_left(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: Shift-WHEELDOWNMOUSE -> view2d.scroll_down : MOUSE -> PRESS

   Scroll Down

   bpy.ops.view2d.scroll_down(deltax=0, deltay=0, page=False)
   
   
.. km:hotkeyd:: Shift-WHEELUPMOUSE -> view2d.scroll_up : MOUSE -> PRESS

   Scroll Up

   bpy.ops.view2d.scroll_up(deltax=0, deltay=0, page=False)
   
   
.. km:hotkeyd:: NDOF_MOTION -> view2d.ndof : NDOF -> ANY

   NDOF Pan/Zoom

   bpy.ops.view2d.ndof()
   
   
.. km:hotkeyd:: WHEELOUTMOUSE -> view2d.zoom_out : MOUSE -> PRESS

   Zoom Out

   bpy.ops.view2d.zoom_out(zoomfacx=0, zoomfacy=0)
   
   
.. km:hotkeyd:: WHEELINMOUSE -> view2d.zoom_in : MOUSE -> PRESS

   Zoom In

   bpy.ops.view2d.zoom_in(zoomfacx=0, zoomfacy=0)
   
   
.. km:hotkeyd:: NUMPAD_MINUS -> view2d.zoom_out : KEYBOARD -> PRESS

   Zoom Out

   bpy.ops.view2d.zoom_out(zoomfacx=0, zoomfacy=0)
   
   
.. km:hotkeyd:: NUMPAD_PLUS -> view2d.zoom_in : KEYBOARD -> PRESS

   Zoom In

   bpy.ops.view2d.zoom_in(zoomfacx=0, zoomfacy=0)
   
   
.. km:hotkeyd:: Ctrl-TRACKPADPAN -> view2d.zoom : MOUSE -> ANY

   Zoom 2D View

   bpy.ops.view2d.zoom(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: Any-TIMER1 -> view2d.smoothview : TIMER -> ANY

   Smooth View 2D

   bpy.ops.view2d.smoothview(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0)
   
   
.. km:hotkeyd:: WHEELDOWNMOUSE -> view2d.scroll_down : MOUSE -> PRESS

   Scroll Down

   bpy.ops.view2d.scroll_down(deltax=0, deltay=0, page=False)
   
   
.. km:hotkeyd:: WHEELUPMOUSE -> view2d.scroll_up : MOUSE -> PRESS

   Scroll Up

   bpy.ops.view2d.scroll_up(deltax=0, deltay=0, page=False)
   
   
.. km:hotkeyd:: WHEELDOWNMOUSE -> view2d.scroll_right : MOUSE -> PRESS

   Scroll Right

   bpy.ops.view2d.scroll_right(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: WHEELUPMOUSE -> view2d.scroll_left : MOUSE -> PRESS

   Scroll Left

   bpy.ops.view2d.scroll_left(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: Ctrl-MIDDLEMOUSE -> view2d.zoom : MOUSE -> PRESS

   Zoom 2D View

   bpy.ops.view2d.zoom(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: TRACKPADZOOM -> view2d.zoom : MOUSE -> ANY

   Zoom 2D View

   bpy.ops.view2d.zoom(deltax=0, deltay=0)
   
   
.. km:hotkeyd:: Shift-B -> view2d.zoom_border : KEYBOARD -> PRESS

   Zoom to Border

   bpy.ops.view2d.zoom_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0)
   
   
