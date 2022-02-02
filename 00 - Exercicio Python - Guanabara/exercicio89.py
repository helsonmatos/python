ficha = list()
rsp = ' '
while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media])
    rsp = str(input('Quer continuar? [S/N] '))
    if rsp in 'nN':
        break
print('-'*30)
for i, v in enumerate(ficha):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')
print('-'*30)
notas = 0
while notas != 999:
    notas = int(input('Mostrar notas de qual aluno? '))
    if notas == 999:
        break
    for i, v in enumerate(ficha):
        if notas == i:
            print(f'Notas de {v[0]} são {v[1]} ')
    print('-'*30)


