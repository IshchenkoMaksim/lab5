#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите слово: ")
    m = int(input("Введите номер первой буквы для замены: "))
    n = int(input("Введите номер второй буквы для замены: "))
    m -= 1
    n -= 1

    if m > len(s) or n > len(s):
        print('Неверное число', file=sys.stderr)
        exit(1)
    else:
        t = s[:m] + s[n] + s[m+1:n] + s[m] + s[n+1:]
        print(f"Слово после замены: {t}")
