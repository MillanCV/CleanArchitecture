"""Tests for Address Value Object."""

import pytest

from src import Address


class TestAddress:
    def test_create_address(self):
        address = Address.create(
            street_address="Calle Principal 123",
            postal_code="28001",
            city="Madrid",
        )
        assert address.street_address == "Calle Principal 123"
        assert address.postal_code == "28001"
        assert address.city == "Madrid"

    def test_address_strips_whitespace(self):
        address = Address.create(
            street_address="  Calle Principal 123  ",
            postal_code="  28001  ",
            city="  Madrid  ",
        )
        assert address.street_address == "Calle Principal 123"
        assert address.postal_code == "28001"
        assert address.city == "Madrid"

    INVALID_ADDRESSES = [
        ("", "28001", "Madrid"),  # empty street_address
        ("Calle Principal 123", "", "Madrid"),  # empty postal_code
        ("Calle Principal 123", "28001", ""),  # empty city
        ("   ", "28001", "Madrid"),  # whitespace only street_address
        ("Calle Principal 123", "   ", "Madrid"),  # whitespace only postal_code
        ("Calle Principal 123", "28001", "   "),  # whitespace only city
    ]

    @pytest.mark.parametrize(
        "street_address,postal_code,city",
        INVALID_ADDRESSES,
    )
    def test_create_address_invalid(self, street_address, postal_code, city):
        with pytest.raises(ValueError):
            Address.create(
                street_address=street_address,
                postal_code=postal_code,
                city=city,
            )
