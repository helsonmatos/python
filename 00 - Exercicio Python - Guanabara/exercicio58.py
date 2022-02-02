from random import randint
computador = randint(0,10)
print("""Sou seu computador...
    Acabei de pensar em um número entre 0 e 10.
    Será que você consegue adivinhar qual foi?
""", end=' ')

palpite = int(input('Qual o seu palpite? '))
tentativas = 1

while computador != palpite:
    if computador > palpite:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
        tentativas += 1 
    elif computador < palpite:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual o seu palpite? '))
        tentativas += 1 
    elif computador == palpite:
        tentativas += 1 
    
print(f'Acertou em {tentativas} tentativas. Parabêns!')