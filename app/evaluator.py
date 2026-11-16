
def avaliar_resposta(resposta, esperado):
    resposta = resposta.strip()

    try:
        numero = int(resposta)
    except ValueError:
        return False

    return numero == esperado



import re


def verificar_igualdade(expressao):
    padrao = r"^\s*(\d+(?:\s*\+\s*\d+)*)\s*=\s*(\d+)\s*$"

    if not re.fullmatch(padrao, expressao):
        return False

    esquerda, direita = expressao.split("=")

    numeros = esquerda.split("+")
    soma = sum(int(numero.strip()) for numero in numeros)

    return soma == int(direita.strip())


def encontrar_igualdades(texto):
    padrao = r"\d+(?:\s*\+\s*\d+)+\s*=\s*\d+"

    expressoes = re.findall(padrao, texto)

    resultados = []

    for expressao in expressoes:
        resultados.append({
            "expressao": expressao,
            "correta": verificar_igualdade(expressao)
        })

    return resultados
