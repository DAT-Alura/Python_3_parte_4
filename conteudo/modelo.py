class Programa:
    ano = None
    _nome = None
    _likes = None

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
    duracao = None

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
    temporada = None

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporada} - {self.likes} Likes"


class Playlist:
    nome: str = None
    _programas: list = None

    def __init__(self, nome, programas):
        self._programas = programas
        self.nome = nome

    def __getitem__(self, index):
        return self._programas[index]

    def __len__(self):
        return len(self._programas)

    def __str__(self):
        return self.nome

vingadores = Filme("vingadores", 2018, 160)
vingadores.dar_like()

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

tmep = Serie("Todo mundo em panico", 1999, 100)
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()

demolidor = Serie("Demolidor", 2016, 2)

filmes_e_series = [vingadores, atlanta, tmep, demolidor]

playlist_fim_de_semana = Playlist(
    "Fim de semana",
    filmes_e_series
)

print(f"Tamanho da playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana:
    print(programa)
