from dataclasses import dataclass


@dataclass(frozen=True)
class Address:
    street_address: str
    postal_code: str
    city: str

    def __str__(self) -> str:
        return f"{self.street_address}, {self.postal_code}, {self.city}"

    @classmethod
    def create(cls, street_address: str, postal_code: str, city: str) -> "Address":
        street_address = street_address.strip()
        postal_code = postal_code.strip()
        city = city.strip()

        if not street_address:
            raise ValueError("Address street_address cannot be empty")

        if not postal_code:
            raise ValueError("Address postal_code cannot be empty")

        if not city:
            raise ValueError("Address city cannot be empty")

        return cls(
            street_address=street_address,
            postal_code=postal_code,
            city=city,
        )
