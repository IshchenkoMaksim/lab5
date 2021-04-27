#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите предложение: ")
    x = []
    k = 0
    
    for i in range(len(s)):
        if s[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            x.append(s[i])
            k += 1
        if s[i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and k <= 2:
            x = []
            k = 0
            continue
        if s[i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and k > 2:
            break

    if k <= 2:
        print(
            "Чисел нет, либо подряд идущих менее трёх",
            file=sys.stderr
        )
        exit(1)
    else:
        print("".join(x))
