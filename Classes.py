# MOdelos para criar objetos(instancias). Uma classe encapsula dados(atributos)
# e funcoes(metodos) que operam esses dados.

# self = primeiro parametro de um metodo de instancia, que se refere a propria instamcia do objeto

# construtor(__init__) = metodo chamado quando um novo objeto eh criado, usado
# para inicializar os atributos do objeto

class Carro:
    rodas = 4

    def __init__(self, marca, modelo, ano):
        """"
        Construtor da classe carro.
        Inicializa os atributos de instancia
        """
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        """"Metodo para ligar o carro"""
        print(f"O {self.marca} {self.modelo} esta ligado")
    
    def exibir_detalhes(self):
        """Metodo para exibir os detalhes do carro."""
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
        
# Criando Objetos
meu_carro = Carro("Toyota", "Corolla", 2020)
carro_amigo = Carro("Honda", "Civic", 2022)

#Acessando atributos
print(meu_carro.marca)
print(carro_amigo.modelo)

#Chamando metodos
meu_carro.ligar()
carro_amigo.exibir_detalhes()

#Acessar atributos
print(Carro.rodas)


#Heranca
class Veiculo:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor
        
    def descrever(self):
        print(f"Este eh um veiculo {self.tipo} da cor {self.cor}")

class Moto(Veiculo):
    def __init__(self, cor, cilindrada):
        self.cor = cor
        self.cilindrada = cilindrada
    
    def empinar(self):
        print(f"A moto {self.cor} de {self.cilindrada}cc esta empinando.")
        
    def descrever(self):
        print(f"Esta eh uma Moto da cor {self.cor} com {self.cilindrada}")
    
    
minha_moto = Moto("Preta", 600)
minha_moto.descrever()
minha_moto.empinar()


# #Polimorfismo
# Capacidade de objetos de diferentes classes de serem tratados de forma semelhante
# especialmente quando compartilham um interface ou herdam de uma mesma clase base

# #Encapsulamento
# agrupar dados e metodos que operam sobre esses dados em uma classe
# alem disso, restringir o acesso direto a alguns dos componentes do objeto

class MinhaClasse:
    def __init__(self):
        self.publico = "acessivel de fora"
        self._protegido = "sugerido para uso interno"
        self.__privado = "dificil de acessar diretamente"

obj = MinhaClasse()
print(obj.publico)
print(obj._protegido)
# print(obj.__privado) --> Atribbute error
print(obj._MinhaClasse__privado)

# metodos de classe(@classmethod) e Metodo estaticos(@staticmethod)
# metodos de instancia(padrao): operam em uma instancia especifica da classe(o primeiro argumento eh self)
# metodos de classe: operam na propria classe nao em um instancia especifica(primeiro argumento eh cls, que se refere a classe)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def de_ano_nascimento(cls, nome, ano_nascimento):
        idade = 2025 - ano_nascimento
        return cls(nome, idade)
    
p1 = Pessoa("Joao", 30)
p2 = Pessoa.de_ano_nascimento("ANA", 2000)
print(f"{p2.nome} tem {p2.idade} anos")


#Metodos estaticos: funcoes que pertencem a classe mas nao operam nem na instancia nem na classe.
# nao recebem self nem cls. Sao como funcoes regulares que por alguma razao logiga estap agrupadas dentro de uma classe

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def eh_par(numero):
        return numero % 2 == 0
    
print(Matematica.somar(5, 3))
print(Matematica.eh_par(4))
