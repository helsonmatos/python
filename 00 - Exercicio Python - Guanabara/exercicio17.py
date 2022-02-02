ca = float(input('Comprimento do cateto oposto: '))
co = float(input('Comprimento do cateto adjacente: '))
hipo = (ca ** 2 + co ** 2) ** (1/2)
print(f'\033[37mA hipotenusa vai medir {int(hipo)}\033[m')