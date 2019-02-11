import sys
from math import ceil
from statistics import median


n, *nums = [int(num)
            for num
            in sys.stdin.read().split()]

nums.sort()

q2 = median(nums)

half1, half2 = nums[:n // 2], nums[ceil(n / 2):]

q1 = median(half1)
q3 = median(half2)

q1, q2, q3 = round(q1), round(q2), round(q3)

print(q1, q2, q3, sep = '\n')
