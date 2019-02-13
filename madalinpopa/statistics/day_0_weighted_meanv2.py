nr = int(input())
values = input().split(" ")
index = input().split(" ")


def calculate(items, val, ind):
    result = 0
    sum_val = sum([int(val[i]) * int(ind[i])
                   for i in range(items)
                   if (items == len(val)) and (items == len(ind))])

    result = round(sum_val / sum([int(i) for i in ind]), 1)
    return result


print(calculate(nr, values, index))
