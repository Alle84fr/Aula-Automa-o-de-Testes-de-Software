
def descontar(origin_value, rebate):
    """função para  aplicar desconto - sobre valor do produto original"""
    if 0 <= rebate and rebate <= 100: 
        cento = 1 - (rebate/100)
        final = origin_value * cento
        
        if final == 0: return "Grátis"
        
        elif final == origin_value: return "Sem desconto"
        
        elif final < 0: raise ValueError ("Valor máximo de desconto é 100%")
        
        else: return final
        
    else: raise ValueError ("Desconto deve ser entre 0 e 100")


