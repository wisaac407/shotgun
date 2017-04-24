****
Mesh
****

.. km:module:: mesh

   


---------------
Quick Reference
---------------

+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|Hotkey                                                                                       |Operator                                                     |
+=============================================================================================+=============================================================+
|:km:hk:`Ctrl-A <mesh->Ctrl-A->mesh.select_all>`                                              |:func:`blender:bpy.ops.mesh.select_all`                      |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-MIDDLEMOUSE <mesh->Ctrl-MIDDLEMOUSE->mesh.dupli_extrude_cursor>`                |:func:`blender:bpy.ops.mesh.dupli_extrude_cursor`            |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-MIDDLEMOUSE <mesh->Ctrl-Shift-MIDDLEMOUSE->mesh.dupli_extrude_cursor>`    |:func:`blender:bpy.ops.mesh.dupli_extrude_cursor`            |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`SELECTMOUSE <mesh->SELECTMOUSE->mesh.select_linked>`                                 |:func:`blender:bpy.ops.mesh.select_linked`                   |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-SELECTMOUSE <mesh->Shift-SELECTMOUSE->mesh.select_linked>`                     |:func:`blender:bpy.ops.mesh.select_linked`                   |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-R <mesh->Ctrl-R->mesh.loopcut_slide>`                                           |:func:`blender:bpy.ops.mesh.loopcut_slide`                   |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-R <mesh->Ctrl-Shift-R->mesh.offset_edge_loops_slide>`                     |:func:`blender:bpy.ops.mesh.offset_edge_loops_slide`         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`I <mesh->I->mesh.inset>`                                                             |:func:`blender:bpy.ops.mesh.inset`                           |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-P <mesh->Alt-P->mesh.poke>`                                                      |:func:`blender:bpy.ops.mesh.poke`                            |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-B <mesh->Ctrl-B->mesh.bevel>`                                                   |:func:`blender:bpy.ops.mesh.bevel`                           |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-B <mesh->Ctrl-Shift-B->mesh.bevel>`                                       |:func:`blender:bpy.ops.mesh.bevel`                           |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-SELECTMOUSE <mesh->Alt-SELECTMOUSE->mesh.loop_select>`                           |:func:`blender:bpy.ops.mesh.loop_select`                     |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-Alt-SELECTMOUSE <mesh->Shift-Alt-SELECTMOUSE->mesh.loop_select>`               |:func:`blender:bpy.ops.mesh.loop_select`                     |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Alt-SELECTMOUSE <mesh->Ctrl-Alt-SELECTMOUSE->mesh.edgering_select>`             |:func:`blender:bpy.ops.mesh.edgering_select`                 |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-SELECTMOUSE <mesh->Ctrl-Shift-Alt-SELECTMOUSE->mesh.edgering_select>` |:func:`blender:bpy.ops.mesh.edgering_select`                 |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-SELECTMOUSE <mesh->Ctrl-SELECTMOUSE->mesh.shortest_path_pick>`                  |:func:`blender:bpy.ops.mesh.shortest_path_pick`              |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-SELECTMOUSE <mesh->Ctrl-Shift-SELECTMOUSE->mesh.shortest_path_pick>`      |:func:`blender:bpy.ops.mesh.shortest_path_pick`              |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`A <mesh->A->mesh.select_all>`                                                        |:func:`blender:bpy.ops.mesh.select_all`                      |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-I <mesh->Ctrl-I->mesh.select_all>`                                              |:func:`blender:bpy.ops.mesh.select_all`                      |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_PLUS <mesh->Ctrl-NUMPAD_PLUS->mesh.select_more>`                         |:func:`blender:bpy.ops.mesh.select_more`                     |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-NUMPAD_MINUS <mesh->Ctrl-NUMPAD_MINUS->mesh.select_less>`                       |:func:`blender:bpy.ops.mesh.select_less`                     |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-NUMPAD_PLUS <mesh->Ctrl-Shift-NUMPAD_PLUS->mesh.select_next_item>`        |:func:`blender:bpy.ops.mesh.select_next_item`                |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-NUMPAD_MINUS <mesh->Ctrl-Shift-NUMPAD_MINUS->mesh.select_prev_item>`      |:func:`blender:bpy.ops.mesh.select_prev_item`                |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-M <mesh->Ctrl-Shift-Alt-M->mesh.select_non_manifold>`                 |:func:`blender:bpy.ops.mesh.select_non_manifold`             |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-L <mesh->Ctrl-L->mesh.select_linked>`                                           |:func:`blender:bpy.ops.mesh.select_linked`                   |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`L <mesh->L->mesh.select_linked_pick>`                                                |:func:`blender:bpy.ops.mesh.select_linked_pick`              |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-L <mesh->Shift-L->mesh.select_linked_pick>`                                    |:func:`blender:bpy.ops.mesh.select_linked_pick`              |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-Alt-F <mesh->Ctrl-Shift-Alt-F->mesh.faces_select_linked_flat>`            |:func:`blender:bpy.ops.mesh.faces_select_linked_flat`        |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-G <mesh->Shift-G->wm.call_menu>`                                               |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Tab <mesh->Ctrl-Tab->wm.call_menu>`                                             |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`H <mesh->H->mesh.hide>`                                                              |:func:`blender:bpy.ops.mesh.hide`                            |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-H <mesh->Shift-H->mesh.hide>`                                                  |:func:`blender:bpy.ops.mesh.hide`                            |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-H <mesh->Alt-H->mesh.reveal>`                                                    |:func:`blender:bpy.ops.mesh.reveal`                          |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-N <mesh->Ctrl-N->mesh.normals_make_consistent>`                                 |:func:`blender:bpy.ops.mesh.normals_make_consistent`         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-N <mesh->Ctrl-Shift-N->mesh.normals_make_consistent>`                     |:func:`blender:bpy.ops.mesh.normals_make_consistent`         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`E <mesh->E->view3d.edit_mesh_extrude_move_normal>`                                   |:func:`blender:bpy.ops.view3d.edit_mesh_extrude_move_normal` |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-E <mesh->Alt-E->wm.call_menu>`                                                   |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-E <mesh->Shift-E->transform.edge_crease>`                                      |:func:`blender:bpy.ops.transform.edge_crease`                |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-R <mesh->Alt-R->mesh.spin>`                                                      |:func:`blender:bpy.ops.mesh.spin`                            |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-F <mesh->Alt-F->mesh.fill>`                                                      |:func:`blender:bpy.ops.mesh.fill`                            |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-Alt-F <mesh->Shift-Alt-F->mesh.beautify_fill>`                                 |:func:`blender:bpy.ops.mesh.beautify_fill`                   |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-T <mesh->Ctrl-T->mesh.quads_convert_to_tris>`                                   |:func:`blender:bpy.ops.mesh.quads_convert_to_tris`           |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-T <mesh->Ctrl-Shift-T->mesh.quads_convert_to_tris>`                       |:func:`blender:bpy.ops.mesh.quads_convert_to_tris`           |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-J <mesh->Alt-J->mesh.tris_convert_to_quads>`                                     |:func:`blender:bpy.ops.mesh.tris_convert_to_quads`           |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`V <mesh->V->mesh.rip_move>`                                                          |:func:`blender:bpy.ops.mesh.rip_move`                        |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-V <mesh->Alt-V->mesh.rip_move_fill>`                                             |:func:`blender:bpy.ops.mesh.rip_move_fill`                   |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-D <mesh->Alt-D->mesh.rip_edge_move>`                                             |:func:`blender:bpy.ops.mesh.rip_edge_move`                   |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-M <mesh->Alt-M->mesh.merge>`                                                     |:func:`blender:bpy.ops.mesh.merge`                           |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-S <mesh->Alt-S->transform.shrink_fatten>`                                        |:func:`blender:bpy.ops.transform.shrink_fatten`              |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`F <mesh->F->mesh.edge_face_add>`                                                     |:func:`blender:bpy.ops.mesh.edge_face_add`                   |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-D <mesh->Shift-D->mesh.duplicate_move>`                                        |:func:`blender:bpy.ops.mesh.duplicate_move`                  |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-A <mesh->Shift-A->wm.call_menu>`                                               |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`P <mesh->P->mesh.separate>`                                                          |:func:`blender:bpy.ops.mesh.separate`                        |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Y <mesh->Y->mesh.split>`                                                             |:func:`blender:bpy.ops.mesh.split`                           |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`J <mesh->J->mesh.vert_connect_path>`                                                 |:func:`blender:bpy.ops.mesh.vert_connect_path`               |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-V <mesh->Shift-V->transform.vert_slide>`                                       |:func:`blender:bpy.ops.transform.vert_slide`                 |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-ACTIONMOUSE <mesh->Ctrl-ACTIONMOUSE->mesh.dupli_extrude_cursor>`                |:func:`blender:bpy.ops.mesh.dupli_extrude_cursor`            |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-Shift-ACTIONMOUSE <mesh->Ctrl-Shift-ACTIONMOUSE->mesh.dupli_extrude_cursor>`    |:func:`blender:bpy.ops.mesh.dupli_extrude_cursor`            |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`X <mesh->X->wm.call_menu>`                                                           |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`DEL <mesh->DEL->wm.call_menu>`                                                       |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-X <mesh->Ctrl-X->mesh.dissolve_mode>`                                           |:func:`blender:bpy.ops.mesh.dissolve_mode`                   |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-DEL <mesh->Ctrl-DEL->mesh.dissolve_mode>`                                       |:func:`blender:bpy.ops.mesh.dissolve_mode`                   |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`K <mesh->K->mesh.knife_tool>`                                                        |:func:`blender:bpy.ops.mesh.knife_tool`                      |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-K <mesh->Shift-K->mesh.knife_tool>`                                            |:func:`blender:bpy.ops.mesh.knife_tool`                      |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-P <mesh->Ctrl-P->object.vertex_parent_set>`                                     |:func:`blender:bpy.ops.object.vertex_parent_set`             |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`W <mesh->W->wm.call_menu>`                                                           |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-F <mesh->Ctrl-F->wm.call_menu>`                                                 |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-E <mesh->Ctrl-E->wm.call_menu>`                                                 |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-V <mesh->Ctrl-V->wm.call_menu>`                                                 |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-H <mesh->Ctrl-H->wm.call_menu>`                                                 |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`U <mesh->U->wm.call_menu>`                                                           |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-G <mesh->Ctrl-G->wm.call_menu>`                                                 |:func:`blender:bpy.ops.wm.call_menu`                         |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-0 <mesh->Ctrl-0->object.subdivision_set>`                                       |:func:`blender:bpy.ops.object.subdivision_set`               |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-1 <mesh->Ctrl-1->object.subdivision_set>`                                       |:func:`blender:bpy.ops.object.subdivision_set`               |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-2 <mesh->Ctrl-2->object.subdivision_set>`                                       |:func:`blender:bpy.ops.object.subdivision_set`               |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-3 <mesh->Ctrl-3->object.subdivision_set>`                                       |:func:`blender:bpy.ops.object.subdivision_set`               |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-4 <mesh->Ctrl-4->object.subdivision_set>`                                       |:func:`blender:bpy.ops.object.subdivision_set`               |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Ctrl-5 <mesh->Ctrl-5->object.subdivision_set>`                                       |:func:`blender:bpy.ops.object.subdivision_set`               |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Shift-O <mesh->Shift-O->wm.context_cycle_enum>`                                      |:func:`blender:bpy.ops.wm.context_cycle_enum`                |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`O <mesh->O->wm.context_toggle_enum>`                                                 |:func:`blender:bpy.ops.wm.context_toggle_enum`               |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+
|:km:hk:`Alt-O <mesh->Alt-O->wm.context_toggle_enum>`                                         |:func:`blender:bpy.ops.wm.context_toggle_enum`               |
+---------------------------------------------------------------------------------------------+-------------------------------------------------------------+


------------------
Detailed Reference
------------------

.. note:: Hotkeys marked with the "(default)" prefix are inherited from the default blender keymap

   

.. km:hotkey:: Ctrl-A -> mesh.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.mesh.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkey:: Ctrl-MIDDLEMOUSE -> mesh.dupli_extrude_cursor : MOUSE -> PRESS

   Duplicate or Extrude to Cursor

   bpy.ops.mesh.dupli_extrude_cursor(rotate_source=True)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Rotate Source |True    |
   +--------------+--------+
   
   
.. km:hotkey:: Ctrl-Shift-MIDDLEMOUSE -> mesh.dupli_extrude_cursor : MOUSE -> PRESS

   Duplicate or Extrude to Cursor

   bpy.ops.mesh.dupli_extrude_cursor(rotate_source=True)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Rotate Source |False   |
   +--------------+--------+
   
   
.. km:hotkey:: SELECTMOUSE -> mesh.select_linked : MOUSE -> DOUBLE_CLICK

   Select Linked All

   bpy.ops.mesh.select_linked(delimit={'SEAM'})
   
   
.. km:hotkey:: Shift-SELECTMOUSE -> mesh.select_linked : MOUSE -> DOUBLE_CLICK

   Select Linked All

   bpy.ops.mesh.select_linked(delimit={'SEAM'})
   
   
.. km:hotkeyd:: Ctrl-R -> mesh.loopcut_slide : KEYBOARD -> PRESS

   Loop Cut and Slide

   bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "edge_index":-1, "mesh_select_mode_init":(False, False, False)}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":False, "release_confirm":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Loop Cut    |N/A     |
   +------------+--------+
   |Edge Slide  |N/A     |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-R -> mesh.offset_edge_loops_slide : KEYBOARD -> PRESS

   Offset Edge Slide

   bpy.ops.mesh.offset_edge_loops_slide(MESH_OT_offset_edge_loops={"use_cap_endpoint":False}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":False, "release_confirm":False})
   
   
   +-----------------+--------+
   |Properties:      |Values: |
   +=================+========+
   |Offset Edge Loop |N/A     |
   +-----------------+--------+
   |Edge Slide       |N/A     |
   +-----------------+--------+
   
   
.. km:hotkeyd:: I -> mesh.inset : KEYBOARD -> PRESS

   Inset Faces

   bpy.ops.mesh.inset(use_boundary=True, use_even_offset=True, use_relative_offset=False, use_edge_rail=False, thickness=0.01, depth=0, use_outset=False, use_select_inset=False, use_individual=False, use_interpolate=True)
   
   
.. km:hotkeyd:: Alt-P -> mesh.poke : KEYBOARD -> PRESS

   Poke Faces

   bpy.ops.mesh.poke(offset=0, use_relative_offset=False, center_mode='MEAN_WEIGHTED')
   
   
.. km:hotkeyd:: Ctrl-B -> mesh.bevel : KEYBOARD -> PRESS

   Bevel

   bpy.ops.mesh.bevel(offset_type='OFFSET', offset=0, segments=1, profile=0.5, vertex_only=False, clamp_overlap=False, loop_slide=True, material=-1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Vertex Only |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-B -> mesh.bevel : KEYBOARD -> PRESS

   Bevel

   bpy.ops.mesh.bevel(offset_type='OFFSET', offset=0, segments=1, profile=0.5, vertex_only=False, clamp_overlap=False, loop_slide=True, material=-1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Vertex Only |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-SELECTMOUSE -> mesh.loop_select : MOUSE -> PRESS

   Loop Select

   bpy.ops.mesh.loop_select(extend=False, deselect=False, toggle=False, ring=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Deselect      |False   |
   +--------------+--------+
   |Toggle Select |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Shift-Alt-SELECTMOUSE -> mesh.loop_select : MOUSE -> PRESS

   Loop Select

   bpy.ops.mesh.loop_select(extend=False, deselect=False, toggle=False, ring=False)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend Select |False   |
   +--------------+--------+
   |Deselect      |False   |
   +--------------+--------+
   |Toggle Select |True    |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Alt-SELECTMOUSE -> mesh.edgering_select : MOUSE -> PRESS

   Edge Ring Select

   bpy.ops.mesh.edgering_select(extend=False, deselect=False, toggle=False, ring=True)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend        |False   |
   +--------------+--------+
   |Deselect      |False   |
   +--------------+--------+
   |Toggle Select |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-Alt-SELECTMOUSE -> mesh.edgering_select : MOUSE -> PRESS

   Edge Ring Select

   bpy.ops.mesh.edgering_select(extend=False, deselect=False, toggle=False, ring=True)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Extend        |False   |
   +--------------+--------+
   |Deselect      |False   |
   +--------------+--------+
   |Toggle Select |True    |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-SELECTMOUSE -> mesh.shortest_path_pick : MOUSE -> PRESS

   Pick Shortest Path

   bpy.ops.mesh.shortest_path_pick(use_face_step=False, use_topology_distance=False, use_fill=False, nth=1, skip=1, offset=0, index=-1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Fill Region |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-SELECTMOUSE -> mesh.shortest_path_pick : MOUSE -> PRESS

   Pick Shortest Path

   bpy.ops.mesh.shortest_path_pick(use_face_step=False, use_topology_distance=False, use_fill=False, nth=1, skip=1, offset=0, index=-1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Fill Region |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: A -> mesh.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.mesh.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |TOGGLE  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-I -> mesh.select_all : KEYBOARD -> PRESS

   (De)select All

   bpy.ops.mesh.select_all(action='TOGGLE')
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Action      |INVERT  |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_PLUS -> mesh.select_more : KEYBOARD -> PRESS

   Select More

   bpy.ops.mesh.select_more(use_face_step=True)
   
   
.. km:hotkeyd:: Ctrl-NUMPAD_MINUS -> mesh.select_less : KEYBOARD -> PRESS

   Select Less

   bpy.ops.mesh.select_less(use_face_step=True)
   
   
.. km:hotkeyd:: Ctrl-Shift-NUMPAD_PLUS -> mesh.select_next_item : KEYBOARD -> PRESS

   Select Next Element

   bpy.ops.mesh.select_next_item()
   
   
.. km:hotkeyd:: Ctrl-Shift-NUMPAD_MINUS -> mesh.select_prev_item : KEYBOARD -> PRESS

   Select Previous Element

   bpy.ops.mesh.select_prev_item()
   
   
.. km:hotkeyd:: Ctrl-Shift-Alt-M -> mesh.select_non_manifold : KEYBOARD -> PRESS

   Select Non Manifold

   bpy.ops.mesh.select_non_manifold(extend=True, use_wire=True, use_boundary=True, use_multi_face=True, use_non_contiguous=True, use_verts=True)
   
   
.. km:hotkeyd:: Ctrl-L -> mesh.select_linked : KEYBOARD -> PRESS

   Select Linked All

   bpy.ops.mesh.select_linked(delimit={'SEAM'})
   
   
.. km:hotkeyd:: L -> mesh.select_linked_pick : KEYBOARD -> PRESS

   Select Linked

   bpy.ops.mesh.select_linked_pick(deselect=False, delimit={'SEAM'}, index=-1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-L -> mesh.select_linked_pick : KEYBOARD -> PRESS

   Select Linked

   bpy.ops.mesh.select_linked_pick(deselect=False, delimit={'SEAM'}, index=-1)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Deselect    |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-Alt-F -> mesh.faces_select_linked_flat : KEYBOARD -> PRESS

   Select Linked Flat Faces

   bpy.ops.mesh.faces_select_linked_flat(sharpness=0.0174533)
   
   
.. km:hotkeyd:: Shift-G -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------------------------+
   |Properties: |Values:                            |
   +============+===================================+
   |Name        |VIEW3D_MT_edit_mesh_select_similar |
   +------------+-----------------------------------+
   
   
.. km:hotkeyd:: Ctrl-Tab -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+--------------------------------+
   |Properties: |Values:                         |
   +============+================================+
   |Name        |VIEW3D_MT_edit_mesh_select_mode |
   +------------+--------------------------------+
   
   
.. km:hotkeyd:: H -> mesh.hide : KEYBOARD -> PRESS

   Hide Selection

   bpy.ops.mesh.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-H -> mesh.hide : KEYBOARD -> PRESS

   Hide Selection

   bpy.ops.mesh.hide(unselected=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Unselected  |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-H -> mesh.reveal : KEYBOARD -> PRESS

   Reveal Hidden

   bpy.ops.mesh.reveal()
   
   
.. km:hotkeyd:: Ctrl-N -> mesh.normals_make_consistent : KEYBOARD -> PRESS

   Make Normals Consistent

   bpy.ops.mesh.normals_make_consistent(inside=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Inside      |False   |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-N -> mesh.normals_make_consistent : KEYBOARD -> PRESS

   Make Normals Consistent

   bpy.ops.mesh.normals_make_consistent(inside=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Inside      |True    |
   +------------+--------+
   
   
.. km:hotkeyd:: E -> view3d.edit_mesh_extrude_move_normal : KEYBOARD -> PRESS

   Extrude and Move on Normals

   bpy.ops.view3d.edit_mesh_extrude_move_normal()
   
   
.. km:hotkeyd:: Alt-E -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+----------------------------+
   |Properties: |Values:                     |
   +============+============================+
   |Name        |VIEW3D_MT_edit_mesh_extrude |
   +------------+----------------------------+
   
   
.. km:hotkeyd:: Shift-E -> transform.edge_crease : KEYBOARD -> PRESS

   Edge Crease

   bpy.ops.transform.edge_crease(value=0, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
   
   
.. km:hotkeyd:: Alt-R -> mesh.spin : KEYBOARD -> PRESS

   Spin

   bpy.ops.mesh.spin(steps=9, dupli=False, angle=1.5708, center=(0, 0, 0), axis=(0, 0, 0))
   
   
.. km:hotkeyd:: Alt-F -> mesh.fill : KEYBOARD -> PRESS

   Fill

   bpy.ops.mesh.fill(use_beauty=True)
   
   
.. km:hotkeyd:: Shift-Alt-F -> mesh.beautify_fill : KEYBOARD -> PRESS

   Beautify Faces

   bpy.ops.mesh.beautify_fill(angle_limit=3.14159)
   
   
.. km:hotkeyd:: Ctrl-T -> mesh.quads_convert_to_tris : KEYBOARD -> PRESS

   Triangulate Faces

   bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Quad Method    |BEAUTY  |
   +---------------+--------+
   |Polygon Method |BEAUTY  |
   +---------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-T -> mesh.quads_convert_to_tris : KEYBOARD -> PRESS

   Triangulate Faces

   bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
   
   
   +---------------+--------+
   |Properties:    |Values: |
   +===============+========+
   |Quad Method    |FIXED   |
   +---------------+--------+
   |Polygon Method |CLIP    |
   +---------------+--------+
   
   
.. km:hotkeyd:: Alt-J -> mesh.tris_convert_to_quads : KEYBOARD -> PRESS

   Tris to Quads

   bpy.ops.mesh.tris_convert_to_quads(face_threshold=0.698132, shape_threshold=0.698132, uvs=False, vcols=False, seam=False, sharp=False, materials=False)
   
   
.. km:hotkeyd:: V -> mesh.rip_move : KEYBOARD -> PRESS

   Rip

   bpy.ops.mesh.rip_move(MESH_OT_rip={"mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "release_confirm":False, "use_fill":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Rip         |N/A     |
   +------------+--------+
   |Translate   |N/A     |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-V -> mesh.rip_move_fill : KEYBOARD -> PRESS

   Rip Fill

   bpy.ops.mesh.rip_move_fill(MESH_OT_rip={"mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "release_confirm":False, "use_fill":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Rip         |N/A     |
   +------------+--------+
   |Translate   |N/A     |
   +------------+--------+
   
   
.. km:hotkeyd:: Alt-D -> mesh.rip_edge_move : KEYBOARD -> PRESS

   Extend Vertices

   bpy.ops.mesh.rip_edge_move(MESH_OT_rip_edge={"mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "release_confirm":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +----------------+--------+
   |Properties:     |Values: |
   +================+========+
   |Extend Vertices |N/A     |
   +----------------+--------+
   |Translate       |N/A     |
   +----------------+--------+
   
   
.. km:hotkeyd:: Alt-M -> mesh.merge : KEYBOARD -> PRESS

   Merge

   bpy.ops.mesh.merge(type='CENTER', uvs=False)
   
   
.. km:hotkeyd:: Alt-S -> transform.shrink_fatten : KEYBOARD -> PRESS

   Shrink/Fatten

   bpy.ops.transform.shrink_fatten(value=0, use_even_offset=True, mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
   
   
.. km:hotkeyd:: F -> mesh.edge_face_add : KEYBOARD -> PRESS

   Make Edge/Face

   bpy.ops.mesh.edge_face_add()
   
   
.. km:hotkeyd:: Shift-D -> mesh.duplicate_move : KEYBOARD -> PRESS

   Add Duplicate

   bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, False), "constraint_orientation":'GLOBAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Duplicate   |N/A     |
   +------------+--------+
   |Translate   |N/A     |
   +------------+--------+
   
   
.. km:hotkeyd:: Shift-A -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------+
   |Properties: |Values:          |
   +============+=================+
   |Name        |INFO_MT_mesh_add |
   +------------+-----------------+
   
   
.. km:hotkeyd:: P -> mesh.separate : KEYBOARD -> PRESS

   Separate

   bpy.ops.mesh.separate(type='SELECTED')
   
   
.. km:hotkeyd:: Y -> mesh.split : KEYBOARD -> PRESS

   Split

   bpy.ops.mesh.split()
   
   
.. km:hotkeyd:: J -> mesh.vert_connect_path : KEYBOARD -> PRESS

   Vertex Connect Path

   bpy.ops.mesh.vert_connect_path()
   
   
.. km:hotkeyd:: Shift-V -> transform.vert_slide : KEYBOARD -> PRESS

   Vertex Slide

   bpy.ops.transform.vert_slide(value=0, use_even=False, flipped=False, use_clamp=True, mirror=False, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), correct_uv=False, release_confirm=False)
   
   
.. km:hotkeyd:: Ctrl-ACTIONMOUSE -> mesh.dupli_extrude_cursor : MOUSE -> CLICK

   Duplicate or Extrude to Cursor

   bpy.ops.mesh.dupli_extrude_cursor(rotate_source=True)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Rotate Source |True    |
   +--------------+--------+
   
   
.. km:hotkeyd:: Ctrl-Shift-ACTIONMOUSE -> mesh.dupli_extrude_cursor : MOUSE -> CLICK

   Duplicate or Extrude to Cursor

   bpy.ops.mesh.dupli_extrude_cursor(rotate_source=True)
   
   
   +--------------+--------+
   |Properties:   |Values: |
   +==============+========+
   |Rotate Source |False   |
   +--------------+--------+
   
   
.. km:hotkeyd:: X -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------------------+
   |Properties: |Values:                    |
   +============+===========================+
   |Name        |VIEW3D_MT_edit_mesh_delete |
   +------------+---------------------------+
   
   
.. km:hotkeyd:: DEL -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------------------+
   |Properties: |Values:                    |
   +============+===========================+
   |Name        |VIEW3D_MT_edit_mesh_delete |
   +------------+---------------------------+
   
   
.. km:hotkeyd:: Ctrl-X -> mesh.dissolve_mode : KEYBOARD -> PRESS

   Dissolve Selection

   bpy.ops.mesh.dissolve_mode(use_verts=False, use_face_split=False, use_boundary_tear=False)
   
   
.. km:hotkeyd:: Ctrl-DEL -> mesh.dissolve_mode : KEYBOARD -> PRESS

   Dissolve Selection

   bpy.ops.mesh.dissolve_mode(use_verts=False, use_face_split=False, use_boundary_tear=False)
   
   
.. km:hotkeyd:: K -> mesh.knife_tool : KEYBOARD -> PRESS

   Knife Topology Tool

   bpy.ops.mesh.knife_tool(use_occlude_geometry=True, only_selected=False)
   
   
   +-----------------+--------+
   |Properties:      |Values: |
   +=================+========+
   |Occlude Geometry |True    |
   +-----------------+--------+
   |Only Selected    |False   |
   +-----------------+--------+
   
   
.. km:hotkeyd:: Shift-K -> mesh.knife_tool : KEYBOARD -> PRESS

   Knife Topology Tool

   bpy.ops.mesh.knife_tool(use_occlude_geometry=True, only_selected=False)
   
   
   +-----------------+--------+
   |Properties:      |Values: |
   +=================+========+
   |Occlude Geometry |False   |
   +-----------------+--------+
   |Only Selected    |True    |
   +-----------------+--------+
   
   
.. km:hotkeyd:: Ctrl-P -> object.vertex_parent_set : KEYBOARD -> PRESS

   Make Vertex Parent

   bpy.ops.object.vertex_parent_set()
   
   
.. km:hotkeyd:: W -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------------------+
   |Properties: |Values:                      |
   +============+=============================+
   |Name        |VIEW3D_MT_edit_mesh_specials |
   +------------+-----------------------------+
   
   
.. km:hotkeyd:: Ctrl-F -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+--------------------------+
   |Properties: |Values:                   |
   +============+==========================+
   |Name        |VIEW3D_MT_edit_mesh_faces |
   +------------+--------------------------+
   
   
.. km:hotkeyd:: Ctrl-E -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+--------------------------+
   |Properties: |Values:                   |
   +============+==========================+
   |Name        |VIEW3D_MT_edit_mesh_edges |
   +------------+--------------------------+
   
   
.. km:hotkeyd:: Ctrl-V -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------------------+
   |Properties: |Values:                      |
   +============+=============================+
   |Name        |VIEW3D_MT_edit_mesh_vertices |
   +------------+-----------------------------+
   
   
.. km:hotkeyd:: Ctrl-H -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+---------------+
   |Properties: |Values:        |
   +============+===============+
   |Name        |VIEW3D_MT_hook |
   +------------+---------------+
   
   
.. km:hotkeyd:: U -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------+
   |Properties: |Values:          |
   +============+=================+
   |Name        |VIEW3D_MT_uv_map |
   +------------+-----------------+
   
   
.. km:hotkeyd:: Ctrl-G -> wm.call_menu : KEYBOARD -> PRESS

   Call Menu

   bpy.ops.wm.call_menu(name="")
   
   
   +------------+-----------------------+
   |Properties: |Values:                |
   +============+=======================+
   |Name        |VIEW3D_MT_vertex_group |
   +------------+-----------------------+
   
   
.. km:hotkeyd:: Ctrl-0 -> object.subdivision_set : KEYBOARD -> PRESS

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |0       |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-1 -> object.subdivision_set : KEYBOARD -> PRESS

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |1       |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-2 -> object.subdivision_set : KEYBOARD -> PRESS

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |2       |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-3 -> object.subdivision_set : KEYBOARD -> PRESS

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |3       |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-4 -> object.subdivision_set : KEYBOARD -> PRESS

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |4       |
   +------------+--------+
   
   
.. km:hotkeyd:: Ctrl-5 -> object.subdivision_set : KEYBOARD -> PRESS

   Subdivision Set

   bpy.ops.object.subdivision_set(level=1, relative=False)
   
   
   +------------+--------+
   |Properties: |Values: |
   +============+========+
   |Level       |5       |
   +------------+--------+
   
   
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
   
   
