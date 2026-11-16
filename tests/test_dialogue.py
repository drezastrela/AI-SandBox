
from app.dialogue import preparar_feedback


def test_feedback_preserva_informacoes():
    pergunta = "Quanto é 15 + 27?"
    resposta = "20 + 5 + 7 = 42"
    feedback = "A explicação contém um erro."

    mensagem = preparar_feedback(pergunta, resposta, feedback)

    assert pergunta in mensagem
    assert resposta in mensagem
    assert feedback in mensagem


def test_feedback_inclui_instrucao_correcao():
    mensagem = preparar_feedback(
        "Quanto é 15 + 27?",
        "42",
        "Verifique a explicação."
    )

    assert "Apresente uma nova resposta corrigida." in mensagem
