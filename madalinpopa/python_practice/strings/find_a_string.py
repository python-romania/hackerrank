def count_substring(string, sub_string):
    if 1 <= len(string) <= 200:
        counter = 0
        i = 0
        while i < len(string):
            if string.find(sub_string, i) >= 0:
                i = string.find(sub_string, i) + 1
                counter += 1
            else:
                break
        return counter



if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'
    count = count_substring(string, sub_string)
    print(count)