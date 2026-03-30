#caminho da biblioteca .py
from pathlib import Path
# para ver se teste roda
import platform

#pytest
import pytest

# abrir navegador e cria conexão entre .py e navegador
from selenium import webdriver
# para ações tipo duplo clic
from selenium.webdriver import ActionChains
#configura e inicia ChomeDrive, que junta selenium e chrome
from selenium.webdriver.chrome.service import Service
# by, "por", ex by id, by name, procura por algo
from selenium.webdriver.common.by import By
# teclas como enter, control
from selenium.webdriver.common.keys import Keys

# fixture não repete cód nos testes
@pytest.fixture
def navegador():
    caminho_portal = Path(__file__).with_name("portal.html").resolve()
    servico = Service()
    navegador_chrome = webdriver.Chrome(service=servico)
    navegador_chrome.get(caminho_portal.as_uri())
    yield navegador_chrome
    navegador_chrome.quit()


def test_preencher_formulario(navegador):
    assert navegador.title == "Portal do Colaborador"

    campo_nome = navegador.find_element(By.ID, "nome_usuario")
    campo_email = navegador.find_element(By.ID, "email")
    botao_enviar = navegador.find_element(By.ID, "btn enviar")

    campo_nome.send_keys("Alle")
    campo_email.send_keys("alle@impact.com")
    botao_enviar.click()

    mensagem_sucesso = navegador.find_element(By.ID, "msn sucesso")

    assert mensagem_sucesso.is_displayed()
    assert mensagem_sucesso.text == "Dados enviados com sucesso"


def test_acoes_avancadas_mouse(navegador):
    acoes_mouse = ActionChains(navegador)

    botao_duplo_clique = navegador.find_element(By.ID, "btn duplo")
    botao_clique_direito = navegador.find_element(By.ID, "btn direito")

    acoes_mouse.double_click(botao_duplo_clique).perform()
    assert botao_duplo_clique.text.strip() == "Autorizado"

    acoes_mouse.context_click(botao_clique_direito).perform()
    assert botao_clique_direito.text.strip() == "Menu Aberto"


def test_acoes_teclado(navegador):
    acoes_teclado = ActionChains(navegador)
    campo_observacoes = navegador.find_element(By.ID, "obs")
    novo_texto = "Teste automatizado finalizado."
    tecla_modificadora = Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL

    campo_observacoes.click()
    acoes_teclado.key_down(tecla_modificadora).send_keys("a").key_up(tecla_modificadora).send_keys(Keys.BACKSPACE).perform()
    campo_observacoes.send_keys(novo_texto)

    assert campo_observacoes.get_attribute("value") == novo_texto
