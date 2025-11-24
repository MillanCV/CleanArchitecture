"""Tests for Email Value Object."""

import pytest

from src import Email, validate_email


class TestEmail:
    def test_valid_email(self):
        valid_email = Email(user="m.castrovilarino", domain="gmail.com")

        validated_email = validate_email("m.castrovilarino@gmail.com")

        assert valid_email == validated_email

    def test_valid_email_with_fixture(
        self, valid_email_string, valid_email_object
    ):
        validated_email = validate_email(valid_email_string)

        assert valid_email_object == validated_email

    INVALID_EMAILS = [
        "",  # empty
        "   ",  # spaces only
        "plainaddress",  # no @
        "@domain.com",  # missing user
        "user@",  # missing domain
        "user@.com",  # domain starts with dot
        "user@com",  # no dot in domain
        "user@domain.",  # domain ends with dot
        "user@domain..com",  # double dot
        "user@@domain.com",  # two @
        "user@domain@com",  # extra @
        "user domain@domain.com",  # space in user
        "user@domain .com",  # space in domain
        "user@.domain.com",  # leading dot in domain
        ".user@domain.com",  # leading dot in user
        "user.@domain.com",  # trailing dot in user
        "user..name@domain.com",  # double dot in user
        "user@-domain.com",  # domain starts with -
        "user@domain-.com",  # domain ends with -
        "user@domain,com",  # invalid separator
        "user@domain#com",  # invalid character
        "user@domain!com",  # invalid character
        "user@do_main.com",  # underscore in domain (invalid by DNS)
        "user@111.222.333.4444",  # invalid IP-like domain
        "user@domain.c",  # 1-char TLD
    ]

    @pytest.mark.parametrize("value", INVALID_EMAILS)
    def test_validate_email_invalid(self, value):
        with pytest.raises(ValueError):
            validate_email(value)

    def test_same_email_instances_are_equal(self, valid_email_object):
        email1 = valid_email_object
        email2 = Email(user="john.doe", domain="example.com")

        assert email1 == email2
        assert hash(email1) == hash(email2)

    def test_different_email_instances_are_not_equal(self, valid_email_object):
        email1 = valid_email_object
        email2 = Email(user="jane.doe", domain="example.com")

        assert email1 != email2

    def test_email_can_be_used_in_set(self, valid_email_object):
        email1 = valid_email_object
        email2 = Email(user="john.doe", domain="example.com")
        email3 = Email(user="jane.doe", domain="example.com")

        email_set = {email1, email2, email3}

        assert len(email_set) == 2  # email1 and email2 are the same

