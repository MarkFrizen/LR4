def log_decorator(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            _log_call(message, func, args, kwargs)
            result = func(*args, **kwargs)
            _log_result(message, func, result)
            return result
        return wrapper
    return decorator
def _log_call(message, func, args, kwargs):
    print(f"[{message}] Вызов функции '{func.__name__}'")
def _log_result(message, func, result):
    print(f"[{message}] Функция '{func.__name__}' вернула: {result}")
@log_decorator("INFO")
def add(a, b):
    return a + b
if __name__ == "__main__":
    add(3, 5)