from abc import ABC, abstractmethod


class ViewInterfaz(ABC):
    @abstractmethod
    def show(self, message: str) -> None:
        pass

    @abstractmethod
    def get_input(self, prompt: str) -> str:
        pass
