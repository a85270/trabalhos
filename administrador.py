from empregado import Empregado

class Administrador(Empregado):
    def __init__(self, nome, endereco, phoneNumber, codigo_setor,salario_base,imposto,ajuda_de_custo):
        super().__init__(nome, endereco, phoneNumber,codigo_setor,salario_base,imposto)
        self.ajuda_de_custo = ajuda_de_custo

    def calcular_salario(self):
        salario_administrador = self.ajuda_de_custo + super().calcular_salario()
        return salario_administrador

    def __repr__(self):
        return f"O Aministrador é {self.nome}. A sua morada é: {self.endereco}. O seu contacto telefónico é {self.phoneNumber}. O código de setor é {self.codigo_setor}, e o seu salário é de {self.calcular_salario()} €"

if __name__ == "__main__":
   
    Joao = Administrador("João Abreu","Urb. Principal, lote 1",910907960,10,5000,20,250)
    print(Joao)