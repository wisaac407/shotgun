****
Pose
****

.. km:module:: pose

   


---------------
Quick Reference
---------------

+--------------------------------------------------------------------------------+---------------------------------------------------------+
|Hotkey                                                                          |Operator                                                 |
+================================================================================+=========================================================+
|:km:hk:`A <pose->A->wm.call_menu>`                                              |:func:`blender:bpy.ops.wm.call_menu`                     |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-A <pose->Ctrl-A->pose.select_all>`                                 |:func:`blender:bpy.ops.pose.select_all`                  |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-F <pose->Shift-F->pose.select_mirror>`                            |:func:`blender:bpy.ops.pose.select_mirror`               |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-P <pose->Ctrl-P->object.parent_set>`                               |:func:`blender:bpy.ops.object.parent_set`                |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-A <pose->Shift-A->wm.call_menu>`                                  |:func:`blender:bpy.ops.wm.call_menu`                     |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`H <pose->H->pose.hide>`                                                 |:func:`blender:bpy.ops.pose.hide`                        |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-H <pose->Shift-H->pose.hide>`                                     |:func:`blender:bpy.ops.pose.hide`                        |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Alt-H <pose->Alt-H->pose.reveal>`                                       |:func:`blender:bpy.ops.pose.reveal`                      |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-A <pose->Ctrl-A->wm.call_menu>`                                    |:func:`blender:bpy.ops.wm.call_menu`                     |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Alt-R <pose->Alt-R->pose.rot_clear>`                                    |:func:`blender:bpy.ops.pose.rot_clear`                   |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Alt-G <pose->Alt-G->pose.loc_clear>`                                    |:func:`blender:bpy.ops.pose.loc_clear`                   |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Alt-S <pose->Alt-S->pose.scale_clear>`                                  |:func:`blender:bpy.ops.pose.scale_clear`                 |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Alt-F <pose->Alt-F->pose.quaternions_flip>`                             |:func:`blender:bpy.ops.pose.quaternions_flip`            |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-R <pose->Ctrl-R->pose.rotation_mode_set>`                          |:func:`blender:bpy.ops.pose.rotation_mode_set`           |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-C <pose->Ctrl-C->pose.copy>`                                       |:func:`blender:bpy.ops.pose.copy`                        |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-V <pose->Ctrl-V->pose.paste>`                                      |:func:`blender:bpy.ops.pose.paste`                       |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-Shift-V <pose->Ctrl-Shift-V->pose.paste>`                          |:func:`blender:bpy.ops.pose.paste`                       |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`A <pose->A->pose.select_all>`                                           |:func:`blender:bpy.ops.pose.select_all`                  |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-I <pose->Ctrl-I->pose.select_all>`                                 |:func:`blender:bpy.ops.pose.select_all`                  |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-P <pose->Shift-P->pose.select_parent>`                            |:func:`blender:bpy.ops.pose.select_parent`               |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`LEFT_BRACKET <pose->LEFT_BRACKET->pose.select_hierarchy>`               |:func:`blender:bpy.ops.pose.select_hierarchy`            |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-LEFT_BRACKET <pose->Shift-LEFT_BRACKET->pose.select_hierarchy>`   |:func:`blender:bpy.ops.pose.select_hierarchy`            |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`RIGHT_BRACKET <pose->RIGHT_BRACKET->pose.select_hierarchy>`             |:func:`blender:bpy.ops.pose.select_hierarchy`            |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-RIGHT_BRACKET <pose->Shift-RIGHT_BRACKET->pose.select_hierarchy>` |:func:`blender:bpy.ops.pose.select_hierarchy`            |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`L <pose->L->pose.select_linked>`                                        |:func:`blender:bpy.ops.pose.select_linked`               |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-G <pose->Shift-G->pose.select_grouped>`                           |:func:`blender:bpy.ops.pose.select_grouped`              |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-Shift-F <pose->Ctrl-Shift-F->pose.select_mirror>`                  |:func:`blender:bpy.ops.pose.select_mirror`               |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-Shift-C <pose->Ctrl-Shift-C->pose.constraint_add_with_targets>`    |:func:`blender:bpy.ops.pose.constraint_add_with_targets` |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-Alt-C <pose->Ctrl-Alt-C->pose.constraints_clear>`                  |:func:`blender:bpy.ops.pose.constraints_clear`           |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-I <pose->Shift-I->pose.ik_add>`                                   |:func:`blender:bpy.ops.pose.ik_add`                      |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-Alt-I <pose->Ctrl-Alt-I->pose.ik_clear>`                           |:func:`blender:bpy.ops.pose.ik_clear`                    |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-G <pose->Ctrl-G->wm.call_menu>`                                    |:func:`blender:bpy.ops.wm.call_menu`                     |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-W <pose->Shift-W->wm.call_menu>`                                  |:func:`blender:bpy.ops.wm.call_menu`                     |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-Shift-W <pose->Ctrl-Shift-W->wm.call_menu>`                        |:func:`blender:bpy.ops.wm.call_menu`                     |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Alt-W <pose->Alt-W->wm.call_menu>`                                      |:func:`blender:bpy.ops.wm.call_menu`                     |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-ACCENT_GRAVE <pose->Ctrl-ACCENT_GRAVE->armature.layers_show_all>`  |:func:`blender:bpy.ops.armature.layers_show_all`         |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-M <pose->Shift-M->armature.armature_layers>`                      |:func:`blender:bpy.ops.armature.armature_layers`         |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`M <pose->M->pose.bone_layers>`                                          |:func:`blender:bpy.ops.pose.bone_layers`                 |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-Alt-S <pose->Ctrl-Alt-S->transform.transform>`                     |:func:`blender:bpy.ops.transform.transform`              |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`I <pose->I->anim.keyframe_insert_menu>`                                 |:func:`blender:bpy.ops.anim.keyframe_insert_menu`        |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Alt-I <pose->Alt-I->anim.keyframe_delete_v3d>`                          |:func:`blender:bpy.ops.anim.keyframe_delete_v3d`         |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-I <pose->Ctrl-Shift-Alt-I->anim.keying_set_active_set>`  |:func:`blender:bpy.ops.anim.keying_set_active_set`       |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-L <pose->Ctrl-L->poselib.browse_interactive>`                      |:func:`blender:bpy.ops.poselib.browse_interactive`       |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-L <pose->Shift-L->poselib.pose_add>`                              |:func:`blender:bpy.ops.poselib.pose_add`                 |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Alt-L <pose->Alt-L->poselib.pose_remove>`                               |:func:`blender:bpy.ops.poselib.pose_remove`              |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-Shift-L <pose->Ctrl-Shift-L->poselib.pose_rename>`                 |:func:`blender:bpy.ops.poselib.pose_rename`              |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Ctrl-E <pose->Ctrl-E->pose.push>`                                       |:func:`blender:bpy.ops.pose.push`                        |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Alt-E <pose->Alt-E->pose.relax>`                                        |:func:`blender:bpy.ops.pose.relax`                       |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Shift-E <pose->Shift-E->pose.breakdown>`                                |:func:`blender:bpy.ops.pose.breakdown`                   |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`W <pose->W->wm.call_menu>`                                              |:func:`blender:bpy.ops.wm.call_menu`                     |
+--------------------------------------------------------------------------------+---------------------------------------------------------+
|:km:hk:`Alt-P <pose->Alt-P->wm.call_menu>`                                      |:func:`blender:bpy.ops.wm.call_menu`                     |
+--------------------------------------------------------------------------------+---------------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: A -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------------+
   |Properties: |Values:              |
   +============+=====================+
   |Name        |VIEW3D_MT_pose_apply |
   +------------+---------------------+
   
   
.. km:hotkey:: Ctrl-A -> pose.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.pose.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Shift-F -> pose.select_mirror : KEYBOARD -> PRESS

   Flip Active/Selected Bone

   bpy.ops.pose.select_mirror(only_active=False, extend=False)
   
   
.. km:hotkeyd:: Ctrl-P -> object.parent_set : KEYBOARD -> PRESS

   Make Parent

   bpy.ops.object.parent_set(type='OBJECT', xmirror=False, keep_transform=False)
   
   
.. km:hotkeyd:: Shift-A -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Name        |INFO_MT_add |
   +------------+------------+
   
   
.. km:hotkeyd:: H -> pose.hide : KEYBOARD -> PRESS

   Hide Selected

   bpy.ops.pose.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> pose.hide : KEYBOARD -> PRESS

   Hide Selected

   bpy.ops.pose.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-H -> pose.reveal : KEYBOARD -> PRESS

   Reveal Selected

   bpy.ops.pose.reveal()
   
   
.. km:hotkeyd:: Ctrl-A -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------------+
   |Properties: |Values:              |
   +============+=====================+
   |Name        |VIEW3D_MT_pose_apply |
   +------------+---------------------+
   
   
.. km:hotkeyd:: Alt-R -> pose.rot_clear : KEYBOARD -> PRESS

   Clear Pose Rotation

   bpy.ops.pose.rot_clear()
   
   
.. km:hotkeyd:: Alt-G -> pose.loc_clear : KEYBOARD -> PRESS

   Clear Pose Location

   bpy.ops.pose.loc_clear()
   
   
.. km:hotkeyd:: Alt-S -> pose.scale_clear : KEYBOARD -> PRESS

   Clear Pose Scale

   bpy.ops.pose.scale_clear()
   
   
.. km:hotkeyd:: Alt-F -> pose.quaternions_flip : KEYBOARD -> PRESS

   Flip Quats

   bpy.ops.pose.quaternions_flip()
   
   
.. km:hotkeyd:: Ctrl-R -> pose.rotation_mode_set : KEYBOARD -> PRESS

   Set Rotation Mode

   bpy.ops.pose.rotation_mode_set(type='QUATERNION')
   
   
.. km:hotkeyd:: Ctrl-C -> pose.copy : KEYBOARD -> PRESS

   Copy Pose

   bpy.ops.pose.copy()
   
   
.. km:hotkeyd:: Ctrl-V -> pose.paste : KEYBOARD -> PRESS

   Paste Pose

   bpy.ops.pose.paste(flipped=False, selected_mask=False)
   
   
   +------------------+--------+
   |Properties:       |Values: |
   +==================+========+
   |Flipped on X-Axis |False   |
   +------------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-V -> pose.paste : KEYBOARD -> PRESS

   Paste Pose

   bpy.ops.pose.paste(flipped=False, selected_mask=False)
   
   
   +------------------+--------+
   |Properties:       |Values: |
   +==================+========+
   |Flipped on X-Axis |True    |
   +------------------+--------+
   
   
.. km:hotkeyd:: A -> pose.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.pose.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> pose.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.pose.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-P -> pose.select_parent : KEYBOARD -> PRESS

   Select Parent Bone

   bpy.ops.pose.select_parent()
   
   
.. km:hotkeyd:: LEFT_BRACKET -> pose.select_hierarchy : KEYBOARD -> PRESS

   Select Hierarchy

   bpy.ops.pose.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |PARENT  |
   +------------+--------+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-LEFT_BRACKET -> pose.select_hierarchy : KEYBOARD -> PRESS

   Select Hierarchy

   bpy.ops.pose.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |PARENT  |
   +------------+--------+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: RIGHT_BRACKET -> pose.select_hierarchy : KEYBOARD -> PRESS

   Select Hierarchy

   bpy.ops.pose.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |CHILD   |
   +------------+--------+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-RIGHT_BRACKET -> pose.select_hierarchy : KEYBOARD -> PRESS

   Select Hierarchy

   bpy.ops.pose.select_hierarchy(direction='PARENT', extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Direction   |CHILD   |
   +------------+--------+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: L -> pose.select_linked : KEYBOARD -> PRESS

   Select Connected

   bpy.ops.pose.select_linked(extend=False)
   
   
.. km:hotkeyd:: Shift-G -> pose.select_grouped : KEYBOARD -> PRESS

   Select Grouped

   bpy.ops.pose.select_grouped(extend=False, type='LAYER')
   
   
.. km:hotkeyd:: Ctrl-Shift-F -> pose.select_mirror : KEYBOARD -> PRESS

   Flip Active/Selected Bone

   bpy.ops.pose.select_mirror(only_active=False, extend=False)
   
   
.. km:hotkeyd:: Ctrl-Shift-C -> pose.constraint_add_with_targets : KEYBOARD -> PRESS

   Add Constraint (with Targets)

   bpy.ops.pose.constraint_add_with_targets(type='<UNKNOWN ENUM>')
   
   
.. km:hotkeyd:: Ctrl-Alt-C -> pose.constraints_clear : KEYBOARD -> PRESS

   Clear Pose Constraints

   bpy.ops.pose.constraints_clear()
   
   
.. km:hotkeyd:: Shift-I -> pose.ik_add : KEYBOARD -> PRESS

   Add IK to Bone

   bpy.ops.pose.ik_add(with_targets=True)
   
   
.. km:hotkeyd:: Ctrl-Alt-I -> pose.ik_clear : KEYBOARD -> PRESS

   Remove IK

   bpy.ops.pose.ik_clear()
   
   
.. km:hotkeyd:: Ctrl-G -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------------+
   |Properties: |Values:              |
   +============+=====================+
   |Name        |VIEW3D_MT_pose_group |
   +------------+---------------------+
   
   
.. km:hotkeyd:: Shift-W -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------------------------+
   |Properties: |Values:                       |
   +============+==============================+
   |Name        |VIEW3D_MT_bone_options_toggle |
   +------------+------------------------------+
   
   
.. km:hotkeyd:: Ctrl-Shift-W -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------------------------+
   |Properties: |Values:                       |
   +============+==============================+
   |Name        |VIEW3D_MT_bone_options_enable |
   +------------+------------------------------+
   
   
.. km:hotkeyd:: Alt-W -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-------------------------------+
   |Properties: |Values:                        |
   +============+===============================+
   |Name        |VIEW3D_MT_bone_options_disable |
   +------------+-------------------------------+
   
   
.. km:hotkeyd:: Ctrl-ACCENT_GRAVE -> armature.layers_show_all : KEYBOARD -> PRESS

   Show All Layers

   bpy.ops.armature.layers_show_all(all=True)
   
   
.. km:hotkeyd:: Shift-M -> armature.armature_layers : KEYBOARD -> PRESS

   Change Armature Layers

   bpy.ops.armature.armature_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   
   
.. km:hotkeyd:: M -> pose.bone_layers : KEYBOARD -> PRESS

   Change Bone Layers

   bpy.ops.pose.bone_layers(layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
   
   
.. km:hotkeyd:: Ctrl-Alt-S -> transform.transform : KEYBOARD -> PRESS

   Transform

   bpy.ops.transform.transform(mode='TRANSLATION', value=(0, 0, 0, 0), axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
   +------------+----------+
   |Properties: |Values:   |
   +============+==========+
   |Mode        |BONE_SIZE |
   +------------+----------+
   
   
.. km:hotkeyd:: I -> anim.keyframe_insert_menu : KEYBOARD -> PRESS

   Insert Keyframe Menu

   bpy.ops.anim.keyframe_insert_menu(type='DEFAULT', confirm_success=False, always_prompt=False)
   
   
.. km:hotkeyd:: Alt-I -> anim.keyframe_delete_v3d : KEYBOARD -> PRESS

   Delete Keyframe

   bpy.ops.anim.keyframe_delete_v3d()
   
   
.. km:hotkeyd:: Ctrl-Shift-Alt-I -> anim.keying_set_active_set : KEYBOARD -> PRESS

   Set Active Keying Set

   bpy.ops.anim.keying_set_active_set(type='DEFAULT')
   
   
.. km:hotkeyd:: Ctrl-L -> poselib.browse_interactive : KEYBOARD -> PRESS

   PoseLib Browse Poses

   bpy.ops.poselib.browse_interactive(pose_index=-1)
   
   
.. km:hotkeyd:: Shift-L -> poselib.pose_add : KEYBOARD -> PRESS

   PoseLib Add Pose

   bpy.ops.poselib.pose_add(frame=1, name="Pose")
   
   
.. km:hotkeyd:: Alt-L -> poselib.pose_remove : KEYBOARD -> PRESS

   PoseLib Remove Pose

   bpy.ops.poselib.pose_remove(pose='<UNKNOWN ENUM>')
   
   
.. km:hotkeyd:: Ctrl-Shift-L -> poselib.pose_rename : KEYBOARD -> PRESS

   PoseLib Rename Pose

   bpy.ops.poselib.pose_rename(name="RenamedPose", pose='<UNKNOWN ENUM>')
   
   
.. km:hotkeyd:: Ctrl-E -> pose.push : KEYBOARD -> PRESS

   Push Pose

   bpy.ops.pose.push(prev_frame=0, next_frame=0, percentage=0.5)
   
   
.. km:hotkeyd:: Alt-E -> pose.relax : KEYBOARD -> PRESS

   Relax Pose

   bpy.ops.pose.relax(prev_frame=0, next_frame=0, percentage=0.5)
   
   
.. km:hotkeyd:: Shift-E -> pose.breakdown : KEYBOARD -> PRESS

   Pose Breakdowner

   bpy.ops.pose.breakdown(prev_frame=0, next_frame=0, percentage=0.5)
   
   
.. km:hotkeyd:: W -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------------------+
   |Properties: |Values:                 |
   +============+========================+
   |Name        |VIEW3D_MT_pose_specials |
   +------------+------------------------+
   
   
.. km:hotkeyd:: Alt-P -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-------------------------+
   |Properties: |Values:                  |
   +============+=========================+
   |Name        |VIEW3D_MT_pose_propagate |
   +------------+-------------------------+
   
   
