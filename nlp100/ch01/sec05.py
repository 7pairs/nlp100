#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec05


def n_gram(seq, n):
    return [seq[i:i + n] for i in range(len(seq) - n + 1)]


def sec05_01(text, n):
    words = text.split(' ')
    return n_gram(words, n)


def sec05_02(text, n):
    return n_gram(text, n)
