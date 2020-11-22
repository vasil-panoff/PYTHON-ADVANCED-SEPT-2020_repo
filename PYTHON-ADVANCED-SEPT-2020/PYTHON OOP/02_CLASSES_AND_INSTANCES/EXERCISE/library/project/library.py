from typing import Dict, List, ClassVar

from project.user import User


class Library:
    user_records: List[User]
    books_available: Dict[str, List[str]]
    rented_books: Dict[str, Dict[str, int]]

    def add_user(self, user: User):
        if user in self.user_records:  # NOTE: This may fail
            return f'User with id = {user.user_id} already registered in the library!'

        self.user_records.append(user)

    def remove_user(self, user: User):
        if user not in self.user_records:
            return f'We could not find such user to remove!'

        self.user_records.remove(user)
        del self.rented_books[user.username]   # NOTE: This may be false

    def change_user(self, user_id: int, new_user_id: int):
        user_ids = [u.id for u in self.user_records]
        if user_id not in user_ids:
            return f'There is no user with id = {user_id}!'
        user = self.user_records[user_ids.index(user_id)]
        if user.username == new_username:
            return 'Please check again the provided username - it should be different than the username used so far!'