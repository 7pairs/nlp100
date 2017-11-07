#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec02


def main():
    text1 = 'パトカー'
    text2 = 'タクシー'

    answer = ''.join([c1 + c2 for c1, c2 in zip(text1, text2)])
    print(answer)


if __name__ == '__main__':
    main()
