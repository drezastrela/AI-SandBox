
import json

from app.memory import salvar_resultado


def test_salvar_resultado(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    registro = {
        "modelo": "qwen2.5:1.5b",
        "desafio": "math_001",
        "resposta": "42",
        "aprovado": True
    }

    arquivo = salvar_resultado(registro)

    assert arquivo.exists()

    with arquivo.open("r", encoding="utf-8") as f:
        dados_salvos = json.load(f)

    assert dados_salvos == registro
