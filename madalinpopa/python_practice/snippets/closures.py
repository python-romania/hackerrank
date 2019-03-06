# Problema:
# Avem o lista de preturi si in fiecare zi un pret nou este adaugat in lista.
# Sa se afle media preturilor dupa fiecare pret adaugat.
#

# Varianta 1


class Average:
    def __init__(self):
        self._history = []

    def __call__(self, new_value):
        self._history.append(new_value)
        total = sum(self._history)
        return total / len(self._history)


avg = Average()
print(avg(10))  # 10.0
print(avg(11))  # 10.5
print(avg(12))  # 11.0


# Varianta 2

def make_averager():
    history = [] # variablila locala functie make_averager

    def average(new_value):
        history.append(new_value)
        total = sum(history)
        return total / len(history)

    return average


avg = make_averager()
print(avg(10)) # 10.0
print(avg(11)) # 10.5
print(avg(12)) # 11.0
