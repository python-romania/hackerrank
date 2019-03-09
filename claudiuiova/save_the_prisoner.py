#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    if s + m <= n:
        return s + m - 1
    else:
        m -= n - s + 1
        if m % n == 0:
            return s
        else:
            return m % n



if __name__ == '__main__':
    l1 = ['5 2 1', '5 2 2']
    l2 = ['7 19 2', '3 7 3']

    t = 2

    for t_itr in l2:
        nms = t_itr.split()

        n = int(nms[0])
        m = int(nms[1])
        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        print(result)
