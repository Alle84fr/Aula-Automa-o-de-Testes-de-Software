import unittest

def pode_dirigir(idade):
   return idade >= 18 if True else False
    

print(pode_dirigir(17))

class Dirigir(unittest.TestCase):
    
    def Teste_Dirija(self):
        resultado = pode_dirigir(20)
        self.assertTrue(resultado)
    
    def Teste_Espere(self):
        resultado = pode_dirigir(14)
        self.assertFalse(resultado)
        
if __name__ == "__main__":
    unittest.main()
