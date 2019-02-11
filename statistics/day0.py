import statistics
import collections

count = input("NR: ")
values = str(input("VALUES: ")).split(" ")

def func(n):

    mean = statistics.mean([int(nr) for nr in n ])
    median = statistics.median([int(nr) for nr in n])
    mode = min(collections.Counter([int(nr) for nr in n]))

    print(mean)
    print(median)
    print(mode)


func(values)

