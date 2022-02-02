import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
alunos = [n1, n2, n3, n4]

random.shuffle(alunos)
print(f'\033[321mA ordem de apresentação é: {alunos}\033[m')
