def count_substring(string_, lookup_):
    count, start = 0, 0
    flag = True

    while flag:
        a = string_.find(lookup_, start)
        if a == -1:
            flag = False
        else:
            count += 1
            start = a + 1
    return count


string = str(input())
lookup = str(input())

print(count_substring(string, lookup))
