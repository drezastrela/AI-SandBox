
from app import main


def test_executar_correcao(monkeypatch):
    mensagens_recebidas = []

    def modelo_simulado(mensagem):
        mensagens_recebidas.append(mensagem)
        return "Resposta corrigida de teste"

    monkeypatch.setattr(
        main,
        "perguntar_ao_modelo",
        modelo_simulado
    )

    resultado = main.executar_correcao(
        "Quanto é 15 + 27?",
        "20 + 5 + 7 = 42",
        "Existe um erro na explicação."
    )

    assert resultado == "Resposta corrigida de teste"
    assert len(mensagens_recebidas) == 1
    assert "Quanto é 15 + 27?" in mensagens_recebidas[0]
    assert "20 + 5 + 7 = 42" in mensagens_recebidas[0]
    assert "Existe um erro na explicação." in mensagens_recebidas[0]
