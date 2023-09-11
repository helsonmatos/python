class MinhaClasse:

    def __init__(self,estado):
        self.estado = estado

    @staticmethod
    def meu_metodo():
        print("estou no meu metodo estático")


obj = MinhaClasse(True)
obj.meu_metodo()


    