"""Tests for Password Value Object."""

import pytest

from src import Password


class TestPassword:
    def test_create_password(self, valid_password_string):
        password = Password.from_string(valid_password_string)
        assert password.value == "SecurePass123"

    INVALID_PASSWORDS = [
        "",
        "short",
        "12345678",
        "password",
        "pass123",
    ]

    @pytest.mark.parametrize("value", INVALID_PASSWORDS)
    def test_create_password_invalid(self, value):
        with pytest.raises(ValueError):
            Password.from_string(value)
