
from app.evaluator import avaliar_resposta


def test_resposta_correta():
    assert avaliar_resposta("42", 42) is True


def test_resposta_incorreta():
    assert avaliar_resposta("32", 42) is False


def test_resposta_com_espacos():
    assert avaliar_resposta(" 42 ", 42) is True


def test_resposta_com_texto():
    assert avaliar_resposta("A resposta é 42", 42) is False
