en_studs, en_rnr = int(input()), set(map(int, input().split()))
fr_studs, fr_rnr = int(input()), set(map(int, input().split()))

print(len(en_rnr.union(fr_rnr)))
