import unittest

def validar_senha_avancada(senha):
  
    #any - há pelo menos um destes?
    verif_num = any(char.isdigit() for char in senha)
    verif_upp = any(c.isupper() for c in senha)
  
    if len(senha)<8:
      return False
    
    if verif_num and verif_upp:
        return True

class TesteVerificarSenha(unittest.TestCase):
    
    def test_Senha_true(self):
        self.assertTrue(validar_senha_avancada("abaCate45"))
    
    def test_Senha_False1(self):
        self.assertFalse(validar_senha_avancada("Cavalo"))
        
    def test_Senha_False2(self):
        self.assertFalse(validar_senha_avancada("camelo456"))
        
    def test_Senha_False3(self):
        self.assertFalse(validar_senha_avancada("Uva56"))
        
    def test_Senha_False4(self):
        self.assertFalse(validar_senha_avancada("12365897"))
        
if __name__ == "__main__":
    unittest.main()