#Exerrcício 2
#Questionário CNH

try:
    idade = int(input('Digite sua idade: '))

    if idade < 18:
        print('É preciso ser maior de idade para participar dos cursos')
    elif idade >= 18:
        cnh = int(input('''
        Você já possui CNH?

        Se sim digite [1]
        Se não digite [2]

        Digite sua opção: '''))
        if cnh == 1:
            print('Você pode partcipar dos cursos de: Direção Defensiva e Defesa Pessoal.')
        elif cnh == 2:
                print('Você pode participar dos cursos de: Defesa Pessoal.')
        else :
                print('Resposta inválida!!!')
except:
    print('Idade inválida!!!')