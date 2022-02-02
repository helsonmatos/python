nome = input('Digite seu nome completo: ').strip()
letras = nome.split()
espacos = nome.count(" ")
frase = len(nome) - espacos
print(f'\033[31mSeu nome em Maiúscula é {nome.upper()}\033[m')
print(f'\033[32mSeu nome em Minúscula é {nome.lower()}\033[m')
print(f'\033[35mSeu nome ao todo tem {int(frase)} letras.\033[m')
print(f'\033[37mSeu primeiro nome tem {nome.find(" ")} letras\033[m')
