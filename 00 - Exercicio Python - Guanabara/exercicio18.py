import math as m

valor = float(input('Digite o angulo: '))
seno = m.sin(m.radians(valor))
cos = m.cos(m.radians(valor))
tang = m.tan(m.radians(valor))
print(f'\033[35mO angulo em {valor} tem o SENO de {seno:.2f}.\033[m')
print(f'\033[33mO angulo em {valor} tem o COSSENO de {cos:.2f}.\033[m')
print(f'\033[31mO angulo em {valor} tem o TANGENTE de {tang:.2f}.\033[m')