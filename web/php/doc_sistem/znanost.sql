-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 30, 2022 at 08:44 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `znanost`
--

-- --------------------------------------------------------

--
-- Table structure for table `citati`
--

CREATE TABLE `citati` (
  `ID` int(11) NOT NULL,
  `datoteka` varchar(50) NOT NULL,
  `znanstvenikID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `citati`
--

INSERT INTO `citati` (`ID`, `datoteka`, `znanstvenikID`) VALUES
(1, 'elements.txt', 1),
(2, 'fear.txt', 1),
(3, 'function_of_science.txt', 1),
(4, 'silence.txt', 1),
(5, 'work.txt', 1),
(6, 'imagination.txt', 2),
(7, 'knowledge.txt', 2),
(8, 'problems.txt', 2),
(9, 'talent.txt', 2),
(10, 'anwsers.txt', 5),
(11, 'physics.txt', 5),
(12, 'universe.txt', 5),
(13, 'appearance.txt', 6),
(14, 'giants.txt', 6),
(15, 'gravity.txt', 6),
(16, 'madness.txt', 6);

-- --------------------------------------------------------

--
-- Table structure for table `znanstveniki`
--

CREATE TABLE `znanstveniki` (
  `ID` int(11) NOT NULL,
  `ime` varchar(30) NOT NULL,
  `priimek` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `znanstveniki`
--

INSERT INTO `znanstveniki` (`ID`, `ime`, `priimek`) VALUES
(1, 'Dmitri', 'Mendeleev'),
(2, 'Albert', 'Einstein'),
(5, 'Edward', 'Witten'),
(6, 'Isaac', 'Newton');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `citati`
--
ALTER TABLE `citati`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `znanstveniki`
--
ALTER TABLE `znanstveniki`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `citati`
--
ALTER TABLE `citati`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `znanstveniki`
--
ALTER TABLE `znanstveniki`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
