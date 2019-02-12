# from __future__ import braces

lines = input()
numbers = input()

def format_string_to_list(input_numbers):
    numbers = input_numbers.split()
    numbers = list(map(int, numbers))
    return numbers

numbers = format_string_to_list(numbers)

def calculate_mean(numbers):

    sum = 0
    mean = 0

    if(len(numbers) > 0):
        for number in numbers:
            sum += int(number)

        mean = sum / len(numbers)
        return round(mean, 1)



def calculate_median(numbers):
    median = 0
    half = 0

    if(len(numbers) > 0):
        numbers.sort()

        if len(numbers) % 2 == 0:
            half = int(len(numbers) / 2)
            median = int(numbers[half - 1]) + int(numbers[half])
            median = median / 2
        else:
            median = int(numbers[int(len(numbers) / 2)])

    return round(median, 1)


def calculate_mode(numbers):
    counts = {}
    more_counts = []

    for number in numbers:
        if number in counts:
            counts[number] = counts[number] + 1
        else:
            counts[number] = 1

    min_values = min(counts.values())
    max_values = max(counts.values())

    if(min_values == max_values):
        return min(counts)
    else:
        for idx in counts:
            if(counts[idx] == max_values):
                more_counts.append(idx)
        return min(more_counts)

print(calculate_mean(numbers))
print(calculate_median(numbers))
print(calculate_mode(numbers))
