
def termometrica (tipo_temperatura, temperatura):

    """função quer recebe entrada em um tipo de grau de temperatura e converte para outra"""
    
    # atenção isdigt() é para string
    if isinstance(temperatura, (int, float)):
        if tipo_temperatura.lower() == "c":
            # arrendondar valor para 2 casas
            fahe = (9/5)*temperatura+32
            return round(fahe, 2)
        else:
            if tipo_temperatura.lower() == "f":
                celso = (5/9)*(temperatura-32)
                return round(celso, 2)
    else:
        raise ValueError ("Temperaura deve ser apenas valor numérico")
    