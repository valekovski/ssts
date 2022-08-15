-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Gostitelj: 127.0.0.1
-- Čas nastanka: 24. jun 2022 ob 14.12
-- Različica strežnika: 10.4.22-MariaDB
-- Različica PHP: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Zbirka podatkov: `todo`
--

-- --------------------------------------------------------

--
-- Struktura tabele `opravila`
--

CREATE TABLE `opravila` (
  `id` int(11) NOT NULL,
  `opis` varchar(250) NOT NULL,
  `opravljeno` int(1) NOT NULL DEFAULT 0,
  `userID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Odloži podatke za tabelo `opravila`
--

INSERT INTO `opravila` (`id`, `opis`, `opravljeno`, `userID`) VALUES
(1, 'uči se za popravni izpit', 0, 1),
(2, 'telovadi vsaj 30 min', 0, 1),
(3, 'uči se za popravni izpit', 0, 2),
(4, 'telovadi vsaj 30 min', 0, 2),
(5, 'uči se za popravni izpit', 1, 3),
(6, 'telovadi vsaj 30 min', 0, 3),
(7, 'uči se za popravni izpit', 0, 4),
(8, 'telovadi vsaj 30 min', 0, 4),
(9, 'uči se za popravni izpit', 0, 5),
(10, 'telovadi vsaj 30 min', 0, 5),
(11, 'uči se za popravni izpit', 0, 6),
(12, 'telovadi vsaj 30 min', 0, 6),
(13, 'uči se za popravni izpit', 0, 7),
(14, 'telovadi vsaj 30 min', 0, 7),
(15, 'uči se za popravni izpit', 0, 8),
(16, 'telovadi vsaj 30 min', 0, 8),
(17, 'uči se za popravni izpit', 0, 9),
(18, 'telovadi vsaj 30 min', 0, 9),
(19, 'uči se za popravni izpit', 0, 10),
(20, 'telovadi vsaj 30 min', 0, 10),
(21, 'uči se za popravni izpit', 0, 11),
(22, 'telovadi vsaj 30 min', 0, 11),
(23, 'uči se za popravni izpit', 0, 12),
(24, 'telovadi vsaj 30 min', 0, 12),
(25, 'uči se za popravni izpit', 0, 13),
(26, 'telovadi vsaj 30 min', 0, 13),
(27, 'uči se za popravni izpit', 0, 14),
(28, 'telovadi vsaj 30 min', 0, 14),
(29, 'uči se za popravni izpit', 0, 15),
(30, 'telovadi vsaj 30 min', 0, 15),
(31, 'uči se za popravni izpit', 0, 16),
(32, 'telovadi vsaj 30 min', 0, 16),
(33, 'uči se za popravni izpit', 0, 17),
(34, 'telovadi vsaj 30 min', 0, 17),
(35, 'uči se za popravni izpit', 0, 18),
(36, 'telovadi vsaj 30 min', 0, 18),
(37, 'uči se za popravni izpit', 0, 19),
(38, 'telovadi vsaj 30 min', 0, 19),
(39, 'uči se za popravni izpit', 0, 20),
(40, 'telovadi vsaj 30 min', 0, 20),
(41, 'uči se za popravni izpit', 0, 21),
(42, 'telovadi vsaj 30 min', 0, 21),
(43, 'uči se za popravni izpit', 0, 22),
(44, 'telovadi vsaj 30 min', 0, 22),
(45, 'uči se za popravni izpit', 0, 23),
(46, 'telovadi vsaj 30 min', 0, 23),
(47, 'uči se za popravni izpit', 0, 24),
(48, 'telovadi vsaj 30 min', 0, 24),
(49, 'uči se za popravni izpit', 0, 25),
(50, 'telovadi vsaj 30 min', 0, 25),
(51, 'uči se za popravni izpit', 0, 26),
(52, 'telovadi vsaj 30 min', 0, 26),
(53, 'uči se za popravni izpit', 0, 27),
(54, 'telovadi vsaj 30 min', 0, 27),
(55, 'uči se za popravni izpit', 0, 28),
(56, 'telovadi vsaj 30 min', 0, 28),
(57, 'uči se za popravni izpit', 0, 29),
(58, 'telovadi vsaj 30 min', 0, 29),
(59, 'uči se za popravni izpit', 0, 30),
(60, 'telovadi vsaj 30 min', 0, 30),
(61, 'uči se za popravni izpit', 0, 31),
(62, 'telovadi vsaj 30 min', 0, 31),
(63, 'uči se za popravni izpit', 0, 32),
(64, 'telovadi vsaj 30 min', 0, 32),
(65, 'uči se za popravni izpit', 0, 33),
(66, 'telovadi vsaj 30 min', 0, 33);

-- --------------------------------------------------------

--
-- Struktura tabele `uporabniki`
--

CREATE TABLE `uporabniki` (
  `id` int(11) NOT NULL,
  `username` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Odloži podatke za tabelo `uporabniki`
--

INSERT INTO `uporabniki` (`id`, `username`) VALUES
(1, 'Bosancic'),
(2, 'causevic'),
(3, 'coha'),
(4, 'Drinic'),
(5, 'Drolec'),
(6, 'Fehric'),
(7, 'Gashi'),
(8, 'Gjorgev'),
(9, 'Habbe'),
(10, 'Hafizovic'),
(11, 'Halozan'),
(12, 'Kikelj'),
(13, 'Kuruzar'),
(14, 'Lukman'),
(15, 'Murgoski'),
(16, 'Resanovic'),
(17, 'Pestotnik'),
(18, 'Poznic'),
(19, 'Protic'),
(20, 'Ramic'),
(21, 'Ravnik'),
(22, 'Rihar'),
(23, 'Rozina'),
(24, 'salamon'),
(25, 'soban'),
(26, 'stuhec'),
(27, 'Tabakovic'),
(28, 'Truden'),
(29, 'Virant'),
(30, 'Zabukovec'),
(31, 'Zeggai'),
(32, 'zeleznik'),
(33, 'zinko');

--
-- Indeksi zavrženih tabel
--

--
-- Indeksi tabele `opravila`
--
ALTER TABLE `opravila`
  ADD PRIMARY KEY (`id`);

--
-- Indeksi tabele `uporabniki`
--
ALTER TABLE `uporabniki`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT zavrženih tabel
--

--
-- AUTO_INCREMENT tabele `opravila`
--
ALTER TABLE `opravila`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT tabele `uporabniki`
--
ALTER TABLE `uporabniki`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
