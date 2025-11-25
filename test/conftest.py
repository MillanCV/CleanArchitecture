"""Shared pytest fixtures for all tests."""

import pytest

from src import Email, Password, User


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
def valid_user(user_name, valid_email_string, valid_password_string):
    """Fixture for a valid User entity."""
    return User(
        name=user_name, email=valid_email_string, password=valid_password_string
    )
