#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec11

import re


def main():
    with open('hightemp.txt') as f:
        text = f.read()

    answer = re.sub(r'\t', ' ', text)
    print(answer)


if __name__ == '__main__':
    main()
