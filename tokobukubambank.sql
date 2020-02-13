-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 13 Feb 2020 pada 20.40
-- Versi server: 10.1.38-MariaDB
-- Versi PHP: 7.3.2

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
-- Struktur dari tabel `bukudetail`
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
-- Dumping data untuk tabel `bukudetail`
--

INSERT INTO `bukudetail` (`id`, `title`, `author`, `date_published`, `pages`, `type`) VALUES
(1, 'Death Note', 'Ryuk', '2000-02-04', 300, 'Cursed'),
(2, 'Life note', 'Shiryu', '2000-02-04', 300, 'blessed'),
(3, 'Kiss Note', 'Guri', '2000-02-04', 300, 'Unknown');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `bukudetail`
--
ALTER TABLE `bukudetail`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `bukudetail`
--
ALTER TABLE `bukudetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
