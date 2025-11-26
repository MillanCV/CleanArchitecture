from dataclasses import dataclass


@dataclass
class UserData:
    name: str
    email: str
    password: str
    street_address: str
    postal_code: str
    city: str

