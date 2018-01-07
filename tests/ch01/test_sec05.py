#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec05

from nlp100.ch01.sec05 import sec05_01, sec05_02


def test_sec05_01_should_return_word_bi_gram():
    actual = sec05_01('I am an NLPer', 2)
    assert actual == [
        ['I', 'am'],
        ['am', 'an'],
        ['an', 'NLPer'],
    ]


def test_sec05_02_should_return_character_bi_gram():
    actual = sec05_02('I am an NLPer', 2)
    assert actual == [
        'I ',
        ' a',
        'am',
        'm ',
        ' a',
        'an',
        'n ',
        ' N',
        'NL',
        'LP',
        'Pe',
        'er',
    ]
