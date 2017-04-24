import bpy
import os


def full_compare(a, b):
    """Check if a and b are exactly equal keymap items."""
    for prop in ['idname', 'type',  'value',  'any', 'shift', 'ctrl', 'alt', 'oskey', 'key_modifier']:
        if getattr(a, prop, None) != getattr(b, prop, None):
            return False
    # At this point they are probably the same but let's check all the properties too
    for prop in a.properties.keys():
        # Pointer properties are set when the operator is run
        if a.properties.rna_type.properties[prop].type != 'POINTER':
            if getattr(a.properties, prop, None) != getattr(b.properties, prop, None):
                return False
    return True


default_hotkeys = {}
class KeyMap:
    def __init__(self, kc, name, space_type, region_type, modal, use_trash=False):
        self.km = kc.keymaps.new(name, space_type=space_type, region_type=region_type, modal=modal)
        self.kc = kc

        self._use_trash = use_trash
        if self._use_trash:
            self.trash = kc.keymaps.new('trash')

    def __enter__(self):
        if self._use_trash:
            return self.km, self.trash
        return self.km

    def __exit__(self, exc_type, exc_val, exc_tb):
        wm = bpy.context.window_manager
        dkm = wm.keyconfigs.default.keymaps[self.km.name]

        # Add all the default blender keymap items
        # Because they are getting added last the previous hotkeys will override them
        for k in dkm.keymap_items:
            # Skip adding this keymap item if it's in the trash keymap
            if self._use_trash:
                skip_kmi = False
                for tkmi in self.trash.keymap_items:
                    if full_compare(tkmi, k):
                        skip_kmi = True
                        break
                if skip_kmi:
                    continue

            kmi = self.km.keymap_items.new(k.idname, k.type, k.value, any=k.any, shift=k.shift, ctrl=k.ctrl,
                                           alt=k.alt, oskey=k.oskey)
            for prop in k.properties.keys():
                # Pointer properties are set when the operator is run
                if k.properties.rna_type.properties[prop].type != 'POINTER':
                    kmi_props_setattr(kmi.properties, prop, getattr(k.properties, prop))

            # Keep track of the default keymap items for use in documentation.
            default_hotkeys.setdefault(self.km.name, []).append(kmi)

        # Delete the trash keymap
        if self._use_trash:
            self.kc.keymaps.remove(self.trash)


