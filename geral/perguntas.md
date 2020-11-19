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

---
