palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO',
'GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR',
'FUTURO')
print('-'*35)
for palavra in palavras:
    print(f'A palavra {palavra} tem: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')
    print()
        

print('-'*35)