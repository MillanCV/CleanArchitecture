"""Email Value Object.

Represents an email address as an immutable value object.
"""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    """Email value object.

    Represents an email address with user and domain parts.
    Immutable and compared by value.
    """

    user: str
    domain: str

    def __eq__(self, other):
        if not isinstance(other, Email):
            return False
        return self.user == other.user and self.domain == other.domain

    def __hash__(self):
        return hash((self.user, self.domain))


def validate_email(email_address: str) -> Email:
    """Validate and create an Email value object.

    Args:
        email_address: The email address string to validate.

    Returns:
        Email: A validated Email value object.

    Raises:
        ValueError: If the email address is invalid.
    """
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
