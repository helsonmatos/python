from random import randint
from time import sleep

numero = input('Em que número eu pensei? ')
numeroM = randint(0,5)
print('PROCESSANDOO>>>>>>')

sleep(2)

if numero == numeroM:
    print('\033[35mAcertou gayzudooooo!!!')
else:
    print(f'\033[35mVocê ERRRRRRRRRRROU! Eu pensei no {numeroM}.')