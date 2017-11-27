#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec07


def template(x, y, z):
    return '{0}時の{1}は{2}'.format(x, y, z)


def main():
    x = 12
    y = '気温'
    z = 22.4

    answer = template(x, y, z)
    print(answer)


if __name__ == '__main__':
    main()
