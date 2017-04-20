*********
Animation
*********

.. km:module:: animation


---------------
Quick Reference
---------------

+-----------------------------------------------------------------+------------------------------------------------+
|Hotkey                                                           |Operator                                        |
+=================================================================+================================================+
|:km:hk:`SELECTMOUSE <animation->SELECTMOUSE->anim.change_frame>` |:func:`blender:bpy.ops.anim.change_frame`       |
+-----------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Alt-P <animation->Alt-P->anim.previewrange_clear>`       |:func:`blender:bpy.ops.anim.previewrange_clear` |
+-----------------------------------------------------------------+------------------------------------------------+
|:km:hk:`ACTIONMOUSE <animation->ACTIONMOUSE->anim.change_frame>` |:func:`blender:bpy.ops.anim.change_frame`       |
+-----------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Ctrl-T <animation->Ctrl-T->wm.context_toggle>`           |:func:`blender:bpy.ops.wm.context_toggle`       |
+-----------------------------------------------------------------+------------------------------------------------+
|:km:hk:`P <animation->P->anim.previewrange_set>`                 |:func:`blender:bpy.ops.anim.previewrange_set`   |
+-----------------------------------------------------------------+------------------------------------------------+
|:km:hk:`Alt-P <animation->Alt-P->anim.previewrange_clear>`       |:func:`blender:bpy.ops.anim.previewrange_clear` |
+-----------------------------------------------------------------+------------------------------------------------+


------------------
Detailed Reference
------------------

.. km:hotkey:: SELECTMOUSE -> anim.change_frame

   Change Frame

   bpy.ops.anim.change_frame(frame=0, snap=False)
   
   
.. km:hotkey:: Alt-P -> anim.previewrange_clear

   Clear Preview Range

   bpy.ops.anim.previewrange_clear()
   
   
.. km:hotkey:: ACTIONMOUSE -> anim.change_frame

   Change Frame

   bpy.ops.anim.change_frame(frame=0, snap=False)
   
   
.. km:hotkey:: Ctrl-T -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+------------------------+
   |Properties:        |Values:                 |
   +===================+========================+
   |Context Attributes |space_data.show_seconds |
   +-------------------+------------------------+
   
   
.. km:hotkey:: P -> anim.previewrange_set

   Set Preview Range

   bpy.ops.anim.previewrange_set(xmin=0, xmax=0, ymin=0, ymax=0)
   
   
.. km:hotkey:: Alt-P -> anim.previewrange_clear

   Clear Preview Range

   bpy.ops.anim.previewrange_clear()
   
   
