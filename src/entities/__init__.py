"""Entities module.

Entities are objects that have a unique identity and can change over time.
They are compared by their identity (ID), not by their attributes.
"""

from src.entities.user import User

__all__ = ["User"]

