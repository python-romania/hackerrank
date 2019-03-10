# !/bin/python3

import os
import sys

# Problem taken from hackerrank
# Link: https://www.hackerrank.com/challenges/drawing-book/problem

#
# Complete the pageCount function below.
#

def pageCount(n, p):
    page_turns = 0
    if n in [2, 3]:
        return page_turns

    page_turns = n // 2 + 1
    pt_from_start_untill_p = 1 + p // 2
    percentage_of_p_from_page_turns = p / n

    if percentage_of_p_from_page_turns > 0.5:
        return page_turns - pt_from_start_untill_p
    else:
        return pt_from_start_untill_p - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()


