from itertools import product

# https://www.hackerrank.com/challenges/maximize-it/problem


def f(x):
    return x ** 2


K, M = map(int, input().split())
lists = [list(map(int, input().split()))
         for _
         in range(K)]

lists = [[f(x) % M for x in list_[1::]] for list_ in lists]
# lists = [[f(max(list_)) % M] for list_ in lists]
assignations = product(*lists)
mx = 0
for t in assignations:
    sm = sum(t)
    if sm % M == 0:
        continue
    else:
        if sm > mx:
            mx = sum(t)

print(mx)
