from src.domain.use_cases.add_user import AddUserUseCase
from src.domain.use_cases.list_users import ListUsersUseCase
from src.presentation.view_interfaz import ViewInterfaz


class Presenter:
    def __init__(
        self,
        view: ViewInterfaz,
        add_user_use_case: AddUserUseCase,
        list_users_use_case: ListUsersUseCase,
    ):
        self.view = view
        self.add_user_use_case = add_user_use_case
        self.list_user_use_case = list_users_use_case

    def add_user(self):
        self.view.show("")
        name = self.view.get_input("Name: ")
        email = self.view.get_input("Email: ")
        password = self.view.get_input("Password: ")

        self.view.show(f"{name} {email} {password}")
