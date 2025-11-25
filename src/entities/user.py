"""User Entity.

Represents a user in the system with a unique identity.
"""

import uuid

from src.value_objects.address import Address
from src.value_objects.email import Email
from src.value_objects.password import Password


class User:
    """User entity.

    Represents a user with a unique identity (ID).
    Users are compared by their ID, not by their attributes.
    """

    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        address: Address,
    ):
        """Initialize a User entity.

        Args:
            name: The user's name.
            email: The user's email address (will be validated).
            password: The user's password (will be validated).
            address: The user's address.
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = Email.from_string(email)
        self.password = Password.from_string(password)
        self.address = address

    def __eq__(self, other):
        """Compare users by their ID."""
        if not isinstance(other, User):
            return False
        return self.id == other.id
