from person import Pessoa

class Empregado(Pessoa):
    def __init__(self, nome, endereco, phoneNumber, codigo_setor,salario_base,imposto):
        super().__init__(nome, endereco, phoneNumber)
        self.codigo_setor = codigo_setor
        self.salario_base = salario_base
        self.imposto = imposto

    def calcular_salario(self):
        salario_liquido = self.salario_base *(100-self.imposto) /100
        return salario_liquido

    def __repr__(self):
        return f"O empregado é: {self.nome}, mora na rua {self.endereco}, e tem como contcto telefónico {self.phoneNumber}.O seu cógigo de setor é: {self.codigo_setor}, e o seu salário liquido é de {self.calcular_salario()} €"


if __name__ == "__main__":
    
    Antonio = Empregado("Antonio", "Rua dos empregados, nº3", 913245678, 1, 1200, 20)
    print(Antonio)