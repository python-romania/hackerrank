import math


def calculate_mean(numbers_):
    mean_ = None
    if len(numbers_) > 0:
        mean_ = round(sum(number for number in numbers_) / len(numbers_), 1)
    return mean_


def avg_mean_distance(numbers_):
    # using absolute
    # return sum(abs(number - mean) for number in numbers) / len(numbers)

    # average square distance to the mean
    # name of data = variance
    mean = calculate_mean(numbers_)
    average_square_distance_to_mean = sum(((number - mean) ** 2) for number in numbers_) / len(numbers_)
    distance = round(math.sqrt(average_square_distance_to_mean), 1)
    return distance


# expecting int: ex. 5
total = input()

# expecting list: ex. 1 2 3 4 5
nums = list(map(int, input().split()))
avg_mean_dist = avg_mean_distance(nums)

print(avg_mean_dist)
