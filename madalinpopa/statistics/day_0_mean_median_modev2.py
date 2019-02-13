# input
# count: 10
# values: 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

# get the input from stdin
count = input("NR: ")
values = input("VALUES: ").split(" ")


# sort list function
def bubbleSort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    return data


# calculate mean
def calculate_mean(data):
    total_sum_of_elements = sum([int(nr) for nr in data])
    mean = round(total_sum_of_elements / len(data), 1)

    return mean


# calculate median
def calculate_median(data):
    sorted_data = bubbleSort([int(nr) for nr in data])
    nr_of_elements = len(sorted_data)
    median = 0

    if nr_of_elements < 1:
        return None
    elif nr_of_elements % 2 == 1:
        median = sorted_data[nr_of_elements // 2]
    else:
        median = round(sum(
            sorted_data[nr_of_elements // 2 - 1:nr_of_elements // 2 + 1]) / 2,
                       1)

    return median


# calculate mode
def calculate_mode(data):
    elements = [int(nr) for nr in data]
    mode = 0

    counter = dict()

    for el in elements:
        if el not in counter:
            counter[el] = 1
        else:
            counter[el] += 1

    max_value = max([v for v in counter.values()])
    min_value = min([k for k in counter.keys()])

    if max_value > 1:
        mode = [k for k, v in counter.iteritems() if v == max_value]
    else:
        mode = min_value

    return mode


print(calculate_mean(values))
print(calculate_median(values))
print(calculate_mode(values))
