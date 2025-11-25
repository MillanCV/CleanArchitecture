"""Tests for Email Value Object."""

import pytest

from src import Email


class TestEmail:
    def test_create_email(self, valid_email_string):
        email = Email.from_string(valid_email_string)
        assert email.value == "john.doe@example.com"

    def test_email_normalized(self):
        email = Email.from_string("JOHN.DOE@EXAMPLE.COM")
        assert email.value == "john.doe@example.com"

    INVALID_EMAILS = [
        "",
        "plainaddress",
        "@domain.com",
        "user@",
        "user@com",
        "user@domain..com",
        "user@@domain.com",
        "user domain@domain.com",
        ".user@domain.com",
        "user@-domain.com",
    ]

    @pytest.mark.parametrize("value", INVALID_EMAILS)
    def test_create_email_invalid(self, value):
        with pytest.raises(ValueError):
            Email.from_string(value)


