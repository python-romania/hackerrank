total_integers = int(input())
integer_list = input()
weight_list = input()
integer_list_collection = list(map(int, integer_list.split()))
weight_list_collection = list(map(int, weight_list.split()))


def calculate_weighted_mean(integer_list_collection, weight_list_collection, total_input_integers):
    if len(integer_list_collection) == total_input_integers and len(weight_list_collection) == total_input_integers:
        upper_sum = 0;
        for i in range(total_input_integers):
            upper_sum += integer_list_collection[i] * weight_list_collection[i]

        weighted_mean = upper_sum / sum(weight_list_collection)
        return round(weighted_mean, 1)
    else:
        return None
print(calculate_weighted_mean(integer_list_collection, weight_list_collection, total_integers))
