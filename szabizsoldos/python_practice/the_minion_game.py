def minion_game(string_):
    vowels = "AEIOU"
    string_len = len(string_)
    kevin_sc, stuart_sc = 0, 0
    for i in range(string_len):
        if string_[i] in vowels:
            kevin_sc += (string_len - i)
        else:
            stuart_sc += (string_len - i)

    if kevin_sc > stuart_sc:
        print('Kevin', kevin_sc)
    elif kevin_sc < stuart_sc:
        print('Stuart', stuart_sc)
    else:
        print('Draw')


s = str(input())
minion_game(s)
