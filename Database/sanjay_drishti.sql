-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 27, 2020 at 04:01 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sanjay_drishti`
--

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `course_code` varchar(15) NOT NULL,
  `course_name` varchar(15) NOT NULL,
  `faculty_handling` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `faculties`
--

CREATE TABLE `faculties` (
  `emp_id` int(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `contact` int(10) NOT NULL,
  `school` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `faculties`
--

INSERT INTO `faculties` (`emp_id`, `name`, `email`, `contact`, `school`) VALUES
(50784, 'Dr Jeganathan L', 'jeganathanl@vitfac.ac.in', 6359, 'SCOPE');

-- --------------------------------------------------------

--
-- Table structure for table `faculty_reg_courses`
--

CREATE TABLE `faculty_reg_courses` (
  `emp_id` int(6) NOT NULL,
  `course_1` varchar(10) NOT NULL,
  `course_2` varchar(10) NOT NULL,
  `course_3` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `faculty_reg_courses`
--

INSERT INTO `faculty_reg_courses` (`emp_id`, `course_1`, `course_2`, `course_3`) VALUES
(50784, 'cse3002', 'cse1001', 'cse2004');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `reg_no` varchar(9) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `contact_no` varchar(10) NOT NULL,
  `college` varchar(15) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`reg_no`, `name`, `email`, `contact_no`, `college`, `password`) VALUES
('18BCE1020', 'Chandan Kumar', 'thechandankumar18@gmail.com', '9521790908', 'VIT Chennai', 'alphaboi'),
('18BCE1352', 'Pratik', 'pratik@gamil.com', '987456324', 'VIT Chennai', 'alpha');

-- --------------------------------------------------------

--
-- Table structure for table `stud_reg_courses`
--

CREATE TABLE `stud_reg_courses` (
  `reg_no` varchar(9) NOT NULL,
  `course_1` varchar(8) NOT NULL,
  `course_2` varchar(8) NOT NULL,
  `course_3` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stud_reg_courses`
--

INSERT INTO `stud_reg_courses` (`reg_no`, `course_1`, `course_2`, `course_3`) VALUES
('18BCE1352', 'cse2001', 'cse1001', 'cse2002');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`course_code`);

--
-- Indexes for table `faculties`
--
ALTER TABLE `faculties`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `faculty_reg_courses`
--
ALTER TABLE `faculty_reg_courses`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`reg_no`);

--
-- Indexes for table `stud_reg_courses`
--
ALTER TABLE `stud_reg_courses`
  ADD PRIMARY KEY (`reg_no`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `faculty_reg_courses`
--
ALTER TABLE `faculty_reg_courses`
  ADD CONSTRAINT `faculty_reg_courses_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `faculties` (`emp_id`);

--
-- Constraints for table `stud_reg_courses`
--
ALTER TABLE `stud_reg_courses`
  ADD CONSTRAINT `stud_reg_courses_ibfk_1` FOREIGN KEY (`reg_no`) REFERENCES `students` (`reg_no`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
