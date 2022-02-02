import random 

n1 = input('\033[35mAluno 1: \033[m')
n2 = input('\033[32mAluno 2: \033[m')
n3 = input('\033[34mAluno 3: \033[m')
n4 = input('\033[36mAluno 4: \033[m')
alunos = [n1, n2, n3, n4]

random.shuffle(alunos)
print(alunos)
