import pytest
from app import RepositorioUsuariosFake, GerenciadorUsuario

# criar repositório fake
@pytest.fixture
def repositorio_fake():
    return RepositorioUsuariosFake()

# gerencia o repositório fake
@pytest.fixture
def gerenciador(repositorio_fake):
    return GerenciadorUsuario(repositorio_fake)


def test_adicionar_e_buscar_usuario(gerenciador):
    nome = "Alessandra"
    gerenciador.registrar_usuario(nome)
    assert gerenciador.encontrar_usuario(nome) == nome


def test_buscar_usuario_inexistente(gerenciador):
    assert gerenciador.encontrar_usuario("Inexistente") is None
