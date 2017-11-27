#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec15

import sys


def main():
    with open('hightemp.txt') as f:
        print(''.join(f.readlines()[-int(sys.argv[1]):]))


if __name__ == '__main__':
    main()
