import bpy
import os


class KeyMap:
    def __init__(self, kc, name, space_type, region_type, modal):
        self.km = kc.keymaps.new(name, space_type=space_type, region_type=region_type, modal=modal)

    def __enter__(self):
        return self.km

    def __exit__(self, exc_type, exc_val, exc_tb):
        wm = bpy.context.window_manager
        dkm = wm.keyconfigs.default.keymaps[self.km.name]

        # Add all the default blender keymap items that don't conflict with the new keymap items
        for k in dkm.keymap_items:
            for k2 in self.km.keymap_items:
                if k.compare(k2):
                    break
            else:
                kmi = self.km.keymap_items.new(k.idname, k.type, k.value, any=k.any, shift=k.shift, ctrl=k.ctrl,
                                               alt=k.alt, oskey=k.oskey)
                for prop, val in k.properties.items():
                    kmi_props_setattr(kmi.properties, prop, val)


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
    pass

# Map Mask Editing
with KeyMap(kc, 'Mask Editing', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map File Browser Main
with KeyMap(kc, 'File Browser Main', space_type='FILE_BROWSER', region_type='WINDOW', modal=False) as km:
    pass

# Map SequencerPreview
with KeyMap(kc, 'SequencerPreview', space_type='SEQUENCE_EDITOR', region_type='WINDOW', modal=False) as km:
    pass

# Map Clip Editor
with KeyMap(kc, 'Clip Editor', space_type='CLIP_EDITOR', region_type='WINDOW', modal=False) as km:
    pass

# Map Clip Graph Editor
with KeyMap(kc, 'Clip Graph Editor', space_type='CLIP_EDITOR', region_type='WINDOW', modal=False) as km:
    pass

# Map Clip Dopesheet Editor
with KeyMap(kc, 'Clip Dopesheet Editor', space_type='CLIP_EDITOR', region_type='WINDOW', modal=False) as km:
    pass

# Map Outliner
with KeyMap(kc, 'Outliner', space_type='OUTLINER', region_type='WINDOW', modal=False) as km:
    pass

# Map Graph Editor
with KeyMap(kc, 'Graph Editor', space_type='GRAPH_EDITOR', region_type='WINDOW', modal=False) as km:
    pass

# Map 3D View
with KeyMap(kc, '3D View', space_type='VIEW_3D', region_type='WINDOW', modal=False) as km:
    pass

# Map Face Mask
with KeyMap(kc, 'Face Mask', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Weight Paint Vertex Selection
with KeyMap(kc, 'Weight Paint Vertex Selection', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Pose
with KeyMap(kc, 'Pose', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Object Mode
with KeyMap(kc, 'Object Mode', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Curve
with KeyMap(kc, 'Curve', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Metaball
with KeyMap(kc, 'Metaball', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Lattice
with KeyMap(kc, 'Lattice', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Particle
with KeyMap(kc, 'Particle', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Node Editor
with KeyMap(kc, 'Node Editor', space_type='NODE_EDITOR', region_type='WINDOW', modal=False) as km:
    pass

# Map Timeline
with KeyMap(kc, 'Timeline', space_type='TIMELINE', region_type='WINDOW', modal=False) as km:
    pass

# Map Mesh
with KeyMap(kc, 'Mesh', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Armature
with KeyMap(kc, 'Armature', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map View2D
with KeyMap(kc, 'View2D', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Image Paint
with KeyMap(kc, 'Image Paint', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Sequencer
with KeyMap(kc, 'Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW', modal=False) as km:
    pass

# Map Animation
with KeyMap(kc, 'Animation', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Image
with KeyMap(kc, 'Image', space_type='IMAGE_EDITOR', region_type='WINDOW', modal=False) as km:
    pass

# Map Markers
with KeyMap(kc, 'Markers', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Animation Channels
with KeyMap(kc, 'Animation Channels', space_type='EMPTY', region_type='WINDOW', modal=False) as km:
    pass

# Map Info
with KeyMap(kc, 'Info', space_type='INFO', region_type='WINDOW', modal=False) as km:
    pass

# Map Dopesheet
with KeyMap(kc, 'Dopesheet', space_type='DOPESHEET_EDITOR', region_type='WINDOW', modal=False) as km:
    pass

# Map NLA Editor
with KeyMap(kc, 'NLA Editor', space_type='NLA_EDITOR', region_type='WINDOW', modal=False) as km:
    pass
