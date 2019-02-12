import sys


def fac(n):
    return 1 if n is 0 else n*fac(n-1)


def c(n, x):
    return fac(n) / (fac(x) * fac(n-x))


def pb_binom(x, n, p):
    return c(n, x) * (p ** x) * ((1 - p) ** (n - x))


data = sys.stdin.read().split()

pb_faulty, batch_size = int(data[0]) / 100, int(data[1])

p1 = sum(pb_binom(k, batch_size, pb_faulty) for k in range(0, 2 + 1))
p2 = sum(pb_binom(k, batch_size, pb_faulty) for k in range(2, batch_size + 1))

p1, p2 = round(p1, 3), round(p2, 3)

print(p1)
print(p2)
