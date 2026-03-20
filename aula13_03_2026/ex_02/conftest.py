import pytest


@pytest.fixture(scope="session")
def banco_de_dados_de_teste():
    return "Conexão Global Estabelecida"


@pytest.fixture(autouse=True)
def configurar_ambiente_de_teste():
    print("Cache limpo antes do teste")
