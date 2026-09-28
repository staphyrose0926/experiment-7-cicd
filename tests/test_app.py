from app import add_numbers, multiply_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_add_zero():
    assert add_numbers(10, 0) == 10


def test_multiply_numbers():
    assert multiply_numbers(4, 5) == 20


def test_negative_numbers():
    assert add_numbers(-2, -3) == -5
