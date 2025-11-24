"""Value Objects module.

Value Objects are immutable objects that are defined by their attributes
rather than their identity. They are compared by value, not by reference.
"""

from src.value_objects.email import Email
from src.value_objects.password import Password

__all__ = ["Email", "Password"]
