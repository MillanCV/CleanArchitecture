import re

from dataclasses import dataclass


@dataclass
class Email:
    user: str
    domain: str


@dataclass
class Password:
    value: str


def validate_email(email_address: str) -> Email:
    EMAIL_PATTERN = re.compile(
        r"^(?P<local_part>[a-zA-Z0-9_.+-]+)@"
        r"(?P<domain>[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"
    )

    if not isinstance(email_address, str):
        raise ValueError("Email must be a string")

    normalized_email = email_address.strip().lower()

    # Check for empty string after stripping
    if not normalized_email:
        raise ValueError(f"Invalid email: {email_address}")

    # Check for double dots anywhere
    if ".." in normalized_email:
        raise ValueError(f"Invalid email: {email_address}")

    match = EMAIL_PATTERN.match(normalized_email)
    if not match:
        raise ValueError(f"Invalid email: {email_address}")

    local_part = match.group("local_part")
    domain = match.group("domain")

    # Local part cannot start or end with dot
    if local_part.startswith(".") or local_part.endswith("."):
        raise ValueError(f"Invalid email: {email_address}")

    # Domain labels validation
    domain_labels = domain.split(".")
    if len(domain_labels) < 2:
        raise ValueError(f"Invalid email: {email_address}")

    # TLD must be at least 2 characters
    if len(domain_labels[-1]) < 2:
        raise ValueError(f"Invalid email: {email_address}")

    # Each domain label cannot start or end with hyphen
    for label in domain_labels:
        if label.startswith("-") or label.endswith("-"):
            raise ValueError(f"Invalid email: {email_address}")

    # Reject IP-like domains (4 numeric labels)
    if len(domain_labels) == 4 and all(label.isdigit() for label in domain_labels):
        raise ValueError(f"Invalid email: {email_address}")

    return Email(
        user=local_part,
        domain=domain,
    )


def validate_password(password_value: str) -> Password:
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

    def _validate_email(self, email_address: str) -> Email:
        return validate_email(email_address)

    def _validate_password(self, password_value: str) -> Password:
        return validate_password(password_value)
