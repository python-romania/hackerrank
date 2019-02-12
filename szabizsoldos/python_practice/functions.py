def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    else:
        if year % 100 == 0:
            leap = False
        else:
            if year % 4 == 0:
                leap = True
    
    return leap


input_year = int(input())
print(is_leap(input_year))
