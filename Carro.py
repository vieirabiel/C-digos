class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self, ligar):
        print(f"{self.marca} está {ligar}!")

    def informacoes(self):
        print(f"{self.marca} é um {self.modelo} do ano de {self.ano}.")


gol = Carro("🚚Gol", "Fiat", 2006)
gol.ligar("ligado")
gol.informacoes()
print("---------------------")

palio = Carro("🚓Palio", "Fiat", 2009)
palio.ligar("ligado")
palio.informacoes()
