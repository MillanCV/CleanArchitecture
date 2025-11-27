from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.presentation.presenter import Presenter


class ViewInterfaz(ABC):
    @abstractmethod
    def show(self, message: str) -> None:
        pass

    @abstractmethod
    def get_input(self, prompt: str) -> str:
        pass

    @abstractmethod
    def run(self, presenter: "Presenter") -> None:
        pass
