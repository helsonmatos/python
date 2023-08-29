class Pessoa:

    def __init__(self, name: str, idade: int) -> None:
        self.name = name
        self.idade = idade

    def dirigir(self, veiculo) -> None:
        print(f'Dirigindo um(a) {veiculo}')

    def cantar(self) -> None:
        print('lalalala')

    def apresentar_idade(self) -> int:
        return self.idade


ney = Pessoa('Neymar',31)