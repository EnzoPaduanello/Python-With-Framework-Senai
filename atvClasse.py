#Enzo Vitoriano Puttini Paduanello

class Pet:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Pet):
    def fazer_som(self):
        return "Au au!"

class Gato(Pet):
    def fazer_som(self):
        return "Miau!"

class Peixe(Pet):
    def fazer_som(self):
        return "Glub glub!"


cachorro = Cachorro("Olavo")
gato = Gato("Neeko")
peixe = Peixe("Nemo")


print(f"O cachorro {cachorro.nome} faz: {cachorro.fazer_som()}")
print(f"O gato {gato.nome} faz: {gato.fazer_som()}")
print(f"O peixe {peixe.nome} faz: {peixe.fazer_som()}")
