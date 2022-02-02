from random import randint
print('='*30)
print('VAMOS JOGAR PAR OU IMPAR')
print('='*30)
total = 0
par_impar_result = ''
vitoria = 0
while total < 30:
    computador = randint(1,10)
    valor = int(input('Diga um valor: '))
    par_ou_impar = str(input('Par ou Ìmpar? [P/I]: ')).lower()
    print('='*30)
    total = valor + computador
    
    if total % 2 == 0:
        par_impar_result = 'p'
        if par_ou_impar == par_impar_result:
            print(f'Você jogou {valor} e o computador {computador}.\nTotal deu {total} PAR')    
            print('Você GANHOU!')
            vitoria += 1
        else:
            print(f'Você jogou {valor} e o computador {computador}.\nTotal deu {total} IMPAR')
            print('Você PERDEU')
            break
    elif total % 2 != 0:
        par_impar_result = 'i'
        if par_ou_impar == par_impar_result:
            print(f'Você jogou {valor} e o computador {computador}.\nTotal deu {total} IMPAR')
            print('Você GANHOU!')
            vitoria += 1
        else:
            print(f'Você jogou {valor} e o computador {computador}.\nTotal deu {total} PAR')
            print('Você PERDEU')
            break
            


print(f'Você venceu {vitoria} veze(s)')