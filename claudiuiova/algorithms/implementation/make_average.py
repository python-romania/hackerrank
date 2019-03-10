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

print(avg(10))
print(avg(11))
