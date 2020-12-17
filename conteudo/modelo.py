class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.likes} Likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(
            f"{self.nome} - {self.ano} - {self.duracao} - {self.likes} Likes"
        )

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.likes} Likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporada} - {self.likes} Likes"


vingadores = Filme("vingadores", 2018, 160)
vingadores.dar_like()

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)


print(repr(atlanta))