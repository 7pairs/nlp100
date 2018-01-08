#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec06

from nlp100.ch01.sec06 import sec06_01, sec06_02, sec06_03, sec06_04


def test_sec06_01_should_return_union():
    actual = sec06_01('paraparaparadise', 'paragraph')
    assert actual == {
        'ad',
        'ag',
        'ap',
        'ar',
        'di',
        'gr',
        'is',
        'pa',
        'ph',
        'ra',
        'se',
    }


def test_sec06_02_should_return_intersection():
    actual = sec06_02('paraparaparadise', 'paragraph')
    assert actual == {
        'ap',
        'ar',
        'pa',
        'ra',
    }


def test_sec06_03_should_return_difference_set():
    actual = sec06_03('paraparaparadise', 'paragraph')
    assert actual == {
        'ad',
        'di',
        'is',
        'se',
    }


def test_sec06_04_should_return_true_when_call_with_paraparaparadise():
    actual = sec06_04('paraparaparadise', 'se')
    assert actual is True


def test_sec06_04_should_return_false_when_call_with_paragraph():
    actual = sec06_04('paragraph', 'se')
    assert actual is False
