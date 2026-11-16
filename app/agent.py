import json
from urllib.request import Request, urlopen


def perguntar_ao_modelo(pergunta):
	endereco = "http://localhost:11434/api/generate"

	dados = {
		"model": "qwen2.5:1.5b",
		"prompt": pergunta,
		"stream": False,
	}

	requisicao = Request(
		endereco,
		data=json.dumps(dados).encode("utf-8"),
		headers={"Content-Type": "application/json"},
	)

	with urlopen(requisicao, timeout=120) as resposta:
		resultado = json.load(resposta)

	return resultado["response"]


if __name__ == "__main__":
	resposta = perguntar_ao_modelo("Quanto é 15 + 27?")
	print("Resposta do Qwen:")
	print(resposta)
