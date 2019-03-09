import sys
from operator import mul
from functools import reduce


def fac(n: int) -> int:
    return reduce(mul, range(1, n + 1), 1)


def c(n: int, k: int) -> int:
    return fac(n) // (fac(k) * fac(n - k))


def pb_binom(k: int, n: int, p: float) -> float:
    return c(n, k) * (p ** k) * ((1 - p) ** (n - k))


prop_m, prop_f = list(map(float, sys.stdin.read().split()))

pb_m = prop_m / (prop_m + prop_f)

p = sum(pb_binom(k, 6, pb_m) for k in (3, 4, 5, 6))

p = round(p, 3)

print(p)