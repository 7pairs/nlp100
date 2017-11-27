#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec17

import csv


def main():
    with open('hightemp.txt') as f:
        reader = csv.reader(f, delimiter='\t')
        answer = {rows[0] for rows in reader}

    print(answer)


if __name__ == '__main__':
    main()
