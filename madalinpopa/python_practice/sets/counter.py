from collections import Counter

X = int(input())
shoes = [int(val) for val in input().split()]
N = int(input())

shoe_collection = Counter(shoes)
total_money = 0

for i in range(N):
    size, money = [int(val) for val in input().split()]

    if shoe_collection.get(size):
        total_money += money
        shoe_collection[size] -= 1

print(total_money)