#!/bin/python3

import math
import os
import random
import re
import sys


def calculate_sums(s):
    lines_sum = []
    columns_sum = []
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for idx, i in enumerate(s):
        lines_sum.append(sum(i))
        primary_diagonal_sum += s[idx][idx]
        secondary_diagonal_sum += s[idx][len(s) - idx - 1]
        columns_sum.append(sum([s[x][idx] for x in range(len(s))]))

    return lines_sum, columns_sum, primary_diagonal_sum, secondary_diagonal_sum


# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    lines_sum, columns_sum, primary_diagonal_sum, secondary_diagonal_sum = calculate_sums(s)
    changed_s = s[:]

    return None


if __name__ == '__main__':
    s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]

    result = formingMagicSquare(s)
