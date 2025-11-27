from typing import TYPE_CHECKING

from src.presentation.view_interfaz import ViewInterfaz
from src.domain.use_cases.dtos.user import UserData

if TYPE_CHECKING:
    from src.presentation.presenter import Presenter


class Terminal(ViewInterfaz):
    def show(self, message: str) -> None:
        print(message)

    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def _show_welcome(self) -> None:
        """Display welcome message."""
        self.show("")
        self.show("=" * 50)
        self.show("Welcome to the app")
        self.show("=" * 50)
        self.show("")

    def _show_menu(self) -> None:
        """Display menu options."""
        self.show("Choose an option")
        self.show("=" * 50)
        self.show("1 - Add user")
        self.show("2 - List users")
        self.show("3 - Exit")
        self.show("")

    def _get_menu_choice(self) -> str:
        """Get menu choice from user."""
        return self.get_input("Choose option (1-3): ")

    def _show_goodbye(self) -> None:
        """Display goodbye message."""
        self.show("")
        self.show("=" * 50)
        self.show("Goodbye!")
        self.show("=" * 50)
        self.show("")

    def _show_invalid_option(self) -> None:
        """Display invalid option message."""
        self._show_message_with_separators("Invalid option. Please select 1, 2, or 3.")

    def _show_message_with_separators(self, message: str) -> None:
        """Display a message with separators."""
        self.show("")
        self.show("=" * 50)
        self.show(message)
        self.show("=" * 50)
        self.show("")

    def _show_error(self, error_message: str) -> None:
        """Display error message."""
        self.show("")
        self.show("=" * 50)
        self.show("Something went wrong")
        self.show(f"Error: {error_message}")
        self.show("=" * 50)
        self.show("")

    def _show_success_message(self, message: str) -> None:
        """Display success message."""
        self.show("")
        self.show("=" * 50)
        self.show(message)
        self.show("=" * 50)
        self.show("")

    def _show_user(self, user) -> None:
        """Display user information."""
        self.show("=" * 50)
        self.show("")
        self.show(user)
        self.show("")
        self.show("=" * 50)

    def _add_user(self, presenter: "Presenter") -> None:
        """Handle adding a user."""
        self.show("=" * 50)
        self.show("Adding a new user")
        self.show("=" * 50)
        self.show("")

        name = self.get_input("Name: ")
        email = self.get_input("Email: ")
        password = self.get_input("Password: ")
        street_address = self.get_input("Street address: ")
        postal_code = self.get_input("Postal Code: ")
        city = self.get_input("City: ")

        user_data = UserData(
            name=name,
            email=email,
            password=password,
            street_address=street_address,
            postal_code=postal_code,
            city=city,
        )

        result = presenter.add_user(user_data)

        if not result["success"]:
            self._show_error(result["error"] or "Failed to add user")
        else:
            self._show_success_message("User added successfully")
            if result["user"]:
                self._show_user(result["user"])
            self.show("")

    def _list_users(self, presenter: "Presenter") -> None:
        """Handle listing users."""
        result = presenter.list_users()

        if result["error"]:
            self._show_error(result["error"])
        else:
            users = result["users"]
            if len(users) == 0:
                self._show_message_with_separators("No users found")
                return

            self._show_message_with_separators("Listing users")
            for user in users:
                self._show_user(user)
                self.show("")

    def run(self, presenter: "Presenter") -> None:
        """Run the terminal interface."""
        self._show_welcome()

        while True:
            self._show_menu()
            choice = self._get_menu_choice()
            self.show("")

            if choice == "1":
                self._add_user(presenter)
            elif choice == "2":
                self._list_users(presenter)
            elif choice == "3":
                self._show_goodbye()
                break
            else:
                self._show_invalid_option()
