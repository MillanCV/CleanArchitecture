from typing import TYPE_CHECKING, TypedDict

from src.domain.entities import User
from src.domain.use_cases.dtos.user import UserData
from src.domain.use_cases.add_user import AddUserUseCase
from src.domain.use_cases.list_users import ListUsersUseCase

if TYPE_CHECKING:
    from src.presentation.view_interfaz import ViewInterfaz


class AddUserResult(TypedDict):
    success: bool
    user: User | None
    error: str | None


class ListUsersResult(TypedDict):
    users: list[User]
    error: str | None


class Presenter:
    """Presenter handles presentation logic and returns data structures.
    Rendering is handled by views (TerminalView, ApiView).
    """

    def __init__(
        self,
        view: "ViewInterfaz",
        add_user_use_case: AddUserUseCase,
        list_users_use_case: ListUsersUseCase,
    ):
        self.view = view
        self.add_user_use_case = add_user_use_case
        self.list_user_use_case = list_users_use_case

    def add_user(self, user_data: UserData) -> AddUserResult:
        """Add a user and return result data structure."""
        try:
            user = self.add_user_use_case.execute(user_data=user_data)
            return {"success": True, "user": user, "error": None}
        except ValueError as e:
            return {"success": False, "user": None, "error": str(e)}

    def list_users(self) -> ListUsersResult:
        """List all users and return result data structure."""
        try:
            users = self.list_user_use_case.execute()
            return {"users": users, "error": None}
        except ValueError as e:
            return {"users": [], "error": str(e)}
