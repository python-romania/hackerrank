import itertools

classifications = ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC', 'DA', 'DC']
classifications.reverse()
classification_values = (i for i in range(0, 21, 2))
classification_data = list(itertools.zip_longest(classification_values, classifications))


print(classification_data)
