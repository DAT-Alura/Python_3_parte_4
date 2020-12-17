# Aula 1

Qual a vantagem de criar uma classe com construtor __init__?

Por exemplo, sem o contrutor teríamos:

```py
class Produto:
    pass
```

Com o construtor __init__ ficaria:

```py
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
```

A - Não é possível criar uma classe sem definir um construtor.

__B__ - É mais fácil criar com o inicializador, já que informamos os argumentos.
> Correto, sem o construtor nós precisaríamos definir os atributos depois de instanciar, teríamos o trabalho de descobrir quais atributos definir.

C - Criar com o inicializador não tem vantagem nenhuma na criação de objetos.

D - Criar com o inicializador é vantajoso quando quisermos definir todos os métodos da classe.

---

De acordo com o que foi visto na aula, como deve ser a saída do código abaixo?

```py
jonas = 'jonas augusto'
print(f'Meu nome não é {jonas.title()}')
```

A - Meu nome não é jonas Augusto

B - Meu nome não é jonas augusto

__C__ - Meu nome não é Jonas Augusto
> Correto, o title pega a primeira letra de cada palavra e coloca em maiúsculo.

D - Meu nome não é jonas_augusto

---

Qual a vantagem de usar um property ao invés de métodos getters e setters?

__A__ - Os properties são importantes, pois quem depende da classe não precisa mudar.
> Certo, usar property é uma ótima prática. Quando criamos getters e setters todos os lugares que já acessam a classe precisam mudar.

B - O getter e setter é uma boa prática, o property não é muito usado.

C - O property faz com que a classe fique menor.

D - Não tem diferença entre os dois modelos de acesso.

# Aula 2

Tenho 2 classes que têm comportamentos iguais:

```py
class Carro:
    def abastecer(self, litros):
        pass

class Moto:
    def abastecer(self, litros):
        pass
```

Utilizando herança, como posso fazer para remover esta duplicação?

A -
```py
class Veiculo:
    def abastecer(self, litros):
        pass

class Moto : Veiculo
    pass

class Carro : Veiculo
    pass
```

B -
```py
class Veiculo:
    def abastecer(self, litros):
        pass

class Moto extends Veiculo:
    pass

class Carro extends Veiculo:
    pass
```

C -
```py
class Veiculo:
    pass

class Moto(Veiculo):
    def abastecer(self, litros):
        pass

class Carro(Veiculo):
    def abastecer(self, litros):
        pass
```

__D__ -
```py
class Veiculo:
    def abastecer(self, litros):
        pass

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass
```
> Correto, desta forma, o método abastecer é herdado pelas classes Moto e Carro.

---

Quais as vantagens de usar herança para generalizar classes similares?

A - Melhora a performance da classe

__B__ - Compartilhar código com as subclasses
> Correta! Todas as subclasses tem acesso aos métodos criados na superclasse.

C - Deixar o código das subclasses mais bonito

__D__ - Reduz a duplicação de código e pontos de falha
> Correta! A herança faz com que o seu código não fique duplicado, reduzindo os pontos de falha.

---

Existem diversas formas de usar herança, mas em alguns momentos queremos fazer algo a mais na subclasse, algo que usa em parte o comportamento da superclasse e adiciona alguma nova funcionalidade.

Como podemos fazer isto?

__A__ - Criar um método com a nova funcionalidade e que também chama o método super() (utilizando comportamentos da superclasse).
> Correto! Neste caso, conseguimos adicionar comportamento utilizando código da super classe.

B - Criar um método com nome diferente do método da superclasse, sem chamar super().

C - Criar um método que só chama o método super()


# Aula 3

Falamos sobre polimorfismo, e que, quando usamos herança, ganhamos essa vantagem junto com a redução da duplicação. Mas do que se trata o polimorfismo?

A - É quando temos várias classes iguais.

B - É uma forma de herança sem compartilhar comportamento.

C - Polimorfismo é a ideia de compartilhar código entre várias classes.

__D__ - É quando não importa a classe sendo usada, contanto que esta classe herde de uma superclasse específica.
> Correto. Um código que espera uma superclasse, pode receber qualquer classe filha, reduzindo a quantidade de ifs às vezes, pois não precisamos mais verificar o tipo da classe.

---

Usando polimorfismo, consigo gerar relatórios de qualquer tipo, usando o código abaixo:

```py
class Relatorio:
    def gera_relatorio(self):
        print('Relatório geral')

class RelatorioUsuarios(Relatorio):
    def gera_relatorio(self):
        print('Relatório dos usuários')

class RelatorioCustos(Relatorio):
    def gera_relatorio(self):
        print('Relatório de custos')

relatorio1 = RelatorioUsuarios()
relatorio2 = RelatorioCustos()
relatorio3 = RelatorioUsuarios()
relatorio4 = RelatorioUsuarios()

relatorios = [relatorio1, relatorio2, relatorio3, relatorio4]
for rel in relatorios:
    rel.gera_relatorio()
```

Em que trecho do código ocorre o polimorfismo?

A -
```py
relatorios = [relatorio1, relatorio2, relatorio3, relatorio4]
```

__B__ -
```py
def gera_relatorio(self):
    print('Relatório geral')
```
> Correto, neste momento não importa qual é a classe do relatório.

C -
```py
for rel in relatorios:
    rel.gera_relatorio()
```

D -
```py
class RelatorioUsuarios(Relatorio):

e

class RelatorioCustos(Relatorio):
```

---

Temos uma classe que define NotaFiscal, então queremos definir uma forma de exibir um objeto NotaFiscal como string para o usuário do sistema.

Qual o jeito pythônico de fazer isto, modificando somente a classe NotaFiscal?

A - Criar um método to_string na classe.

B - Criar um atributo nome na classe.

C - Criar um método str() que retorna este nome como string.

__D__ - Criar o método especial __str__ que retornará uma representação string do objeto.
> Correto, este método é chamado pelo print() e pelo str(), ambos built-ins da linguagem.


# Aula 4

Quando podemos usar um objeto no for?


__A__ - O Objeto deve ser iterable.
> Correto, o objeto deve ser iterable. O que significa isso, veremos ainda nesse curso.

B - A classe deve herdar da classe ForIn.

C - O Objeto deve ter o método len.

D - Qualquer objeto é iterable.

---

Quando quero criar uma classe e ela se parece com uma listagem, quais as vantagens de herdar um list?

__A__ - Não vou precisar fazer tudo na mão.
> Correto, não preciso reinventar a roda, se a classe mãe já tem o que eu preciso.

__B__ - Vou ter as facilidades de suporte do for in, in e outras expressões da linguagem.
> Correto, ganho um monte de vantagens só porque os aspectos pythonicos da linguagem já conhecem a estrutura da minha classe.

C - Vou conseguir criar objetos de forma mais performática.

D - Não vou poder mudar nem criar comportamentos na minha classe.

---

Quais as desvantagens de se fazer herança de uma classe que não conhecemos completamente?

A - Não temos acesso a todos os métodos.

__B__ - Pode ter comportamentos indesejados internamente, como métodos dependentes.
> Correto, as vezes o código desconhecido tem efeitos colaterais também.

__C__ - Não podemos sair modificando tudo, pois podemos criar bugs.
> Correto, no caso se, alguém depende do comportamento da superclasse e nós mudarmos, não tem como controlar a consequência.

D - Temos menos duplicação usando o código da superclasse.
