#   Problema:
#   Avem o lista de preturi si in fiecare zi un pret nou este adaugat in lista.
#   Sa se afle media preturilor dupa fiecare pret adaugat.


def make_averager():
    history = []

    def average(n):
        history.append(n)
        return {
            'entries': len(history),
            'result': sum(history) / len(history)
        }
    return average



avg = make_averager()
avg(10)
avg(20)
avg(30)
avg(40)
print(avg(0))
