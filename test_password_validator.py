import pytest
from password_validator import validate_password


def test_valid_password():
    assert validate_password("ValidPass123!") == "valid"

def test_password_empty_string():
    assert validate_password("") == "Password is empty."

def test_password_contains_a_space():
    assert validate_password("hell o") == "Password may not contain any spaces."

def test_password_too_short():
    assert validate_password("shorty") == "Password must be at least 8 characters long."

def test_password_missing_uppercase():
    assert validate_password("password") == "Password needs to contain at least one uppercase letter."

def test_password_missing_lowercase():
    assert validate_password("PASSWORD") == "Password needs to contain at least one lowercase letter."

def test_password_missing_digit():
    assert validate_password("Password") == "Password needs to contain at least one digit."

def test_password_missing_special_character():
    assert validate_password("Passw0rd") == "Password needs to contain at least one special character."


@pytest.mark.parametrize("invalid_input", [
    17,
    None,
    ["dog", "cat"],
    {"password": "hello"}
])

def test_password_invalid_input(invalid_input):
    with pytest.raises(TypeError):
        validate_password(invalid_input)