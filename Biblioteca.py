class Biblioteca:
    def __init__(self, nome, autor, edicao, categoria):
        self.nome = nome
        self.autor = autor
        self.edicao = edicao
        self.categoria = categoria

    def descricao(self):
        print(
            f"{self.nome} é um livro do {self.autor} do ano de {self.edicao} na categoria de {self.categoria}.")


livro = Biblioteca("📕It", "Fernando Saldanha", 2006, "suspense")
livro.descricao()
print("---------------------")

livro2 = Biblioteca("📙It 2", "Fernando Saldanha", 2008, "suspense")
livro2.descricao()
