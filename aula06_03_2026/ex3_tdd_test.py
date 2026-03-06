
import pytest
from ex3_tdd_regra3 import calcular_valor_estacionamento

# lembrar que a entrada é de min e não hora, posso por entrada em horas e multiplicar por min
def test_1h():
    assert calcular_valor_estacionamento(60) == 10.00
    
def test_5h48():
    assert calcular_valor_estacionamento(5.48*60) == (35)
    
def test_23h59():
    assert calcular_valor_estacionamento(23.59*60) == (50)
    
def test_24h():
    assert calcular_valor_estacionamento(24*60) == 50.00

def test_0():
    with pytest.raises(ValueError): calcular_valor_estacionamento(0)

def test_negativo():
    with pytest.raises(ValueError): calcular_valor_estacionamento(-6)