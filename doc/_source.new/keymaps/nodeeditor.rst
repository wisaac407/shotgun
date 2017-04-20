***********
Node Editor
***********

.. km:module:: nodeeditor


---------------
Quick Reference
---------------

+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|Hotkey                                                                                          |Operator                                                |
+================================================================================================+========================================================+
|:km:hk:`W <nodeeditor->W->wm.call_menu>`                                                        |:func:`blender:bpy.ops.wm.call_menu`                    |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`SELECTMOUSE <nodeeditor->SELECTMOUSE->node.show_active_node_image>`                     |:func:`blender:bpy.ops.node.show_active_node_image`     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`ACTIONMOUSE <nodeeditor->ACTIONMOUSE->node.show_active_node_image>`                     |:func:`blender:bpy.ops.node.show_active_node_image`     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-EQUAL <nodeeditor->Shift-EQUAL->wm.call_menu>`                                    |:func:`blender:bpy.ops.wm.call_menu`                    |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Alt-0 <nodeeditor->Ctrl-Alt-0->node.nw_merge_nodes>`                               |:func:`blender:bpy.ops.node.nw_merge_nodes`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Alt-NUMPAD_0 <nodeeditor->Ctrl-Alt-NUMPAD_0->node.nw_merge_nodes>`                 |:func:`blender:bpy.ops.node.nw_merge_nodes`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Alt-EVT_TWEAK_S <nodeeditor->Ctrl-Alt-EVT_TWEAK_S->node.select_lasso>`             |:func:`blender:bpy.ops.node.select_lasso`               |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-SELECTMOUSE <nodeeditor->Alt-SELECTMOUSE->node.backimage_sample>`                   |:func:`blender:bpy.ops.node.backimage_sample`           |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-P <nodeeditor->Alt-P->node.parent_clear>`                                           |:func:`blender:bpy.ops.node.parent_clear`               |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`NDOF_BUTTON_FIT <nodeeditor->NDOF_BUTTON_FIT->node.view_all>`                           |:func:`blender:bpy.ops.node.view_all`                   |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-A <nodeeditor->Ctrl-A->node.select_all>`                                           |:func:`blender:bpy.ops.node.select_all`                 |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-G <nodeeditor->Shift-G->node.select_same_type>`                                   |:func:`blender:bpy.ops.node.select_same_type`           |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-Tab <nodeeditor->Shift-Tab->node.group_edit>`                                     |:func:`blender:bpy.ops.node.group_edit`                 |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-F <nodeeditor->Alt-F->node.detach_translate_attach>`                                |:func:`blender:bpy.ops.node.detach_translate_attach`    |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`ACTIONMOUSE <nodeeditor->ACTIONMOUSE->node.select>`                                     |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`SELECTMOUSE <nodeeditor->SELECTMOUSE->node.select>`                                     |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-ACTIONMOUSE <nodeeditor->Ctrl-ACTIONMOUSE->node.select>`                           |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <nodeeditor->Ctrl-SELECTMOUSE->node.select>`                           |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-ACTIONMOUSE <nodeeditor->Alt-ACTIONMOUSE->node.select>`                             |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-SELECTMOUSE <nodeeditor->Alt-SELECTMOUSE->node.select>`                             |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Alt-ACTIONMOUSE <nodeeditor->Ctrl-Alt-ACTIONMOUSE->node.select>`                   |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Alt-SELECTMOUSE <nodeeditor->Ctrl-Alt-SELECTMOUSE->node.select>`                   |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-ACTIONMOUSE <nodeeditor->Shift-ACTIONMOUSE->node.select>`                         |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <nodeeditor->Shift-SELECTMOUSE->node.select>`                         |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-ACTIONMOUSE <nodeeditor->Ctrl-Shift-ACTIONMOUSE->node.select>`               |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-SELECTMOUSE <nodeeditor->Ctrl-Shift-SELECTMOUSE->node.select>`               |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-Alt-ACTIONMOUSE <nodeeditor->Shift-Alt-ACTIONMOUSE->node.select>`                 |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-Alt-SELECTMOUSE <nodeeditor->Shift-Alt-SELECTMOUSE->node.select>`                 |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-ACTIONMOUSE <nodeeditor->Ctrl-Shift-Alt-ACTIONMOUSE->node.select>`       |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-SELECTMOUSE <nodeeditor->Ctrl-Shift-Alt-SELECTMOUSE->node.select>`       |:func:`blender:bpy.ops.node.select`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`EVT_TWEAK_S <nodeeditor->EVT_TWEAK_S->node.select_border>`                              |:func:`blender:bpy.ops.node.select_border`              |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Alt-EVT_TWEAK_A <nodeeditor->Ctrl-Alt-EVT_TWEAK_A->node.select_lasso>`             |:func:`blender:bpy.ops.node.select_lasso`               |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-EVT_TWEAK_A <nodeeditor->Ctrl-Shift-Alt-EVT_TWEAK_A->node.select_lasso>` |:func:`blender:bpy.ops.node.select_lasso`               |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`C <nodeeditor->C->node.select_circle>`                                                  |:func:`blender:bpy.ops.node.select_circle`              |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`LEFTMOUSE <nodeeditor->LEFTMOUSE->node.link>`                                           |:func:`blender:bpy.ops.node.link`                       |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-LEFTMOUSE <nodeeditor->Ctrl-LEFTMOUSE->node.link>`                                 |:func:`blender:bpy.ops.node.link`                       |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`LEFTMOUSE <nodeeditor->LEFTMOUSE->node.resize>`                                         |:func:`blender:bpy.ops.node.resize`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-LEFTMOUSE <nodeeditor->Shift-LEFTMOUSE->node.add_reroute>`                        |:func:`blender:bpy.ops.node.add_reroute`                |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-LEFTMOUSE <nodeeditor->Ctrl-LEFTMOUSE->node.links_cut>`                            |:func:`blender:bpy.ops.node.links_cut`                  |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-LEFTMOUSE <nodeeditor->Ctrl-Shift-LEFTMOUSE->node.select_link_viewer>`       |:func:`blender:bpy.ops.node.select_link_viewer`         |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-MIDDLEMOUSE <nodeeditor->Alt-MIDDLEMOUSE->node.backimage_move>`                     |:func:`blender:bpy.ops.node.backimage_move`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`V <nodeeditor->V->node.backimage_zoom>`                                                 |:func:`blender:bpy.ops.node.backimage_zoom`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-V <nodeeditor->Alt-V->node.backimage_zoom>`                                         |:func:`blender:bpy.ops.node.backimage_zoom`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-HOME <nodeeditor->Alt-HOME->node.backimage_fit>`                                    |:func:`blender:bpy.ops.node.backimage_fit`              |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-ACTIONMOUSE <nodeeditor->Alt-ACTIONMOUSE->node.backimage_sample>`                   |:func:`blender:bpy.ops.node.backimage_sample`           |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`F <nodeeditor->F->node.link_make>`                                                      |:func:`blender:bpy.ops.node.link_make`                  |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-F <nodeeditor->Shift-F->node.link_make>`                                          |:func:`blender:bpy.ops.node.link_make`                  |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-A <nodeeditor->Shift-A->wm.call_menu>`                                            |:func:`blender:bpy.ops.wm.call_menu`                    |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-D <nodeeditor->Shift-D->node.duplicate_move>`                                     |:func:`blender:bpy.ops.node.duplicate_move`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-D <nodeeditor->Ctrl-Shift-D->node.duplicate_move_keep_inputs>`               |:func:`blender:bpy.ops.node.duplicate_move_keep_inputs` |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-P <nodeeditor->Ctrl-P->node.parent_set>`                                           |:func:`blender:bpy.ops.node.parent_set`                 |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-P <nodeeditor->Alt-P->node.detach>`                                                 |:func:`blender:bpy.ops.node.detach`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-J <nodeeditor->Ctrl-J->node.join>`                                                 |:func:`blender:bpy.ops.node.join`                       |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`H <nodeeditor->H->node.hide_toggle>`                                                    |:func:`blender:bpy.ops.node.hide_toggle`                |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`M <nodeeditor->M->node.mute_toggle>`                                                    |:func:`blender:bpy.ops.node.mute_toggle`                |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-H <nodeeditor->Shift-H->node.preview_toggle>`                                     |:func:`blender:bpy.ops.node.preview_toggle`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-H <nodeeditor->Ctrl-H->node.hide_socket_toggle>`                                   |:func:`blender:bpy.ops.node.hide_socket_toggle`         |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`HOME <nodeeditor->HOME->node.view_all>`                                                 |:func:`blender:bpy.ops.node.view_all`                   |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`NDOF_BUTTON_FIT <nodeeditor->NDOF_BUTTON_FIT->node.view_all>`                           |:func:`blender:bpy.ops.node.view_all`                   |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`NUMPAD_PERIOD <nodeeditor->NUMPAD_PERIOD->node.view_selected>`                          |:func:`blender:bpy.ops.node.view_selected`              |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`B <nodeeditor->B->node.select_border>`                                                  |:func:`blender:bpy.ops.node.select_border`              |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`X <nodeeditor->X->node.delete>`                                                         |:func:`blender:bpy.ops.node.delete`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`DEL <nodeeditor->DEL->node.delete>`                                                     |:func:`blender:bpy.ops.node.delete`                     |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-X <nodeeditor->Ctrl-X->node.delete_reconnect>`                                     |:func:`blender:bpy.ops.node.delete_reconnect`           |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`A <nodeeditor->A->node.select_all>`                                                     |:func:`blender:bpy.ops.node.select_all`                 |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-I <nodeeditor->Ctrl-I->node.select_all>`                                           |:func:`blender:bpy.ops.node.select_all`                 |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-L <nodeeditor->Shift-L->node.select_linked_to>`                                   |:func:`blender:bpy.ops.node.select_linked_to`           |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`L <nodeeditor->L->node.select_linked_from>`                                             |:func:`blender:bpy.ops.node.select_linked_from`         |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-G <nodeeditor->Shift-G->node.select_grouped>`                                     |:func:`blender:bpy.ops.node.select_grouped`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-G <nodeeditor->Ctrl-Shift-G->node.select_grouped>`                           |:func:`blender:bpy.ops.node.select_grouped`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-RIGHT_BRACKET <nodeeditor->Shift-RIGHT_BRACKET->node.select_same_type_step>`      |:func:`blender:bpy.ops.node.select_same_type_step`      |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-LEFT_BRACKET <nodeeditor->Shift-LEFT_BRACKET->node.select_same_type_step>`        |:func:`blender:bpy.ops.node.select_same_type_step`      |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-F <nodeeditor->Ctrl-F->node.find_node>`                                            |:func:`blender:bpy.ops.node.find_node`                  |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-G <nodeeditor->Ctrl-G->node.group_make>`                                           |:func:`blender:bpy.ops.node.group_make`                 |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-G <nodeeditor->Alt-G->node.group_ungroup>`                                          |:func:`blender:bpy.ops.node.group_ungroup`              |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`P <nodeeditor->P->node.group_separate>`                                                 |:func:`blender:bpy.ops.node.group_separate`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Tab <nodeeditor->Tab->node.group_edit>`                                                 |:func:`blender:bpy.ops.node.group_edit`                 |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Tab <nodeeditor->Ctrl-Tab->node.group_edit>`                                       |:func:`blender:bpy.ops.node.group_edit`                 |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-R <nodeeditor->Ctrl-R->node.read_renderlayers>`                                    |:func:`blender:bpy.ops.node.read_renderlayers`          |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-R <nodeeditor->Shift-R->node.read_fullsamplelayers>`                              |:func:`blender:bpy.ops.node.read_fullsamplelayers`      |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Z <nodeeditor->Z->node.render_changed>`                                                 |:func:`blender:bpy.ops.node.render_changed`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-C <nodeeditor->Ctrl-C->node.clipboard_copy>`                                       |:func:`blender:bpy.ops.node.clipboard_copy`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-V <nodeeditor->Ctrl-V->node.clipboard_paste>`                                      |:func:`blender:bpy.ops.node.clipboard_paste`            |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-B <nodeeditor->Ctrl-B->node.viewer_border>`                                        |:func:`blender:bpy.ops.node.viewer_border`              |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Alt-B <nodeeditor->Ctrl-Alt-B->node.clear_viewer_border>`                          |:func:`blender:bpy.ops.node.clear_viewer_border`        |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`G <nodeeditor->G->node.translate_attach>`                                               |:func:`blender:bpy.ops.node.translate_attach`           |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`EVT_TWEAK_A <nodeeditor->EVT_TWEAK_A->node.translate_attach>`                           |:func:`blender:bpy.ops.node.translate_attach`           |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`EVT_TWEAK_S <nodeeditor->EVT_TWEAK_S->node.translate_attach>`                           |:func:`blender:bpy.ops.node.translate_attach`           |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`G <nodeeditor->G->transform.translate>`                                                 |:func:`blender:bpy.ops.transform.translate`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`EVT_TWEAK_A <nodeeditor->EVT_TWEAK_A->transform.translate>`                             |:func:`blender:bpy.ops.transform.translate`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`EVT_TWEAK_S <nodeeditor->EVT_TWEAK_S->transform.translate>`                             |:func:`blender:bpy.ops.transform.translate`             |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`R <nodeeditor->R->transform.rotate>`                                                    |:func:`blender:bpy.ops.transform.rotate`                |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`S <nodeeditor->S->transform.resize>`                                                    |:func:`blender:bpy.ops.transform.resize`                |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-D <nodeeditor->Alt-D->node.move_detach_links>`                                      |:func:`blender:bpy.ops.node.move_detach_links`          |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-EVT_TWEAK_A <nodeeditor->Alt-EVT_TWEAK_A->node.move_detach_links_release>`          |:func:`blender:bpy.ops.node.move_detach_links_release`  |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Alt-EVT_TWEAK_S <nodeeditor->Alt-EVT_TWEAK_S->node.move_detach_links>`                  |:func:`blender:bpy.ops.node.move_detach_links`          |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Shift-Tab <nodeeditor->Shift-Tab->wm.context_toggle>`                                   |:func:`blender:bpy.ops.wm.context_toggle`               |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Tab <nodeeditor->Ctrl-Shift-Tab->wm.context_menu_enum>`                      |:func:`blender:bpy.ops.wm.context_menu_enum`            |
+------------------------------------------------------------------------------------------------+--------------------------------------------------------+


------------------
Detailed Reference
------------------

.. km:hotkey:: W -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+--------------------------------+
   |Properties: |Values:                         |
   +============+================================+
   |Name        |AMTH_NODE_MT_amaranth_templates |
   +------------+--------------------------------+
   
   
.. km:hotkeyi:: SELECTMOUSE -> node.show_active_node_image

   NODE_OT_show_active_node_image

   
.. km:hotkeyi:: ACTIONMOUSE -> node.show_active_node_image

   NODE_OT_show_active_node_image

   
.. km:hotkey:: Shift-EQUAL -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------------------+
   |Properties: |Values:                    |
   +============+===========================+
   |Name        |NODE_MT_nw_node_align_menu |
   +------------+---------------------------+
   
   
.. km:hotkeyi:: Ctrl-Alt-0 -> node.nw_merge_nodes

   NODE_OT_nw_merge_nodes

   
.. km:hotkeyi:: Ctrl-Alt-NUMPAD_0 -> node.nw_merge_nodes

   NODE_OT_nw_merge_nodes

   
.. km:hotkey:: Ctrl-Alt-EVT_TWEAK_S -> node.select_lasso

   Lasso Select

   bpy.ops.node.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkey:: Alt-SELECTMOUSE -> node.backimage_sample

   Backimage Sample

   bpy.ops.node.backimage_sample()
   
   
.. km:hotkeyi:: Alt-P -> node.parent_clear

   NODE_OT_parent_clear

   
.. km:hotkey:: NDOF_BUTTON_FIT -> node.view_all

   View All

   bpy.ops.node.view_all()
   
   
.. km:hotkey:: Ctrl-A -> node.select_all

   (De)select All

   bpy.ops.node.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyi:: Shift-G -> node.select_same_type

   NODE_OT_select_same_type

   
.. km:hotkey:: Shift-Tab -> node.group_edit

   Edit Group

   bpy.ops.node.group_edit(exit=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Exit        |True    |
   +------------+--------+
   
   
.. km:hotkey:: Alt-F -> node.detach_translate_attach

   Detach and Move

   bpy.ops.node.detach_translate_attach(NODE_OT_detach={}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False}, NODE_OT_attach={})
   
   
   +-------------+--------+
   |Properties:  |Values: |
   +=============+========+
   |Detach Nodes |N/A     |
   +-------------+--------+
   |Translate    |N/A     |
   +-------------+--------+
   |Attach Nodes |N/A     |
   +-------------+--------+
   
   
.. km:hotkey:: ACTIONMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: SELECTMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-ACTIONMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-SELECTMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Alt-ACTIONMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Alt-SELECTMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Alt-ACTIONMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Alt-SELECTMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Shift-ACTIONMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Shift-SELECTMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-ACTIONMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-SELECTMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Shift-Alt-ACTIONMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Shift-Alt-SELECTMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-Alt-ACTIONMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-Alt-SELECTMOUSE -> node.select

   Select

   bpy.ops.node.select(mouse_x=0, mouse_y=0, extend=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: EVT_TWEAK_S -> node.select_border

   Border Select

   bpy.ops.node.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, tweak=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Tweak       |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Alt-EVT_TWEAK_A -> node.select_lasso

   Lasso Select

   bpy.ops.node.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-Alt-EVT_TWEAK_A -> node.select_lasso

   Lasso Select

   bpy.ops.node.select_lasso(path=[], deselect=False, extend=True)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkey:: C -> node.select_circle

   Circle Select

   bpy.ops.node.select_circle(x=0, y=0, radius=1, gesture_mode=0)
   
   
.. km:hotkey:: LEFTMOUSE -> node.link

   Link Nodes

   bpy.ops.node.link(detach=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Detach      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-LEFTMOUSE -> node.link

   Link Nodes

   bpy.ops.node.link(detach=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Detach      |True    |
   +------------+--------+
   
   
.. km:hotkey:: LEFTMOUSE -> node.resize

   Resize Node

   bpy.ops.node.resize()
   
   
.. km:hotkey:: Shift-LEFTMOUSE -> node.add_reroute

   Add Reroute

   bpy.ops.node.add_reroute(path=[], cursor=6)
   
   
.. km:hotkey:: Ctrl-LEFTMOUSE -> node.links_cut

   Cut Links

   bpy.ops.node.links_cut(path=[], cursor=9)
   
   
.. km:hotkey:: Ctrl-Shift-LEFTMOUSE -> node.select_link_viewer

   Link Viewer

   bpy.ops.node.select_link_viewer(NODE_OT_select={"mouse_x":0, "mouse_y":0, "extend":False}, NODE_OT_link_viewer={})
   
   
   +--------------------+--------+
   |Properties:         |Values: |
   +====================+========+
   |Select              |N/A     |
   +--------------------+--------+
   |Link to Viewer Node |N/A     |
   +--------------------+--------+
   
   
.. km:hotkey:: Alt-MIDDLEMOUSE -> node.backimage_move

   Background Image Move

   bpy.ops.node.backimage_move()
   
   
.. km:hotkey:: V -> node.backimage_zoom

   Background Image Zoom

   bpy.ops.node.backimage_zoom(factor=1.2)
   
   
   +------------+------------------+
   |Properties: |Values:           |
   +============+==================+
   |Factor      |0.833329975605011 |
   +------------+------------------+
   
   
.. km:hotkey:: Alt-V -> node.backimage_zoom

   Background Image Zoom

   bpy.ops.node.backimage_zoom(factor=1.2)
   
   
   +------------+-------------------+
   |Properties: |Values:            |
   +============+===================+
   |Factor      |1.2000000476837158 |
   +------------+-------------------+
   
   
.. km:hotkey:: Alt-HOME -> node.backimage_fit

   Background Image Fit

   bpy.ops.node.backimage_fit()
   
   
.. km:hotkey:: Alt-ACTIONMOUSE -> node.backimage_sample

   Backimage Sample

   bpy.ops.node.backimage_sample()
   
   
.. km:hotkey:: F -> node.link_make

   Make Links

   bpy.ops.node.link_make(replace=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Replace     |False   |
   +------------+--------+
   
   
.. km:hotkey:: Shift-F -> node.link_make

   Make Links

   bpy.ops.node.link_make(replace=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Replace     |True    |
   +------------+--------+
   
   
.. km:hotkey:: Shift-A -> wm.call_menu

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+------------+
   |Properties: |Values:     |
   +============+============+
   |Name        |NODE_MT_add |
   +------------+------------+
   
   
.. km:hotkey:: Shift-D -> node.duplicate_move

   Duplicate

   bpy.ops.node.duplicate_move(NODE_OT_duplicate={"keep_inputs":False}, NODE_OT_translate_attach={"TRANSFORM_OT_translate":{"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False}, "NODE_OT_attach":{}, "NODE_OT_insert_offset":{}})
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Duplicate Nodes |N/A     |
   +----------------+--------+
   |Move and Attach |N/A     |
   +----------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-D -> node.duplicate_move_keep_inputs

   Duplicate

   bpy.ops.node.duplicate_move_keep_inputs(NODE_OT_duplicate={"keep_inputs":False}, NODE_OT_translate_attach={"TRANSFORM_OT_translate":{"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False}, "NODE_OT_attach":{}, "NODE_OT_insert_offset":{}})
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Duplicate Nodes |N/A     |
   +----------------+--------+
   |Move and Attach |N/A     |
   +----------------+--------+
   
   
.. km:hotkey:: Ctrl-P -> node.parent_set

   Make Parent

   bpy.ops.node.parent_set()
   
   
.. km:hotkey:: Alt-P -> node.detach

   Detach Nodes

   bpy.ops.node.detach()
   
   
.. km:hotkey:: Ctrl-J -> node.join

   Join Nodes

   bpy.ops.node.join()
   
   
.. km:hotkey:: H -> node.hide_toggle

   Hide

   bpy.ops.node.hide_toggle()
   
   
.. km:hotkey:: M -> node.mute_toggle

   Toggle Node Mute

   bpy.ops.node.mute_toggle()
   
   
.. km:hotkey:: Shift-H -> node.preview_toggle

   Toggle Node Preview

   bpy.ops.node.preview_toggle()
   
   
.. km:hotkey:: Ctrl-H -> node.hide_socket_toggle

   Toggle Hidden Node Sockets

   bpy.ops.node.hide_socket_toggle()
   
   
.. km:hotkey:: HOME -> node.view_all

   View All

   bpy.ops.node.view_all()
   
   
.. km:hotkey:: NDOF_BUTTON_FIT -> node.view_all

   View All

   bpy.ops.node.view_all()
   
   
.. km:hotkey:: NUMPAD_PERIOD -> node.view_selected

   View Selected

   bpy.ops.node.view_selected()
   
   
.. km:hotkey:: B -> node.select_border

   Border Select

   bpy.ops.node.select_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True, tweak=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Tweak       |False   |
   +------------+--------+
   
   
.. km:hotkey:: X -> node.delete

   Delete

   bpy.ops.node.delete()
   
   
.. km:hotkey:: DEL -> node.delete

   Delete

   bpy.ops.node.delete()
   
   
.. km:hotkey:: Ctrl-X -> node.delete_reconnect

   Delete with Reconnect

   bpy.ops.node.delete_reconnect()
   
   
.. km:hotkey:: A -> node.select_all

   (De)select All

   bpy.ops.node.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-I -> node.select_all

   (De)select All

   bpy.ops.node.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkey:: Shift-L -> node.select_linked_to

   Select Linked To

   bpy.ops.node.select_linked_to()
   
   
.. km:hotkey:: L -> node.select_linked_from

   Select Linked From

   bpy.ops.node.select_linked_from()
   
   
.. km:hotkey:: Shift-G -> node.select_grouped

   Select Grouped

   bpy.ops.node.select_grouped(extend=False, type='TYPE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-G -> node.select_grouped

   Select Grouped

   bpy.ops.node.select_grouped(extend=False, type='TYPE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Extend      |True    |
   +------------+--------+
   
   
.. km:hotkey:: Shift-RIGHT_BRACKET -> node.select_same_type_step

   Activate Same Type Next/Prev

   bpy.ops.node.select_same_type_step(prev=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Previous    |False   |
   +------------+--------+
   
   
.. km:hotkey:: Shift-LEFT_BRACKET -> node.select_same_type_step

   Activate Same Type Next/Prev

   bpy.ops.node.select_same_type_step(prev=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Previous    |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-F -> node.find_node

   Find Node

   bpy.ops.node.find_node(prev=False)
   
   
.. km:hotkey:: Ctrl-G -> node.group_make

   Make Group

   bpy.ops.node.group_make()
   
   
.. km:hotkey:: Alt-G -> node.group_ungroup

   Ungroup

   bpy.ops.node.group_ungroup()
   
   
.. km:hotkey:: P -> node.group_separate

   Separate

   bpy.ops.node.group_separate(type='COPY')
   
   
.. km:hotkey:: Tab -> node.group_edit

   Edit Group

   bpy.ops.node.group_edit(exit=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Exit        |False   |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-Tab -> node.group_edit

   Edit Group

   bpy.ops.node.group_edit(exit=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Exit        |True    |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-R -> node.read_renderlayers

   Read Render Layers

   bpy.ops.node.read_renderlayers()
   
   
.. km:hotkey:: Shift-R -> node.read_fullsamplelayers

   Read Full Sample Layers

   bpy.ops.node.read_fullsamplelayers()
   
   
.. km:hotkey:: Z -> node.render_changed

   Render Changed Layer

   bpy.ops.node.render_changed()
   
   
.. km:hotkey:: Ctrl-C -> node.clipboard_copy

   Copy to Clipboard

   bpy.ops.node.clipboard_copy()
   
   
.. km:hotkey:: Ctrl-V -> node.clipboard_paste

   Paste from Clipboard

   bpy.ops.node.clipboard_paste()
   
   
.. km:hotkey:: Ctrl-B -> node.viewer_border

   Viewer Border

   bpy.ops.node.viewer_border(gesture_mode=0, xmin=0, xmax=0, ymin=0, ymax=0, extend=True)
   
   
.. km:hotkey:: Ctrl-Alt-B -> node.clear_viewer_border

   Clear Viewer Border

   bpy.ops.node.clear_viewer_border()
   
   
.. km:hotkey:: G -> node.translate_attach

   Move and Attach

   bpy.ops.node.translate_attach(TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False}, NODE_OT_attach={}, NODE_OT_insert_offset={})
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Translate     |N/A     |
   +--------------+--------+
   |Attach Nodes  |N/A     |
   +--------------+--------+
   |Insert Offset |N/A     |
   +--------------+--------+
   
   
.. km:hotkey:: EVT_TWEAK_A -> node.translate_attach

   Move and Attach

   bpy.ops.node.translate_attach(TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False}, NODE_OT_attach={}, NODE_OT_insert_offset={})
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Translate     |N/A     |
   +--------------+--------+
   |Attach Nodes  |N/A     |
   +--------------+--------+
   |Insert Offset |N/A     |
   +--------------+--------+
   
   
.. km:hotkey:: EVT_TWEAK_S -> node.translate_attach

   Move and Attach

   bpy.ops.node.translate_attach(TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False}, NODE_OT_attach={}, NODE_OT_insert_offset={})
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Translate     |N/A     |
   +--------------+--------+
   |Attach Nodes  |N/A     |
   +--------------+--------+
   |Insert Offset |N/A     |
   +--------------+--------+
   
   
.. km:hotkey:: G -> transform.translate

   Translate

   bpy.ops.transform.translate(value=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
   +-------------------+--------+
   |Properties:        |Values: |
   +===================+========+
   |Confirm on Release |True    |
   +-------------------+--------+
   
   
.. km:hotkey:: EVT_TWEAK_A -> transform.translate

   Translate

   bpy.ops.transform.translate(value=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
   +-------------------+--------+
   |Properties:        |Values: |
   +===================+========+
   |Confirm on Release |True    |
   +-------------------+--------+
   
   
.. km:hotkey:: EVT_TWEAK_S -> transform.translate

   Translate

   bpy.ops.transform.translate(value=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
   +-------------------+--------+
   |Properties:        |Values: |
   +===================+========+
   |Confirm on Release |True    |
   +-------------------+--------+
   
   
.. km:hotkey:: R -> transform.rotate

   Rotate

   bpy.ops.transform.rotate(value=0, axis=(0, 0, 0), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, release_confirm=False)
   
   
.. km:hotkey:: S -> transform.resize

   Resize

   bpy.ops.transform.resize(value=(1, 1, 1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, release_confirm=False)
   
   
.. km:hotkey:: Alt-D -> node.move_detach_links

   Detach

   bpy.ops.node.move_detach_links(NODE_OT_links_detach={}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False}, NODE_OT_insert_offset={})
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Detach Links  |N/A     |
   +--------------+--------+
   |Translate     |N/A     |
   +--------------+--------+
   |Insert Offset |N/A     |
   +--------------+--------+
   
   
.. km:hotkey:: Alt-EVT_TWEAK_A -> node.move_detach_links_release

   Detach

   bpy.ops.node.move_detach_links_release(NODE_OT_links_detach={}, NODE_OT_translate_attach={"TRANSFORM_OT_translate":{"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False}, "NODE_OT_attach":{}, "NODE_OT_insert_offset":{}})
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Detach Links    |N/A     |
   +----------------+--------+
   |Move and Attach |N/A     |
   +----------------+--------+
   
   
.. km:hotkey:: Alt-EVT_TWEAK_S -> node.move_detach_links

   Detach

   bpy.ops.node.move_detach_links(NODE_OT_links_detach={}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False}, NODE_OT_insert_offset={})
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Detach Links  |N/A     |
   +--------------+--------+
   |Translate     |N/A     |
   +--------------+--------+
   |Insert Offset |N/A     |
   +--------------+--------+
   
   
.. km:hotkey:: Shift-Tab -> wm.context_toggle

   Context Toggle

   bpy.ops.wm.context_toggle(data_path="")
   
   
   +-------------------+-----------------------+
   |Properties:        |Values:                |
   +===================+=======================+
   |Context Attributes |tool_settings.use_snap |
   +-------------------+-----------------------+
   
   
.. km:hotkey:: Ctrl-Shift-Tab -> wm.context_menu_enum

   Context Enum Menu

   bpy.ops.wm.context_menu_enum(data_path="")
   
   
   +-------------------+--------------------------------+
   |Properties:        |Values:                         |
   +===================+================================+
   |Context Attributes |tool_settings.snap_node_element |
   +-------------------+--------------------------------+
   
   
