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



def quartiles_func(total_nums, nums_list):
    sorted_list = sorted(nums_list)

    if total_nums % 2 == 1:
        lower_half = sorted_list[0:int(len(sorted_list) / 2)]
        upper_half = sorted_list[int(len(sorted_list) / 2)+1:]
    else:
        lower_half = sorted_list[0:int(len(sorted_list) / 2)]
        upper_half = sorted_list[int(len(sorted_list) / 2):]

    q2 = int(median_func(sorted_list))
    q1 = int(median_func(lower_half))
    q3 = int(median_func(upper_half))

    return {'q1': q1, 'q2': q2, 'q3': q3}

def interquartile_func(nums, elements, frequencies):
    dataset_container = []
    for index, el in enumerate(elements):
        for i in range(frequencies[index]):
            dataset_container.append(el)
    quartiles = quartiles_func(nums, dataset_container)
    interquartile = quartiles.get('q3') - quartiles.get('q1')
    return float(interquartile)


input_nums = int(5)
elms = "10 40 30 50 20"
freqs = "1 2 3 4 5"

input_elms = list(map(int, elms.split()))
input_freq = list(map(int, freqs.split()))

print(interquartile_func(input_nums, input_elms, input_freq))
