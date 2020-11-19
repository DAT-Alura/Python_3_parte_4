class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


class Serie:

    def __init__(self, nome, ano, temporada):
        self.__nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
print(
    f"Nome: {vingadores.nome}; "
    f"Ano: {vingadores.ano}; "
    f"Duracao: {vingadores.duracao}; "
    f"Likes: {vingadores.likes}."
)

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(
    f"Nome: {atlanta.nome}; "
    f"Ano: {atlanta.ano}; "
    f"Temporada: {atlanta.temporada}; "
    f"Likes: {atlanta.likes}."
)
