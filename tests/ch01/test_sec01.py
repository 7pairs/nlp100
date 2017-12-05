#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec01

from nlp100.ch01.sec01 import sec01


def test_should_return_patcar_when_call_sec01_with_patatokukasi():
    actual = sec01('パタトクカシーー')
    assert actual == 'パトカー'
