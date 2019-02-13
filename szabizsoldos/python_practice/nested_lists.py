from operator import itemgetter
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students.append([name, score])
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 40]]
students = sorted(students, key=itemgetter(1))
second_highest = None
for i in range(5):
    second_highest = students[0][1]
    for name, grade in students:
        if grade > second_highest:
            second_highest = grade
            break
print('\n'.join([name for name, grade in sorted(students) if grade == second_highest]))
