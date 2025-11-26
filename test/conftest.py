"""Shared pytest fixtures for all tests."""

import pytest

from src import Address, Email, Password, User
from src.domain.repositories.repository import UserRepository


@pytest.fixture
def valid_email_string():
    """Fixture for a valid email string."""
    return "john.doe@example.com"


@pytest.fixture
def valid_email_object():
    """Fixture for a valid Email value object."""
    return Email(value="john.doe@example.com")


@pytest.fixture
def valid_password_string():
    """Fixture for a valid password string."""
    return "SecurePass123"


@pytest.fixture
def valid_password_object():
    """Fixture for a valid Password value object."""
    return Password(value="SecurePass123")


@pytest.fixture
def user_name():
    """Fixture for a user name."""
    return "John Doe"


@pytest.fixture
def valid_address():
    """Fixture for a valid Address value object."""
    return Address.create(
        street_address="Calle Principal 123",
        postal_code="28001",
        city="Madrid",
    )


@pytest.fixture
def valid_user(user_name, valid_email_string, valid_password_string, valid_address):
    """Fixture for a valid User entity."""
    return User(
        name=user_name,
        email=valid_email_string,
        password=valid_password_string,
        address=valid_address,
    )


class FakeUserRepository(UserRepository):
    """In-memory fake implementation of UserRepository for testing."""

    def __init__(self):
        self._users: list[User] = []

    def save_user(self, user: User) -> User:
        """Save a user to the fake repository."""
        self._users.append(user)
        return user

    def find_by_email(self, email: str) -> bool:
        """Check if an email exists in the repository."""
        normalized_email = email.strip().lower()
        return any(user.email.value == normalized_email for user in self._users)

    def get_users(self) -> list[User]:
        """Get all users from the repository."""
        return self._users.copy()


@pytest.fixture
def fake_user_repository():
    """Fixture for FakeUserRepository instance."""
    return FakeUserRepository()
