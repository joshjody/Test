-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 17, 2020 at 01:59 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.0.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tokobukubambank`
--

-- --------------------------------------------------------

--
-- Table structure for table `bukudetail`
--

CREATE TABLE `bukudetail` (
  `id` int(11) NOT NULL,
  `title` varchar(600) NOT NULL,
  `author` varchar(300) NOT NULL,
  `date_published` date NOT NULL,
  `pages` int(11) NOT NULL,
  `type` varchar(360) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bukudetail`
--

INSERT INTO `bukudetail` (`id`, `title`, `author`, `date_published`, `pages`, `type`) VALUES
(3, 'Kiss Note', 'Guri', '2000-02-04', 300, 'Unknown'),
(4, 'udin books', 'udin', '2002-02-03', 30, 'diary book'),
(8, 'Death Note', 'Ryuk', '2002-01-01', 300, 'Cursed');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bukudetail`
--
ALTER TABLE `bukudetail`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bukudetail`
--
ALTER TABLE `bukudetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
