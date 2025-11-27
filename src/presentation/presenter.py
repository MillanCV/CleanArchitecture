from src.domain.entities import User
from src.domain.use_cases.dtos.user import UserData
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
        self.view.show("=" * 50)
        self.view.show("Adding a new user")
        self.view.show("=" * 50)
        self.view.show("")

        name = self.view.get_input("Name: ")
        email = self.view.get_input("Email: ")
        password = self.view.get_input("Password: ")

        street_address = self.view.get_input("Street address: ")
        postal_code = self.view.get_input("Postal Code: ")
        city = self.view.get_input("City: ")

        userData = UserData(
            name=name,
            email=email,
            password=password,
            street_address=street_address,
            postal_code=postal_code,
            city=city,
        )

        try:
            user = self.add_user_use_case.execute(user_data=userData)
        except ValueError as e:
            self.show_error(str(e))
        else:
            self.show_success_message("User added successfully")
            self.show_user(user)
            self.view.show("")

    def list_users(self):
        try:
            users = self.list_user_use_case.execute()
        except ValueError as e:
            self.show_error(str(e))
        else:
            if len(users) == 0:
                self.show_message_with_separators("No users found")
                return

            self.show_message_with_separators("Listing users")
            for user in users:
                self.show_user(user)
                self.view.show("")

    # Show user
    def show_user(self, user: User):
        self.view.show("=" * 50)
        self.view.show("")
        self.view.show(user)
        self.view.show("")
        self.view.show("=" * 50)

    def show_welcome(self):
        self.view.show("")
        self.view.show("=" * 50)
        self.view.show("Welcome to the app")
        self.view.show("=" * 50)
        self.view.show("")

    def show_menu(self):
        self.view.show("Choose an option")
        self.view.show("=" * 50)
        self.view.show("1 - Add user")
        self.view.show("2 - List users")
        self.view.show("3 - Exit")
        self.view.show("")

    def get_menu_choice(self) -> str:
        return self.view.get_input("Choose option (1-3): ")

    def show_separator(self):
        self.view.show("=" * 50)

    def show_goodbye(self):
        self.view.show("")
        self.view.show("=" * 50)
        self.view.show("Goodbye!")
        self.view.show("=" * 50)
        self.view.show("")

    def show_invalid_option(self):
        message = "Invalid option. Please select 1, 2, or 3."
        self.show_message_with_separators(message)

    def show_error(self, error_message: str):
        self.view.show("")
        self.view.show("=" * 50)
        self.view.show("Something went wrong")
        self.view.show(f"Error: {error_message}")
        self.view.show("=" * 50)
        self.view.show("")

    def show_success_message(self, message: str):
        self.view.show("")
        self.view.show("=" * 50)
        self.view.show(message)
        self.view.show("=" * 50)
        self.view.show("")

    def show_message_with_separators(self, message: str) -> None:
        self.view.show("")
        self.view.show("=" * 50)
        self.view.show(message)
        self.view.show("=" * 50)
        self.view.show("")
