class Cachorro(object):
    def __init__ (self, nome, raca):
        
        self.raca = raca
        self.nome = nome
        print(f'Parabéns, eu sou {self.nome}, da raça {self.raca} seu novo cachorro')
    
    def late(self):
        print(f'{self.nome} late')
    
caramelo = Cachorro("Paçoca", "Bulldog")
caramelo.late()

caraDeChinelo = Cachorro("Cara de chinelo", "Humano")
caraDeChinelo.late()

print('')

class Gato(object):
    def __init__(self, nome):
        self.nome = nome
        print(f'Parabéns, eu sou {self.nome}, seu novo gato')
        
    def  mia(self):
            print(f'{self.nome} mía')
            
sergio = Gato('Sergio')
sergio.mia()

print('')

#Criando uma classe para deixar mais prático
class Animal(object):
    def __init__(self, tipo, raca, nome, anoNasc, som, cor):
        self.tipo = tipo
        self.raca = raca
        self.nome = nome
        self.anoNasc = anoNasc
        self.som = som
        self.cor = cor
        
        print(f'Meu nome é {self.nome}, sou um(a) {self.tipo} {self.raca}. Nasci no ano {self.anoNasc}.')
    
    def somAnimal(self):
        print(f'{self.nome} {self.som}')
        
    def idadeAnimal(self, anoAtual):
        return anoAtual - self.anoNasc
    
    def setAnoNasc(self, ano):
        self.anoNasc = ano
    
animal1 = Animal("onça", "pintada", "Jonas", 2020, "ruge", '')

idade = animal1.idadeAnimal(2024)
print(f'Idade do {animal1.nome}: {idade}')

animal1.setAnoNasc(2017)
idade = animal1.idadeAnimal(2024)
print(f'Idade do {animal1.nome}: {idade}. Ano de nnascimento: {animal1.anoNasc}')

animal1.somAnimal() 

animal1.cor = 'azul'
print(animal1.cor)