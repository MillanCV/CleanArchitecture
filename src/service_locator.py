from src.domain.repositories.repository import UserRepository
from src.domain.use_cases.add_user import AddUserUseCase
from src.domain.use_cases.list_users import ListUsersUseCase
from src.infrastructure.in_memory_repository import InMemoryRepository
from src.presentation.terminal.terminal_view import Terminal
from src.presentation.presenter import Presenter


class ServiceLocator:
    def __init__(self):
        # Repositories
        self._repository: UserRepository = InMemoryRepository()

        # View
        self._view = Terminal()

        # Presenter
        self._presenter = Presenter(
            view=self._view,
            add_user_use_case=AddUserUseCase(self._repository),
            list_users_use_case=ListUsersUseCase(self._repository),
        )

    @property
    def view(self):
        return self._view

    @property
    def presenter(self):
        return self._presenter
