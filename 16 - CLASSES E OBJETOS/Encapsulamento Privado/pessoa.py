class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self):
        print('Correndo')

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento
        print('bebendo...')

    def __apresentar_documento(self):
        print(self.__cpf)

    def print_cpf(self):
        print(self.__cpf)

ronaldo = Pessoa('Ronaldo', 40, '129310238')
print(ronaldo.nome)
print(ronaldo.idade)
ronaldo.print_cpf()

ronaldo.beber('cerveja')
ronaldo.beber('coca')