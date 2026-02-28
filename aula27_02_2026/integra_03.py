def calcular_preco_final(preco_base, cupom=None, frete_gratis=False):
    '''Se recebe PRMO10 desconto de 10%
    Se recebe PROMO20 deconto de 20%
    se valor for maior ou igual que 500 frete grátis
    se valor for menor que valor do frrete -20 - o valor total será do frete'''

    if preco_base <= 0:
        raise ValueError("Preço deve ser maior que zero")

    desconto = 0

    if cupom == "PROMO10":
        desconto = 0.10
    elif cupom == "PROMO20":
        desconto = 0.20


    preco_com_desconto = preco_base * (1 - desconto)

    if frete_gratis or preco_com_desconto > 500:
        frete = 0
    else:
        frete = 20

    return preco_com_desconto + frete