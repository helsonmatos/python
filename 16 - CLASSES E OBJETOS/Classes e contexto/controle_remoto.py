class ControleRemoto:

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print(f"canal Avancado")
        
    def voltar_canal(self):
        print(f"Voltar canal")
        
    def escolher_canal(self, canal):
        print(f"Alterado para o canal: {canal}")


controle_sala = ControleRemoto('Samsung','sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.escolher_canal(12)
controle_sala.avancar_canal()