#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    valleys_crossed = 0
    is_in_valley = False

    for char in s:
        if char == 'D':
            sea_level -= 1
        else:
            sea_level += 1

        if sea_level < 0:
            is_in_valley = True

        if sea_level == 0 and is_in_valley:
            valleys_crossed += 1
            is_in_valley = False

    return valleys_crossed


if __name__ == '__main__':
    n = 12

    s = "DDUUDDUDUUUD"

    result = countingValleys(n, s)
    print(result)
