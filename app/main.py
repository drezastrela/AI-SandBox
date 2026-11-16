
from app.agent import perguntar_ao_modelo
from app.evaluator import avaliar_resposta
from app.challenges import desafios
from app.memory import salvar_resultado

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

        registro = {
            "modelo": "qwen2.5:1.5b",
            "desafio": desafio["id"],
            "pergunta": desafio["pergunta"],
            "resposta": resposta,
            "esperado": desafio["esperado"],
            "aprovado": aprovado
        }

        arquivo = salvar_resultado(registro)
        print(f"Resultado salvo em: {arquivo}")

        if aprovado:
            aprovados += 1

    print("\n--- RESUMO ---")
    print(f"Total de testes: {total}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {total - aprovados}")


if __name__ == "__main__":
    executar_experimentos()
