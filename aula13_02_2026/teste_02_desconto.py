import unittest

def calcular_desconto(valor, percentagem):
    
    p = percentagem/100
    porcento = valor*(p)
    
    #virgula forma um tupla
    cinquenta_cento = valor*0.5
    if porcento > cinquenta_cento:
        valor = valor * (1 - 0.5)
    else:
        valor = valor*(1-p)
        
    return valor

print(calcular_desconto(100, 55))

class TesteDesconto(unittest.TestCase):
    
    #teste 1 - True
    def teste_true(self):
        result = calcular_desconto(100, 70)
        self.assertTrue(result)
        
    #teste 2 - False
    def teste_false1(self):
        result = calcular_desconto(100, 100)
        self.assertFalse(result)
    #teste 3 - False
    def teste_false2(self):
        result = calcular_desconto(50, 20)
        self.assertFalse(result)
    #teste 2 - False
    def teste_false3(self):
        result = calcular_desconto(15, 0)
        self.assertFalse(result)

if __name__=="__main__":
    unittest.main()
    
# Retorno

# retorno do print(calcular_desconto(100, 55))
# >>> 50.0
# 3 F são que 3 testes falharam
# . é que um teste foi true
# >>> FFF.

# ======================================================================
# FAIL: teste_false1 (__main__.TesteDesconto.teste_false1)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\arfur\Documents\python_geral\gionavi\aula13_02_2026\teste_02_desconto.py", line 29, in teste_false1
#     self.assertFalse(result)
#     ~~~~~~~~~~~~~~~~^^^^^^^^

# * Aqui qualquer n° diferente de 0 é true
# AssertionError: 50.0 is not false

# ======================================================================
# FAIL: teste_false2 (__main__.TesteDesconto.teste_false2)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\arfur\Documents\python_geral\gionavi\aula13_02_2026\teste_02_desconto.py", line 33, in teste_false2
#     self.assertFalse(result)
#     ~~~~~~~~~~~~~~~~^^^^^^^^
# AssertionError: 40.0 is not false

# ======================================================================
# FAIL: teste_false3 (__main__.TesteDesconto.teste_false3)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\arfur\Documents\python_geral\gionavi\aula13_02_2026\teste_02_desconto.py", line 37, in teste_false3
#     self.assertFalse(result)
#     ~~~~~~~~~~~~~~~~^^^^^^^^
# AssertionError: 7.5 is not false

# ----------------------------------------------------------------------
# Ran 4 tests in 0.002s

# FAILED (failures=3)