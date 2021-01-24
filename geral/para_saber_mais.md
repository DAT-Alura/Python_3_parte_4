# Atributos de classe

Quando criamos atributos no inicializador, estamos definindo quais serão as características do objeto sendo definido. Mas esta não é a única forma de adicionar características ao objeto ou mesmo à classe.

O aspecto dinâmico da linguagem permite que seja possível adicionar atributos até sem precisar do __init__. Veja abaixo:

```py
class Pessoa:
    pass

pessoa = Pessoa()
pessoa.nome = 'Jade'
print(pessoa.nome)
```

Se você tentar executar este código, verá que funciona perfeitamente.

Optamos em usar o inicializador, primeiro para facilitar a criação de novos objetos e segundo para diminuir a confusão em saber o que a classe precisa para criar um objeto aceitável. Sem o init, não dá para saber facilmente quais atributos a classe possui.

Normalmente usamos o init para definir os atributos, mas o que fazer se precisarmos definir um valor padrão para todos os objetos? Ou até criar um atributo que será compartilhado para todas as instâncias?

Para isto, vai ser necessário criar um atributo ligado à classe, ao invés de ligado à instância (self). Por exemplo:

```py
class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False

pe = Pessoa('00000000001', 'Ruby')
print(pe.valida_cpf())

pe = Pessoa('0000000000', 'Cristal')
print(pe.valida_cpf())
```

Veja como o valor de tamanho_cpf é usado por todas as instâncias.

Esse é um atributo de classe. É possível alterar o valor deste atributo, mudando seu estado e não é necessário criar uma instância para acessá-lo.

No trecho de código acima, precisamos usar o __class__ para definir que queremos o atributo de classe. Dentro do nosso método de instância precisamos fazer desta forma.

Se não fizermos deste jeito, podemos ter problemas, como no código abaixo. Faça um teste:

```py
class Pessoa:
    tamanho_cpf = 11

p = Pessoa()

print(p.tamanho_cpf)

p.tamanho_cpf = 12

print(p.tamanho_cpf)

print(Pessoa.tamanho_cpf)
```

O que acontece é que, caso não exista o atributo tamanho_cpf na instância, o Python busca o atributo na classe. Em seguida, adicionamos um atributo tamanho_cpf na instância e quando dizemos que o valor é 12, o atributo da classe não é alterado, já que são atributos diferentes, um da classe e outro só da instância.

# Metodos estaticos e de classe

Da mesma forma que temos alguns atributos diretamente da classe, e que são acessíveis sem necessidade de criar uma instância, conseguimos também criar métodos ligados à classe.

Há duas formas de criar estes métodos:

## Métodos de classe

São métodos declarados com @classmethod. Quando criamos um método de classe, temos acesso aos atributos da classe. Da mesma forma com os atributos de classe, podemos acessar estes métodos de dentro dos métodos de instância, a partir de __class__, se desejarmos:

```py
class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'
```

Perceba que, ao invés de self, passamos cls para o método, já que neste caso sempre recebemos uma instância da classe como primeiro argumento. O nome cls é uma convenção, assim como self.

## Métodos estáticos

A outra forma de criar métodos ligados à classe é com a declaração @staticmethod. Veja abaixo:

```py
class FolhaDePagamento:
    @staticmethod
    def log():
        return f'Isso é um log qualquer'
```

Note que, no caso acima, não precisamos passar nenhum primeiro argumento fixo para o método estático. Nesse caso, não é possível acessar as informações da classe, porém o método estático é acessível a partir da classe e também da instância.

## Cuidados a tomar...

Sempre que você usar métodos estáticos em classes que contém herança, observe se não está tentando acessar alguma informação da classe a partir do método estático, pois isso pode dar algumas dores de cabeça pra entender o motivo dos problemas.

Alguns pythonistas não aconselham o uso do @staticmethod, já que poderia ser substituído por uma simples função no corpo do módulo. Outros mais puristas entendem que os métodos estáticos fazem sentido, sim, e que devem ser vistos como responsabilidade das classes.

# Outra forma de representação

Nós vimos como usar ```__str__``` para representar um objeto como string de forma legível.

Falamos sobre uma outra forma de representação, ela pode ajudar bastante se precisarmos encontrar um erro, ou debugar o código.

Assim como o ```__str__```, existe outro método especial chamado ```__repr__```, que é usado para mostrar uma representação que ajude no debug ou log de um código.

Por exemplo, se você quiser entender como funciona seu objeto, ou se está válido, e imprimir o seu valor string, qual resultado abaixo facilita sua vida?

```py
> Filme(nome='vingadores', ano=2018, duracao=160)
```

Ou

```py
> "Filme: Vingadores de 2018 - 160 min"
```

A primeira deixa bem claro como funciona o objeto. Normalmente, a segunda forma ilustra o que um usuário final ficaria satisfeito em ver.

A ideia da primeira versão é remover ambiguidade e permite, por exemplo, recriar o objeto, já que está mostrando todas as informações.

Outro exemplo, se chamarmos o repr de um objeto do tipo list, podemos ter uma ideia do que é esperado quando criarmos o nosso próprio com ```__repr__```:

```py
lista = [1, 2, 4, 5]

print(repr(lista))
```

Se pegarmos o resultado do print, conseguimos recriar o objeto lista.

# Criando ABC

Verificamos que é possível usar classes abstratas do sistema, e conseguimos alguns benefícios de bandeja, por exemplo:

- Tenho um erro que me diz, em tempo de instanciação, se eu esqueci de implementar algum método da superclasse
- E também sou impedido de instanciar um objeto do tipo da superclasse, pra não ter problema com os métodos abstratos.
- Ainda posso aproveitar código dos meus métodos abstratos (que podem ter implementação na classe mãe)

Se você ficou com curiosidade sobre como criar uma classe abstrata, vamos pensar no seguinte caso: imagine que não queremos permitir que ninguém instancie um objeto da classe ```Programa```, e queremos garantir que todo mundo implemente o ```__str__``` nas suas subclasses. Parece uma boa ideia.

Para fazer isso, o nosso código ficaria assim:

```py
from abc import ABCMeta, abstractmethod
class Programa(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass
```

Apenas com isso, podemos garantir que o ```__str__``` será implementado nas nossas subclasses, se não for implementado em alguma, será avisado em tempo de instanciação (não vai conseguir criar instâncias).
