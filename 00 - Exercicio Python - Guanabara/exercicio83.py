expressao = []
expressao_char = str(input('Digite uma expressão: '))
for i in expressao_char:
    if i == '(':
        expressao.append('(')
    elif i == ')':
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(')')
            break
if len(expressao) == 0:
    print('Expressão está válida.')
else:
    print('Sua expressão está errada!')

