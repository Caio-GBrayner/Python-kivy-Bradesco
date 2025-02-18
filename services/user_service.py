from repositories import IUserRepository
from entities import User

class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def create_user(self, email: str, password: str, name: str, created: str):
        user = User(name, email, password, created)
        self.user_repository.add_user(user)

    def login(self, email: str, password: str) -> bool:
        return self.user_repository.validate_user(email, password)

    def get_user_info(self, email: str) -> User:
        return self.user_repository.get_user(email)