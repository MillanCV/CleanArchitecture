"""Tests for Password Value Object."""

import pytest

from src import Password, validate_password


class TestPassword:
    def test_valid_password(self):
        valid_password = Password(value="password123")

        validated_password = validate_password("password123")

        assert valid_password == validated_password

    def test_valid_password_with_fixture(
        self, valid_password_string, valid_password_object
    ):
        validated_password = validate_password(valid_password_string)

        assert valid_password_object == validated_password

    def test_valid_password_with_special_chars(self):
        valid_password = Password(value="MyPass123!")

        validated_password = validate_password("MyPass123!")

        assert valid_password == validated_password

    INVALID_PASSWORDS = [
        "",  # empty
        "short",  # less than 8 characters
        "1234567",  # 7 characters, no letter
        "abcdefgh",  # 8 characters, no number
        "ABCDEFGH",  # 8 characters uppercase, no number
        "12345678",  # 8 characters, no letter
        "pass123",  # 7 characters (has letter and number but too short)
    ]

    @pytest.mark.parametrize("value", INVALID_PASSWORDS)
    def test_validate_password_invalid(self, value):
        with pytest.raises(ValueError):
            validate_password(value)

    def test_password_not_string(self):
        with pytest.raises(ValueError, match="Password must be a string"):
            validate_password(12345678)

    def test_password_too_short(self):
        with pytest.raises(ValueError, match="at least 8 characters"):
            validate_password("pass123")

    def test_password_no_letter(self):
        with pytest.raises(ValueError, match="at least one letter"):
            validate_password("12345678")

    def test_password_no_number(self):
        with pytest.raises(ValueError, match="at least one number"):
            validate_password("password")

    def test_same_password_instances_are_equal(self, valid_password_object):
        password1 = valid_password_object
        password2 = Password(value="SecurePass123")

        assert password1 == password2
        assert hash(password1) == hash(password2)

    def test_different_password_instances_are_not_equal(
        self, valid_password_object
    ):
        password1 = valid_password_object
        password2 = Password(value="DifferentPass123")

        assert password1 != password2

    def test_password_can_be_used_in_set(self, valid_password_object):
        password1 = valid_password_object
        password2 = Password(value="SecurePass123")
        password3 = Password(value="DifferentPass123")

        password_set = {password1, password2, password3}

        assert len(password_set) == 2  # password1 and password2 are the same

