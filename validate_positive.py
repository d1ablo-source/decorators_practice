from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in [*args, *kwargs.values()]:
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError(f"{func.__name__}: expected int, got {value!r}")
            if value <= 0:
                raise ValueError(f"{func.__name__}: expected > 0, got {value!r}")
        return func(*args, **kwargs)
    return wrapper


@validate_positive
def user_id(id: int):
    return id

print(user_id(2))
print(user_id("abc"))