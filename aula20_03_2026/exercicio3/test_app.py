import pytest
from unittest.mock import call
from app import ProcessadorDeAcoes

def test_executar_processo_com_mock(mocker):

    processador = ProcessadorDeAcoes()

    mock_validar = mocker.patch.object(processador, "validar_dados", return_value=True)
    mock_salvar = mocker.patch.object(processador, "salvar_dados", return_value=True)

    dados = {"nome": "teste"}
    resultado = processador.executar_processo(dados)

    roteiro_esperado = [
        call(dados),
        call(dados)
    ]
    mock_validar.assert_has_calls([roteiro_esperado[0]])
    mock_salvar.assert_has_calls([roteiro_esperado[1]])

    assert resultado == "Processo concluído com sucesso"

