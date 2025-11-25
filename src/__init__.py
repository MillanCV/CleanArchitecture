"""Domain layer - Clean Architecture.

This package contains the domain layer with:
- Value Objects: Immutable objects compared by value
- Entities: Objects with unique identity
- Domain Services: Business logic validations
"""

from src.entities import User
from src.value_objects import Email, Password

__all__ = [
    "Email",
    "Password",
    "User",
]
