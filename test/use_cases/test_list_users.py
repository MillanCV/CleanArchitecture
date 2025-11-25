"""Tests for ListUsersUseCase."""

from src.entities import User
from src.use_cases.list_users import ListUsersUseCase


class TestListUsersUseCase:
    """Test cases for ListUsersUseCase."""

    def test_execute_returns_empty_list_when_no_users(
        self,
        fake_user_repository,
    ):
        """Test that execute returns empty list when repository is empty."""
        # Arrange
        use_case = ListUsersUseCase(repository=fake_user_repository)

        # Act
        result = use_case.execute()

        # Assert
        assert result == []
        assert len(result) == 0

    def test_execute_returns_all_users(
        self,
        fake_user_repository,
        valid_address,
    ):
        """Test that execute returns all users from repository."""
        # Arrange
        use_case = ListUsersUseCase(repository=fake_user_repository)

        # Add users directly to repository
        user1 = User(
            name="John Doe",
            email="john.doe@example.com",
            password="SecurePass123",
            address=valid_address,
        )
        user2 = User(
            name="Jane Doe",
            email="jane.doe@example.com",
            password="AnotherPass123",
            address=valid_address,
        )

        fake_user_repository.save_user(user1)
        fake_user_repository.save_user(user2)

        # Act
        result = use_case.execute()

        # Assert
        assert len(result) == 2
        assert user1 in result
        assert user2 in result

    def test_execute_returns_users_in_order_added(
        self, fake_user_repository, valid_address
    ):
        """Test that users are returned in the order they were added."""
        # Arrange
        use_case = ListUsersUseCase(repository=fake_user_repository)

        user1 = User(
            name="First User",
            email="first@example.com",
            password="SecurePass123",
            address=valid_address,
        )
        user2 = User(
            name="Second User",
            email="second@example.com",
            password="SecurePass123",
            address=valid_address,
        )
        user3 = User(
            name="Third User",
            email="third@example.com",
            password="SecurePass123",
            address=valid_address,
        )

        fake_user_repository.save_user(user1)
        fake_user_repository.save_user(user2)
        fake_user_repository.save_user(user3)

        # Act
        result = use_case.execute()

        # Assert
        assert len(result) == 3
        assert result[0] == user1
        assert result[1] == user2
        assert result[2] == user3
