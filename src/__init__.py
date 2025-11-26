"""Domain layer - Clean Architecture.

This package contains the domain layer with:
- Value Objects: Immutable objects compared by value
- Entities: Objects with unique identity
- Domain Services: Business logic validations
"""

from src.domain.entities import User
from src.domain.value_objects import Address, Email, Password

__all__ = [
    "Address",
    "Email",
    "Password",
    "User",
]
