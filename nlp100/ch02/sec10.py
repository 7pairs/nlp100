#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec10


def main():
    with open('hightemp.txt') as f:
        answer = len(f.readlines())
    print(answer)


if __name__ == '__main__':
    main()
