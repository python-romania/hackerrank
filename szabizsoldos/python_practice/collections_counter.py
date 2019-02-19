from collections import Counter
shoes = int(input())
sizes = Counter(list(map(int, input().split())))
cust = int(input())

revenue = 0

for c in range(cust):
    size, price = map(int, input().split())
    if sizes[size]:
        revenue += price
        sizes[size] -= 1

print(revenue)
