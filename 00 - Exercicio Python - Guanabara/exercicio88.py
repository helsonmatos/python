from random import sample
from time import sleep

print('-'*35)
print('         JOGA NA MEGA SENA')
print('-'*35)

sorteio = int(input('Quantos jogos você quer que eu sorteie? '))
count = 0
jogos = []
print(f'-=-=-= SORTEANDO {sorteio} JOGOS -=-=-=')
sleep(1)
while count < sorteio:
    count += 1
    jogos.append(sample(range(60),6))
    jogos[count-1].sort()
    

for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v} ')
    sleep(0.8)

print('-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')

    