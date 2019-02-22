import fileinput
import os
import datetime

fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, '../scrapy/tutorial/new_products.csv')
new_filename = os.path.join(fileDir, '../scrapy/tutorial/no_duplicates_products.csv')
os.remove(new_filename)

with open(filename, 'r') as in_file, open(new_filename, 'w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)
