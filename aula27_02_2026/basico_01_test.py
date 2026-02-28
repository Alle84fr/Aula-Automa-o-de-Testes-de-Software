# ativar venv 
# python -m venv venv
# venv\Scripts\activate
# python -m pip install pytest
# python -m pytest
# pip install pytest-cov

# para rodar teste apenas -> pytest

# para rodar se pasta -> pytest -v basico_01_test --cov-branch

# para rodar se file ->  python -m pytest .\aula27_02_2026\basico_01_test.py -v

# para função específica -: python -m pytest basico_01_test.py::test_soma -v

# gerar "relatório -> coverage html


import pytest
from basico_01 import somar, dividir, multiplicar, subtrair



def test_soma():
    assert somar(15,9) == 24
    
def test_subtrai():
    result = 15-9
    assert subtrair(15,9) == 6

def test_multiplica():
    assert multiplicar (15,9) == 135

def test_dividir():
    assert dividir(15, 9) == pytest.approx(1.66666667)