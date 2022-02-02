from time import sleep
primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
digito = 0
soma = 0
mult = 0
maior_numero = 0

while digito != 5 :
    print(""" [ 1 ] SOMAR
 [ 2 ] MULTIPLICAR
 [ 3 ] MAIOR
 [ 4 ] NOVOS NÙMEROS
 [ 5 ] SAIR DO PROGRAMA""")
    digito = int(input('O que você quer fazer? '))
    if digito == 1:
        soma = primeiro_valor + segundo_valor
        print(f'A soma de {primeiro_valor} e {segundo_valor} é {soma}.')
        sleep(1)
    elif digito == 2:
        mult = primeiro_valor * segundo_valor
        print(f'A multiplicação de {primeiro_valor} e {segundo_valor} é {mult}.')
        sleep(1)
    elif digito == 3:
        if primeiro_valor > segundo_valor:
            maior_numero = primeiro_valor
            print(f'O maior número entre {primeiro_valor} e {segundo_valor} é {primeiro_valor}.')
            sleep(1)
        elif primeiro_valor < segundo_valor:
            maior_numero = segundo_valor
            print(f'O maior número entre {primeiro_valor} e {segundo_valor} é {segundo_valor}.')
            sleep(1)
    elif digito == 4:
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
        sleep(1)
    elif digito == 5:
        digito = 5
        sleep(1)
    else:
        print('Tente novamente.')
        sleep(1)
    print('==========================')
print('VOCÊ FINALIZOU O PROGRAMA!')