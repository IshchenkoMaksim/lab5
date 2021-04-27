#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите два предложения: ")
    x = []
    y = []
    r = []
    k = 0

    s = s.replace(",", "")
    s = s.lower()
    
    for i in range(len(s)):
        if s[i] in [".", "!", "?"]:
            x = s[:i]
            y = s[i+2:-1]
            k += 1
            break
    if k == 0 or y == "":
        print("Ошибка!", file=sys.stderr)
        exit(1)

    x = x.split()
    y = y.split()

    for i in range(len(x)):
        if x[i] in y:
            r.append(x[i])
    r = ", ".join(r)

    if r == "":
        print("Повторяющихся слов нет")
    else:
        print(f"Слово/ва: {r} - из первого предложения, также повторяются во втором")
