import random 
from time import sleep

print("""
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
""")
jogada = int(input('Qual é a sua jogada? '))
computador = random.randint(0,2)

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
pedra = 0
papel = 1
tesoura = 2

if computador == pedra: #computador jogou pedra
    print('Computador jogou PEDRA')
    if jogada == pedra:
        print('Você jogou PEDRA')
        print('EMPATE!')
    elif jogada == papel:   
        print('Você jogou PAPEL')
        print('VOCÊ VENCEU!')
    elif jogada == tesoura:
        print('Você jogou TESOURA')
        print('VOCÊ PERDEU!')

elif computador == papel:#computador jogou papel
    print('Computador jogou PAPEL')
    if jogada == pedra:
        print('Você jogou PEDRA')
        print('VOCÊ PERDEU!')
    elif jogada == papel:
        print('Você jogou PAPEL')
        print('EMPATE!')
    elif jogada == tesoura:
        print('Você jogou TESOURA')
        print('VOCÊ VENCEU!')

elif computador == tesoura:#computador jogou tesoura
    print('Computador jogou TESOURA')
    if jogada == pedra:
        print('Você jogou PEDRA')
        print('VOCÊ VENCEU!')
    elif jogada == papel:
        print('Você jogou PAPEL')
        print('VOCÊ PERDEU!')
    elif jogada == tesoura:
        print('Você jogou TESOURA')
        print('EMPATE!')






