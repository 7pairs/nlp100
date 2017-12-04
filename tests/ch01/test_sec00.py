#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec00

from nlp100.ch01.sec00 import sec00


def test_should_return_desserts_when_call_sec00_with_stressed():
    actual = sec00('stressed')
    assert actual == 'desserts'
