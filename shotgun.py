import bpy
import os

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
km = kc.keymaps.new('UV Editor', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Mask Editing
km = kc.keymaps.new('Mask Editing', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map File Browser Main
km = kc.keymaps.new('File Browser Main', space_type='FILE_BROWSER', region_type='WINDOW', modal=False)

# Map SequencerPreview
km = kc.keymaps.new('SequencerPreview', space_type='SEQUENCE_EDITOR', region_type='WINDOW', modal=False)

# Map Clip Editor
km = kc.keymaps.new('Clip Editor', space_type='CLIP_EDITOR', region_type='WINDOW', modal=False)

# Map Clip Graph Editor
km = kc.keymaps.new('Clip Graph Editor', space_type='CLIP_EDITOR', region_type='WINDOW', modal=False)

# Map Clip Dopesheet Editor
km = kc.keymaps.new('Clip Dopesheet Editor', space_type='CLIP_EDITOR', region_type='WINDOW', modal=False)

# Map Outliner
km = kc.keymaps.new('Outliner', space_type='OUTLINER', region_type='WINDOW', modal=False)

# Map Graph Editor
km = kc.keymaps.new('Graph Editor', space_type='GRAPH_EDITOR', region_type='WINDOW', modal=False)

# Map 3D View
km = kc.keymaps.new('3D View', space_type='VIEW_3D', region_type='WINDOW', modal=False)

# Map Face Mask
km = kc.keymaps.new('Face Mask', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Weight Paint Vertex Selection
km = kc.keymaps.new('Weight Paint Vertex Selection', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Pose
km = kc.keymaps.new('Pose', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Object Mode
km = kc.keymaps.new('Object Mode', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Curve
km = kc.keymaps.new('Curve', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Metaball
km = kc.keymaps.new('Metaball', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Lattice
km = kc.keymaps.new('Lattice', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Particle
km = kc.keymaps.new('Particle', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Node Editor
km = kc.keymaps.new('Node Editor', space_type='NODE_EDITOR', region_type='WINDOW', modal=False)

# Map Timeline
km = kc.keymaps.new('Timeline', space_type='TIMELINE', region_type='WINDOW', modal=False)

# Map Mesh
km = kc.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Armature
km = kc.keymaps.new('Armature', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map View2D
km = kc.keymaps.new('View2D', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Image Paint
km = kc.keymaps.new('Image Paint', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Sequencer
km = kc.keymaps.new('Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW', modal=False)

# Map Animation
km = kc.keymaps.new('Animation', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Image
km = kc.keymaps.new('Image', space_type='IMAGE_EDITOR', region_type='WINDOW', modal=False)

# Map Markers
km = kc.keymaps.new('Markers', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Animation Channels
km = kc.keymaps.new('Animation Channels', space_type='EMPTY', region_type='WINDOW', modal=False)

# Map Info
km = kc.keymaps.new('Info', space_type='INFO', region_type='WINDOW', modal=False)

# Map Dopesheet
km = kc.keymaps.new('Dopesheet', space_type='DOPESHEET_EDITOR', region_type='WINDOW', modal=False)

# Map NLA Editor
km = kc.keymaps.new('NLA Editor', space_type='NLA_EDITOR', region_type='WINDOW', modal=False)
