"""Tests for User Entity."""

import pytest

from src import User


class TestUser:
    def test_create_user(self, valid_user, user_name, valid_address):
        assert valid_user.name == user_name
        assert valid_user.email.value == "john.doe@example.com"
        assert valid_user.password.value == "SecurePass123"
        assert valid_user.address == valid_address

    def test_create_user_email_normalized(
        self, user_name, valid_password_string, valid_address
    ):
        user = User(
            name=user_name,
            email="JOHN.DOE@EXAMPLE.COM",
            password=valid_password_string,
            address=valid_address,
        )
        assert user.email.value == "john.doe@example.com"

    def test_user_has_id(self, valid_user):
        assert valid_user.id is not None
        assert isinstance(valid_user.id, str)

    def test_create_user_with_invalid_email(
        self, user_name, valid_password_string, valid_address
    ):
        with pytest.raises(ValueError):
            User(
                name=user_name,
                email="invalid-email",
                password=valid_password_string,
                address=valid_address,
            )

    def test_create_user_with_invalid_password(
        self, user_name, valid_email_string, valid_address
    ):
        with pytest.raises(ValueError):
            User(
                name=user_name,
                email=valid_email_string,
                password="short",
                address=valid_address,
            )

    def test_users_with_same_id_are_equal(
        self, valid_email_string, valid_password_string, valid_address
    ):
        user1 = User(
            name="John Doe",
            email=valid_email_string,
            password=valid_password_string,
            address=valid_address,
        )
        user2 = User(
            name="Jane Doe",
            email="jane.doe@example.com",
            password="DifferentPass123",
            address=valid_address,
        )
        user2.id = user1.id
        assert user1 == user2

    def test_users_with_different_ids_are_not_equal(
        self, user_name, valid_email_string, valid_password_string, valid_address
    ):
        user1 = User(
            name=user_name,
            email=valid_email_string,
            password=valid_password_string,
            address=valid_address,
        )
        user2 = User(
            name=user_name,
            email=valid_email_string,
            password=valid_password_string,
            address=valid_address,
        )
        assert user1.id != user2.id
        assert user1 != user2
