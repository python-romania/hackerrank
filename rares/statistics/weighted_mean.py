import sys
from operator import mul

from typing import *


def vector_product(v1: Iterable[int], v2: Iterable[int]) -> int:
    return sum(map(mul, v1, v2))


n, *data = list(map(int, sys.stdin.read().split()))
nums, weights = data[:n], data[n:]

wmean = vector_product(nums, weights) / sum(weights)

wmean = round(wmean, 1)
print(wmean)