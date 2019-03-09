def make_averager():
    history = []  # variablila locala functie make_averager

    def average(new_value):
        history.append(new_value)
        total = sum(history)
        return total / len(history)

    return average


avg = make_averager()
print(avg(10)) # 10.0
print(avg(11)) # 10.5
print(avg(12)) # 11.0