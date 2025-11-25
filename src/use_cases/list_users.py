from src.repositories.repository import UserRepository
from src.entities import User


class ListUsersUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self) -> list[User]:
        return self.repository.get_users()
