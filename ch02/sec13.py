#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec13

import csv


def main():
    with open('col1.txt') as inf1, open('col2.txt') as inf2, open('col1+2.txt', 'w') as outf:
        for e1, e2 in zip(inf1, inf2):
            outf.write('{0}\t{1}\n'.format(e1.strip(), e2.strip()))


if __name__ == '__main__':
    main()
