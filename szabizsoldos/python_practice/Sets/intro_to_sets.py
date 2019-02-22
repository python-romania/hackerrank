def average(array):
    s = set()
    for i in array:
        s.add(i)

    return sum(s) / len(s)


n = int(10)
arr = list(map(int, '161 182 161 154 176 170 167 171 170 174'.split()))
result = average(arr)
print(result)
