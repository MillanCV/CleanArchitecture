import pytest

from src.main import Email, Password, validate_email, validate_password


class TestEmailValidation:
    def test_valid_email(self):
        valid_email = Email(user="m.castrovilarino", domain="gmail.com")

        validated_email = validate_email("m.castrovilarino@gmail.com")

        assert valid_email == validated_email

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


class TestPasswordValidation:
    def test_valid_password(self):
        valid_password = Password(value="password123")

        validated_password = validate_password("password123")

        assert valid_password == validated_password

    def test_valid_password_with_special_chars(self):
        valid_password = Password(value="MyPass123!")

        validated_password = validate_password("MyPass123!")

        assert valid_password == validated_password

    INVALID_PASSWORDS = [
        "",  # empty
        "short",  # less than 8 characters
        "1234567",  # 7 characters, no letter
        "abcdefgh",  # 8 characters, no number
        "ABCDEFGH",  # 8 characters uppercase, no number
        "12345678",  # 8 characters, no letter
        "pass123",  # 7 characters (has letter and number but too short)
    ]

    @pytest.mark.parametrize("value", INVALID_PASSWORDS)
    def test_validate_password_invalid(self, value):
        with pytest.raises(ValueError):
            validate_password(value)

    def test_password_not_string(self):
        with pytest.raises(ValueError, match="Password must be a string"):
            validate_password(12345678)

    def test_password_too_short(self):
        with pytest.raises(ValueError, match="at least 8 characters"):
            validate_password("pass123")

    def test_password_no_letter(self):
        with pytest.raises(ValueError, match="at least one letter"):
            validate_password("12345678")

    def test_password_no_number(self):
        with pytest.raises(ValueError, match="at least one number"):
            validate_password("password")
