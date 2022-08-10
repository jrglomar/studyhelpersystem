-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 10, 2022 at 09:03 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `studyhelpersystem`
--

-- --------------------------------------------------------

--
-- Table structure for table `academicactivity`
--

CREATE TABLE `academicactivity` (
  `AcademicActivityID` int(11) NOT NULL,
  `SubjectID` int(11) DEFAULT NULL,
  `GradingSystemID` int(11) DEFAULT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `Score` float DEFAULT NULL,
  `Max_Score` float DEFAULT NULL,
  `Result` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `academicactivity`
--

INSERT INTO `academicactivity` (`AcademicActivityID`, `SubjectID`, `GradingSystemID`, `Title`, `Score`, `Max_Score`, `Result`) VALUES
(3, 7, 9, 'Assignment 1', 95, 100, 95),
(4, 7, 14, 'Exam 1', 85, 100, 85),
(5, 8, 20, 'Exam 1', 95, 100, 95),
(6, 9, 25, 'Project 1', 78, 100, 78);

-- --------------------------------------------------------

--
-- Table structure for table `gradingsystem`
--

CREATE TABLE `gradingsystem` (
  `GradingSystemID` int(11) NOT NULL,
  `Type` varchar(255) DEFAULT NULL,
  `Percentage` float DEFAULT NULL,
  `SubjectID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gradingsystem`
--

INSERT INTO `gradingsystem` (`GradingSystemID`, `Type`, `Percentage`, `SubjectID`) VALUES
(9, 'Assignment', 10, 7),
(10, 'Attendance', 10, 7),
(11, 'Recitation', 10, 7),
(12, 'Quiz', 20, 7),
(13, 'Project', 25, 7),
(14, 'Exam', 25, 7),
(15, 'Assignment', 10, 8),
(16, 'Attendance', 10, 8),
(17, 'Recitation', 10, 8),
(18, 'Quiz', 20, 8),
(19, 'Project', 25, 8),
(20, 'Exam', 25, 8),
(21, 'Assignment', 10, 9),
(22, 'Attendance', 10, 9),
(23, 'Recitation', 10, 9),
(24, 'Quiz', 20, 9),
(25, 'Project', 25, 9),
(26, 'Exam', 25, 9);

-- --------------------------------------------------------

--
-- Table structure for table `reminder`
--

CREATE TABLE `reminder` (
  `ReminderID` int(11) NOT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `Due_Date` varchar(255) DEFAULT NULL,
  `Details` varchar(500) DEFAULT NULL,
  `StudentID` int(11) DEFAULT NULL,
  `ReminderTypeID` int(11) DEFAULT NULL,
  `Subject` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reminder`
--

INSERT INTO `reminder` (`ReminderID`, `Title`, `Due_Date`, `Details`, `StudentID`, `ReminderTypeID`, `Subject`) VALUES
(4, 'Test Assignment 1', '2022-08-11', '\n', 3, 3, 'Programming');

-- --------------------------------------------------------

--
-- Table structure for table `remindertype`
--

CREATE TABLE `remindertype` (
  `ReminderTypeID` int(11) NOT NULL,
  `Description` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `remindertype`
--

INSERT INTO `remindertype` (`ReminderTypeID`, `Description`) VALUES
(3, 'Assignment'),
(4, 'Project');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `StudentID` int(11) NOT NULL,
  `Username` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`StudentID`, `Username`, `Password`, `Email`) VALUES
(3, 'jrglomar', 'User01', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `SubjectID` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Start_Time` varchar(255) DEFAULT NULL,
  `End_Time` varchar(255) DEFAULT NULL,
  `Day_Schedule` varchar(500) DEFAULT NULL,
  `Description` varchar(255) DEFAULT NULL,
  `StudentID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`SubjectID`, `Name`, `Start_Time`, `End_Time`, `Day_Schedule`, `Description`, `StudentID`) VALUES
(7, 'Programming', '12:00:00', '15:00:00', 'Tuesday', 'Room: 104-A\nProf: Ma\'am Gatchalian\n', 3),
(8, 'Database Administration', '15:00:00', '18:00:00', 'Monday', 'Room: 103-B\nProf: Ma\'am Cherry Doromal\n', 3),
(9, 'Discrete Math', '10:00:00', '13:00:00', 'Wednesday', 'Room: 102-C\nProf: Ma\'am Alma Fernandez\n', 3);

-- --------------------------------------------------------

--
-- Table structure for table `subject_grade`
--

CREATE TABLE `subject_grade` (
  `SubjectGradeID` int(11) NOT NULL,
  `Final_Grade` float DEFAULT NULL,
  `SubjectID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject_grade`
--

INSERT INTO `subject_grade` (`SubjectGradeID`, `Final_Grade`, `SubjectID`) VALUES
(2, 95.75, 7),
(3, 98.75, 8),
(4, 94.5, 9);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `academicactivity`
--
ALTER TABLE `academicactivity`
  ADD PRIMARY KEY (`AcademicActivityID`),
  ADD KEY `SubjectID` (`SubjectID`),
  ADD KEY `GradingSystemID` (`GradingSystemID`);

--
-- Indexes for table `gradingsystem`
--
ALTER TABLE `gradingsystem`
  ADD PRIMARY KEY (`GradingSystemID`),
  ADD KEY `SubjectID` (`SubjectID`);

--
-- Indexes for table `reminder`
--
ALTER TABLE `reminder`
  ADD PRIMARY KEY (`ReminderID`),
  ADD KEY `StudentID` (`StudentID`),
  ADD KEY `ReminderTypeID` (`ReminderTypeID`);

--
-- Indexes for table `remindertype`
--
ALTER TABLE `remindertype`
  ADD PRIMARY KEY (`ReminderTypeID`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`StudentID`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`SubjectID`),
  ADD KEY `StudentID` (`StudentID`);

--
-- Indexes for table `subject_grade`
--
ALTER TABLE `subject_grade`
  ADD PRIMARY KEY (`SubjectGradeID`),
  ADD KEY `SubjectID` (`SubjectID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `academicactivity`
--
ALTER TABLE `academicactivity`
  MODIFY `AcademicActivityID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `gradingsystem`
--
ALTER TABLE `gradingsystem`
  MODIFY `GradingSystemID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `reminder`
--
ALTER TABLE `reminder`
  MODIFY `ReminderID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `remindertype`
--
ALTER TABLE `remindertype`
  MODIFY `ReminderTypeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `StudentID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `subject`
--
ALTER TABLE `subject`
  MODIFY `SubjectID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `subject_grade`
--
ALTER TABLE `subject_grade`
  MODIFY `SubjectGradeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `academicactivity`
--
ALTER TABLE `academicactivity`
  ADD CONSTRAINT `academicactivity_ibfk_1` FOREIGN KEY (`SubjectID`) REFERENCES `subject` (`SubjectID`),
  ADD CONSTRAINT `academicactivity_ibfk_2` FOREIGN KEY (`GradingSystemID`) REFERENCES `gradingsystem` (`GradingSystemID`);

--
-- Constraints for table `gradingsystem`
--
ALTER TABLE `gradingsystem`
  ADD CONSTRAINT `gradingsystem_ibfk_1` FOREIGN KEY (`SubjectID`) REFERENCES `subject` (`SubjectID`);

--
-- Constraints for table `reminder`
--
ALTER TABLE `reminder`
  ADD CONSTRAINT `reminder_ibfk_1` FOREIGN KEY (`StudentID`) REFERENCES `students` (`StudentID`),
  ADD CONSTRAINT `reminder_ibfk_2` FOREIGN KEY (`ReminderTypeID`) REFERENCES `remindertype` (`ReminderTypeID`);

--
-- Constraints for table `subject`
--
ALTER TABLE `subject`
  ADD CONSTRAINT `subject_ibfk_1` FOREIGN KEY (`StudentID`) REFERENCES `students` (`StudentID`);

--
-- Constraints for table `subject_grade`
--
ALTER TABLE `subject_grade`
  ADD CONSTRAINT `subject_grade_ibfk_1` FOREIGN KEY (`SubjectID`) REFERENCES `subject` (`SubjectID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
