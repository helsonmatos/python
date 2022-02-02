quilome = int(input('Digite quantos KM é sua viagem: '))

if quilome <= 200:
    valor = quilome * 0.50
    print(f'\033[35mSua viagem vai custar R${valor}0')

else:
    valor = quilome * 0.45
    print(f'\033[35mSua viagem vai custar R${valor}0')