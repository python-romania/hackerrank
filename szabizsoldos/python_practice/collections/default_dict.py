from collections import defaultdict


n_m = list(map(int, input().split()))
d = defaultdict(list)

for i in n_m:
    for l in range(i):
        d[i].append(input())

for i in d.get(n_m[1]):
    for x in i:
        lst = []
        if x in d.get(n_m[0]):
            j = 1
            for x1 in d.get(n_m[0]):
                if x == x1:
                    lst.append(j)
                j += 1
        else:
            print(-1)
        print(*lst, sep=' ')

