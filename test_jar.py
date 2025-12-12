import pytest
from jar import Jar

def test_init_default():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_init_custom_capacity():
    jar = Jar(5)
    assert jar.capacity == 5

def test_init_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-3)
    with pytest.raises(ValueError):
        Jar("ten")

def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

def test_deposit_exceeds_capacity():
    jar = Jar(4)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

def test_withdraw_too_many():
    jar = Jar(5)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(4)


def test_str():
    jar = Jar()
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
