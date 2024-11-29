CREATE FUNCTION CalcularValorTotalEncomenda(encomendaID INT) RETURNS decimal(10,2)
BEGIN
    DECLARE total DECIMAL(10,2);
    SELECT SUM((Quantidade * ValorUnitarioVenda * (1 - Desconto / 100)) * (1 + IVA / 100))
    INTO total
    FROM EncomendasCliente
    JOIN Livro ON EncomendasCliente.CodlivroID = Livro.CodLivroID
    WHERE EncomendasCliente.NencomendaID = encomendaID;
    RETURN total;
END