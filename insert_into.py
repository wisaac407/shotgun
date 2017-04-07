#!/usr/bin/python

import re
import yaml


if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as data, open(sys.argv[2], 'r+') as target:
        data = yaml.load(data)
        target_str = target.read()
        target.seek(0)

        for keymap, groups in data.items():
            name = re.escape(' '.join(re.findall('[A-Z][a-z]+', keymap)))


            pattern = r"(with KeyMap\(kc, '" + name + r'[^\n]+\n) {4}pass'

            repl = r'\1'
            for group in groups:
                for line in group:
                    repl += '    ' + line + '\n'
                repl += '\n'
            # Strip trailing newline
            repl = repl[:-1]
            target_str = re.sub(pattern, repl, target_str)

        target.write(target_str)
