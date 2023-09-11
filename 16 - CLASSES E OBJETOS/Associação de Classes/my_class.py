class Interruptor:

    def __init__(self, comodo) -> None:
        self.__comodo = comodo

    def acender(self):
        print(f"acendendo {self.__comodo}")
    
    def desligar(self):
        print(f"desligando {self.__comodo}")



class Pessoa:

    def acender_luz(self, interruptor: Interruptor):
        interruptor.acender()

    def desligar_luz(self, interruptor: Interruptor):
        interruptor.desligar()

    def dormir(self):
        print("dormindo")



junior = Pessoa()
interruptor_quarto = Interruptor("quarto")
interruptor_cozinha = Interruptor("cozinha")

interruptor_cozinha.acender()
junior.acender_luz(interruptor_quarto)
junior.desligar_luz(interruptor_cozinha)
junior.dormir()