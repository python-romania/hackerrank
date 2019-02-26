# Input
a = int('4')
b = set('2 4 5 9'.split())
c = int('4')
d = set('2 4 11 12'.split())

# STEP 1: Print the result
output = set()
output.update(b.difference(d))
output.update(d.difference(b))
x = sorted(output, key=lambda i: int(i))
print(*x, sep='\n')
