from abc import ABC, abstractmethod
from entities import User

class IUserRepository(ABC):
    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def get_user(self, email: str) -> User:
        pass

    @abstractmethod
    def validate_user(self, email: str, password: str) -> bool:
        pass