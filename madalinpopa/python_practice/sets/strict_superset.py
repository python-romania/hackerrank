# STEP 1: Get the input
a = set(input().split())
n = int(input())


found = [] # store boolean values if found or not

# STEP 2: Check each subset  
for i in range(n):
    sub_set = set(input().split())
    if a.issuperset(sub_set):
        found.append(True)
    else:
        found.append(False)

if False in found:
    print(False)
else:
    print(True)
