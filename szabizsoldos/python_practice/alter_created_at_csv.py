import csv
import os
import datetime

fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, '../scrapy/tutorial/products.csv')
new_filename = os.path.join(fileDir, '../scrapy/tutorial/new_products.csv')

new_file = []
with open(filename, newline='') as csv_file:
    products_reader = csv.reader(csv_file, delimiter=',')
    i = 0
    for row in products_reader:
        if i > 0:
            row[7] = row[7].split(" ")
            row[7] = row[7][0]
            # if row in new_file:
            #     print('existing row found')
            #     continue
            # else:
            #     print('new row added')
            new_file.append(row)
        else:
            new_file.append(row)
        i += 1

with open(new_filename, 'w', newline='') as csvfile:
    products_write = csv.writer(csvfile, delimiter=',')
    for row in new_file:
        products_write.writerow(row)
    print("Finished writing file")
