# Password Policy Validator

Small Python project demonstrating test automation using pytest.

The project implements a password validation function and a test suite covering both valid and invalid inputs, including edge cases and type validation.

## Project structure

- password_validator.py # validation logic
- test_password_validator.py # pytest test suite

## Features

Validates passwords according to defined security rules:

- minimum length: 8 characters
- at least one uppercase letter
- at least one lowercase letter
- at least one digit
- at least one special character
- spaces are not allowed
- input must be a string (TypeError raised otherwise)

## Tech stack

- Python
- pytest

## Test coverage

The test suite demonstrates:

- positive and negative test cases
- edge case validation
- exception testing using pytest.raises
- parameterized tests for invalid input types
- clear and readable test structure

## Running tests

pytest -v

## Running the validator (CLI)

python password_validator.py "YourPassword123!"

Example output:

- valid
- Password needs to contain at least one digit.
- Password may not contain any spaces.