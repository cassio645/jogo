def jogar(usuario, banco):

    # passando os dados do usuário e do banco de dados para minusculas e sem espaços iniciais
    resp_user = usuario.strip().lower()
    resp = banco.strip().lower()

    #verifica se o usuário acertou.
    if resp_user == resp:
        return f"Acertou {resp}"
    elif resp_user:
        return f'Errou {resp}. Sua resposta foi "{resp_user}"'
    else:
        # Para None ou vazio
        return f'Errou {resp}. Você não respondeu'

