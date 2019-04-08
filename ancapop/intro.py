
print("hello, acesta este primul proiect PYTHON !")
x = 3
print(x)
x = 4
print(x)
print(x + 4)
x = (x + 4)
print(x)
#programare imperativa
#adik x poate fii si 3 si 4, citirea se face pe linii una dupa alta nu simultan

"""
name = input("care este numele tau?")
print('Hi ' + name)
culoarea_preferata = input("care este culoarea ta preferata ?")
print("Culoarea mea preferata este " + culoarea_preferata)
"""
a = 4 + 5
print(a)

a = a + 8

print(a)


#this program adds to variables and shows up the sum

a = 5 #variable named 'a'
b = 4 #variable named 'b'

sum = a + b

print (sum)


# f5 pentru a rula modulul, apoi dai type(a)shell si ruleaza valoarea lui a

a = 5 #integer
b = 3.12 #float numbers
# strign - sequence of characters
name = 'Anca'

sentence = 'I\'m from blabla'

isBig = False  # bool BOOLEAN
sizeOfSection = 4 #camelcase - case senzitive
print (isBig)
"""
arithmetic operators

+ add
- substract
* multiply  a se folosi asterix nu litera x in python

/ divide  ---rezultatul  apare ca float number de fiecare data la impartire

() - parenthesis -- for changing order of math operation--

** raising -- ridicarea la putere
// floor division --rezultatul este doar numarul intred de dinaintea virgulei--
% - modulo - the remainder operators(what is left after division)ce ramane dupa impartire ca intreg
"restul"

"""
VAT = 25
calculatedVAT = (1 + VAT / 100) # in RAM

netPriceOfShoes = 100
netPriceOfTv = 2000
netPriceOfXccc = 500
netPriceOfXfff = 600

 # grossPriceOfShoes = netPriceOfShoes * (1 + VAT / 100)
grossPriceOfShoes = netPriceOfShoes * calculatedVAT
grossPriceOfTv = netPriceOfTv * calculatedVAT
grossPriceOfXccc = netPriceOfXccc * calculatedVAT
grossPriceOfXfff = netPriceOfXfff * calculatedVAT

x = 5; y = 3; z = 5
# daca declaram variabile in continuare, le despartim prin punct si virgula intre ele, dar nu si dupa ultima variabila declarata

a,b,c = 1,"test",True

i = j = k = 1

print (i)


'''

+=   x += 5  it is a short way of writing: x = x +5
-=   x -= 5  it is a short way of writing: x = x - 5
*=   x *= 5  it is a short way of writing: x = x * 5
/=   x /= 5  it is a short way of writing: x = x / 5
%=   x %= 5  it is a short way of writing: x = x % 5
//=  x //= 5  it is a short way of writing: x = x // 5
**=  x ** = 5  it is a short way of writing:  x = x ** 5

'''


name = "anca"
lastName = "ioana"

fullName = name + " " + lastName

print(fullName)

print(lastName[1])
print(lastName[2])
print(lastName[:3])
print(lastName[3:])
print(lastName[-1])
