import random
from time import sleep
from operator import itemgetter

jogadores = dict()
jogadores['Jogador 1'] = random.randint(1,6)
jogadores['Jogador 2'] = random.randint(1,6)
jogadores['Jogador 3'] = random.randint(1,6)
jogadores['Jogador 4'] = random.randint(1,6)
ranking = list()

print('-='*20)
print('Valores sorteados')
sleep(0.7)
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.7)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*20)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} .')
    sleep(0.7)
print('-='*20)