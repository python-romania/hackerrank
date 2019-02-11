import sys
from math import ceil
from itertools import chain
from statistics import median


n, *data = list(map(int, sys.stdin.read().split()))
nums, freqs = data[:n], data[n:]

n = sum(freqs)
nums = sorted(list(chain.from_iterable((num,) * freq 
                                       for num, freq 
                                       in zip(nums, freqs))))

q2 = median(nums)

half1, half2 = nums[:n // 2], nums[ceil(n / 2):]

q1 = median(half1)
q3 = median(half2)

iqr = float(q3 - q1)

print(iqr)
