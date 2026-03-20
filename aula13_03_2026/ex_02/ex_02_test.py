def test_conexao_1(banco_de_dados_de_teste):
    print(banco_de_dados_de_teste)
    assert banco_de_dados_de_teste == "Conexão Global Estabelecida"


def test_conexao_2(banco_de_dados_de_teste):
    print(banco_de_dados_de_teste)
    assert "Conexão Global Estabelecida" in banco_de_dados_de_teste
