class Circo:

    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        elif tipo == 2:
            self.apresentar_palhaco()

        
    def apresentar_malabarista(self):
        print("Malabarista apresentando...")

    def apresentar_palhaco(self):
        print("Palhaco apresentando...")


circo = Circo()
circo.apresentar(1)
