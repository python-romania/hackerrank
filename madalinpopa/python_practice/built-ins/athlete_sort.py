#!/bin/python3

# get the number of rows (athletes) and columns(attributes)
athletes, attributes = (int(x) for x in input().split())

# get the rows with attributes for each athlete
rows = []
for _ in range(athletes):
    rows.append([int(x) for x in input().split()])

# chose an attribute (column) to sort rows
sort_by = int(input())

rows.sort(key=lambda row: row[sort_by])

for row in rows:
    print(*row)


