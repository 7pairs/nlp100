#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec12

import csv


def main():
    with open('hightemp.txt') as inf, open('col1.txt', 'w') as outf1, open('col2.txt', 'w') as outf2:
        reader = csv.reader(inf, delimiter='\t')
        for rows in reader:
            outf1.write(rows[0] + '\n')
            outf2.write(rows[1] + '\n')


if __name__ == '__main__':
    main()
