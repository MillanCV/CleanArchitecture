import sqlite3

from src.domain.entities.user import User
from src.domain.repositories.repository import UserRepository
from src.domain.value_objects.address import Address


class SQLiteRepository(UserRepository):
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Create the users table schema if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                street_address TEXT NOT NULL,
                postal_code TEXT NOT NULL,
                city TEXT NOT NULL
            )""")
        self.conn.commit()

    def save_user(self, user: User) -> User:
        """Save a user to the database."""
        self.cursor.execute(
            """INSERT INTO users (id, name, email, password,
               street_address, postal_code, city)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                user.id,
                user.name,
                user.email.value,
                user.password.value,
                user.address.street_address,
                user.address.postal_code,
                user.address.city,
            ),
        )
        self.conn.commit()
        return user

    def find_by_email(self, email: str) -> bool:
        """Check if an email exists in the repository."""
        normalized_email = email.strip().lower()
        self.cursor.execute("SELECT * FROM users WHERE email = ?", (normalized_email,))
        return self.cursor.fetchone() is not None

    def get_users(self) -> list[User]:
        """Get all users from the repository."""
        self.cursor.execute(
            """SELECT id, name, email, password,
               street_address, postal_code, city FROM users"""
        )
        rows = self.cursor.fetchall()

        users = []
        for row in rows:
            (
                user_id,
                name,
                email_str,
                password_str,
                street_address,
                postal_code,
                city,
            ) = row

            # Reconstruct Address value object
            address = Address(
                street_address=street_address,
                postal_code=postal_code,
                city=city,
            )

            # Reconstruct User entity with value objects
            user = User(
                name=name,
                email=email_str,
                password=password_str,
                address=address,
                user_id=user_id,
            )
            users.append(user)

        return users

    def close(self):
        """Close the database connection."""
        self.conn.close()
