-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 10, 2015 at 03:20 AM
-- Server version: 5.5.43-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `teach_me`
--

-- --------------------------------------------------------

--
-- Table structure for table `answered_questions`
--

CREATE TABLE IF NOT EXISTS `answered_questions` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) NOT NULL,
  `course_id` int(10) NOT NULL,
  `question_id` int(10) NOT NULL,
  `answer_id` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE IF NOT EXISTS `answers` (
  `answer_id` int(10) NOT NULL AUTO_INCREMENT,
  `question_id` int(10) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `correct` tinyint(4) NOT NULL,
  PRIMARY KEY (`answer_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`answer_id`, `question_id`, `answer`, `correct`) VALUES
(1, 1, 'y', 0),
(2, 1, 'n', 1),
(3, 2, 'yy', 1),
(4, 2, 'nn', 0),
(5, 3, 'y', 0),
(6, 3, 'n', 1),
(7, 4, 'yy', 1),
(8, 4, 'nn', 0),
(9, 5, 'n', 1),
(10, 5, 'b', 0),
(11, 6, 'nn', 0),
(12, 6, 'bb', 1);

-- --------------------------------------------------------

--
-- Table structure for table `completed_courses`
--

CREATE TABLE IF NOT EXISTS `completed_courses` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) NOT NULL,
  `course_id` int(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE IF NOT EXISTS `courses` (
  `course_id` int(10) NOT NULL AUTO_INCREMENT,
  `author_id` int(10) NOT NULL,
  `title` varchar(100) NOT NULL,
  `type` varchar(30) NOT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`course_id`, `author_id`, `title`, `type`, `date`) VALUES
(1, 7, 'Prime numbers', 'Math', '2015-07-10 00:45:28'),
(2, 7, 'Triangles', 'Math', '2015-07-10 00:47:37');

-- --------------------------------------------------------

--
-- Table structure for table `courses_taken`
--

CREATE TABLE IF NOT EXISTS `courses_taken` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) NOT NULL,
  `course_id` int(10) NOT NULL,
  `date_log` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `courses_taken`
--

INSERT INTO `courses_taken` (`id`, `user_id`, `course_id`, `date_log`) VALUES
(1, 7, 2, '2015-07-10 03:09:50'),
(2, 7, 2, '2015-07-10 03:09:57');

-- --------------------------------------------------------

--
-- Table structure for table `course_types`
--

CREATE TABLE IF NOT EXISTS `course_types` (
  `type_id` int(10) NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `course_types`
--

INSERT INTO `course_types` (`type_id`, `type`) VALUES
(1, 'Mathemathics'),
(2, 'History'),
(3, 'Geography'),
(4, 'Biology'),
(5, 'Literature');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE IF NOT EXISTS `questions` (
  `question_id` int(10) NOT NULL AUTO_INCREMENT,
  `course_id` int(10) NOT NULL,
  `question` varchar(100) NOT NULL,
  PRIMARY KEY (`question_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`question_id`, `course_id`, `question`) VALUES
(1, 1, 'q'),
(2, 1, 'qq'),
(3, 1, 'q'),
(4, 1, 'qq'),
(5, 2, 'm'),
(6, 2, 'mm');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(10) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `role`) VALUES
(6, 'Morrghana', '1234', 'marina.uzunova3@gmail.com', 'admin'),
(7, 'bebidi', '1234', 'bebidi@sladko.com', 'student'),
(8, 'bebi', 'zxc', 'bebi@a.com', '');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
