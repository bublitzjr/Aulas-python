-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 19-Abr-2021 às 21:39
-- Versão do servidor: 10.4.17-MariaDB
-- versão do PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `hoteis`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `cidades`
--

CREATE TABLE `cidades` (
  `id_cidade` int(11) NOT NULL,
  `nome_cidade` varchar(100) NOT NULL,
  `regiao` varchar(100) DEFAULT NULL,
  `fkEstado` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `cidades`
--

INSERT INTO `cidades` (`id_cidade`, `nome_cidade`, `regiao`, `fkEstado`) VALUES
(1, 'Blumenau', 'Nordeste', 1),
(2, 'Rio Branco', 'Centro', 2),
(3, 'Gaspar', 'Nordeste', 1),
(4, 'Chapeco', 'Noroeste', 1),
(5, 'Criciuma', 'Sudeste', 1),
(6, 'Cruzeiro do Sul', 'Noroeste', 2),
(7, 'Curitiba', 'Central', 3),
(8, 'Porto Alegre', 'Sudoeste', 4),
(9, 'João Pessoa', 'Sudeste', 5);

-- --------------------------------------------------------

--
-- Estrutura da tabela `estados`
--

CREATE TABLE `estados` (
  `id_estado` int(11) NOT NULL,
  `nome_estado` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `estados`
--

INSERT INTO `estados` (`id_estado`, `nome_estado`) VALUES
(1, 'Santa Catarina'),
(2, 'Acre'),
(3, 'Parana'),
(4, 'Rio grande do sul'),
(5, 'Paraiba');

-- --------------------------------------------------------

--
-- Estrutura da tabela `hoteis`
--

CREATE TABLE `hoteis` (
  `id_hotel` int(11) NOT NULL,
  `nome_hotel` varchar(100) NOT NULL,
  `classificacao` int(11) NOT NULL,
  `preco_diaria` float NOT NULL,
  `academia` tinyint(1) NOT NULL,
  `pisicina` tinyint(1) NOT NULL,
  `refeicoes` tinyint(1) NOT NULL,
  `vagas` int(11) NOT NULL,
  `fkCidade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `hoteis`
--

INSERT INTO `hoteis` (`id_hotel`, `nome_hotel`, `classificacao`, `preco_diaria`, `academia`, `pisicina`, `refeicoes`, `vagas`, `fkCidade`) VALUES
(1, 'IBIS', 3, 160, 0, 1, 1, 3, 1),
(2, 'Nobile', 5, 250, 1, 1, 1, 1, 2),
(3, 'Gloria', 2, 50, 1, 0, 0, 2, 1),
(4, 'Hotel Fazenda', 5, 1200, 1, 1, 1, 20, 3),
(5, 'Plaza', 4, 500, 0, 1, 0, 15, 1),
(6, 'HimmelBlau', 5, 2000, 1, 1, 1, 9, 1),
(7, 'Bila do Vale', 1, 45, 0, 0, 0, 30, 1),
(8, 'Sesc', 3, 100, 1, 1, 1, 15, 1),
(9, 'Hotel 10', 5, 10, 0, 1, 0, 10, 1),
(10, 'Hostel Rota do vale', 2, 80, 0, 0, 0, 5, 1),
(11, 'Resort Ecoar', 3, 120, 0, 1, 1, 4, 3),
(12, 'Cascaneia', 4, 490, 0, 1, 1, 12, 3),
(13, 'Steinhausen', 3, 374.89, 0, 0, 1, 45, 3),
(14, 'Rio da Prata', 3, 280.9, 0, 1, 1, 22, 3),
(15, 'Arraial do Ouro', 4, 473.2, 0, 1, 1, 10, 3);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `cidades`
--
ALTER TABLE `cidades`
  ADD PRIMARY KEY (`id_cidade`),
  ADD KEY `cidades_FK` (`fkEstado`);

--
-- Índices para tabela `estados`
--
ALTER TABLE `estados`
  ADD PRIMARY KEY (`id_estado`);

--
-- Índices para tabela `hoteis`
--
ALTER TABLE `hoteis`
  ADD PRIMARY KEY (`id_hotel`),
  ADD KEY `hoteis_FK` (`fkCidade`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cidades`
--
ALTER TABLE `cidades`
  MODIFY `id_cidade` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de tabela `estados`
--
ALTER TABLE `estados`
  MODIFY `id_estado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `hoteis`
--
ALTER TABLE `hoteis`
  MODIFY `id_hotel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `cidades`
--
ALTER TABLE `cidades`
  ADD CONSTRAINT `cidades_FK` FOREIGN KEY (`fkEstado`) REFERENCES `estados` (`id_estado`);

--
-- Limitadores para a tabela `hoteis`
--
ALTER TABLE `hoteis`
  ADD CONSTRAINT `hoteis_FK` FOREIGN KEY (`fkCidade`) REFERENCES `cidades` (`id_cidade`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
