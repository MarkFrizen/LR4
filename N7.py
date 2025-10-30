def log_decorator(func):
    def wrapper(*args, **kwargs):
        _log_call(func, args, kwargs)
        result = func(*args, **kwargs)
        _log_result(func, result)
        return result
    return wrapper


def _log_call(func, args, kwargs):
    print(f"Вызов функции '{func.__name__}' с аргументами: args={args}, kwargs={kwargs}")
def _log_result(func, result):
    print(f"Функция '{func.__name__}' вернула: {result}")



@log_decorator
def add(a, b):
    return a + b

@log_decorator
def minus(a, b):
    return a - b

if __name__ == "__main__":
    add(3, 5)
    minus(20, 4)