class Carro:
    def __init__(self, cor, marca, ano):
        self.cor = cor
        self.marca = marca
        self.ano = ano
    def Atributos(self):
        print(f'A marca do carro é {self.marca}')

c = Carro(cor="cinza", marca="bmw", ano="2024")
c.Atributos()
"""
class Carro:
    def __init__(self, cor, marca, ano):
        self.cor = cor
        self.marca = marca
        self.ano = ano
    def Atributos(self):
        print(f'A marca do carro é {self.marca}')

c = Carro(cor="cinza", marca="bmw", ano="2024")
c.Atributos()
"""