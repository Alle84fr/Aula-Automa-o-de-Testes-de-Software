import unittest

def cadastrar_senha(senha):
    
    if senha == "12345678":
        raise ValueError("Processo interrompido")
    
    if len(senha) != 8:
        if len(senha)<8:
            raise ValueError("Senha muito curta")
        if len(senha)>8:
            raise ValueError("Senha muito longa")
    else:
        return True

class Test_Cadastro(unittest.TestCase):
    
    #teste true
    #def INICIAR EM TEST E NÃO TESTE
    def test_Cad_true(self):
        retorno = cadastrar_senha("15987639")
        self.assertTrue(retorno)
        
    #teste False
    def test_Cad_false1(self):
        #ele tem com valor o raise valueError
        with self.assertRaises(ValueError):
            cadastrar_senha("1277889")
        
    def test_Cad_false2(self):
        with self.assertRaises(ValueError):
            cadastrar_senha("1378895698")

    def test_Cad_exception(self):
        with self.assertRaises(ValueError):
            cadastrar_senha("12345678")

if __name__ == "__main__":
    unittest.main()
    
# with self.assertRaises(ValueErroe)

# testa se aparece o erro, exceção, epera que dê o erro - e se acontece o erro dá teste ok

# cria um bloco observando o valor de erro