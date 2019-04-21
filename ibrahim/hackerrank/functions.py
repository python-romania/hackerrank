def is_leap(leap_year):
    leap = False

    if leap_year % 4 == 0 and (leap_year % 100 != 0 or leap_year % 400 == 0):
        leap = True

    return leap


year = int(input())
print(is_leap(year))
