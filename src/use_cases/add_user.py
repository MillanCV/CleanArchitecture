from src.repositories.repository import UserRepository
from src.dtos.user import UserData
from src.entities import User
from src.value_objects import Address


class AddUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user_data: UserData) -> User:
        if self.repository.find_by_email(user_data.email):
            raise ValueError("Email already exists, we can't two users with same email")

        address = Address(
            street_address=user_data.street_address,
            postal_code=user_data.postal_code,
            city=user_data.city,
        )

        user = User(
            name=user_data.name,
            email=user_data.email,
            password=user_data.password,
            address=address,
        )

        return self.repository.save_user(user=user)
