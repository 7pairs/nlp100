#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec03

import re


def sec03(text):
    return [len(w) for w in re.sub(r'[,.]', '', text).split()]
