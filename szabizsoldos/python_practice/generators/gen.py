xvec = [10, 20, 30]
yvec = [7, 5, 3]

zipped = sum(x*y for x, y in zip(xvec, yvec))
print(zipped)
