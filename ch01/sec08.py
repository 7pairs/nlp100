#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec08


def cipher(text):
    return ''.join([chr(219 - ord(c)) if c.islower() else c for c in text])


def main():
    text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

    answer = cipher(text)
    print(answer)


if __name__ == '__main__':
    main()
