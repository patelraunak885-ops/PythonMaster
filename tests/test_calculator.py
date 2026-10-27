from calculator import add


def test_add_two_integers() -> None:
    assert add(2, 3) == 5


def test_add_negative_numbers() -> None:
    assert add(-2, -3) == -5


def test_add_integer_and_float() -> None:
    assert add(2, 3.5) == 5.5
