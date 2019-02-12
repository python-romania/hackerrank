input_nums = int(input())
raw_nums = input()
input_nums_list = list(map(int, raw_nums.split()))


def median_func(nums_list):
    if nums_list:
        nums_list.sort()

        if len(nums_list) % 2 == 0:
            half = int(len(nums_list) / 2)
            median = int(nums_list[half - 1]) + int(nums_list[half])
            median = median / 2
        else:
            median = int(nums_list[int(len(nums_list) / 2)])
        return round(median, 1)
    else:
        return None


def quartiles(total_nums, nums_list):
    if total_nums and nums_list and len(nums_list) > 0:
        sorted_list = sorted(nums_list)

        if total_nums % 2 == 1:
            q2 = int(median_func(nums_list))
            q1 = int(median_func(nums_list[0:nums_list.index(q2)]))
            q3 = int(median_func(nums_list[nums_list.index(q2)+1:]))
        else:
            lower_half = sorted_list[0:int(len(sorted_list) / 2)]
            upper_half = sorted_list[int(len(sorted_list) / 2):]

            q2 = int(median_func(sorted_list))
            q1 = int(median_func(lower_half))
            q3 = int(median_func(upper_half))

    else:
        q1, q2, q3 = None, None, None

    return {'q1': q1, 'q2': q2, 'q3': q3}


quartiles = quartiles(input_nums, input_nums_list)
for quartile in quartiles.values():
    print(quartile)
