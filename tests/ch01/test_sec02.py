#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec02

from nlp100.ch01.sec02 import sec02


def test_sec02_should_return_patatokukashi():
    actual = sec02('パトカー', 'タクシー')
    assert actual == 'パタトクカシーー'
