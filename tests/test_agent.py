
from app.agent import perguntar_ao_modelo


def test_agente_responde():
    resposta = perguntar_ao_modelo("Diga apenas: teste")

    assert isinstance(resposta, str)
    assert len(resposta.strip()) > 0
