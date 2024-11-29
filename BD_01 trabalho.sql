DROP DATABASE IF EXISTS trabalhoSI;
CREATE DATABASE trabalhoSI;
USE trabalhoSI;
CREATE TABLE Cliente (

    NClienteID INT not null,
    Nome VARCHAR(255),
    Morada VARCHAR(255),
    CodigoPostal VARCHAR(8) not null,
    Localidade VARCHAR(20) not null,
    NIF varchar (9),
    Telefone int not null,
    Email VARCHAR(100) not null,
    
    PRIMARY KEY (NClienteID)
);

CREATE TABLE Lojas (
    CodLojaID  INT not null,
    Website varchar(50),
	LojaFisica INT not null,
    StockArmazém int not null,
	StockLoja int not null,
    NClienteID INT not null,
    PRIMARY KEY (CodLojaID),
    Constraint fk_NClienteID  foreign key ( NClienteID ) references Cliente( NClienteID ) on delete restrict on update cascade);


CREATE TABLE EncomendasEditora (

    NEncomendaEdit  INT not null,
    DataEncomenda datetime,
    Quantidadeencomenda INT not null,
    EstadoEncomenda VARCHAR(50) not null,
	CodLojaID int not null,
   
    PRIMARY KEY (NEncomendaEdit),
    Constraint fk_CodLojaID  foreign key ( CodLojaID ) references Lojas( CodLojaID ) on delete restrict on update cascade);


CREATE TABLE Editora (

    CodEditoraID INT not null,
    Designacao VARCHAR(255),
    Morada VARCHAR(255),
    CodigoPostal VARCHAR(8) not null,
    Localidade VARCHAR(20) not null,
    Pais VARCHAR(20) not null,
    Telefone int not null,
    Email VARCHAR(100) not null,
    NEncomendaEdit  INT not null,
    PRIMARY KEY (CodEditoraID),
    Constraint fk_NEncomendaEdit foreign key ( NEncomendaEdit) references EncomendasEditora( NEncomendaEdit) on delete restrict on update cascade
);

 CREATE TABLE Fatura(
    
    NFatura INT not null,
    InfCliente INT not null,
    Inftotalpagar decimal(10,2),
    Data_ date,
    PRIMARY KEY (NFatura)
);

CREATE TABLE EncomendasCliente  ( 
	NencomendaID INT NOT NULL ,
    Data_  DATE ,
    Quantidade INT NOT NULL,
    Entregue TINYINT(1) NOT NULL,
    Pago TINYINT(1) NOT NULL,
    Nfatura INT NOT NULL,
    NclienteID INT NOT NULL,
    CodlojaID INT NOT NULL ,
    
	PRIMARY KEY(NencomendaID),
    Constraint fk_Nfatura foreign key ( Nfatura) references Fatura( Nfatura) on delete restrict on update cascade,
    Constraint fk_NclienteID1 foreign key (NclienteID) references Cliente( NclienteID) on delete restrict on update cascade,
    Constraint fk_CodlojaID1 foreign key ( CodlojaID) references Lojas( CodlojaID) on delete restrict on update cascade
);

CREATE TABLE Livro (
    
    CodLivroID INT not null,
    NencomendaID int not null,
    Titulo VARCHAR(100) not null,
    BreveDescricao TEXT,
    Autores VARCHAR(150) not null,
    PaisPublicacao VARCHAR(100) not null,
    Idioma VARCHAR(50) not null,
    Categoria VARCHAR(50) not null,
    AnoPublicacao INT NOT NULL,
    CodEditoraID INT not null,
    ISBN VARCHAR(20),
    ValorUnitarioFornecedor DECIMAL(10, 2),
    ValorUnitarioVenda DECIMAL(10, 2),
    Estado varchar (20),
    Stock varchar(20),

    PRIMARY KEY (CodLivroID),
    Constraint fk_CodEditoraID foreign key (CodEditoraID) references Editora(CodEditoraID) on delete restrict on update cascade,
    Constraint fk_NencomendaID foreign key (NencomendaID) references EncomendasCliente(NencomendaID) on delete restrict on update cascade 
   );
CREATE TABLE CategoriaFuncionário(
    
    CodCategoria INT not null,
    Níveis Varchar(50),
    Designação varchar(250),
    
    PRIMARY KEY (CodCategoria));
    

    
