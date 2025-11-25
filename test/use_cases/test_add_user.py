"""Tests for AddUserUseCase."""

import pytest

from src.dtos.user import UserData
from src.use_cases.add_user import AddUserUseCase


class TestAddUserUseCase:
    """Test cases for AddUserUseCase."""

    def test_execute_successfully_adds_user(self, fake_user_repository, valid_address):
        """Test that a user can be added successfully."""
        # Arrange
        use_case = AddUserUseCase(repository=fake_user_repository)
        user_data = UserData(
            name="John Doe",
            email="john.doe@example.com",
            password="SecurePass123",
            street_address=valid_address.street_address,
            postal_code=valid_address.postal_code,
            city=valid_address.city,
        )

        # Act
        result = use_case.execute(user_data)

        # Assert
        assert result is not None
        assert result.name == "John Doe"
        assert result.email.value == "john.doe@example.com"
        assert result.password.value == "SecurePass123"
        assert result.address == valid_address
        assert len(fake_user_repository.get_users()) == 1
        assert fake_user_repository.get_users()[0] == result

    def test_execute_raises_error_when_email_already_exists(
        self, fake_user_repository, valid_address
    ):
        """Test that adding a user with existing email raises ValueError."""
        # Arrange
        use_case = AddUserUseCase(repository=fake_user_repository)
        user_data = UserData(
            name="John Doe",
            email="john.doe@example.com",
            password="SecurePass123",
            street_address=valid_address.street_address,
            postal_code=valid_address.postal_code,
            city=valid_address.city,
        )

        # Add first user
        use_case.execute(user_data)

        # Act & Assert
        with pytest.raises(ValueError, match="Email already exists"):
            use_case.execute(user_data)

        # Verify only one user was added
        assert len(fake_user_repository.get_users()) == 1

    def test_execute_validates_email_format(
        self,
        fake_user_repository,
        valid_address,
    ):
        """Test that invalid email format raises error during User creation."""
        # Arrange
        use_case = AddUserUseCase(repository=fake_user_repository)
        user_data = UserData(
            name="John Doe",
            email="invalid-email",  # Invalid email format
            password="SecurePass123",
            street_address=valid_address.street_address,
            postal_code=valid_address.postal_code,
            city=valid_address.city,
        )

        # Act & Assert
        with pytest.raises(ValueError, match="Invalid email"):
            use_case.execute(user_data)
