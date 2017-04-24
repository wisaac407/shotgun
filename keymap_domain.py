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

import re

from sphinx import addnodes
from sphinx.domains import Domain, ObjType
from sphinx.locale import l_, _
from sphinx.directives import ObjectDescription, Directive
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode
from docutils.parsers.rst import directives
from docutils import nodes


km_sig_re = re.compile('^ ?([^\s]+) -> ([\w.]*) : ([^\s]+) -> ([\w.]*)$')


class KeymapModule(Directive):
    """
    Directive to mark description of a new module.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'platform': lambda x: x,
        'synopsis': lambda x: x,
        'noindex': directives.flag,
        'deprecated': directives.flag,
    }

    def run(self):
        env = self.state.document.settings.env
        modname = self.arguments[0].strip()
        noindex = 'noindex' in self.options
        env.ref_context['km:module'] = modname
        ret = []
        if not noindex:
            env.domaindata['km']['modules'][modname] = \
                (env.docname, self.options.get('synopsis', ''),
                 self.options.get('platform', ''), 'deprecated' in self.options)
            # make a duplicate entry in 'objects' to facilitate searching for
            # the module in KeymapDomain.find_obj()
            env.domaindata['km']['objects'][modname] = (env.docname, 'module')
            targetnode = nodes.target('', '', ids=['module-' + modname],
                                      ismod=True)
            self.state.document.note_explicit_target(targetnode)
            # the platform and synopsis aren't printed; in fact, they are only
            # used in the modindex currently
            ret.append(targetnode)
            indextext = _('%s (module)') % modname
            inode = addnodes.index(entries=[('single', indextext,
                                             'module-' + modname, '', None)])
            ret.append(inode)
        return ret


class KeymapHotkey(ObjectDescription):
    """Keymap Hotkey"""

    def handle_signature(self, sig, signode):
        """
        Transform a hotkey signature into RST nodes.
        """
        m = km_sig_re.match(sig)
        if m is None:
            raise ValueError
        name, operator, map_type, value = m.groups()

        # determine module and class name (if applicable), as well as full name
        modname = self.options.get(
            'module', self.env.ref_context.get('km:module'))
        fullname = modname + '->' + name + '->' + operator

        signode['module'] = modname
        signode['fullname'] = fullname

        sig_prefix = self.get_signature_prefix()
        if sig_prefix:
            signode += addnodes.desc_annotation(sig_prefix, sig_prefix)

        signode += addnodes.desc_name(name, name)

        signode += addnodes.desc_returns(operator, operator)

        map_type = ' : ' + map_type

        signode += addnodes.desc_annotation(map_type, map_type)
        signode += addnodes.desc_returns(value, value)

        return fullname, name

    def get_index_text(self, modname, name):
        """Return the text for the index entry of the object."""
        return modname + ' ' + name[1]

    def get_signature_prefix(self):
        return ''

    def add_target_and_index(self, name, sig, signode):
        modname = self.options.get(
            'module', self.env.ref_context.get('km:module'))
        fullname = name[0]
        # note target
        if fullname not in self.state.document.ids:
            signode['names'].append(fullname)
            signode['ids'].append(fullname)
            signode['first'] = (not self.names)
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['km']['objects']
            objects[fullname] = (self.env.docname, self.objtype)

        indextext = self.get_index_text(modname, name)
        if indextext:
            self.indexnode['entries'].append(('single', indextext,
                                              fullname, '', None))


# Useful for development.
class KeymapInvalidHotkey(KeymapHotkey):
    def get_signature_prefix(self):
        return '(invalid) '


class KeymapDefaultHotkey(KeymapHotkey):
    def get_signature_prefix(self):
        return '(default) '


class KmXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        refnode['km:module'] = env.ref_context.get('km:module')
        return title, target


class KeymapDomain(Domain):
    """Keymap domain."""

    name = 'km'
    label = 'Keymap'

    object_types = {
        'hk': ObjType(l_('hotkey'), 'hotkey', 'hk'),
        'module': ObjType(l_('module'), 'mod'),
    }

    directives = {
        'hotkey': KeymapHotkey,
        'hotkeyi': KeymapInvalidHotkey,
        'hotkeyd': KeymapDefaultHotkey,
        'module': KeymapModule,
    }

    roles = {
        'hk': KmXRefRole()
    }

    initial_data = {
        'objects': {},  # fullname -> docname, objtype
        'modules': {}
    }

    def clear_doc(self, docname):
        for name, (doc, typ) in self.data['objects'].copy().items():
            if doc == docname:
                del self.data['objects'][name]

    def resolve_xref(self, env, fromdocname, builder, typ, target, node,
                     contnode):
        objects = self.data['objects']
        if target in objects:
            objtype = 'hk'
            return make_refnode(builder, fromdocname,
                                objects[target][0],
                                target,
                                contnode, target + ' ' + objtype)

    def get_objects(self):
        for name, (docname, typ) in self.data['objects'].items():
            yield name, name, typ, docname, name, 1


def setup(app):
    app.add_domain(KeymapDomain)

    # return {
    #     'version': 'builtin',
    #     'parallel_read_safe': True,
    #     'parallel_write_safe': True,
    # }

