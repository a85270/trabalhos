from person import Pessoa

class Fornecedor(Pessoa):
        def __init__(self,nome, endereco, phoneNumber,valor_credito,valor_divida):
            super().__init__(nome,endereco,phoneNumber)
            self.valor_credito = valor_credito
            self.valor_divida = valor_divida

        def obter_saldo(self):
            saldo_atual = self.valor_divida - self.valor_credito
            return saldo_atual

        def __repr__(self):
            return f"O fornecedor é:{self.nome}. Morada: {self.endereco}. Contacto telefónico: {self.phoneNumber}. Tem como saldo: {self.obter_saldo()} €"



if __name__ == "__main__":
    
    saldo = Fornecedor("Tintas 24","Av. Pintada",91919191,5000,6000)
    print(saldo)
