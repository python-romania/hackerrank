
# get the input from stdin
count = input("NR: ")
values = str(input("VALUES: ")).split(" ")


# sort list function
def bubbleSort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    return data


