x = [3, 9, 2, 6, 5]


def bubbleSort(dataset):
    # start with the array length and decrement each time
    for i in range(len(dataset) - 1, 0, -1):
        # examine each item pair
        for j in range(i):
            # swap items if needed
            if dataset[j] > dataset[j + 1]:
                print("dataset[j]: ", dataset[j])
                temp = dataset[j]
                dataset[j] = dataset[j + 1]
                print("dataset[j + 1]: ", dataset[j])
                dataset[j + 1] = temp
                print("dataset[j + 1]: ", dataset[j])

        print("Current state: ", dataset)


def bubble(data):
    for i in range(len(data) -1, 0, -1):
        for j in range(i):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    return data


bubbleSort(x)
