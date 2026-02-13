import unittest

def validar_fromato_cpf(cpf):
    
    
   return (
        isinstance(cpf, str) and
        len(cpf) == 11 and
        cpf.isdigit()
    )

class Teste_Validar_Cpf(unittest.TestCase):
    
    def test_True(self):
        self.assertTrue(validar_fromato_cpf("55599988869"))
    
    def test_False1(self):
        self.assertFalse(validar_fromato_cpf("111222333666"))
    
    def test_False2(self):
        self.assertFalse(validar_fromato_cpf("111-222-333.12"))
    
    def test_False3(self):
        self.assertFalse(validar_fromato_cpf("1234567890A"))
        
    def test_False5(self):
        self.assertFalse(validar_fromato_cpf("1234567"))
        
    def test_False6(self):
        self.assertFalse(validar_fromato_cpf(1234567890))

if __name__ == "__main__":
    unittest.main()
    
# EFFFFE
# E - erro de execução
# F - Falha
# . - passou