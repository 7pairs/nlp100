#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec04


def sec04(text, single_char_index):
    return {w[:1 if i in single_char_index else 2]: i for i, w in enumerate(text.split(), 1)}
