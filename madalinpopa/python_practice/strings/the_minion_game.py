def minion_game(s):
    vowels = "AEIOU"
    lens = len(s)
    kscore, stscore = 0, 0
    for i in range(lens):
        if s[i] in vowels:
            kscore += (lens - i)
        else:
            stscore += (lens - i)

    if kscore > stscore:
        print('Kevin', kscore)
    elif kscore < stscore:
        print('Stuart', stscore)
    else:
        print('Draw')


s = 'BANANA'
minion_game(s)