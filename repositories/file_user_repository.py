from entities import User
class FileUserRepository:

    def __init__(self, filename: str):
        self.__filename = filename
        self.__users = self._load_users()

    def _load_users(self):
        try:
            with open(self.__filename, "r") as file:
                users = {}
                for line in file:
                    email, password, name, created = line.strip().split(";")
                    users[email] = User(email, password, name, created = None)
                    return users
        except FileNotFoundError:
            return {}

    def add_user(self, user: User):
        if user.email in self.__users:
            raise ValueError("E-mail already exists")
        self.__users[user.email] = user
        self._save_users()

    def _save_users(self):
        with open(self.__filename, "w") as file:
            for user in self.__users.values():
                file.write(f"{user.email};{user.password};{user.name};{user.created}\n")

    def get_user(self, email: str) -> User:
        if email not in self.__users:
            raise ValueError("User not found")
        return self.__users[email]

    def validate_user (self, email: str, password: str) -> bool:
        user = self.get_user(email)
        return user.password == password


