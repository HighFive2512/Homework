from library import Library
from user import User

class Registration:
    def add_user(user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user.user_id)
        else:
            return f"User with id = {user.user_id} already registered in the library!"
    def remove_user(user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user.user_id)
        else:
            return "We could not find such user to remove!"
    def change_username(user_id: int, new_username: str, library: Library):
        if user_id in library.user_records:
            if User.user_id