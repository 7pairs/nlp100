#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec03

from nlp100.ch01.sec03 import sec03


def test_sec03_should_return_pi_list():
    actual = sec03('Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.')
    assert actual == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
