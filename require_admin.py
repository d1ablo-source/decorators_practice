from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not kwargs.get("is_admin", False):
            return "Недостаточно прав"
        return func(*args, **kwargs)
    return wrapper

@require_admin
def delete_user(user_id, is_admin=False):
    print(f"id: {user_id}, is_admin: {is_admin}")
    return "Пользователь удалён"

print(delete_user(user_id=1, is_admin=True))
print(delete_user(3, False))