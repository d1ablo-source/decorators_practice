from functools import wraps

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0   # после @wraps, чтобы не затереть
    return wrapper

@count_calls
def add(a, b):
    print(f"result function: ", end="")
    return a + b

print(add(2, 4))
print(add(2, 5))
print(add.calls)  # 2
print(add(2, 5))
print(add.calls)