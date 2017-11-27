#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://www.cl.ecei.tohoku.ac.jp/nlp100/#sec09

import random


def shuffle_word(word):
    if len(word) <= 4:
        return word

    chars = list(word[1:-1])
    random.shuffle(chars)
    return word[0] + ''.join(chars) + word[-1]


def main():
    text = "I couldn't believe that I could actually understand what I was reading : " \
           "the phenomenal power of the human mind ."

    answer = ' '.join([shuffle_word(w) for w in text.split()])
    print(answer)


if __name__ == '__main__':
    main()
