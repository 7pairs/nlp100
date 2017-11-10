#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec05

import enum


class Mode(enum.Enum):
    WORD = 1
    CHAR = 2


def n_gram(text, n, mode):
    if mode == Mode.WORD:
        return _n_gram(text.split(), n)
    elif mode == Mode.CHAR:
        return _n_gram(text, n)


def _n_gram(seq, n):
    return [seq[i:i + n] for i in range(len(seq) - n + 1)]


def main():
    text = 'I am an NLPer'

    answer1 = n_gram(text, 2, Mode.WORD)
    answer2 = n_gram(text, 2, Mode.CHAR)
    print(answer1)
    print(answer2)


if __name__ == '__main__':
    main()
