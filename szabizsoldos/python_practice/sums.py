lst = "1 3 6 7 8 2 3 5"
lst = lst.split()

def calculate_fn(nums):
    return sum([int(i) for i in nums])


print(calculate_fn(lst))
