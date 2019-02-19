if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    if 2 <= n <= 10:
        data = []
        for i in arr:
            if -100 <= i <= 100:
                if i not in data:
                    data.append(i)
        print(sorted(data, reverse=True)[1])
