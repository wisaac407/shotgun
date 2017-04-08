#!/usr/bin/python

import re
import yaml


if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as data, open(sys.argv[2], 'r+') as target:
        data = yaml.load(data)
        target_str = target.read()
        target.seek(0)

        pattern = re.compile(r"(with KeyMap\(kc, '([^']+)'[^\n]+\n) {4}pass")

        def repl(match):
            header, name = match.groups()
            name = 'map' + name.replace(' ', '')

            s = header
            for group in data[name]:
                for line in group:
                    s += '    ' + line + '\n'
                s += '\n'
            return s

        target.write(pattern.sub(repl, target_str))
