********
Metaball
********

.. km:module:: metaball

   


---------------
Quick Reference
---------------

+------------------------------------------------------------+-----------------------------------------------+
|Hotkey                                                      |Operator                                       |
+============================================================+===============================================+
|:km:hk:`Ctrl-A <metaball->Ctrl-A->mball.select_all>`        |:func:`blender:bpy.ops.mball.select_all`       |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-A <metaball->Shift-A->object.metaball_add>`   |:func:`blender:bpy.ops.object.metaball_add`    |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Alt-H <metaball->Alt-H->mball.reveal_metaelems>`    |:func:`blender:bpy.ops.mball.reveal_metaelems` |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`H <metaball->H->mball.hide_metaelems>`              |:func:`blender:bpy.ops.mball.hide_metaelems`   |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-H <metaball->Shift-H->mball.hide_metaelems>`  |:func:`blender:bpy.ops.mball.hide_metaelems`   |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`X <metaball->X->mball.delete_metaelems>`            |:func:`blender:bpy.ops.mball.delete_metaelems` |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`DEL <metaball->DEL->mball.delete_metaelems>`        |:func:`blender:bpy.ops.mball.delete_metaelems` |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-D <metaball->Shift-D->mball.duplicate_move>`  |:func:`blender:bpy.ops.mball.duplicate_move`   |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`A <metaball->A->mball.select_all>`                  |:func:`blender:bpy.ops.mball.select_all`       |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Ctrl-I <metaball->Ctrl-I->mball.select_all>`        |:func:`blender:bpy.ops.mball.select_all`       |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-G <metaball->Shift-G->mball.select_similar>`  |:func:`blender:bpy.ops.mball.select_similar`   |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Shift-O <metaball->Shift-O->wm.context_cycle_enum>` |:func:`blender:bpy.ops.wm.context_cycle_enum`  |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`O <metaball->O->wm.context_toggle_enum>`            |:func:`blender:bpy.ops.wm.context_toggle_enum` |
+------------------------------------------------------------+-----------------------------------------------+
|:km:hk:`Alt-O <metaball->Alt-O->wm.context_toggle_enum>`    |:func:`blender:bpy.ops.wm.context_toggle_enum` |
+------------------------------------------------------------+-----------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> mball.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.mball.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-A -> object.metaball_add : KEYBOARD -> PRESS

   Add Metaball

   bpy.ops.object.metaball_add(type='BALL', radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   
   
.. km:hotkeyd:: Alt-H -> mball.reveal_metaelems : KEYBOARD -> PRESS

   Reveal

   bpy.ops.mball.reveal_metaelems()
   
   
.. km:hotkeyd:: H -> mball.hide_metaelems : KEYBOARD -> PRESS

   Hide

   bpy.ops.mball.hide_metaelems(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> mball.hide_metaelems : KEYBOARD -> PRESS

   Hide

   bpy.ops.mball.hide_metaelems(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: X -> mball.delete_metaelems : KEYBOARD -> PRESS

   Delete

   bpy.ops.mball.delete_metaelems()
   
   
.. km:hotkeyd:: DEL -> mball.delete_metaelems : KEYBOARD -> PRESS

   Delete

   bpy.ops.mball.delete_metaelems()
   
   
.. km:hotkeyd:: Shift-D -> mball.duplicate_move : KEYBOARD -> PRESS

   Duplicate

   bpy.ops.mball.duplicate_move(MBALL_OT_duplicate_metaelems={}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +-----------------------+--------+
   |Properties:            |Values: |
   +=======================+========+
   |Duplicate Metaelements |N/A     |
   +-----------------------+--------+
   |Translate              |N/A     |
   +-----------------------+--------+
   
   
.. km:hotkeyd:: A -> mball.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.mball.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> mball.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.mball.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-G -> mball.select_similar : KEYBOARD -> PRESS

   Select Similar

   bpy.ops.mball.select_similar(type='TYPE', threshold=0.1)
   
   
.. km:hotkeyd:: Shift-O -> wm.context_cycle_enum : KEYBOARD -> PRESS

   Context Enum Cycle

   bpy.ops.wm.context_cycle_enum(data_path="", reverse=False, wrap=False)
   
   
   +-------------------+----------------------------------------+
   |Properties:        |Values:                                 |
   +===================+========================================+
   |Context Attributes |tool_settings.proportional_edit_falloff |
   +-------------------+----------------------------------------+
   |Wrap               |True                                    |
   +-------------------+----------------------------------------+
   
   
.. km:hotkeyd:: O -> wm.context_toggle_enum : KEYBOARD -> PRESS

   Context Toggle Values

   bpy.ops.wm.context_toggle_enum(data_path="", value_1="", value_2="")
   
   
   +-------------------+--------------------------------+
   |Properties:        |Values:                         |
   +===================+================================+
   |Context Attributes |tool_settings.proportional_edit |
   +-------------------+--------------------------------+
   |Value              |DISABLED                        |
   +-------------------+--------------------------------+
   |Value              |ENABLED                         |
   +-------------------+--------------------------------+
   
   
.. km:hotkeyd:: Alt-O -> wm.context_toggle_enum : KEYBOARD -> PRESS

   Context Toggle Values

   bpy.ops.wm.context_toggle_enum(data_path="", value_1="", value_2="")
   
   
   +-------------------+--------------------------------+
   |Properties:        |Values:                         |
   +===================+================================+
   |Context Attributes |tool_settings.proportional_edit |
   +-------------------+--------------------------------+
   |Value              |DISABLED                        |
   +-------------------+--------------------------------+
   |Value              |CONNECTED                       |
   +-------------------+--------------------------------+
   
   
