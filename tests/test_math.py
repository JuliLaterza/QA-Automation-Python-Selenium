import pytest

def add_two_numbers(a, b):
    return a + b

@pytest.mark.small
def test_small_numbers():
    assert add_two_numbers(1, 2) == 3, "The sum of 1 and 2 should be 3."

@pytest.mark.large
def test_large_numbers():
    assert add_two_numbers(1000, 3000) == 4000, "The sum of 1000 and 3000 should be 4000"


print("ok")
