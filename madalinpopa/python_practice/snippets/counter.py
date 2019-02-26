from collections import Counter

a = [1,2,3,4,5,1,3,3,1]
b = Counter(a)

print(f'Initial list: {a}')
print(f'Counter: {b}')

c = [[1,2],[3,4],[5,6]]

for i in range(len(c)):
    if c[i][0] in b:
        print(c[i][0])