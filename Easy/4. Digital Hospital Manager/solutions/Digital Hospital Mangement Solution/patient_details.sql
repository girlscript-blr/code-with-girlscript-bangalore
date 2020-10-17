-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 17, 2020 at 12:29 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `my_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `patient_details`
--

CREATE TABLE `patient_details` (
  `Patient ID` int(11) NOT NULL,
  `Full Name` varchar(20) NOT NULL,
  `Phone Number` int(10) NOT NULL,
  `Emergency Contact Number` int(10) NOT NULL,
  `Age` int(11) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `Blood Type` varchar(5) NOT NULL,
  `Weight` int(11) NOT NULL,
  `Height` int(11) NOT NULL,
  `Symptoms` varchar(100) NOT NULL,
  `Date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient_details`
--

INSERT INTO `patient_details` (`Patient ID`, `Full Name`, `Phone Number`, `Emergency Contact Number`, `Age`, `Gender`, `Blood Type`, `Weight`, `Height`, `Symptoms`, `Date`) VALUES
(1, 'kkkkkkk', 1234567898, 1234567897, 12, 'ssss', 'dddd', 12, 34, 'eeee', '0000-00-00 00:00:00'),
(2, 'ddddd', 1234567897, 1234567897, 23, 'dfgg', 'dfff', 34, 45, 'ffff', '2020-10-16 20:28:42'),
(3, 'pallavi savant', 2147483647, 1234567897, 0, 'dfgh', 'ert', 12, 345, 'ddddd', '2020-10-16 20:32:32'),
(4, 'pallavi savant', 2147483647, 1234567897, 0, 'dfgh', 'ert', 12, 345, 'ddddd', '2020-10-16 20:32:43'),
(5, 'pallavi savant', 2147483647, 1234567897, 0, 'dfgh', 'ert', 12, 345, 'ddddd', '2020-10-16 20:33:10'),
(6, 'pallavi savant', 2147483647, 1234567897, 0, 'dfgh', 'ert', 12, 345, 'ddddd', '2020-10-16 20:33:35'),
(7, 'pallavi savant', 2147483647, 1234567897, 0, 'dfgh', 'ert', 12, 345, 'ddddd', '2020-10-16 20:37:02'),
(8, 'pallavi savant', 2147483647, 1234567897, 0, 'dfgh', 'ert', 12, 345, 'ddddd', '2020-10-16 20:45:16'),
(9, 'pallavi savant', 2147483647, 1234567897, 0, 'dfgh', 'ert', 12, 345, 'ddddd', '2020-10-16 20:46:20'),
(10, 'pallavi savant', 2147483647, 1234567897, 0, 'dfgh', 'ert', 12, 345, 'ddddd', '2020-10-16 20:48:39'),
(11, 'pallavi savant', 2147483647, 1234567897, 0, 'dfgh', 'ert', 12, 345, 'ddddd', '2020-10-16 20:51:05'),
(12, 'pallavi savant', 2147483647, 1234567897, 0, 'dfgh', 'ert', 12, 345, 'ddddd', '2020-10-16 20:54:01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `patient_details`
--
ALTER TABLE `patient_details`
  ADD PRIMARY KEY (`Patient ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `patient_details`
--
ALTER TABLE `patient_details`
  MODIFY `Patient ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
