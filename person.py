class Pessoa:
    def __init__(self,nome,endereco,phoneNumber):
        self.nome = nome
        self.endereco = endereco
        self.phoneNumber = phoneNumber

    def __repr__(self):
        return f"O individo chama-se {self.nome}, mora na rua {self.endereco}, e tem como contacto telefónico {self.phoneNumber}"

    @classmethod
    def cria_anonimo(cls):
        return cls("John Doe", 'Unknown', 000000)

if __name__ == "__main__":
    person = Pessoa("João Pereira","Rua da programação", 11199922)
    print(person)
    anonimo = Pessoa.cria_anonimo()
    print(anonimo)

        