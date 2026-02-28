# coverage run -m pytest .\aula27_02_2026\integra_03_test.py -v
# coverage report -m
# coverage html

import pytest
from integra_03 import calcular_preco_final

def test_val_0():
    with pytest.raises(ValueError):
        calcular_preco_final(0)

def test_val_5():
    assert calcular_preco_final(5.15) == 5.15 + 20

def test_val_99():
    assert calcular_preco_final(99.99, "PROMO10") == pytest.approx(109.991)

def test_val_100():
    assert calcular_preco_final(100, "PROMO10") == 110

def test_val_3569():
    assert calcular_preco_final(3569, "PROMO20", frete_gratis=True) == 3569 * 0.8
    
def test_promo20():
    assert calcular_preco_final(365.02, "PROMO20") == 365.02 * 0.8 + 20