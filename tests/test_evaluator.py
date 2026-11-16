
from app.evaluator import avaliar_resposta, verificar_igualdade, encontrar_igualdades

def test_resposta_correta():
    assert avaliar_resposta("42", 42) is True


def test_resposta_incorreta():
    assert avaliar_resposta("32", 42) is False


def test_resposta_com_espacos():
    assert avaliar_resposta(" 42 ", 42) is True


def test_resposta_com_texto():
    assert avaliar_resposta("A resposta é 42", 42) is False


def test_igualdade_correta():
    assert verificar_igualdade("15 + 27 = 42") is True


def test_igualdade_incorreta():
    assert verificar_igualdade("20 + 5 + 7 = 42") is False


def test_igualdade_corrigida():
    assert verificar_igualdade("20 + 5 + 7 = 32") is True


def test_expressao_invalida():
    assert verificar_igualdade("texto qualquer") is False


def test_encontrar_igualdade_incorreta():
    texto = "A resposta é 42, mas calculei 20 + 5 + 7 = 42."

    resultados = encontrar_igualdades(texto)

    assert len(resultados) == 1
    assert resultados[0]["expressao"] == "20 + 5 + 7 = 42"
    assert resultados[0]["correta"] is False


def test_encontrar_igualdade_correta():
    texto = "O cálculo é 15 + 27 = 42."

    resultados = encontrar_igualdades(texto)

    assert len(resultados) == 1
    assert resultados[0]["correta"] is True


def test_encontrar_multiplas_igualdades():
    texto = "15 + 27 = 42, mas 20 + 5 + 7 = 42 está errado."

    resultados = encontrar_igualdades(texto)

    assert len(resultados) == 2
    assert resultados[0]["correta"] is True
    assert resultados[1]["correta"] is False


def test_texto_sem_igualdades():
    texto = "A resposta final é quarenta e dois."

    resultados = encontrar_igualdades(texto)

    assert resultados == []
