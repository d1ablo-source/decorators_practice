import time
from functools import wraps
from math import sqrt

UNITS = {"s": 1, "ms": 1000}

def timer(unit):
    if unit not in UNITS:
        raise ValueError(f"unit must be on of {list(UNITS)}")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("БРОСАЮ")
            start = time.perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                elapsed = (time.perf_counter() - start) * UNITS[unit]
                print(f"Время падения: {elapsed:.2f}{unit}")
        return wrapper
    return decorator



@timer(unit="ms")
def falling(height):
    time.sleep(sqrt(2))
    print(f"Упал с высоты {height}м")

falling(10)
