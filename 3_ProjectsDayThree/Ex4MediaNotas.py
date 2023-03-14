#Exercício 4
#Receber 4 notas do usuário e apresentar a média das mesmas usando dicionário

nota1 = float(input('Digite a 1º nota: ')); nota2 = float(input('Digite a 2º nota: '))
nota3 = float(input('Digite a 3º nota: ')); nota4 = float(input('Digite a 4º nota: '))

notas_gerais = {
    'nota1':nota1,
    'nota2':nota2,
    'nota3':nota3,
    'nota4':nota4
    }

todas_notas = [notas_gerais['nota1'], notas_gerais['nota2'],notas_gerais['nota3'],notas_gerais['nota4']]
nota_geral = 0

for nota in todas_notas:
    nota_geral += nota
    media = nota_geral/len(notas_gerais)
print(media)