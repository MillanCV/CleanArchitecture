"""Password Value Object.

Represents a password as an immutable value object.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Password:
    """Password value object.

    Represents a password as an immutable value.
    Compared by value, not by reference.
    """

    value: str

    def __eq__(self, other):
        if not isinstance(other, Password):
            return False
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)


def validate_password(password_value: str) -> Password:
    """Validate and create a Password value object.

    Args:
        password_value: The password string to validate.

    Returns:
        Password: A validated Password value object.

    Raises:
        ValueError: If the password doesn't meet requirements:
            - Must be at least 8 characters long
            - Must contain at least one letter
            - Must contain at least one number
    """
    if not isinstance(password_value, str):
        raise ValueError("Password must be a string")

    if len(password_value) < 8:
        raise ValueError("Password must be at least 8 characters long")

    contains_letter = any(char.isalpha() for char in password_value)
    if not contains_letter:
        raise ValueError("Password must contain at least one letter")

    contains_number = any(char.isdigit() for char in password_value)
    if not contains_number:
        raise ValueError("Password must contain at least one number")

    return Password(value=password_value)
