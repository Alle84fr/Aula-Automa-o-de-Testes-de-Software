import pytest
# primeiro criar file da função, não faça a função, apernas mostre que ela será feita
# importa
# rode a função para dar erro
# depois de rodar, crie a função
# rode a teste para dar certo
from ex1_tdd_regra1 import descontar

def test_desconto_desc64():
    """64%"""
    assert descontar(49, 64) == pytest.approx(17.64, rel=1e-4)
    # rel=1e-2 = 1% de tolerancia de valor decimal

def test_desconto_descTotal():
    """100%"""
    assert descontar(49, 100) == "Grátis"

def test_desconto_semDesc():
    """0%"""
    assert descontar(49, 0) == "Sem desconto"

def test_desconto_porcMenor():
    """-12%"""
    with pytest.raises(ValueError):descontar(49,-12)

def test_desconto_porcMaior():
    """125%"""
    with pytest.raises(ValueError):descontar(49,125)


# 1° rodada resuktado deve ser
# pytest 
# ========================================================================================= test session starts ==========================================================================================
# platform win32 -- Python 3.13.3, pytest-9.0.2, pluggy-1.6.0
# rootdir: C:\Users\arfur\Documents\python_geral\gionavi\aula06_03_2026
# plugins: cov-7.0.0
# collected 1 item                                                                                                                                                                                        

# ex1_tdd_test.py F                                                                                                                                                                                 [100%]

# =============================================================================================== FAILURES =============================================================================================== 
# ____________________________________________________________________________________________ test_desconto .....

# 12° rodada

