#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec06


def bi_gram(seq):
    return {seq[i:i + 2] for i in range(len(seq) - 1)}


def sec06_01(text1, text2):
    x = bi_gram(text1)
    y = bi_gram(text2)
    return x | y


def sec06_02(text1, text2):
    x = bi_gram(text1)
    y = bi_gram(text2)
    return x & y


def sec06_03(text1, text2):
    x = bi_gram(text1)
    y = bi_gram(text2)
    return x - y


def sec06_04(text, element):
    elements = bi_gram(text)
    return element in elements
