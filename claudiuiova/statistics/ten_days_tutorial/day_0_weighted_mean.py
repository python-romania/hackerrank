# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import functools


def calculate_weighted_mean(data, weights):
    zipped_elements = list(zip(data, weights))
    elements_sum = sum(list(map(lambda k: functools.reduce(lambda y, z: y*z, k), zipped_elements)))

    return round(elements_sum / sum(weights), 1)


if __name__ == "__main__":
    inputs = sys.stdin.readlines()
    number_of_elements = int(inputs[0])
    input_data = list(map(int, inputs[1].split()))
    input_weights = list(map(int, inputs[2].split()))

    result = calculate_weighted_mean(input_data, input_weights)

    sys.stdout.write(str(result))

