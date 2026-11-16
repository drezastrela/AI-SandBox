
from app.agent import perguntar_ao_modelo
from app.evaluator import avaliar_resposta
from app.challenges import desafios


def executar_experimentos():
    total = len(desafios)
    aprovados = 0

    print("Iniciando bateria de testes do AI Sandbox...")

    for desafio in desafios:
        print(f"\nExecutando: {desafio['id']}")

        resposta = perguntar_ao_modelo(desafio["pergunta"])

        aprovado = avaliar_resposta(
            resposta,
            desafio["esperado"]
        )

        print(f"Resposta do modelo: {resposta}")
        print(f"Resultado: {'PASSED' if aprovado else 'FAILED'}")

        if aprovado:
            aprovados += 1

    print("\n--- RESUMO ---")
    print(f"Total de testes: {total}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {total - aprovados}")


if __name__ == "__main__":
    executar_experimentos()
