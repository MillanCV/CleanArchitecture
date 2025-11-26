from src.domain.entities.user import User
from src.domain.repositories.repository import UserRepository


class InMemoryRepository(UserRepository):
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
