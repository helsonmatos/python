prim = float(input('Primeiro segmento: '))
prim2 = float(input('Segundo segmento: '))
prim3 = float(input('Terceiro segmento: '))

if prim < prim2 + prim3 and prim2 < prim + prim3 and prim3 < prim + prim2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if prim == prim2 and prim == prim3 and prim2 == prim3:
        print('EQUILÀTERO')
    elif prim == prim2 or prim2 == prim3 or prim == prim3:
        print('ISÒSCELES')
    else:
        print('ESCALENO')
else:
    print(f'\033[35mOs segmentos acima NÂO PODEM FORMAR um triângulo.')


