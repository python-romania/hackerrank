class Dog:

    # self.tricks = [] is not the same as declaring it in
    # __init__ method, it will be shared by all objects

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


a = Dog('Vizsla')
a.add_trick('roll overs')

b = Dog('Labrador')
b.add_trick('jump')

print(a.name, a.tricks)
print(b.name, b.tricks)
