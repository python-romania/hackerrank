A = set(list(map(int, input().split())))
N = int(input())
is_valid = 0

for i in range(N):
    if A.issuperset(set(list(map(int, input().split())))):
        is_valid += 1

if N == is_valid:
    print(True)
else:
    print(False)
