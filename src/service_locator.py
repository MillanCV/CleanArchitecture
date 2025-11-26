from src.domain.repositories.repository import UserRepository
from src.domain.use_cases.add_user import AddUserUseCase
from src.domain.use_cases.list_users import ListUsersUseCase
from src.infrastructure.in_memory_repository import InMemoryRepository
from src.presentation.terminal.terminal_view import Terminal
from src.presentation.presenter import Presenter


class ServiceLocator:
    def __init__(self):
        self.repository: UserRepository = InMemoryRepository

        self.view = Terminal()
        self.presenter = Presenter(
            view=self.view,
            add_user_use_case=AddUserUseCase(self.repository),
            list_users_use_case=ListUsersUseCase(self.repository),
        )
        self.view.presenter = self.presenter
