"""Tests for User Entity."""

import pytest

from src import Email, Password, User


class TestUser:
    def test_create_user_with_valid_data(
        self, user_name, valid_email_string, valid_password_string
    ):
        user = User(
            name=user_name, email=valid_email_string, password=valid_password_string
        )

        assert user.name == user_name
        assert isinstance(user.email, Email)
        assert user.email.user == "john.doe"
        assert user.email.domain == "example.com"
        assert isinstance(user.password, Password)
        assert user.password.value == valid_password_string

    def test_create_user_with_fixture(self, valid_user, user_name):
        assert valid_user.name == user_name
        assert isinstance(valid_user.email, Email)
        assert isinstance(valid_user.password, Password)

    def test_create_user_with_invalid_email(self, user_name, valid_password_string):
        with pytest.raises(ValueError):
            User(name=user_name, email="invalid-email", password=valid_password_string)

    def test_create_user_with_invalid_password(self, user_name, valid_email_string):
        with pytest.raises(ValueError):
            User(name=user_name, email=valid_email_string, password="short")

    def test_create_user_with_empty_email(self, user_name, valid_password_string):
        with pytest.raises(ValueError):
            User(name=user_name, email="", password=valid_password_string)

    def test_create_user_with_empty_password(self, user_name, valid_email_string):
        with pytest.raises(ValueError):
            User(name=user_name, email=valid_email_string, password="")

    def test_create_user_with_password_no_letter(self, user_name, valid_email_string):
        with pytest.raises(ValueError, match="at least one letter"):
            User(name=user_name, email=valid_email_string, password="12345678")

    def test_create_user_with_password_no_number(self, user_name, valid_email_string):
        with pytest.raises(ValueError, match="at least one number"):
            User(name=user_name, email=valid_email_string, password="SecurePass")

    def test_create_user_with_password_too_short(self, user_name, valid_email_string):
        with pytest.raises(ValueError, match="at least 8 characters"):
            User(name=user_name, email=valid_email_string, password="Pass123")

    def test_create_user_email_normalized(self, user_name, valid_password_string):
        user = User(
            name=user_name, email="JOHN.DOE@EXAMPLE.COM", password=valid_password_string
        )

        assert user.email.user == "john.doe"
        assert user.email.domain == "example.com"

    def test_create_user_multiple_users(self):
        user1 = User(
            name="Alice Smith", email="alice@example.com", password="AlicePass123"
        )
        user2 = User(name="Bob Johnson", email="bob@example.com", password="BobPass123")

        assert user1.name == "Alice Smith"
        assert user2.name == "Bob Johnson"
        assert user1.email.domain == user2.email.domain
        assert user1.password.value != user2.password.value

    def test_user_has_id(self, valid_user):
        assert valid_user.id is not None
        assert isinstance(valid_user.id, str)
        assert len(valid_user.id) > 0

    def test_users_with_same_id_are_equal(
        self, valid_email_string, valid_password_string
    ):
        user_id = "test-id-123"
        user1 = User(
            name="John Doe",
            email=valid_email_string,
            password=valid_password_string,
            user_id=user_id,
        )
        user2 = User(
            name="Jane Doe",  # Different name
            email="jane.doe@example.com",  # Different email
            password="DifferentPass123",  # Different password
            user_id=user_id,  # Same ID
        )

        assert user1 == user2
        assert hash(user1) == hash(user2)

    def test_users_with_different_ids_are_not_equal(
        self, user_name, valid_email_string, valid_password_string
    ):
        user1 = User(
            name=user_name,
            email=valid_email_string,
            password=valid_password_string,
            user_id="id-1",
        )
        user2 = User(
            name=user_name,  # Same name
            email=valid_email_string,  # Same email
            password=valid_password_string,  # Same password
            user_id="id-2",  # Different ID
        )

        assert user1 != user2

    def test_user_can_be_used_in_set(
        self, user_name, valid_email_string, valid_password_string
    ):
        user_id = "test-id-123"
        user1 = User(
            name=user_name,
            email=valid_email_string,
            password=valid_password_string,
            user_id=user_id,
        )
        user2 = User(
            name="Jane Doe",
            email="jane.doe@example.com",
            password="DifferentPass123",
            user_id=user_id,  # Same ID as user1
        )
        user3 = User(
            name="Bob Smith",
            email="bob@example.com",
            password="BobPass123",
            user_id="different-id",  # Different ID
        )

        user_set = {user1, user2, user3}

        assert len(user_set) == 2  # user1 and user2 are the same (same ID)
