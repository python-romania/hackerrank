def merge_the_tools(string, k):
    # STEP 1: Split the list as per given K
    parts = []
    for i in range(0, len(string), k):
        parts.append(string[i:i+k])

    # STEP 2: Remove duplicats
    output = []
    for part in parts:
        temp_part = []
        for letter in part:
            if letter not in temp_part:
                temp_part.append(letter)
        output.append(temp_part)

    # STEP 3: Print the output
    for i in range(len(output)):
        print("".join(output[i]))

if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)