T = int(input())  # number of test cases


for i in range(T):
    al_ = int(input())
    as_ = set(list(map(int, input().split())))

    bl_ = int(input())
    bs_ = set(list(map(int, input().split())))

    if as_.issubset(bs_):
        print(True)
    else:
        print(False)
