cars = {
        'dacia': 'Duster',
        'skoda': 'Kodiaq',
        'ford': 'Focus'
}

def foo(dacia, skoda, ford):
    print("First car ", dacia, ", second car ", skoda, ", third car ", ford, sep='')

foo(**cars)