CREATE TABLE FUNCIONARIO(

CodFuncionarioID INT NOT NULL ,
Nome           VARCHAR(40) NOT NULL,
Telefone       VARCHAR(14) NOT NULL,
Morada         VARCHAR(50) NOT NULL,
CodPostal      VARCHAR(8)  NOT NULL,
Localidade 	   VARCHAR(50) NOT NULL,
País 		   VARCHAR(50) NOT NULL,
Email		   VARCHAR(50) NOT NULL,
CodEscalao     INT NOT NULL ,
Salario 	   DECIMAL(10,2),
Designacao     VARCHAR(50) NOT NULL,
Data_ingresso  DATE NOT NULL,
CodCategoria   INT NOT NULL,
NEncomendaEdit  INT not null,
NencomendaID INT NOT NULL ,
PRIMARY KEY(CodFuncionarioID),
Constraint fk_CodCategoria foreign key (CodCategoria) references CategoriaFuncionário(CodCategoria) on delete restrict on update cascade,
Constraint fk_NEncomendaEdit1 foreign key (NEncomendaEdit) references EncomendasEditora(NEncomendaEdit) on delete restrict on update cascade,
Constraint fk_NencomendaID2 foreign key (NencomendaID) references EncomendasCliente(NencomendaID) on delete restrict on update cascade
);
    
    








CREATE TABLE encomendaproduto (

Nencomenda INT,
CodlivroID INT NOT NULL,
PreçounitarioH Decimal,
EncomendaProduto INT, 
Preçounitário Decimal(10,2),
IVAH INT,
NencomendaID INT NOT NULL ,
PRIMARY KEY (Nencomenda,CodlivroID),
Constraint fk_CodlivroID foreign key (CodlivroID) references Livro(CodlivroID) on delete restrict on update cascade,
Constraint fk_NencomendaID1 foreign key (NencomendaID) references EncomendasCliente(NencomendaID) on delete restrict on update cascade

);
CREATE TABLE historicocategoria (

CodFuncionarioID INT NOT NULL ,
CodCategoria INT not null,
Níveis VARCHAR(50),

PRIMARY KEY (CodFuncionarioID,CodCategoria),
Constraint fk_CodFuncionarioID foreign key (CodFuncionarioID) references FUNCIONARIO(CodFuncionarioID) on delete restrict on update cascade,
Constraint fk_CodCategoria1 foreign key (CodCategoria) references CategoriaFuncionário(CodCategoria) on delete restrict on update cascade

);
CREATE TABLE Vendas (

Quantidade INT NOT NULL,
Preçounitario Decimal,
IVA INT
);



INSERT INTO Fatura (NFatura,InfCliente,Inftotalpagar,Data_)
VALUES
(1, 12365, 15.00, '2022-08-15'),
(2, 23474, 22.00, '2022-09-20'),
(3, 14621, 09.00, '2022-06-17');

INSERT INTO Cliente (NClienteID, Nome, NIF, Morada, CodigoPostal, Localidade, Telefone, Email)
VALUES
('001', 'João Silva', '123456789', 'Rua do Cliente, 456', '4321-098', 'Cidade A', '987654321', 'joao@example.com'),
('002', 'Maria Santos', '987654321', 'Avenida do Cliente, 789', '9876-543', 'Cidade B', '123456789', 'maria@example.com'),
('003', 'Carlos Oliveira', '654321987', 'Praça do Cliente, 012', '1098-765', 'Cidade C', '456789012', 'carlos@example.com');

INSERT INTO Lojas(CodLojaID,Website,LojaFisica ,stockArmazém,StockLoja,NClienteID)
VALUES
( 1, 'loja1.pt', 02, 100, 25,'001'),
(2, 'loja2.pt', 03, 200,10,'002' ),
(3, 'loja3.pt', 04, 50,5, '003');

INSERT INTO EncomendasEditora (NEncomendaEdit,DataEncomenda,Quantidadeencomenda,EstadoEncomenda,CodLojaID)
VALUES
(001,'2023-11-13', 100,'Entregue',1),
(002,'2023-10-13', 180,'Não Entregue',1),
(003,'2023-09-20', 39,'Entregue',2);


