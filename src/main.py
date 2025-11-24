import re

from dataclasses import dataclass


@dataclass
class Email:
    user: str
    domain: str


@dataclass
class Password:
    password: str


class User:
    def __init__(
        self,
        name: str,
        email: str,
        password: str,
    ):
        self.name = name
        self.email = self._validate_email(email)
        self.password = self._validate_password(password)

    def _validate_email(str) -> Email:
        EMAIL_REGEX = re.compile(
            r"^(?P<user>[a-zA-Z0-9_.+-]+)@"
            r"(?P<domain>[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"
        )

        if not isinstance(value, str):
            raise ValueError("Email must be a string")

        value = value.strip().lower()

        # Check for empty string after stripping
        if not value:
            raise ValueError(f"Invalid email: {value}")

        # Check for double dots anywhere
        if ".." in value:
            raise ValueError(f"Invalid email: {value}")

        match = EMAIL_REGEX.match(value)
        if not match:
            raise ValueError(f"Invalid email: {value}")

        user = match.group("user")
        domain = match.group("domain")

        # User cannot start or end with dot
        if user.startswith(".") or user.endswith("."):
            raise ValueError(f"Invalid email: {value}")

        # Domain parts validation
        domain_parts = domain.split(".")
        if len(domain_parts) < 2:
            raise ValueError(f"Invalid email: {value}")

        # TLD must be at least 2 characters
        if len(domain_parts[-1]) < 2:
            raise ValueError(f"Invalid email: {value}")

        # Each domain part cannot start or end with hyphen
        for part in domain_parts:
            if part.startswith("-") or part.endswith("-"):
                raise ValueError(f"Invalid email: {value}")

        # Reject IP-like domains (4 numeric parts)
        if len(domain_parts) == 4 and all(part.isdigit() for part in domain_parts):
            raise ValueError(f"Invalid email: {value}")

        return Email(
            user=user,
            domain=domain,
        )

    def _validate_password(str) -> Password:
        if not isinstance(value, str):
            raise ValueError("Password must be a string")

        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")

        has_letter = any(c.isalpha() for c in value)
        if not has_letter:
            raise ValueError("Password must contain at least one letter")

        has_number = any(c.isdigit() for c in value)
        if not has_number:
            raise ValueError("Password must contain at least one number")

        return Password(password=value)
