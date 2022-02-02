print('='*15)
print('     10 TERMOS DE UMA PA')
print('='*15)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
c = 10
quan_termos = 0
while c > 0:
    print(primeiro_termo, end=' => ')
    primeiro_termo += razao
    c -= 1
    if c == 0:
        print('PAUSA')
        c = int(input('\nAcrescentar mais números na sequência? '))
print('FIM')