
# rodar -> pytest
# rodar -> python -m pytest .\aula27_02_2026\trata_exc_02_test.py -v
# intalar -> python -m pip install coverage
# rodar (já está dentro da pasta aula27..)-> coverage run -m pytest trata_exc_02_test.py -v ou -> coverage run -m pytest -v
#gerar relatório, mostrar no terminal -> coverage report -m
#coverage html
# apagar dados antigos -> coverage erase 

from trata_exc_02 import raiz_quadrada, calcular_media, comparar
from basico_01 import somar
import pytest

def test_media():
    lista = [2,9.01,8,0.98,4]
    assert calcular_media(lista) == pytest.approx(4.798)

def test_raiz():
    valor = somar(15,9)
    assert raiz_quadrada(valor) == pytest.approx(4.89897949)
    
def test_raiz_negativo():
    valor = somar(-15,0)
    assert raiz_quadrada(valor) == "Valor precisa ser positivo"

def test_par():
    assert comparar(15,9) is True

def test_impar():
    assert comparar(16,9) is False