def kmi_props_setattr(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except AttributeError:
        print("Warning: property '%s' not found in keymap item '%s'" %
              (attr, kmi_props.__class__.__name__))
    except Exception as e:
        print("Warning: %r" % e)


wm = bpy.context.window_manager
kc = wm.keyconfigs.new(os.path.splitext(os.path.basename(__file__))[0])

# Map UV Editor
with KeyMap(kc, 'UV Editor', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('uv.select_border', 'B', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'pinned', True)

    kmi = km.keymap_items.new('uv.select_lasso', 'EVT_TWEAK_S', 'ANY', ctrl=True)
    kmi_props_setattr(kmi.properties, 'deselect', False)

    kmi = km.keymap_items.new('uv.select_lasso', 'EVT_TWEAK_S', 'ANY', shift=True, ctrl=True)
    kmi_props_setattr(kmi.properties, 'deselect', True)

    kmi = km.keymap_items.new('uv.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('uv.cursor_set', 'ACTIONMOUSE', 'PRESS', ctrl=True)

# Map Mask Editing
with KeyMap(kc, 'Mask Editing', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('mask.add_vertex_slide', 'SELECTMOUSE', 'PRESS', ctrl=True)

    kmi = km.keymap_items.new('mask.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('mask.select_lasso', 'EVT_TWEAK_S', 'ANY', ctrl=True, alt=True)
    kmi_props_setattr(kmi.properties, 'deselect', False)

    kmi = km.keymap_items.new('mask.select_lasso', 'EVT_TWEAK_S', 'ANY', shift=True, ctrl=True, alt=True)
    kmi_props_setattr(kmi.properties, 'deselect', True)

    kmi = km.keymap_items.new('mask.slide_point', 'SELECTMOUSE', 'PRESS')
    kmi.active = False

    kmi = km.keymap_items.new('mask.slide_spline_curvature', 'SELECTMOUSE', 'PRESS')

    kmi = km.keymap_items.new('uv.cursor_set', 'ACTIONMOUSE', 'PRESS', ctrl=True)

# Map File Browser Main
with KeyMap(kc, 'File Browser Main', space_type='FILE_BROWSER', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('file.select', 'LEFTMOUSE', 'CLICK', alt=True)
    kmi_props_setattr(kmi.properties, 'extend', True)
    kmi_props_setattr(kmi.properties, 'fill', True)

    kmi = km.keymap_items.new('file.select_all_toggle', 'A', 'PRESS', ctrl=True)

# Map Clip Editor
with KeyMap(kc, 'Clip Editor', space_type='CLIP_EDITOR', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('clip.view_pan', 'ACTIONMOUSE', 'PRESS')

    kmi = km.keymap_items.new('clip.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('clip.select_lasso', 'EVT_TWEAK_S', 'ANY', ctrl=True, alt=True)
    kmi_props_setattr(kmi.properties, 'deselect', False)

    kmi = km.keymap_items.new('clip.select_lasso', 'EVT_TWEAK_S', 'ANY', shift=True, ctrl=True, alt=True)
    kmi_props_setattr(kmi.properties, 'deselect', True)

    kmi = km.keymap_items.new('clip.cursor_set', 'ACTIONMOUSE', 'PRESS', ctrl=True)

# Map Clip Graph Editor
with KeyMap(kc, 'Clip Graph Editor', space_type='CLIP_EDITOR', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('clip.change_frame', 'SELECTMOUSE', 'PRESS', ctrl=True)

    kmi = km.keymap_items.new('clip.graph_select_all_markers', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('clip.graph_select_border', 'EVT_TWEAK_L', 'ANY', any=True)

# Map Clip Dopesheet Editor
with KeyMap(kc, 'Clip Dopesheet Editor', space_type='CLIP_EDITOR', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('clip.dopesheet_select_channel', 'SELECTMOUSE', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'extend', True)

# Map Outliner
with KeyMap(kc, 'Outliner', space_type='OUTLINER', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('outliner.selected_toggle', 'A', 'PRESS', ctrl=True)

# Map Graph Editor
with KeyMap(kc, 'Graph Editor', space_type='GRAPH_EDITOR', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('wm.context_set_enum', 'TAB', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
    kmi_props_setattr(kmi.properties, 'value', 'DOPESHEET_EDITOR')

    kmi = km.keymap_items.new('graph.cursor_set', 'SELECTMOUSE', 'DOUBLE_CLICK')

    kmi = km.keymap_items.new('graph.select_leftright', 'SELECTMOUSE', 'PRESS', alt=True)
    kmi_props_setattr(kmi.properties, 'mode', 'CHECK')
    kmi_props_setattr(kmi.properties, 'extend', False)

    kmi = km.keymap_items.new('graph.select_leftright', 'SELECTMOUSE', 'PRESS', shift=True, alt=True)
    kmi_props_setattr(kmi.properties, 'mode', 'CHECK')
    kmi_props_setattr(kmi.properties, 'extend', True)

    kmi = km.keymap_items.new('graph.select_all_toggle', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'invert', False)

    kmi = km.keymap_items.new('graph.select_lasso', 'EVT_TWEAK_S', 'ANY', ctrl=True)
    kmi_props_setattr(kmi.properties, 'deselect', False)

    kmi = km.keymap_items.new('graph.select_lasso', 'EVT_TWEAK_S', 'ANY', shift=True, ctrl=True)
    kmi_props_setattr(kmi.properties, 'deselect', True)

    kmi = km.keymap_items.new('graph.clean', 'O', 'PRESS')

    kmi = km.keymap_items.new('graph.delete', 'X', 'PRESS')

    kmi = km.keymap_items.new('graph.delete', 'DEL', 'PRESS')

    kmi = km.keymap_items.new('graph.click_insert', 'SELECTMOUSE', 'CLICK', ctrl=True)

# Map 3D View
with KeyMap(kc, '3D View', space_type='VIEW_3D', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('view3d.cursor3d', 'ACTIONMOUSE', 'PRESS', ctrl=True)

    kmi = km.keymap_items.new('view3d.move', 'RIGHTMOUSE', 'PRESS')

    kmi = km.keymap_items.new('view3d.select_lasso', 'EVT_TWEAK_A', 'ANY', alt=True)
    kmi_props_setattr(kmi.properties, 'deselect', False)

    kmi = km.keymap_items.new('view3d.select_lasso', 'EVT_TWEAK_A', 'ANY', alt=True, shift=True)
    kmi_props_setattr(kmi.properties, 'deselect', True)

    kmi = km.keymap_items.new('transform.skin_resize', 'A', 'PRESS')

    kmi = km.keymap_items.new('object.select_grouped', 'SELECTMOUSE', 'DOUBLE_CLICK')
    kmi_props_setattr(kmi.properties, 'type', 'GROUP')

    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_S', 'ANY', alt=True)
    kmi_props_setattr(kmi.properties, 'extend', False)

    kmi = km.keymap_items.new('view3d.select_border', 'EVT_TWEAK_S', 'ANY', alt=True, shift=True)
    kmi_props_setattr(kmi.properties, 'extend', True)

# Map Face Mask
with KeyMap(kc, 'Face Mask', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('paint.face_select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

# Map Weight Paint Vertex Selection
with KeyMap(kc, 'Weight Paint Vertex Selection', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('paint.vert_select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('view3d.select_lasso', 'EVT_TWEAK_S', 'ANY', ctrl=True)
    kmi_props_setattr(kmi.properties, 'deselect', False)

    kmi = km.keymap_items.new('view3d.select_lasso', 'EVT_TWEAK_S', 'ANY', shift=True, ctrl=True)
    kmi_props_setattr(kmi.properties, 'deselect', True)

# Map Pose
with KeyMap(kc, 'Pose', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS')
    kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_pose_apply')

    kmi = km.keymap_items.new('pose.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('pose.select_mirror', 'F', 'PRESS', shift=True)

# Map Object Mode
with KeyMap(kc, 'Object Mode', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('object.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS')
    kmi_props_setattr(kmi.properties, 'name', 'VIEW3D_MT_object_apply')

# Map Curve
with KeyMap(kc, 'Curve', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('curve.vertex_add', 'SELECTMOUSE', 'CLICK', ctrl=True)

    kmi = km.keymap_items.new('curve.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('curve.delete', 'X', 'PRESS')

    kmi = km.keymap_items.new('curve.delete', 'DEL', 'PRESS')

# Map Metaball
with KeyMap(kc, 'Metaball', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('mball.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

# Map Lattice
with KeyMap(kc, 'Lattice', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('lattice.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

# Map Particle
with KeyMap(kc, 'Particle', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('particle.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

# Map Node Editor
with KeyMap(kc, 'Node Editor', space_type='NODE_EDITOR', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('wm.call_menu', 'EQUAL', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'name', 'NODE_MT_nw_node_align_menu')

    kmi = km.keymap_items.new('node.select_lasso', 'EVT_TWEAK_S', 'ANY', ctrl=True, alt=True)
    kmi_props_setattr(kmi.properties, 'deselect', False)

    kmi = km.keymap_items.new('node.backimage_sample', 'SELECTMOUSE', 'PRESS', alt=True)

    kmi = km.keymap_items.new('node.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('node.group_edit', 'TAB', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'exit', True)

    kmi = km.keymap_items.new('node.detach_translate_attach', 'F', 'PRESS', alt=True)

# Map Timeline
with KeyMap(kc, 'Timeline', space_type='TIMELINE', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('anim.change_frame', 'LEFTMOUSE', 'PRESS')

# Map Mesh
with KeyMap(kc, 'Mesh', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('mesh.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('mesh.select_similar', 'G', 'PRESS', shift=True)

    kmi = km.keymap_items.new('mesh.vert_connect', 'J', 'PRESS')

    kmi = km.keymap_items.new('mesh.dupli_extrude_cursor', 'SELECTMOUSE', 'CLICK', ctrl=True)
    kmi_props_setattr(kmi.properties, 'rotate_source', True)

    kmi = km.keymap_items.new('mesh.dupli_extrude_cursor', 'SELECTMOUSE', 'CLICK', shift=True, ctrl=True)
    kmi_props_setattr(kmi.properties, 'rotate_source', False)

# Map Armature
with KeyMap(kc, 'Armature', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('armature.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('armature.delete', 'X', 'PRESS')

    kmi = km.keymap_items.new('armature.delete', 'DEL', 'PRESS')

    kmi = km.keymap_items.new('armature.click_extrude', 'SELECTMOUSE', 'CLICK', ctrl=True)

    kmi = km.keymap_items.new('armature.separate', 'P', 'PRESS', ctrl=True, alt=True)

# Map View2D
with KeyMap(kc, 'View2D', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('view2d.pan', 'MIDDLEMOUSE', 'ANY')

    kmi = km.keymap_items.new('view2d.pan', 'ACTIONMOUSE', 'ANY')
    kmi.active = False

# Map Image Paint
with KeyMap(kc, 'Image Paint', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('wm.context_menu_enum', 'R', 'PRESS')
    kmi_props_setattr(kmi.properties, 'data_path', 'tool_settings.image_paint.brush.texture_angle_source_random')

# Map Sequencer
with KeyMap(kc, 'Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('sequencer.select_all', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'action', 'TOGGLE')

    kmi = km.keymap_items.new('view2d.pan', 'RIGHTMOUSE', 'PRESS')

# Map Animation
with KeyMap(kc, 'Animation', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('anim.change_frame', 'SELECTMOUSE', 'DOUBLE_CLICK')

# Map Image
with KeyMap(kc, 'Image', space_type='IMAGE_EDITOR', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('image.view_all', 'F', 'PRESS')
    kmi_props_setattr(kmi.properties, 'fit_view', True)

    kmi = km.keymap_items.new('image.view_pan', 'ACTIONMOUSE', 'PRESS')

    kmi = km.keymap_items.new('image.sample', 'SELECTMOUSE', 'PRESS')

# Map Markers
with KeyMap(kc, 'Markers', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('marker.move', 'EVT_TWEAK_S', 'ANY', alt=True)

    kmi = km.keymap_items.new('marker.select_all', 'A', 'PRESS', ctrl=True)

# Map Animation Channels
with KeyMap(kc, 'Animation Channels', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('anim.channels_select_all_toggle', 'A', 'PRESS', ctrl=True)

# Map Info
with KeyMap(kc, 'Info', space_type='INFO', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('info.select_all_toggle', 'A', 'PRESS', ctrl=True)

# Map Dopesheet
with KeyMap(kc, 'Dopesheet', space_type='DOPESHEET_EDITOR', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('wm.context_toggle_enum', 'TAB', 'PRESS', shift=True)
    kmi_props_setattr(kmi.properties, 'data_path', 'space_data.mode')
    kmi_props_setattr(kmi.properties, 'value_1', 'ACTION')
    kmi_props_setattr(kmi.properties, 'value_2', 'DOPESHEET')

    kmi = km.keymap_items.new('wm.context_set_enum', 'TAB', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'data_path', 'area.type')
    kmi_props_setattr(kmi.properties, 'value', 'GRAPH_EDITOR')

    kmi = km.keymap_items.new('action.select_all_toggle', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'invert', False)

    kmi = km.keymap_items.new('action.clean', 'O', 'PRESS')

    kmi = km.keymap_items.new('action.delete', 'X', 'PRESS')

    kmi = km.keymap_items.new('action.delete', 'DEL', 'PRESS')

# Map NLA Editor
with KeyMap(kc, 'NLA Editor', space_type='NLA_EDITOR', region_type='WINDOW', modal=False) as km:
    kmi = km.keymap_items.new('nla.select_all_toggle', 'A', 'PRESS', ctrl=True)
    kmi_props_setattr(kmi.properties, 'invert', False)

    kmi = km.keymap_items.new('nla.apply_scale', 'A', 'PRESS')
