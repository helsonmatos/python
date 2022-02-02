print('-='*15)
def contagem(inicio,fim,pulando=1):
    print(f'Contagem de {inicio} até {fim} de {abs(pulando)} em {abs(pulando)}')
    for i in range(inicio,fim,pulando):
        print(i,end=' ')
    print('FIM!')
    print('-='*15)
        
contagem(1,10)
contagem(10,0,-2)
print('Agora é sua vez de personalizar a contagem.')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
pulando = int(input('Passo: '))
contagem(inicio,fim,pulando)