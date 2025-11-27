from dataclasses import dataclass


@dataclass(frozen=True)
class Password:
    value: str

    def __str__(self) -> str:
        return self.value

    @classmethod
    def from_string(cls, password_value: str) -> "Password":
        if len(password_value) < 8:
            raise ValueError("Password must be at least 8 characters long")

        contains_letter = any(char.isalpha() for char in password_value)
        if not contains_letter:
            raise ValueError("Password must contain at least one letter")

        contains_number = any(char.isdigit() for char in password_value)
        if not contains_number:
            raise ValueError("Password must contain at least one number")

        return cls(value=password_value)
