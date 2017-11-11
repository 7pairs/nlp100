#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec06


def bi_gram(text):
    return {text[i:i + 2] for i in range(len(text) - 1)}


def main():
    text1 = 'paraparaparadise'
    text2 = 'paragraph'

    x = bi_gram(text1)
    y = bi_gram(text2)
    print('和集合: {0}'.format(x | y))
    print('積集合: {0}'.format(x & y))
    print('差集合: {0}'.format(x - y))
    print("'se' in X: {0}".format('se' in x))
    print("'se' in Y: {0}".format('se' in y))


if __name__ == '__main__':
    main()
