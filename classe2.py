class Pessoa(object):
    def __init__(self,nome):
        self.nome = nome

    def getNome(self):
       return self.nome


class Fisica(Pessoa):
    def __init__(self,nome,cpf):
        super().__init__(nome)
        self.cpf = cpf
    
    def getCPF(self):
        return self.cpf

class Juridica(Pessoa):
    def __init__(self,nome,cnpj):
        super().__init__(nome)
        self.cnpj=cnpj
    
    def getCNPJ(self):
        return self.cnpj

andre = Fisica('Andre dos Santos','222.222.222.222')
print(andre.getNome())
print(andre.getCPF())

google = Juridica('Google inc','0001/658.658.254')
print(google.getNome())
print(google.getCNPJ())