#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec19

from collections import Counter


def main():
    with open('hightemp.txt') as f:
        answer = Counter(l.split('\t')[0] for l in f.readlines())

    print(answer)


if __name__ == '__main__':
    main()
