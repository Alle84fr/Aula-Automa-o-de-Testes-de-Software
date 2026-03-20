import pytest
import os

# inicia o fixture
@pytest.fixture

def log_file():
    #criar o arquivo
    arq = open("test_log.txt", "w")
    
    #Para abrir o file
    yield arq
    
    #fechar,sempre fechar o aqruivo no .py
    arq.close()
    
    #remover, limpar 
    os.remove("test_log.txt")
