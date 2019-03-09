import sys
from collections import Counter

n, *nums = [int(num)
            for num
            in sys.stdin.read().split()]

nums.sort()

mean = sum(nums) / n

median = (nums[n // 2]
          if n % 2 is 1
          else (nums[n // 2 - 1] + nums[n // 2]) / 2)

freqs = Counter(nums)
max_freq = max(freqs.values())
mode = min(val
           for val, freq
           in freqs.items()
           if freq == max_freq)

mean = round(mean, 1)
median = round(median, 1)

print(mean)
print(median)
print(mode)