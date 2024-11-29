
from empregado import Empregado

class Operario(Empregado):
    def __init__(self, nome, endereco, phoneNumber, codigo_setor,salario_base,imposto,valor_producao,comissao):
        super().__init__(nome, endereco, phoneNumber,codigo_setor,salario_base,imposto)
        self.valor_producao = valor_producao
        self.comissao = comissao

    def __repr__(self):
        return f"O operário é {self.nome}. A sua morada é: {self.endereco}. O contacto telefónico é: {self.phoneNumber}. O seu código de setor é: {self.codigo_setor}. Tem de salário : {self.calcular_produtividade()} €"

    def calcular_salario_operario(self):
        salario_operario =self.calcular_salario() + self.comissao
        return salario_operario

    def calcular_produtividade(self):
        calcular_produtividade = self.calcular_salario() - self.valor_producao
        return calcular_produtividade

   

if __name__ == "__main__":
    
    andre = Operario("André Filipe","Quinta das Oliveiras, lote 16",918989098,3,2000,20,145,250)
    print(andre)
