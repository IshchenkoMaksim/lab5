#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    n = 0
    x = 0

    for n in range(len(s) - 4):
        if s[n] == s[n+1] == s[n+2] == s[n+3] == s[n+4]:
            x += 1
            n += 1

    if x >= 1:
        print("yes")
    else:
        print("no")
