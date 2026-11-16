
import json
from datetime import datetime
from pathlib import Path


def salvar_resultado(registro):
    pasta = Path("experiments/results")
    pasta.mkdir(parents=True, exist_ok=True)

    data_hora = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    arquivo = pasta / f"resultado_{data_hora}.json"

    with arquivo.open("w", encoding="utf-8") as f:
        json.dump(registro, f, indent=4, ensure_ascii=False)

    return arquivo
