#aula 2° dia 13/02/2026

#função a ser testada
def soma(a,b):
    return a + b

#teste
def test_soma():
    
    #arrange = organizar dados
    valorA = 10
    valorB = 20
    esperado = 30
    
    #act = agir
    resultado_real = soma(valorA,valorB)
    
    #asert = afirmar
    try:
        assert resultado_real == esperado
        print(f"Soma correta {esperado}")
    except AssertionError:
        print(f"Soma errada, esperava {esperado}, mas foi {resultado_real}")

test_soma()