def fibonacci(n):    # write Fibonacci series up to n
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b


n = int(input())
cube = lambda x: pow(x, 3)  # x ** 3

print(list(map(cube, fibonacci(n))))
