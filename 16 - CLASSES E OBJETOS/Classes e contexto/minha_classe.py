class MinhaClasse:
    
    def __init__(self, att):
        self.meu_atributo = 'Ola Mundo'
        self.meu_atributo2 = att

    def meu_metodo(self):
        print('estou no metodo!')
        print(self.meu_atributo)

    def meu_metodo2(self, num, mult):
        return num + mult
        

objeto = MinhaClasse('Meu segundo atributo')
objeto.meu_metodo()

result = objeto.meu_metodo2(3,2)
print(result)

print(objeto.meu_atributo)
print(objeto.meu_atributo2)