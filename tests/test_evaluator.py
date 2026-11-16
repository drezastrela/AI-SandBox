
from app.evaluator import avaliar_resposta, verificar_igualdade

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
