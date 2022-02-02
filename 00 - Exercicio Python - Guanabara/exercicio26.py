nome = input('Digite um nome : ').upper().strip()
letra = nome
print(f'\033[35mA letra A aparece {nome.count("A")} vezes')
print(f'\033[35mA primeira letra  A aparece na posição {nome.find("A")+1}')
print(f'\033[35mA última letra A aparece na posição {nome.rfind("A") + 1}')