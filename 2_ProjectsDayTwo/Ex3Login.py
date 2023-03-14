#Exercício 3
#Login

nome_criada_login = input('Digite um nome de usuário: ')
senha_criada_login = input('Digite uma senha: ')

def login(nome_criada_login, senha_criada_login):
    nome_inserida = input('Nome de Usuário: ')
    senha_inserida = input('Senha do usuário: ')

    if nome_inserida == nome_criada_login and senha_inserida == senha_criada_login:
        print('Seja Bem Vindo!')
    else:
        print('Acesso Negado!')
    return "Programa Finalizado."

print(login(nome_criada_login, senha_criada_login))