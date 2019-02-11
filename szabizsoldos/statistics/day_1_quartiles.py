total_integers = int(input())
integer_list = input()
integer_list_collection = list(map(int, integer_list.split()))

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

def calculate_quartiles(total_integers, integer_list_collection):

    if total_integers != None and total_integers > 0:

        sorted_list = sorted(integer_list_collection)

        if(total_integers % 2 == 1):

            q2 = int(calculate_median(integer_list_collection))
            q1 = int(calculate_median(integer_list_collection[0:integer_list_collection.index(q2)]))
            q3 = int(calculate_median(integer_list_collection[integer_list_collection.index(q2)+1:]))

            print(q1)
            print(q2)
            print(q3)

        else:

            lower_half = sorted_list[0:int(len(sorted_list) / 2)]
            upper_half = sorted_list[int(len(sorted_list) / 2):]

            q2 = int(calculate_median(sorted_list))
            q1 = int(calculate_median(lower_half))
            q3 = int(calculate_median(upper_half))

            print(q1)
            print(q2)
            print(q3)
    else:
        return None


calculate_quartiles(total_integers, integer_list_collection)
