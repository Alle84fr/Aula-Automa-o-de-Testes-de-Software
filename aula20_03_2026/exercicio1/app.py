

def enviar_mensagem_externa(destinatario:str, conteudo:str):
    return f"Mensagem enviada para {destinatario}: {conteudo}"

def processar_envio(destinatario: str, texto: str):
    return(enviar_mensagem_externa(destinatario,texto))