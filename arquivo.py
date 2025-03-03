import json

ARQUIVO_RANKING = "ranking.json"

def carregar_ranking():
    '''Carrega o ranking do arquivo JSON. Se não existir, retorna uma lista vazia.'''
    try:
        with open(ARQUIVO_RANKING, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_ranking(ranking):
    '''Salva o ranking no arquivo JSON'''
    with open(ARQUIVO_RANKING, "w", encoding="utf-8") as f:
        json.dump(ranking, f, indent=4)

def adicionar_ou_atualizar_usuario(nome, dinheiro):
    '''Adiciona um novo usuário ou atualiza seu dinheiro, ordenando o ranking.'''
    ranking = carregar_ranking()

    for usuario in ranking:
        if usuario["nome"] == nome:
            usuario["dinheiro"] = dinheiro
            break
    else:
        ranking.append({"nome": nome, "dinheiro": dinheiro})

    ranking.sort(key=lambda x: x["dinheiro"], reverse=True)
    salvar_ranking(ranking)

def exibir_ranking():
    '''Exibe o ranking no terminal.'''
    ranking = carregar_ranking()
    print("\nRanking:")
    for i, usuario in enumerate(ranking, start=1):
        print(f"{i}. {usuario['nome']} - R${usuario['dinheiro']:.2f}")