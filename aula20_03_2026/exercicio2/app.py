# classe abstrata = define método, sem implementar, não instancia diretamente
# obrigada quem herdar a implementar os métodos, as classes normais já estão implementadas

from abc import ABC, abstractmethod
from typing import Optional

class IRepositorioUsuario(ABC):
    
    # como a classe abstrata só mostra formula do que fazer, sem roda, ele não possui __init__ (inicialização da classe)
    @abstractmethod
    def adicionar_usuario(self, nome) -> None:
        pass
    
    @abstractmethod
    def buscar_usuario(self, nome) -> Optional[str]:
        pass

# implementação fake = ex: simula banco de dados, sem por usuários e outros dados e simula que ele está rodando
class RepositorioUsuariosFake(IRepositorioUsuario):
    
    def __init__(self):
        self.dict_usuario = {}
        
    def adicionar_usuario(self, nome) -> None:
        self.dict_usuario[nome] = nome
    
    def buscar_usuario(self, nome) -> Optional[str]:
        return self.dict_usuario.get(nome)

# aqui chamo a classe abstrata, implmento e rodo
# pego a regra, add "dados" e rodo
class GerenciadorUsuario:
    
    def __init__(self,IRepositorioUsuario):
        repositorio = IRepositorioUsuario
        self.repositorio = repositorio
    
    # alimentando o diconário
    def registrar_usuario(self, nome) -> None:
        self.repositorio.adicionar_usuario(nome)
        
    # buscando por nome
    # -> Opcional[str] ou retorna string ou valor none
    def encontrar_usuario(self, nome) -> Optional[str]:
        return self.repositorio.buscar_usuario(nome)
    