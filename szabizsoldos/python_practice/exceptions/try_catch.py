T = int(input())

for i in range(T):
    op = input().split()
    try:
        print(int(int(op[0]) / int(op[1])))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
