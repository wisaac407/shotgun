#!/usr/bin/python
import re


def _format(s):
    tokens = re.split('(#[^\n]+\n)', s)

    ret = tokens[0]

    funcs = []

    for token in tokens[1:]:
        if token.startswith('#'):
            ret += token
            funcName = token[1:].replace(' ', '').replace('-', '')
            funcName = funcName[0].lower() + funcName[1:-1]
            funcs.append(funcName)
            ret += 'def %s():\n    ' % funcName
        else:
            ret += '\n    '.join(token.strip().split('\n'))
            ret += '\n\n\n'

    ret += 'def main():\n'
    for funcName in funcs:
        ret += '    ' + funcName + '()\n'

    return ret


def format_keyconfig(filein, fileout):
    with open(filein, 'r') as fin, open(fileout, 'w') as fout:
        fout.write(_format(fin.read()))


if __name__ == '__main__':
    import sys
    format_keyconfig(sys.argv[1], sys.argv[2])
