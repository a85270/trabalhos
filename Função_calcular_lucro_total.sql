CREATE FUNCTION CalcularLucro(dataInicio DATE,dataFim DATE,categoriaLivro VARCHAR(50),codLivro INT,codLoja INT) RETURNS decimal(10,2)
BEGIN
    DECLARE lucroTotal DECIMAL(10, 2);
SELECT 
SUM((EncomendasCliente.Quantidade * Livro.ValorUnitarioVenda * (1 - Livro.Desconto / 100) - Livro.ValorUnitarioFornecedor) * (1 + Livro.IVA / 100)) 
INTO lucroTotal
FROM EncomendasCliente
    JOIN Livro ON EncomendasCliente.CodlivroID = Livro.CodLivroID
    JOIN Lojas ON EncomendasCliente.CodlojaID = Lojas.CodLojaID
    WHERE 
        EncomendasCliente.Data_ BETWEEN dataInicio AND dataFim
        AND (categoriaLivro IS NULL OR Livro.Categoria = categoriaLivro)
        AND (codLivro IS NULL OR Livro.CodLivroID = codLivro)
        AND (codLoja IS NULL OR Lojas.CodLojaID = codLoja);

    RETURN lucroTotal;
END