#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec16

import math
import sys


def main():
    with open('hightemp.txt') as f:
        lines = f.readlines()

    file_count = int(sys.argv[1])
    line_count = math.ceil(len(lines) / file_count)
    for i in range(file_count):
        with open('out{0:02d}.txt'.format(i), 'w') as f:
            for line in lines[i * line_count:(i + 1) * line_count]:
                f.write(line)


if __name__ == '__main__':
    main()
