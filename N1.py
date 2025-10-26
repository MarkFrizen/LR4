def square(x):
    return x ** 2
numbers = list(range(1, 11))
squares = list(map(square, numbers))
print(squares)