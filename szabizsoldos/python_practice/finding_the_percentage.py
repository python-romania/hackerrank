from decimal import Decimal

studs = int(input())

marks = {}
for i in range(1, studs+1):
    inpt = list(input().split())
    name = inpt[0]
    stud_avg = round(Decimal(sum(float(grade) for grade in inpt[1:]) / len(inpt[1:])), 2)
    marks[name] = name
    marks[name] = [grade for grade in inpt[1:]]
    marks[name]= {"avg": stud_avg}


student = str(input())
print(marks[student]['avg'])
