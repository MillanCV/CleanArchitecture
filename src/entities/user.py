"""User Entity.

Represents a user in the system with a unique identity.
"""

import uuid

from src.value_objects.email import Email, validate_email
from src.value_objects.password import Password, validate_password


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
        user_id: str | None = None,
    ):
        """Initialize a User entity.

        Args:
            name: The user's name.
            email: The user's email address (will be validated).
            password: The user's password (will be validated).
            user_id: Optional user ID. If not provided, a UUID will be generated.
        """
        self._id = user_id if user_id else str(uuid.uuid4())
        self.name = name
        self.email = self._validate_email(email)
        self.password = self._validate_password(password)

    @property
    def id(self) -> str:
        """Get the user's unique identifier."""
        return self._id

    def _validate_email(self, email_address: str) -> Email:
        """Validate and create an Email value object."""
        return validate_email(email_address)

    def _validate_password(self, password_value: str) -> Password:
        """Validate and create a Password value object."""
        return validate_password(password_value)

    def __eq__(self, other):
        """Compare users by their ID."""
        if not isinstance(other, User):
            return False
        return self.id == other.id

    def __hash__(self):
        """Hash based on user ID."""
        return hash(self.id)
