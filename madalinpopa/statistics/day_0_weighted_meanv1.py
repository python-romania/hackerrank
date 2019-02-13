# input
# nr = 5
# values = "10 40 30 50 20".split(" ")
# index = "1 2 3 4 5".split(" ")


nr = int(input())
values = input().split(" ")
index = input().split(" ")


def calculate(val, index, lenght):
    result = 0
    sum_val = 0

    lenght_values = len(val)
    lenght_index = len(index)

    if lenght_values == lenght and lenght_index == lenght:
        for i in range(lenght):
            sum_val += int(values[i]) * int(index[i])

    result = round(sum_val / sum([int(i) for i in index]), 1)

    return result


print(calculate(values, index, nr))
