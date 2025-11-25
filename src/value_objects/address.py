"""Address Value Object.

Represents an address as an immutable value object.
"""

from dataclasses import dataclass


@dataclass
class Address:
    """Address value object.

    Represents an address with street, postal code, and city.
    Compared by value.
    """

    street_address: str
    postal_code: str
    city: str

    @classmethod
    def create(cls, street_address: str, postal_code: str, city: str) -> "Address":
        """Create an Address value object.

        Args:
            street_address: The street address.
            postal_code: The postal code.
            city: The city.

        Returns:
            Address: An Address value object.

        Raises:
            ValueError: If any field is empty.
        """
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
