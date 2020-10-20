-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 19, 2020 at 09:09 PM
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
  `Severity` varchar(50) NOT NULL,
  `Medical Details/Comments` varchar(100) DEFAULT NULL,
  `Date Of Admission` timestamp NOT NULL DEFAULT current_timestamp(),
  `Date Of Discharge` date DEFAULT NULL,
  `Discharge Comments` varchar(100) DEFAULT NULL,
  `Date And Time Of Death` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient_details`
--

INSERT INTO `patient_details` (`Patient ID`, `Full Name`, `Phone Number`, `Emergency Contact Number`, `Age`, `Gender`, `Blood Type`, `Weight`, `Height`, `Symptoms`, `Severity`, `Medical Details/Comments`, `Date Of Admission`, `Date Of Discharge`, `Discharge Comments`, `Date And Time Of Death`) VALUES
(48, 'pallavi savant', 2147483647, 1234567897, 0, 'Male', 'A+', 12, 345, 'fever headache', 'Mild Mild Emergency Emergency Emergency Emergency ', 'Enter Comments Here.....', '2020-10-19 18:16:09', NULL, NULL, NULL);

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
  MODIFY `Patient ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
