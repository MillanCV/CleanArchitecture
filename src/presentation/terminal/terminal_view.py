from typing import Optional
from src.presentation.view_interfaz import ViewInterfaz
from src.presentation.presenter import Presenter


class Terminal(ViewInterfaz):
    def __init__(self, presenter: Optional[Presenter] = None):
        self.presenter = presenter

    def show(self, message: str) -> None:
        print(message)

    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def run(self) -> None:
        self.show("Welcome to the app")

        while True:
            self.show("1 - Add user")
            self.show("2 - List users")
            self.show("3 - Exit")

            choice = self.get_input("Choose option(1-3)")

            if choice == "1":
                self.presenter.add_user()
            if choice == "3":
                break
