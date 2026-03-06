import math

def calcular_valor_estacionamento(tempo_em_min):
    """Calcula o valor do estacionamento
    1°h = 10.00
    demais = 5.00
    24h = 50.00"""

    # tratamento para tempo zero e negativo
    if tempo_em_min <= 0:
        raise ValueError("Tempo deve ser maior que zero")

    else:
        # valor inicial da hora
        valor = 10.0

        if tempo_em_min <= 60:
            return valor

        else:
            # tirando 1° hora que é preço de 10
            adicional = tempo_em_min - 60

            # _________ ceiling = arredonda para cima o valor, se são 3h 05, vai para 4
            # tempo total / 60 min (1h) para saber h e min
            horas_adicionais = math.ceil(adicional / 60)

            # valor + (hs * 5) ex: 5hx5= 25reais + 10 do valor
            valor += horas_adicionais * 5

            # valor não passa de 50 - 24h
            
            if valor > 50:
                valor = 50

    return valor