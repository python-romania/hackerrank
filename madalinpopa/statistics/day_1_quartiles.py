# input
n = 10
x = "3 7 8 5 12 14 21 13 50 18".split(" ")

# Step 1: get the input
# n = int(input())
# x = input().split(" ")

# Step 2: transform and sort values
xlist = [int(i) for i in x]
xlist.sort()


# Step 3: find the median
def findm(lval):
    if lval:
        if len(lval) % 2 == 1:
            return lval[len(lval) // 2]
        elif len(lval) % 2 == 0:
            return sum(lval[len(lval) // 2 - 1: len(lval) // 2 + 1]) // 2
        else:
            return None


# Step 4: calculate the quartiles
def calcq(nval, lval):
    if nval > 0 and nval == len(lval):
        if len(lval) % 2 == 1:
            q1 = findm(lval[:lval.index(findm(lval))])
            q2 = findm(lval)
            q3 = findm(lval[lval.index(findm(lval) + 1):])
            print(q1, q2, q3, sep='\n')
        else:
            first_half = lval[:len(lval) // 2]
            second_half = lval[len(lval) // 2:]
            q1 = findm(first_half)
            q2 = findm(lval)
            q3 = findm(second_half)
            print(q1, q2, q3, sep='\n')


# Step 4: output
calcq(n, xlist)
