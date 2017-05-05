# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Contributor(s): Isaac Weaver
#
# ##### END GPL LICENSE BLOCK #####

import os
import sys
import tempfile
import requests
import datetime
import bpy


bl_info = {
    "name": "Shotgun Manager",
    "author": "Isaac Weaver",
    "version": (0, 2, 5),
    "blender": (2, 78, 0),
    "description": "Utility tool for installing Shotgun and keeping it up-to-date",
    "category": "System"
}


def parse_version(version_string):
    """Convert a version string from vx.y.z to a tuple (x, y, z)"""
    version = [0, 0, 0]

    # Loop through up to 3 segments adding them if they are numeric.
    for i, bit in enumerate(version_string.replace('v', '').split('.')[:3]):
        if bit.isnumeric():
            version[i] = int(bit)

    return tuple(version)


class UpdateManager:
    _version = None
    _meta_data = None
    _last_updated = None
    _can_update = False

    def check_for_update(self):
        """Return True if not up-to-date False otherwise"""
        self._can_update = self.version != parse_version(self.meta_data['tag_name'])
        return self._can_update

    def _download(self, wm):
        """Download the latest version of Shotgun reporting the progress to the window manager"""
        # Begin progress report
        wm.progress_begin(0, 100)

        # Now we download Shotgun
        resp = requests.get(self.download_url, stream=True)
        content = b''
        length = int(resp.headers['content-length'])
        for c in resp.iter_content(1024):
            # Update progress report
            progress = int(100 * resp.raw.tell() / length)
            wm.progress_update(progress)
            content += c

        tempdir = tempfile.TemporaryDirectory()
        with open(os.path.join(tempdir.name, 'shotgun.py'), 'wb') as f:
            f.write(content)

        wm.progress_end()

        return tempdir

    def update(self, wm):
        """Update Shotgun, report download progress to the window manager"""
        with self._download(wm) as d:
            self.install_local(os.path.join(d, 'shotgun.py'))

    def install_local(self, path):
        """Install Shotgun from a local file"""
        bpy.ops.wm.keyconfig_import(filepath=path)

        self._can_update = False
        self._read_version_info()

    @property
    def can_update(self):
        return self._can_update

    @property
    def version(self):
        if self._version is None:
            self._read_version_info()
        return self._version

    @property
    def is_installed(self):
        return self.version != (0, 0, 0)

    @property
    def last_updated(self):
        if self._last_updated is None:
            self._read_version_info()
        return self._last_updated

    @property
    def meta_data(self):
        if self._meta_data is None:
            self._meta_data = self._get_meta_data()
        return self._meta_data

    @property
    def download_url(self):
        for asset in self.meta_data['assets']:
            if asset['name'] == 'shotgun.py':
                return asset['browser_download_url']

    def _read_version_info(self):
        """Read the local version file"""
        path = bpy.utils.preset_find('shotgun', 'keyconfig')
        if path:
            sys.path.append(os.path.dirname(path))
            self._version = parse_version(__import__('shotgun').VERSION)
            del sys.modules['shotgun']
            sys.path.pop()

            self._last_updated = datetime.datetime.utcfromtimestamp(os.path.getmtime(path))
        else:
            # Shotgun is not installed!
            self._version = (0, 0, 0)
            self._last_updated = datetime.datetime(1, 1, 1)

    @staticmethod
    def _get_meta_data():
        """Get the meta data of the latest release form github"""
        resp = requests.get('https://api.github.com/repos/wisaac407/shotgun/releases/latest')
        return resp.json()


manager = UpdateManager()


class UpdateShotgun(bpy.types.Operator):
    """Update to the latest version of the Shotgun keymap"""
    bl_idname = 'wm.shotgun_update'
    bl_label = 'Update Shotgun'

    @classmethod
    def poll(cls, context):
        return manager.can_update

    def execute(self, context):
        manager.update(context.window_manager)
        return {'FINISHED'}


class CheckUpdateShotgun(bpy.types.Operator):
    """Update to the latest version of the Shotgun keymap"""
    bl_idname = 'wm.shotgun_check_update'
    bl_label = 'Check For Shotgun Update'

    def execute(self, context):
        if manager.check_for_update():
            self.report({'INFO'}, 'Update available')
        else:
            self.report({'INFO'}, 'Already the latest version')
        return {'FINISHED'}


class EnableShotgun(bpy.types.Operator):
    """Enable the Shotgun keymap"""
    bl_idname = 'wm.shotgun_enable'
    bl_label = 'Enable Shotgun'

    @classmethod
    def poll(cls, context):
        return context.window_manager.keyconfigs.active.name != 'shotgun'

    def execute(self, context):
        wm = context.window_manager

        if manager.is_installed:
            wm.keyconfigs.active = wm.keyconfigs['shotgun']
        else:
            manager.install_local(os.path.join(os.path.dirname(__file__), 'shotgun.py'))

        return {'FINISHED'}


class DisableShotgun(bpy.types.Operator):
    """Disable the Shotgun keymap"""
    bl_idname = 'wm.shotgun_disable'
    bl_label = 'Disable Shotgun'

    @classmethod
    def poll(cls, context):
        return context.window_manager.keyconfigs.active.name == 'shotgun'

    def execute(self, context):
        wm = context.window_manager
        wm.keyconfigs.active = wm.keyconfigs.default

        return {'FINISHED'}


class ShotgunPanel(bpy.types.Panel):
    """Shotgun panel"""
    bl_label = "Shotgun Manager"
    bl_idname = '3DVIEW_PT_shotgun'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    # bl_context = ''

    @classmethod
    def poll(cls, context):
        return context.user_preferences.addons['shotgun_manager'].preferences.show_ui_panel

    def draw(self, context):
        layout = self.layout

        if manager.is_installed:
            layout.label('Current Version: v{}.{}.{}'.format(*manager.version))
            layout.label('Updated On: ' + manager.last_updated.strftime('%b %d %Y'))

            if manager.can_update:
                layout.label('Latest Version: {}'.format(manager.meta_data['tag_name']))
                layout.operator('wm.url_open', text='View Details', icon='URL').url = manager.meta_data['html_url']
                layout.operator('wm.shotgun_update', text='Update To {}'.format(manager.meta_data['tag_name']), icon='FILE_REFRESH')
            else:
                layout.operator('wm.shotgun_check_update', text="Check For Updates", icon='QUESTION')

        if EnableShotgun.poll(context):
            layout.operator('wm.shotgun_enable', icon='FILE_TICK')
        else:
            layout.operator('wm.shotgun_disable', icon='CANCEL')


class ShotgunUserPrefs(bpy.types.AddonPreferences):
    bl_idname = __name__

    show_ui_panel = bpy.props.BoolProperty(
        name='Show UI Panel',
        default=True,
        description='Show/Hide Panel in 3D View properties'
    )

    def draw(self, context):
        self.layout.prop(self, 'show_ui_panel')

        # noinspection PyCallByClass
        ShotgunPanel.draw(self, context)


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)


if __name__ == '__main__':
    register()
