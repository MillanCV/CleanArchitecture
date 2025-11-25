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
        user_id: str | None = None,
    ):
        """Initialize a User entity.

        Args:
            name: The user's name (will be validated).
            email: The user's email address (will be validated).
            password: The user's password (will be validated).
            address: The user's address.
            user_id: Optional unique identifier for the user.
                    If not provided, generates a new UUID.
                    Use when reconstructing from persistence.

        Raises:
            ValueError: If name, email, or password is invalid.
        """
        self.id = user_id if user_id else str(uuid.uuid4())
        self.name = self._validate_name(name)
        self.email = Email.from_string(email)
        self.password = Password.from_string(password)
        self.address = address

    def _validate_name(self, name: str) -> str:
        """Validate and normalize the user's name.

        Args:
            name: The name to validate.

        Returns:
            str: The normalized name (stripped).

        Raises:
            ValueError: If name is empty or contains only whitespace.
        """
        if not name or not name.strip():
            raise ValueError("User name cannot be empty")
        return name.strip()

    def __eq__(self, other):
        """Compare users by their ID."""
        if not isinstance(other, User):
            return False
        return self.id == other.id
