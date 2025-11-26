import uuid

from src.domain.value_objects.address import Address
from src.domain.value_objects.email import Email
from src.domain.value_objects.password import Password


class User:

    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        address: Address,
        user_id: str | None = None,
    ):

        self.id = user_id if user_id else str(uuid.uuid4())
        self.name = self._validate_name(name)
        self.email = Email.from_string(email)
        self.password = Password.from_string(password)
        self.address = address

    def _validate_name(self, name: str) -> str:
        if not name or not name.strip():
            raise ValueError("User name cannot be empty")
        return name.strip()

    def __eq__(self, other: "User") -> bool:
        if not isinstance(other, User):
            return False
        return self.id == other.id
