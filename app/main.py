
from app.agent import perguntar_ao_modelo
from app.evaluator import avaliar_resposta


def executar_experimento():
    pergunta = "Quanto é 15 + 27? Responda apenas com o número."
    resultado_esperado = 42

    print("Iniciando experimento...")

    resposta = perguntar_ao_modelo(pergunta)

    print("Resposta do modelo:", resposta)

    aprovado = avaliar_resposta(resposta, resultado_esperado)

    if aprovado:
        print("Resultado: PASSED")
    else:
        print("Resultado: FAILED")


if __name__ == "__main__":
    executar_experimento()
