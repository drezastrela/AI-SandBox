
def preparar_feedback(pergunta, resposta, feedback):
    mensagem = f"""
Desafio original:
{pergunta}

Resposta anterior do modelo:
{resposta}

Feedback do pesquisador:
{feedback}

Analise o feedback recebido.
Identifique possíveis erros na sua resposta anterior.
Apresente uma nova resposta corrigida.
Verifique se sua correção resolve o problema.
"""
    return mensagem.strip()
