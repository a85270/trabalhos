CREATE PROCEDURE AtualizarIVA(IN novoIVA DECIMAL(5,2))
BEGIN
    UPDATE Livro
    SET IVA = novoIVA;
    SELECT 'O IVA foi atualizado para ', novoIVA AS 'Novo IVA';
END