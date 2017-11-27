#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec03

import re


def main():
    text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

    answer = [len(w) for w in re.sub(r'[,.]', '', text).split()]
    print(answer)


if __name__ == '__main__':
    main()
