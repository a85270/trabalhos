-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 26-Maio-2024 às 02:46
-- Versão do servidor: 10.4.32-MariaDB
-- versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `banca`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `frutas`
--

CREATE TABLE `frutas` (
  `idfrutas` int(11) NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `arvore` varchar(255) DEFAULT NULL,
  `epoca` varchar(255) DEFAULT NULL,
  `validade` date DEFAULT NULL,
  `foto` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `frutas`
--

INSERT INTO `frutas` (`idfrutas`, `nome`, `arvore`, `epoca`, `validade`, `foto`) VALUES
(6, 'maçã', 'macieira', 'verao', '2000-01-01', 0x53706f7274696e675f436c7562655f64655f506f72747567616c2e706e67);

-- --------------------------------------------------------

--
-- Estrutura da tabela `users`
--

CREATE TABLE `users` (
  `idusers` int(11) NOT NULL,
  `username` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `users`
--

INSERT INTO `users` (`idusers`, `username`, `email`, `age`, `password`) VALUES
(1, 'joao', 'joao@ualg.pt', 15, '123456'),
(3, 'alex', 'alex', 19, '9');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `frutas`
--
ALTER TABLE `frutas`
  ADD PRIMARY KEY (`idfrutas`);

--
-- Índices para tabela `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`idusers`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `frutas`
--
ALTER TABLE `frutas`
  MODIFY `idfrutas` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de tabela `users`
--
ALTER TABLE `users`
  MODIFY `idusers` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
