#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec02


def sec02(text1, text2):
    return ''.join([c1 + c2 for c1, c2 in zip(text1, text2)])
