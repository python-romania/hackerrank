import builtins

n = int(input())
ints = tuple(map(int, input().split()))

print(hash(ints))
