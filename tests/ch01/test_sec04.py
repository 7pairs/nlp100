#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec04

from nlp100.ch01.sec04 import sec04


def test_sec04_should_return_element_dictionary():
    text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. ' \
           'New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    single_char_index = {1, 5, 6, 7, 8, 9, 15, 16, 19}

    actual = sec04(text, single_char_index)
    assert actual == {
        'H': 1,
        'He': 2,
        'Li': 3,
        'Be': 4,
        'B': 5,
        'C': 6,
        'N': 7,
        'O': 8,
        'F': 9,
        'Ne': 10,
        'Na': 11,
        'Mi': 12,
        'Al': 13,
        'Si': 14,
        'P': 15,
        'S': 16,
        'Cl': 17,
        'Ar': 18,
        'K': 19,
        'Ca': 20,
    }
