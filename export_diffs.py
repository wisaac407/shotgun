#!/usr/bin/python

import re


def mapper(funcs):
    def func_name(func):
        return func.split('()')[0][4:]

    def func_body(func):
        return '\n'.join(func.split('\n')[2:])

    return {func_name(f): func_body(f) for f in funcs}


def get_funcs(s):
    funcs = re.split('#[^\n]+\n', s)[1:]
    return mapper(funcs)


# def pack_lines(a, b):
#     ret = {}
#     a_lines = a.split('\n')
#     b_lines = b.split('\n')
#     for line in set(a_lines) - set(b_lines):
#         for func, func_str in a_funcs.items():
#             if func_str.find(line) != -1:
#                 lines = ret.setdefault(func, [])
#                 if not re.match(' {4}kmi = km.+', line):
#                     print(line)
#                     index = a_lines.index(line)
#                     while True:
#                         index -= 1
#                         ln = a_lines[index]
#                         print(ln)
#                         # If the line was already added remove it and add it back on the end
#                         if ln in lines:
#                             lines.pop(lines.index(ln))
#                         lines.append(ln)
#                         if re.match(' {4}kmi = km.+', ln):
#                             break
#                 # Avoid adding the line twice
#                 if line not in lines:
#                     lines.append(line)
#     return ret

HOTKEY_PATTERN = re.compile(' {4}kmi = km.+')


def group_hotkeys(lines):
    groups = []
    current_group = None
    for line in lines:
        # Skip whitespace
        if not re.match('^\s+$', line):
            if HOTKEY_PATTERN.match(line):
                if current_group is not None:
                    groups.append(current_group)
                current_group = [line]
            else:
                current_group.append(line)
    return groups


def pack_lines(a, b):
    ret = {}
    a_funcs = get_funcs(a)
    b_funcs = get_funcs(b)

    for func, func_str in a_funcs.items():
        ret[func] = lines = []

        a_lines = func_str.splitlines()
        b_lines = b_funcs[func].splitlines()

        a_groups = group_hotkeys(a_lines)
        b_groups = group_hotkeys(b_lines)

        hotkeys = set()

        for group in a_groups:
            if group not in b_groups:
                # Avoid duplicate hotkeys
                if group[0] in hotkeys:
                    continue
                hotkeys.add(group[0])

                # lines.append('  - ' + group[0][4:] + ':')
                # for line in group[1:]:
                #     lines.append('    - ' + line[4:])
                # lines.append('')
                lines.append('  - [')
                for line in group:
                    lines.append('      "' + line.strip() + '",')
                lines.append('    ]')
    return ret

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as a, open(sys.argv[2]) as b, open(sys.argv[3], 'w') as out:
        a = a.read()
        b = b.read()

        for func, lines in pack_lines(a, b).items():
            out.write(func)
            out.write(':\n')
            out.write('\n'.join(lines))
            out.write('\n\n')
