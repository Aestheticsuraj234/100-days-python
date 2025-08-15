from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args[0].is_admin:
            return func(*args, **kwargs)
        else:
            return "Unauthorized"

    return wrapper


@require_admin
def delete_user(user):
    return f"Deleted {user.name}"


user1 = {"name": "Suraj", "is_admin": True}

print(delete_user(user1))