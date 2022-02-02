nome = str(input('Digite seu nome completo: ')).lower().split()
tem_silva =  'silva' in nome 
print(f'\033[35mSeu nome tem Silva? {tem_silva}\033[35m')