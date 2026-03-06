
import pytest
from ex2_tdd__regra2 import termometrica

def test_fahrenheit():
    """38c -> F"""
    assert termometrica("C", 38) == pytest.approx(100.4, rel=1e-2)

def test_celso():
    """38f -> c"""
    assert termometrica("F", 38) == pytest.approx(3.33)

def test_string():
    """type erro - 35F"""
    with pytest.raises(ValueError):termometrica("c", "49f")

