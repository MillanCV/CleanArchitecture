from abc import ABC, abstractmethod

from src.domain.entities import User


class UserRepository(ABC):
    @abstractmethod
    def save_user(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def get_users(self) -> list[User]:
        pass
