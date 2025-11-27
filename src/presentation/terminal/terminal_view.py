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