INSERT INTO Editora (CodEditoraID, Designacao, Morada, CodigoPostal, Localidade, Pais, Telefone, Email,NEncomendaEdit)
VALUES
(1233, 'Editora A', 'Rua da Editora, 123', '2345678', 'Cidade A', 'Portugal', '123456789', 'info@editoraa.com',001),
(1234, 'Editora B', 'Avenida da Editora, 456', '6789012', 'Cidade B', 'Brasil', '987654321', 'info@editorab.com',002),
(1345, 'Editora C', 'Prédio da Editora, 789', '9123456', 'Cidade C', 'França', '321654987', 'info@editorac.com',003);


INSERT INTO CategoriaFuncionário (CodCategoria,Níveis, Designação )
VALUES
(001, 'Avançado','Administrador' ),
(100, 'Intermédio','Gestor de Marketing'),
(101, 'Intermédio','Gestor de Recursos Humanos');

INSERT INTO Vendas(Quantidade,Preçounitario,IVA)
VALUES
(5,15.99,5),
(2,24.99,5),
(10,30.99,5);






INSERT INTO EncomendasCliente  (NencomendaID, Data_ , Quantidade, Entregue, Pago, Nfatura,NclienteID,CodlojaID)
VALUES
(112365, '2022-08-15', '50', 2, 1, 1,'001',1),
(212365, '2022-09-20', '30', 1, 0,2,'002',2),
(34621,'2022-06-17', '20', 1, 1,3,'003',3);


INSERT INTO Livro (CodLivroID, NencomendaID, Titulo, BreveDescricao, Autores, PaisPublicacao, Idioma, Categoria, AnoPublicacao, CodEditoraID, ISBN, Estado, ValorUnitarioFornecedor, ValorUnitarioVenda,Stock)
VALUES
('001', 112365,'Aventuras de um Viajante', 'Histórias emocionantes...', 'João Silva', 'Portugal', 'Português',  'Aventura', '2022', 1233, '978-1234567890', 'Em Venda', 10.00, 15.00,'S'),
('002', 212365,'O Mistério do Castelo Assombrado', 'Suspense e mistério...', 'Maria Santos', 'Brasil', 'Português',  'Mistério','2021',1234, '978-9876543210', 'Esgotado', 12.50, 18.00,'N'),
('003',34621,'O Pequeno Príncipe', 'Uma história encantadora...', 'Antoine de Saint-Exupéry', 'França', 'Francês',  'Infantil', '2024', 1345, '978-4567890123', 'Indisponível', 8.00, 12.00,'S');


INSERT INTO encomendaproduto (Nencomenda,NencomendaID,CodlivroID,PreçounitarioH,EncomendaProduto,Preçounitário,IVAH)
VALUES
(010101,112365,'001',10, 5,9.99, 5 ),
(135631,212365,'002',20,3, 19.99,5),
(136723,34621,'003',12,4, 11.99,5);


INSERT INTO Funcionario (CodFuncionarioID, Nome, Morada, CodPostal, Localidade, País, Telefone,  Email, CodCategoria, Data_ingresso,Salario,NEncomendaEdit,NencomendaID,CodEscalao,Designacao)
VALUES
('001', 'Ana Silva', 'Rua do Colaborador, 123', 123900, 'Cidade A', 'Portugal', '987654321', 'ana@example.com', 001, '2022-01-10',3800.00, 001,112365,12,"Web designer"),
('002', 'Pedro Oliveira', 'Avenida do Colaborador, 456', 5678121, 'Cidade B', 'Brasil', '123456789', 'pedro@example.com', 100, '2021-03-15',2300.00, 002, 212365,11,"Programador"),
('003', 'Sofia Santos', 'Prédio do Colaborador, 789', 9012323, 'Cidade C', 'França', '456789012','sofia@example.com', 101, '2023-02-05',2000.00, 003, 34621,10, "Tecnico de Manutenção" );




-- Consultar o número de livros vendidos agrupados por mês e ano:

SELECT
    YEAR(EncomendasCliente.Data_) AS Ano,
    MONTH(EncomendasCliente.Data_) AS Mes,
    COUNT(*) AS NumeroLivrosVendidos
FROM
    EncomendasCliente
GROUP BY
    YEAR(EncomendasCliente.Data_),
    MONTH(EncomendasCliente.Data_);
    
    

    
