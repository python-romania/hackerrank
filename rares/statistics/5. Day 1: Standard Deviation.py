# Math bits:
#
# Let miu = mean(xi); i = 1..n
#
# Let f: R -> R; f(x) = x - miu
# Let g: R -> R; g(x) = x^2
#
# (g o f)(x) <=> g(f(x)) <=> g(x - miu) <=> (x - miu)^2 =>
#
# => sum((g o f)(xi), i = 1..n) / n = sigma^2 <=>
#
# <=> mean((g o f)(xi), i = 1..n) = sigma^2 <=>
#
# <=> sigma = sqrt(mean((g o f)(xi), i = 1..n)) <=> 
#
# <=> sigma = mean((g o f)(xi), i = 1..n)^(1/2) <=>
# 
# <=> Line 58

import sys
from statistics import mean
from functools import reduce

from typing import *


def apply(f: Callable, *args, **kwargs):
    return f(*args, **kwargs)


def flip(f):
    def f_(*args, **kwargs):
        return f(*args[::-1], **kwargs)
    return f_


def compose(f: Callable, g: Callable, *fs: Tuple[Callable, ...]) -> Callable:
    funcs = fs[::-1] + (g, f)
    def f_(*args, **kwargs):
        return reduce(flip(apply), funcs[1:], funcs[0](*args, **kwargs))
    return f_


def sub(y: float) -> Callable[[float], float]:
    def sub_(x: float) -> float:
        return x - y
    return sub_


def sqr(x: float) -> float:
    return x ** 2


n, *nums = [int(num)
            for num
            in sys.stdin.read().split()]

stdev = mean(map(compose(sqr, sub(mean(nums))), nums)) ** 0.5

print(stdev)
