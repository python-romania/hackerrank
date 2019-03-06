
l1 = [1, 2, 3]
l2 = list(l1)

l1.append(4)
l2.append(5)

print(l1)
print(l2)

print(l1 == l2)
print(l2 is l1)
print(id(l1))
print(id(l2))

