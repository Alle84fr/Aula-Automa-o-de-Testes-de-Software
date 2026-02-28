from math import sqrt
from statistics import mean
from basico_01 import subtrair

def raiz_quadrada(a):
    if a > 0:
        raiz = sqrt(a)
        return raiz
    else: return "Valor precisa ser positivo"
    
def calcular_media(li):
    cont = 0
    #sempre se cria antes
    soma = 0
    
    for i in li:
        soma += i
        cont += 1
    divisao = soma/cont
    return divisao

def comparar(a,b):
    return subtrair(a,b)%2 == 0
