from itertools import product

R = []
A = list(input().split())
B = list(input().split())

R.append(A)
R.append(B)

print(" ".join(map(str, list(product(*R)))).replace("'", ""))


# Same as above, but more elegant
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*product(A, B))
