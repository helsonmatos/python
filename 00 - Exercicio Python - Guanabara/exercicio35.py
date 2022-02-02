print('*=*' * 20)
print('*=*ANALISADOR DE TRIANGULOS*=*')
print('*=*' * 20)

prim = float(input('Primeiro segmento: '))
prim2 = float(input('Segundo segmento: '))
prim3 = float(input('Terceiro segmento: '))


if prim < prim2 + prim3 and prim2 < prim + prim3 and prim3 < prim + prim2:
    print(f'\033[35mOs segmentos acima PODEM FORMAR um triângulo.')
else:
    print(f'\033[35mOs segmentos acima NÂO PODEM FORMAR um triângulo.')


