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
import re
import shutil
import bpy

INDEX_TEMPLATE = """
=====================
Shotgun Documentation
=====================

Welcome, this is the documentation for Shotgun version {version}.
Shotgun is a custom keymap for `Blender <http://www.blender.org>`_ designed to standardize the keymap and make the most
commonly used operators accessible.

.. toctree::
   :maxdepth: 1

   Overview<overview.rst>
   All Keymaps<keymaps.rst>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

CONF_TEMPLATE = """
#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

extensions = [
    'sphinx.ext.intersphinx',
    'keymap_domain'
]

master_doc = 'index'

project = 'Shotgun'
copyright = '{year}, Isaac Weaver'
author = 'Isaac Weaver'

version = '{version}'
release = '{version}'

intersphinx_mapping = {{
    'blender': ('http://docs.blender.org/api/blender_python_api_master/', '{blender_objects}')
}}
"""

SPECIAL_WHITESPACE_RE = re.compile('([\r\n\t])')


def rep_special_whitespace(m):
    return repr(m.group())[1:-1].replace('\\', '\\\\')


def lookup_operator(op):
    ns, on = op.split('.')
    return getattr(getattr(bpy.ops, ns), on)


def full_compare(a, b, km='Unknown'):
    """Check if a and b are exactly equal keymap items."""
    for prop in ['idname', 'type', 'value', 'any', 'shift', 'ctrl', 'alt', 'oskey', 'key_modifier']:
        if getattr(a, prop, None) != getattr(b, prop, None):
            return False

    # At this point they are probably the same but let's check all the properties too
    for prop in a.properties.keys():
        # Pointer properties are set when the operator is run
        if a.properties.rna_type.properties[prop].type != 'POINTER':
            if getattr(a.properties, prop, None) != getattr(b.properties, prop, None):
                print("Props Differ: km: {} combo: {} op: {} prop: {} a: {} b: {}".format(
                    km, get_key_combo(a), a.idname, prop,
                    getattr(a.properties, prop, None), getattr(b.properties, prop, None)))
                return False
    return True


def is_default_hotkey(kmi):
    """Return True if kmi is a default blender hotkey."""
    try:
        import shotgun
    except ImportError:
        import sys
        sys.path.append(os.path.dirname(os.getcwd()))
        import shotgun
    for name, kmis in shotgun.default_hotkeys.items():
        for dkmi in kmis:
            if full_compare(kmi, dkmi, name):
                return True
    return False


KEY_NAMES_REPLACEMENTS = {
    'COMMA': ',',
    'PERIOD': '.',
    'ONE': '1',
    'TWO': '2',
    'THREE': '3',
    'FOUR': '4',
    'FIVE': '5',
    'SIX': '6',
    'SEVEN': '7',
    'EIGHT': '8',
    'NINE': '9',
    'ZERO': '0',
    'TAB': 'Tab'
}


def get_key_combo(kmi):
    combo = []
    if kmi.any:
        combo.append('Any')
    else:
        if kmi.oskey:
            combo.append('Cmd')
        if kmi.ctrl:
            combo.append('Ctrl')
        if kmi.shift:
            combo.append('Shift')
        if kmi.alt:
            combo.append('Alt')
    if kmi.key_modifier != 'NONE':
        combo.append(kmi.key_modifier)
    combo.append(KEY_NAMES_REPLACEMENTS.get(kmi.type, kmi.type))

    return '-'.join(combo)


def format_props(props):
    """Given KeyMapItem.properties it returns a list of keys and the formatted values for those keys"""
    _keys = props.keys()
    keys = []
    vals = []

    for key in _keys:
        typ = props.rna_type.properties[key]
        keys.append(typ.name)
        val = getattr(props, key)

        if typ.type == 'POINTER':
            val = 'N/A'  # Most likely set when the operator is run (e.g. the object under the cursor)

        vals.append(SPECIAL_WHITESPACE_RE.sub(rep_special_whitespace, str(val)))

    return keys, vals


def create_header(text, type='=', overline=True):
    """Return the text formatted as a header"""
    header = type * len(text)
    if overline:
        return '\n{header}\n{text}\n{header}\n\n'.format(header=header, text=text)
    else:
        return '\n{text}\n{header}\n\n'.format(header=header, text=text)


def create_table(headers, items):
    """Return a formatted table
    
    :param headers: Table headers
    :type headers: list
    :param items: 2-dimensional list of table items (items[row][column])
    :type items: list
    """

    # Lengths of columns
    columns = []

    row_format = '|'
    divider = '+'

    # Reshape items so it's items[column][row]
    for i, col in enumerate(zip(*items)):
        length = len(max(col + (headers[i],), key=len)) + 1  # Add a little padding
        columns.append(length)
        row_format += '{{:{}}}|'.format(length)
        divider += '-' * length + '+'

    row_format += '\n'
    divider += '\n'

    table = divider
    table += row_format.format(*headers)
    table += divider.replace('-', '=')

    for row in items:
        table += row_format.format(*row)
        table += divider

    table += '\n'

    return table


def create_directive(directive, title, body):
    """Format a generic directive"""
    return '.. {}:: {}\n\n{}\n\n'.format(directive, title, indent(body))


def indent(s, level=1):
    indent_s = '   ' * level
    return '\n'.join(indent_s + line for line in s.split('\n'))


def generate_docs(kc):
    docs = {}
    for km in kc.keymaps:
        kmid = km.name.replace(' ', '').lower()
        # Heading with '*' overline and underline
        rst = '*' * len(km.name)
        rst = '\n'.join((rst, km.name, rst)) + '\n\n'

        rst += create_directive('km:module', kmid, '')

        rst += create_header('Quick Reference', '-')

        def to_table_row(kmi):
            combo = get_key_combo(kmi)
            operator = kmi.idname

            combo = ':km:hk:`{} <{}->{}->{}>`'.format(combo, kmid, combo, operator)
            operator = ':func:`blender:bpy.ops.{}`'.format(operator)

            return combo, operator

        rst += create_table(['Hotkey', 'Operator'], list(map(to_table_row, km.keymap_items)))

        rst += create_header('Detailed Reference', '-')
        rst += create_directive('note',
                                'Hotkeys marked with the "(default)" prefix are '
                                'inherited from the default blender keymap', '')

        for kmi in km.keymap_items:
            if kmi.active:
                directive = 'hotkey'
                try:
                    doc = lookup_operator(kmi.idname).__doc__ + '\n\n'
                except AttributeError:
                    print('Invalid Operator: ' + kmi.idname)
                    doc = ''
                    directive = 'hotkeyi'

                if is_default_hotkey(kmi):
                    directive = 'hotkeyd'

                rst += create_directive('km:' + directive,
                                        '{} -> {} : {} -> {}'.format(get_key_combo(kmi), kmi.idname,
                                                                     kmi.map_type, kmi.value),
                                        kmi.name)

                rst += indent(doc)
                rst += '\n'

                props, vals = format_props(kmi.properties)
                if len(props):
                    rst += indent(create_table(['Properties:', 'Values:'], list(zip(props, vals))))
                    rst += '\n'
        docs['keymaps/' + kmid] = rst

    return docs


def get_version():
    import subprocess
    # Try to get the version from the travis build, otherwise get it directly from git.
    if 'TRAVIS_TAG' in os.environ:
        version = os.environ['TRAVIS_TAG']
    else:
        version = subprocess.check_output(['git', 'describe', '--abbrev=0']).decode().strip().replace('v', '')
        print('Getting version from git directly')
    revision = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode().strip()
    return version + ' - ' + revision


def main():
    bpy.ops.wm.keyconfig_import(filepath='../shotgun.py')
    wm = bpy.context.window_manager
    shotgun = wm.keyconfigs['shotgun']
    version = get_version()

    docs = generate_docs(shotgun)

    if not os.path.exists('_source'):
        os.mkdir('_source')

    if not os.path.exists('_source/keymaps'):
        os.mkdir('_source/keymaps')

    # Copy all the pre-written rst files (overwriting if necessary)
    for path in os.listdir('source'):
        source = os.path.join('source', path)
        target = os.path.join('_source', path)

        # If the target path exists remove it
        if os.path.exists(target):
            if os.path.isdir(target):
                shutil.rmtree(target)
            else:
                os.remove(target)

        # Copy to the target path
        if os.path.isdir(source):
            shutil.copytree(source, target)
        else:
            shutil.copy2(source, target)

    # Write all the keymap files
    for kmid, rst in docs.items():
        with open(os.path.join('_source', kmid + '.rst'), 'w') as f:
            f.write(rst)

    # Write the index.rst file
    with open(os.path.join('_source', 'index.rst'), 'w') as f:
        f.write(INDEX_TEMPLATE.format(
            version=version
        ))

    # Write the configure file
    with open(os.path.join('_source', 'conf.py'), 'w') as f:
        import datetime

        f.write(CONF_TEMPLATE.format(
            version=version,
            blender_objects='../blender_objects.inv',
            year=datetime.datetime.now().year
        ))


if __name__ == '__main__':
    main()
