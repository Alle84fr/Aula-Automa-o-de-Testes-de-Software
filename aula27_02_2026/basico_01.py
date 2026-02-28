def somar(a,b):
    soma = a + b
    return soma

def subtrair(a,b):
    subt = a - b
    return subt

def multiplicar(a,b):
    mult = a*b
    return mult

def dividir(a,b):
    divi = a/b
    
    if b == 0:
        raise ValueError("Divisor deve ser diferente de zero")
    else:
        return divi
    