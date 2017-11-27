#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec04


def main():
    text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. ' \
           'New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    single_char_index = {1, 5, 6, 7, 8, 9, 15, 16, 19}

    answer = {w[:1 if i in single_char_index else 2]: i for i, w in enumerate(text.split(), 1)}
    print(answer)


if __name__ == '__main__':
    main()
