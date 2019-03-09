#!/bin/python3

import os
import sys
import itertools

# Hackerrank problem
# Link: https://www.hackerrank.com/challenges/electronics-shop/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards_drives_combinations = [(x, y) for x in keyboards for y in drives]
    combinations_sum = list(sum(k) for k in keyboards_drives_combinations)
    if min(combinations_sum) > b:
        return -1
    else:
        return max(list(x for x in combinations_sum if x <= b))



if __name__ == '__main__':
    bnm = "10 2 3".split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, "3 1".rstrip().split()))

    drives = list(map(int, "5 2 8".rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
