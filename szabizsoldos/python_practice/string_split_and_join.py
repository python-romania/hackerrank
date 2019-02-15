def split_and_join(line):
    return '-'.join(line.split())


line = input()
result = split_and_join(line)
print(result)
