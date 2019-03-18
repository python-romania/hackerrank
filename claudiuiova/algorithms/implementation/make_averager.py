class MakeAverage(object):

    @staticmethod
    def make_averager():
        history = []

        def average(new_value):
            history.append(new_value)
            total = sum(history)
            return total / len(history)

        return average

    def __enter__(self):
        return self

    def __del__(self):
        del self

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self


with MakeAverage() as avg_object:
    avg = avg_object.make_averager()
    print(avg(10))  # 10.0
    print(avg(11))  # 10.5
    print(avg(12))  # 11.0

print(avg(12))
