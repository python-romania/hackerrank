from collections import namedtuple

# Point = namedtuple('Point','x,y')
# pt1 = Point(1, 2)
# pt2 = Point(3, 4)
#
# dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y) # (1*3) + (2*4) = 11
#
# Car = namedtuple('Car', 'Price Mileage Colour Class')
# xyz = Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')

N = int(input())
fields = input().split()

total = 0
for i in range(N):
    students = namedtuple('student', fields)
    column1, column2, column3, column4 = input().split()
    student = students(column1, column2, column3, column4)
    total += int(student.MARKS)

print('{:.2f}'.format(total/N))
