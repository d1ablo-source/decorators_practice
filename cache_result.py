from functools import wraps


def cache_result(func):
    saved = {}
    @wraps(func)
    def wrapper(*args):
        key = (args)
        if key in saved:
            print("Берём из кэша")
            return saved[key]
        print("Вычисляем...")
        result = func(*args)
        saved[key] = result
        return result
    return wrapper

@cache_result
def calculate_cache(a, b):
    return a * b

print(calculate_cache(2, 6))
print(calculate_cache(132, 123))
print(calculate_cache(2, 6))
