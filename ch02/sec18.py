#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec18


def main():
    with open('hightemp.txt') as f:
        answer = sorted(f.readlines(), key=lambda x: float(x.split('\t')[2]), reverse=True)

    print(answer)


if __name__ == '__main__':
    main()
