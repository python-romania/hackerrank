import numpy as np

#
# ints = list(map(int, input().split()))
# ops = []
# # for i in ints:
# a = [list(map(int, input().split()))]
# b = [list(map(int, input().split()))]
#
# numpy.set_printoptions(formatter=None, suppress=True)
#
# print(numpy.add(a, b, dtype=numpy.int))
# print(numpy.subtract(a, b, dtype=numpy.int))
# print(numpy.multiply(a, b, dtype=numpy.int))
# print(numpy.array(a) // numpy.array(b))
# print(numpy.mod(a, b, dtype=numpy.int))
# print(numpy.power(a, b, dtype=numpy.int))

n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a % b, a**b, sep='\n')
