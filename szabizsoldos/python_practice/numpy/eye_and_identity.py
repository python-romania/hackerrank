import numpy

arr = list(map(int, input().split()))

print(str(numpy.eye(arr[0], arr[1], k=0)).replace('1', ' 1').replace('0', ' 0')) # using replace only for hackerrank test case bug
