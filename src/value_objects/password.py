"""Password Value Object.

Represents a password as an immutable value object.
"""

from dataclasses import dataclass


@dataclass
class Password:
    """Password value object.

    Represents a password value.
    Compared by value, not by reference.
    """

    value: str

    @classmethod
    def from_string(cls, password_value: str) -> "Password":
        """Create a Password value object from a string.

        Args:
            password_value: The password string.

        Returns:
            Password: A Password value object.

        Raises:
            ValueError: If the password doesn't meet requirements:
                - Must be at least 8 characters long
                - Must contain at least one letter
                - Must contain at least one number
        """

        if len(password_value) < 8:
            raise ValueError("Password must be at least 8 characters long")

        contains_letter = any(char.isalpha() for char in password_value)
        if not contains_letter:
            raise ValueError("Password must contain at least one letter")

        contains_number = any(char.isdigit() for char in password_value)
        if not contains_number:
            raise ValueError("Password must contain at least one number")

        return cls(value=password_value)
