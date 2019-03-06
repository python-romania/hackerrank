from car_module.CarClass import Car


class Mercedes(Car):
    def __init__(self, make, model, color):
        Car.__init__(self, make, model, color)


mercedes = Mercedes('Mercedes-Benz', 'S-class', 'black')
print(mercedes.get_make())
print(mercedes.get_model())
print(mercedes.get_color())
