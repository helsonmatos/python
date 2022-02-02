nome = input('Digite seu nome completo: ')
nome_fatia = nome.split()
print(f'\033[35mSeu primeiro nome é {nome_fatia[0]}')
print(f'\033[35mSeu ultimo nome é {nome_fatia[-1]}')