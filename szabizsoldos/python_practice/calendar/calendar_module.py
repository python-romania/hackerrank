import calendar


dt = list(map(int, input().split()))
day, month, year = dt[1], dt[0], dt[2]

c = calendar.weekday(year, month, day)
print(calendar.day_name[c].upper())
