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

---
