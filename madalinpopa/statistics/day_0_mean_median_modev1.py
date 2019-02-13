import statistics
import collections

# input
# count: 10
# values: 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

count = input("NR: ")
values = str(input("VALUES: ")).split(" ")


def func(n):
    mean = round(statistics.mean([int(nr) for nr in n]), 1)
    median = round(statistics.median([int(nr) for nr in n]), 1)
    mode = 0

    counter = collections.Counter([int(nr) for nr in n])

    for nr in counter:
        if counter[nr] > 1:
            mode = max(counter)
        else:
            mode = min(counter)

    print(mean)
    print(median)
    print(mode)


func(values)

