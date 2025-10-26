def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def print_fibonacci(n):
    fib_gen = fibonacci()
    for _ in range(n):
        print(next(fib_gen))
if __name__ == "__main__":
    print_fibonacci(10)