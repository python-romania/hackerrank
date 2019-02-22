for i in range(1, int(input())+1):
    print(*[a for a in range(1, i+1)], *[b for b in range(1, i)[::-1]], sep='')

for i in range(1, int(input())+1):
    print(((10**i - 1)//9)*((10**i - 1)//9))
