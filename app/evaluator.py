
def avaliar_resposta(resposta, esperado):
    resposta = resposta.strip()

    try:
        numero = int(resposta)
    except ValueError:
        return False

    return numero == esperado
