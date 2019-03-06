#   flc = first_level_class
#   slc = second_level_class
def get_gauge_value_by_classes(flc, slc):

    associations = {
        'AA': 11.5, 'AB': 10.5, 'AC': 9.5,
        'BA': 8.5, 'BB': 7.5, 'BC': 6.5,
        'CA': 5.5, 'CB': 4.5, 'CC': 3.5,
        'DA': 2.5, 'DC': 1.5,
    }

    if str(flc).isalpha() and str(slc).isalpha():
        compound = flc+slc
        return associations[compound]


first_level_class = 'A'
second_level_class = 'B'

result = get_gauge_value_by_classes(first_level_class, second_level_class)
for i in range(1, 12+1):
    if i < result < i + 1:
        print('gaguge between {} and {} at {}'.format(i, i+1, result))

