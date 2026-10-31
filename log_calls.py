from functools import wraps



def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        parts = [repr(a) for a in args]
        parts += [f"{k}={v!r}" for k, v in kwargs.items()]
        call = f"{func.__name__}({', '.join(parts)})"
        print(f"calling {call}")
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"{call} raised {type(e).__name__}: {e}")
            raise  # пробрасываем оригинальное исключение
        print(f"{call} -> {result!r}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

print(add(2, b=3))
print(add(2, b="1"))