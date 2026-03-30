# python -m pip install pytest pytest-mock
#  python -m pytest -v ou so  python -m pytest

import pytest
from unittest.mock import call
from app import enviar_mensagem_externa,processar_envio
import requests

def test_verificar_smg_ext(mocker):
    
    # guarda o objeto retornado pelo mocker.patch
    caminho_mock = mocker.patch("app.enviar_mensagem_externa")
    
    # valor a ser chamado
    caminho_mock.return_value = "mock garante chamada na ordem exta"
    
    destinatario = "Alessandra"
    
    conteudo = "Exercício 1"
    
    chamar_mock = processar_envio(destinatario,conteudo)
    
    caminho_mock.assert_called_once_with(destinatario, conteudo)
    
    assert chamar_mock == "mock garante chamada na ordem exta"
    
#