print('='*15)
print('     10 TERMOS DE UMA PA')
print('='*15)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao
c = 0
while decimo >= c:
    print(primeiro_termo, end=' -> ')
    primeiro_termo += razao
    c = primeiro_termo
print('FIM')