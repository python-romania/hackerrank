# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import os


def calculate_mean(arr):
    return round(sum(arr) / len(arr), 1)


def calculate_median(arr):
    if len(arr) % 2 == 0:
        return round((arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2, 1)
    else:
        return arr[math.ceil(len(arr) / 2)]


def get_mode(arr):
    set_arr = set(arr)
    mode_elements_with_count = []
    mode_count = 0

    for x in set_arr:
        ct = arr.count(x)
        mode_elements_with_count.append((ct, x))
        if ct > mode_count:
            mode_count = ct

    return min([k[1] for k in mode_elements_with_count if k[0] == mode_count])


if __name__ == "__main__":
    # n = int(input())
    with open("day_0_mean_median_mode_input.txt") as txt:
        content = txt.read()
    arr = sorted(list(map(int, content.split())))

    result = []
    result.append(calculate_mean(arr))
    result.append(calculate_median(arr))
    result.append(get_mode(arr))

    print(result)

