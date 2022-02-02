def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print(f'\033[31mUsuário preferiu não digitar esse número.\033[m')
        else:
            return n 

num = leiaInt('Digite um número: ')
print(f'O valor digitado foi {num}')