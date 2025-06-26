-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 24, 2025 at 12:40 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `amazon`
--

-- --------------------------------------------------------

--
-- Table structure for table `ad`
--

CREATE TABLE `ad` (
  `id` int(15) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `mail` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ad`
--

INSERT INTO `ad` (`id`, `username`, `password`, `mail`) VALUES
(1, 'admin', 'admin@123', 'saranyaselvan13@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Id` int(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `fullname` varchar(20) NOT NULL,
  `location` varchar(30) NOT NULL,
  `image` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`Id`, `username`, `password`, `fullname`, `location`, `image`) VALUES
(1, 'Admin', 'Floris', 'praksh', 'Tirupur', 'successful-businessman.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `fname` varchar(11) NOT NULL,
  `mail` varchar(11) NOT NULL,
  `phno` int(11) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `state` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `image` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`fname`, `mail`, `phno`, `dob`, `gender`, `state`, `city`, `address`, `username`, `password`, `image`) VALUES
('saranya', 'saran@gmail', 2147483647, '2025-02-10', 'female', 'Tamilnadu', 'Tiruppur', 'Kunnathur, Tiruppur', 'saranya  selvan', '788556', 'rapunzel.jpg'),
('abi', 'abi@gmail.c', 2147483647, '2025-01-28', 'female', 'Tamilnadu', 'Erode', 'Thindal,Erode', 'Abinaya', '856974', '1a521eaUS232_3.avif'),
('suba', 'suba@gmail.', 2147483647, '2025-03-05', 'female', 'Tamilnadu', 'Coimbatore', 'Ramanathapuram ,Cbe', 'suba rajesh', '890637', '0f24f3e58140OR_4.avif'),
('maha', 'maha@gmail.', 2147483647, '2025-02-11', 'female', 'Tamilnadu', 'Thanjavur', 'Pattukotati', 'maha chandra', '61231548', '00b6bbdNYFDIVE001559.1.avif');

-- --------------------------------------------------------

--
-- Table structure for table `dealer`
--

CREATE TABLE `dealer` (
  `Id` int(10) NOT NULL,
  `full_Name` varchar(15) NOT NULL,
  `business_Name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `location` varchar(40) NOT NULL,
  `license_No` varchar(20) NOT NULL,
  `raw_Materials` varchar(30) NOT NULL,
  `image` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `Password` varchar(15) NOT NULL,
  `liimage` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dealer`
--

INSERT INTO `dealer` (`Id`, `full_Name`, `business_Name`, `email`, `phone`, `location`, `license_No`, `raw_Materials`, `image`, `status`, `username`, `Password`, `liimage`) VALUES
(26, 'Dharani', 'Dharani Industries', 'bhavadharanigk@gmail.com', '8563214789', 'Erode', 'DI-67809', 'cotton,rayon,nylon', 'dharanilogo.png', 'approved', 'FK26', 'Dharani@123', 'dealer2li.jpeg'),
(27, 'Akash', 'WelTex Industry', 'alok@gmail.com', '9687456320', 'Erode', 'WT-85003', 'cotton,rayon,popcorn', 'mahalogo.png', 'rejected', '', '', 'dealer2li.jpeg'),
(55, 'Saranya', 'Saranya Industries', 'saranyaselvan13@gmail.com', '9097876511', 'Erode', 'SI-93456', 'cotton,rayon', 'sranyalogo.png', 'approved', 'FK55', 'SarodTq', 'lii.jpeg'),
(63, 'Maha', 'Maha Industries', 'mahachandra05@gmail.com', '9867654637', 'Tiruppur', 'GT-98065', 'cotton,rayon', 'mahalogo.png', 'approved', 'FK63', 'Maha@12', 'wholeli3.png'),
(65, 'Gowtham', 'Gowtham Industries', 'gowtham@gmail.com', '9867654637', 'Erode', 'GT-98065', 'cotton,rayon', 'wlogo2.png', 'rejected', '', '', 'images (4dealer3lis.jpeg'),
(66, 'Saran', 'saran industry', 'sara@gmail.com', '9835671892', 'erode', 'si-09287', 'cotton,rayon', 'dharanilogo.png', 'False', '', '', 'dealer2li.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `dispatch`
--

CREATE TABLE `dispatch` (
  `product_id` int(40) NOT NULL,
  `product` varchar(30) NOT NULL,
  `material` varchar(40) NOT NULL,
  `size` varchar(30) NOT NULL,
  `color` varchar(30) NOT NULL,
  `quantity` int(30) NOT NULL,
  `price` varchar(40) NOT NULL,
  `image` varchar(40) NOT NULL,
  `oquantity` varchar(40) NOT NULL,
  `oprice` int(30) NOT NULL,
  `Payment` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `dispatch`
--

INSERT INTO `dispatch` (`product_id`, `product`, `material`, `size`, `color`, `quantity`, `price`, `image`, `oquantity`, `oprice`, `Payment`) VALUES
(73, 'Pant', 'Popcorn', 'small', 'Blue', 250, '200', 'bluepant2.jpeg', '', 0, 'Paid'),
(11, 'T-Shirt', 'Cotton', 'Large', 'White', 300, '280', 'ly sma whi.jpeg.jpg', '', 0, 'Paid'),
(21, 'T-Shirt', 'Lycra', 'large', 'White', 300, '330', 'ly sma whi.jpeg.jpg', '', 0, ''),
(24, 'T-Shirt', 'Rayon', 'small', 'White', 300, '220', 'ly sma whi.jpeg.jpg', '', 0, ''),
(26, 'T-Shirt', 'Rayon', 'medium', 'Black', 300, '250', 'ly sma black.jpeg.jpg', '', 0, 'Paid'),
(10, 'T-Shirt', 'Cotton', 'Large', 'Black', 300, '280', 'men.jpeg', '', 0, ''),
(11, 'T-Shirt', 'Cotton', 'Large', 'White', 300, '280', 'ly sma whi.jpeg.jpg', '', 0, 'Paid'),
(51, 'Pant', 'Cotton', 'large', 'Black', 290, '69000.00', 'blackpant2.jpeg', '', 0, 'Paid'),
(12, 'T-Shirt', 'Cotton', 'Large', 'Blue', 200, '280', 'co lar blue.jpeg.jpg', '', 0, ''),
(15, 'T-Shirt', 'Lycra', 'small', 'Blue', 268, '230', 'blu.jpeg', '100', 23000, 'Paid'),
(29, 'T-Shirt', 'Rayon', 'large', 'Black', 98, '280', 'ly med black.jpeg.jpg', '', 0, 'Paid'),
(30, 'T-Shirt', 'Rayon', 'large', 'White', 260, '280', 'ly med black.jpeg.jpg', '', 0, 'Paid'),
(43, 'T-Shirt', 'Popcorn', 'large', 'White', 100, '30000.00', 'co lar blue.jpeg.jpg', '100', 3000000, ''),
(23, 'T-Shirt', 'Rayon', 'small', 'Black', 284, '220', 'ly sma black.jpeg.jpg', '', 0, 'Paid'),
(27, 'T-Shirt', 'Rayon', 'medium', 'White', 300, '250', 'co lar white.avif', '', 0, ''),
(61, 'Pant', 'Lycra', 'large', 'White', 300, '300', 'whitepant2.jpeg', '', 0, 'Paid'),
(37, 'T-Shirt', 'Popcorn', 'small', 'White', 200, '210', 'co lar white.avif', '', 0, ''),
(63, 'Pant', 'Rayon', 'small', 'Black', 313, '220', 'blackpant3.jpeg', '', 0, 'Paid');

-- --------------------------------------------------------

--
-- Table structure for table `manager`
--

CREATE TABLE `manager` (
  `id` int(15) NOT NULL,
  `name` varchar(30) NOT NULL,
  `mail` varchar(40) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `location` varchar(40) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `image` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `manager`
--

INSERT INTO `manager` (`id`, `name`, `mail`, `phone`, `location`, `username`, `password`, `image`) VALUES
(0, 'Bharath', 'bharath12@gmail.com', '9687456320', 'Tiruppur', 'Manager', 'Bharath@123', 'managerimg.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL,
  `order_id` varchar(50) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_method` varchar(50) DEFAULT NULL,
  `payment_date` datetime DEFAULT NULL,
  `card_info` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`payment_id`, `order_id`, `amount`, `payment_method`, `payment_date`, `card_info`) VALUES
(1, '1', 1800000.00, 'bank_transfer', '2025-03-24 14:54:43', 'N/A');

-- --------------------------------------------------------

--
-- Table structure for table `payment_history`
--

CREATE TABLE `payment_history` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `payment_method` varchar(50) NOT NULL,
  `payment_date` datetime NOT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `transaction_id` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `production`
--

CREATE TABLE `production` (
  `id` int(15) NOT NULL,
  `product` varchar(30) NOT NULL,
  `material` varchar(30) NOT NULL,
  `size` varchar(40) NOT NULL,
  `color` varchar(40) NOT NULL,
  `quantity` int(50) NOT NULL,
  `deadline` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `status` varchar(30) NOT NULL,
  `info` varchar(30) NOT NULL,
  `price` int(40) NOT NULL,
  `image` varchar(40) NOT NULL,
  `oquantity` varchar(40) NOT NULL,
  `oprice` int(11) NOT NULL,
  `wid` int(40) NOT NULL,
  `payment_status` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `production`
--

INSERT INTO `production` (`id`, `product`, `material`, `size`, `color`, `quantity`, `deadline`, `status`, `info`, `price`, `image`, `oquantity`, `oprice`, `wid`, `payment_status`) VALUES
(4, 'T-Shirt', 'Cotton', 'small', 'Black', 300, '2025-03-21 09:50:09.716936', 'Accepted', '', 200, 'ss.jpeg', '8', 1600, 1, '0'),
(5, 'T-Shirt', 'Cotton', 'small', 'White', 250, '2025-03-20 11:24:04.448646', 'Accepted', 'Urgent', 200, 'sw.jpeg', '100', 20000, 5, '0'),
(6, 'T-Shirt', 'Cotton', 'medium', 'Black', 400, '2025-03-20 03:44:49.094098', 'Accepted', '', 230, 'black co large.jpeg.jpg', '200', 46000, 1, '0'),
(7, 'T-Shirt', 'Cotton', 'medium', 'White', 300, '2025-03-20 11:23:50.006984', 'Accepted', '', 230, 'co sma white.jpeg.jpg', '100', 23000, 4, '0'),
(8, 'T-Shirt', 'Cotton', 'medium', 'Red', 200, '2025-03-19 17:51:09.129311', 'Ordered', '', 230, 'co med red.jpeg.jpg', '100', 23000, 0, '0'),
(13, 'T-Shirt', 'Lycra', 'small', 'Black', 300, '2025-03-19 17:50:28.946531', 'Ordered', 'Urgent', 230, 'ly med black.jpeg.jpg', '180', 41400, 0, '0'),
(14, 'T-Shirt', 'Lycra', 'small', 'White', 400, '2025-03-21 10:01:13.019231', 'Accepted', '', 230, 'ly med whi.jpeg.jpg', '100', 23000, 1, '0'),
(16, 'T-Shirt', 'Lycra', 'medium', 'Black', 250, '2025-03-20 03:01:32.080671', 'Ordered', '', 260, 'bb.jpeg', '150', 39000, 4, '0'),
(18, 'T-Shirt', 'Lycra', 'medium', 'Purple', 400, '2025-03-19 18:00:02.850849', 'Ordered', '', 260, 'ly med purple.jpeg.jpg', '100', 26000, 0, '0'),
(19, 'T-Shirt', 'Lycra', 'medium', 'Red', 250, '2025-03-20 02:37:19.928220', 'Ordered', '', 260, 'ly med red.jpeg.jpg', '100', 26000, 1, '0'),
(20, 'T-Shirt', 'Lycra', 'large', 'Black', 300, '2025-03-21 09:38:22.235468', 'Accepted', 'Urgent', 330, 'ly med black.jpeg.jpg', '150', 49500, 1, '0'),
(22, 'T-Shirt', 'Lycra', 'large', 'Blue', 300, '2025-03-19 17:55:27.643667', 'finished', 'None', 330, 'bss.jpeg', '150', 0, 0, '0'),
(23, 'T-Shirt', 'Rayon', 'small', 'Black', 0, '2025-03-21 09:46:21.746856', 'finished', 'None', 220, 'ly sma black.jpeg.jpg', '150', 0, 0, '0'),
(25, 'T-Shirt', 'Rayon', 'small', 'Blue', 300, '2025-03-20 08:45:48.496240', 'finished', 'None', 220, 'blu.jpeg', '150', 0, 0, '0'),
(26, 'T-Shirt', 'Rayon', 'medium', 'Black', 50, '2025-03-20 17:17:57.641597', 'finished', 'None', 250, 'ly sma black.jpeg.jpg', '150', 0, 0, '0'),
(27, 'T-Shirt', 'Rayon', 'medium', 'White', 0, '2025-03-21 10:53:59.724875', 'finished', 'None', 250, 'co lar white.avif', '150', 0, 0, '0'),
(28, 'T-Shirt', 'Rayon', 'medium', 'Red', 300, '2025-03-20 08:48:06.168547', 'finished', 'None', 250, 'co med red.jpeg.jpg', '150', 0, 0, '0'),
(29, 'T-Shirt', 'Rayon', 'large', 'Black', 30, '2025-03-20 17:20:09.082848', 'finished', 'Urgent', 280, 'ly med black.jpeg.jpg', '150', 0, 0, '0'),
(30, 'T-Shirt', 'Rayon', 'large', 'White', 10, '2025-03-20 17:20:30.875741', 'finished', 'None', 280, 'ly med black.jpeg.jpg', '150', 0, 0, '0'),
(31, 'T-Shirt', 'Rayon', 'large', 'Blue', 250, '2025-03-20 08:49:29.029487', 'finished', 'None', 280, 'att.jpeg', '150', 0, 0, '0'),
(33, 'T-Shirt', 'Rayon', 'large', 'Purple', 300, '2025-03-20 08:49:51.387805', 'finished', 'None', 280, 'tshirt.jpeg', '150', 0, 0, '0'),
(36, 'T-Shirt', 'Popcorn', 'small', 'Black', 350, '2025-03-20 08:51:31.548793', 'finished', 'None', 210, 'att.jpeg', '150', 0, 0, '0'),
(37, 'T-Shirt', 'Popcorn', 'small', 'White', 50, '2025-03-21 10:54:37.607636', 'finished', 'None', 210, 'co lar white.avif', '150', 0, 0, '0'),
(38, 'T-Shirt', 'Popcorn', 'small', 'Blue', 200, '2025-03-20 08:50:37.167169', 'finished', 'None', 210, 'ly med red.jpeg.jpg', '150', 0, 0, '0'),
(39, 'T-Shirt', 'Popcorn', 'medium', 'Black', 300, '2025-03-20 08:50:46.409421', 'finished', 'None', 250, 'cs.jpeg', '150', 0, 0, '0'),
(40, 'T-Shirt', 'Popcorn', 'medium', 'Red', 250, '2025-03-20 08:51:59.950079', 'finished', 'None', 250, 'co lar blue.jpeg.jpg', '150', 0, 0, '0'),
(41, 'T-Shirt', 'Popcorn', 'medium', 'White', 300, '2025-03-20 08:52:25.128629', 'finished', 'None', 250, 'tshirt.jpeg', '150', 0, 0, '0'),
(42, 'T-Shirt', 'Popcorn', 'large', 'Black', 350, '2025-03-20 08:52:38.422693', 'finished', 'None', 300, 'bb.jpeg', '150', 0, 0, '0'),
(43, 'T-Shirt', 'Popcorn', 'large', 'White', 50, '2025-03-23 09:26:07.779228', 'Accepted', 'None', 300, 'co lar blue.jpeg.jpg', '150', 0, 0, '0'),
(44, 'T-Shirt', 'Popcorn', 'large', 'Blue', 300, '2025-03-20 09:00:13.558379', 'finished', 'None', 300, 'bss.jpeg', '150', 0, 0, '0'),
(45, 'Pant', 'Cotton', 'small', 'Black', 450, '2025-03-20 09:05:28.836694', 'finished', 'None', 150, 'blackpant1.jpeg', '150', 0, 0, '0'),
(46, 'Pant', 'Cotton', 'small', 'Black', 400, '2025-03-20 09:06:26.133848', 'Ordered', 'None', 150, 'blackpant2.jpeg', '122', 18300, 0, '0'),
(47, 'Pant', 'Cotton', 'small', 'Blue', 500, '2025-03-20 09:11:26.229055', 'finished', 'Urgent', 150, 'bluepant1.jpeg', '150', 0, 0, '0'),
(48, 'Pant', 'Cotton', 'medium', 'Black', 450, '2025-03-20 09:12:28.668811', 'finished', 'None', 190, 'blackpant1.jpeg', '150', 0, 0, '0'),
(49, 'Pant', 'Cotton', 'medium', 'White', 450, '2025-03-20 09:13:28.467842', 'finished', 'None', 190, 'whitepant1.jpeg', '150', 0, 0, '0'),
(50, 'Pant', 'Cotton', 'medium', 'Blue', 350, '2025-03-20 09:12:59.618597', 'finished', 'Urgent', 190, 'whitepant1.jpeg', '150', 0, 0, '0'),
(51, 'Pant', 'Cotton', 'large', 'Black', 150, '2025-03-20 17:18:52.748523', 'finished', 'None', 230, 'blackpant2.jpeg', '150', 0, 0, '0'),
(52, 'Pant', 'Cotton', 'large', 'White', 450, '2025-03-20 09:14:03.270131', 'finished', 'None', 230, 'whitepant2.jpeg', '150', 0, 0, '0'),
(53, 'Pant', 'Cotton', 'large', 'Blue', 400, '2025-03-20 09:14:11.780929', 'finished', 'None', 230, 'bluepant2.jpeg', '150', 0, 0, '0'),
(54, 'Pant', 'Lycra', 'small', 'Black', 450, '2025-03-20 09:15:09.370585', 'finished', 'None', 230, 'blackpant3.jpeg', '150', 0, 0, '0'),
(55, 'Pant', 'Lycra', 'small', 'White', 400, '2025-03-20 09:15:21.415648', 'finished', 'None', 230, 'whitepant3.jpeg', '150', 0, 0, '0'),
(56, 'Pant', 'Lycra', 'small', 'Blue', 500, '2025-03-20 09:15:31.092638', 'finished', 'None', 230, 'bluepant3.jpeg', '150', 0, 0, '0'),
(57, 'Pant', 'Lycra', 'medium', 'Black', 450, '2025-03-20 09:16:18.182900', 'finished', 'Urgent', 250, 'blackpant1.jpeg', '150', 0, 0, '0'),
(58, 'Pant', 'Lycra', 'medium', 'White', 500, '2025-03-20 09:16:28.481399', 'finished', 'None', 250, 'whitepant1.jpeg', '150', 0, 0, '0'),
(59, 'Pant', 'Lycra', 'medium', 'Blue', 450, '2025-03-20 09:16:37.806915', 'finished', 'None', 250, 'bluepant4.jpeg', '150', 0, 0, '0'),
(60, 'Pant', 'Lycra', 'large', 'Black', 400, '2025-03-20 09:16:47.562833', 'finished', 'None', 300, 'blackpant2.jpeg', '150', 0, 0, '0'),
(61, 'Pant', 'Lycra', 'large', 'White', 0, '2025-03-21 10:54:26.214009', 'finished', 'Urgent', 300, 'whitepant2.jpeg', '150', 0, 0, '0'),
(62, 'Pant', 'Lycra', 'large', 'Blue', 450, '2025-03-20 09:17:06.725526', 'finished', 'Urgent', 300, 'bluepant1.jpeg', '150', 0, 0, '0'),
(63, 'Pant', 'Rayon', 'small', 'Black', 67, '2025-03-21 10:55:14.114712', 'finished', 'None', 220, 'blackpant3.jpeg', '150', 0, 0, '0'),
(64, 'Pant', 'Rayon', 'small', 'White', 450, '2025-03-20 09:18:34.989970', 'finished', 'None', 220, 'whitepant2.jpeg', '150', 0, 0, '0'),
(65, 'Pant', 'Rayon', 'small', 'Blue', 450, '2025-03-20 09:19:00.701591', 'finished', 'None', 220, 'bluepant2.jpeg', '150', 0, 0, '0'),
(66, 'Pant', 'Rayon', 'medium', 'Black', 450, '2025-03-20 09:19:09.734954', 'finished', 'None', 250, 'blackpant1.jpeg', '150', 0, 0, '0'),
(67, 'Pant', 'Rayon', 'medium', 'White', 500, '2025-03-20 09:19:46.859304', 'finished', 'None', 250, 'whitepant2.jpeg', '150', 0, 0, '0'),
(68, 'Pant', 'Rayon', 'large', 'Blue', 450, '2025-03-20 09:19:57.577953', 'finished', 'None', 290, 'bluepant1.jpeg', '150', 0, 0, '0'),
(69, 'Pant', 'Rayon', 'large', 'Black', 450, '2025-03-20 09:20:39.821933', 'finished', 'None', 290, 'blackpant3.jpeg', '150', 0, 0, '0'),
(70, 'Pant', 'Rayon', 'large', 'White', 500, '2025-03-20 09:20:48.398441', 'finished', 'None', 290, 'whitepant3.jpeg', '150', 0, 0, '0'),
(71, 'Pant', 'Popcorn', 'small', 'Black', 400, '2025-03-20 09:43:36.208598', 'Accepted', 'Urgent', 200, 'blackpant2.jpeg', '1', 200, 1, '0'),
(72, 'Pant', 'Popcorn', 'small', 'White', 450, '2025-03-20 09:22:11.884673', 'finished', 'None', 200, 'whitepant2.jpeg', '150', 0, 0, '0'),
(73, 'Pant', 'Popcorn', 'small', 'Blue', 200, '2025-03-20 17:16:46.067016', 'finished', 'None', 200, 'bluepant2.jpeg', '150', 0, 0, '0'),
(74, 'Pant', 'Popcorn', 'medium', 'Black', 450, '2025-03-20 09:23:40.057717', 'finished', 'None', 230, 'whitepant3.jpeg', '150', 0, 0, '0'),
(75, 'Pant', 'Popcorn', 'medium', 'White', 450, '2025-03-24 10:34:10.878970', 'finished', 'None', 230, 'blackpant3.jpeg', '150', 0, 0, '0'),
(76, 'Pant', 'Popcorn', 'medium', 'Blue', 450, '2025-03-24 10:34:14.344460', 'finished', 'None', 230, 'whitepant3.jpeg', '150', 0, 0, '0'),
(77, 'Pant', 'Popcorn', 'large', 'Black', 450, '2025-03-20 09:25:05.751383', 'Requested', 'Urgent', 260, 'blackpant3.jpeg', '150', 0, 0, '0'),
(78, 'Pant', 'Popcorn', 'large', 'White', 400, '2025-03-20 09:25:15.872976', 'Finished', 'None', 260, 'whitepant3.jpeg', '150', 0, 0, '0'),
(79, 'Pant', 'Popcorn', 'large', 'Blue', 500, '2025-03-20 09:25:49.322732', 'Finished', 'None', 260, 'bluepant4.jpeg', '150', 0, 0, '0'),
(83, 'Tshirts', 'Cotton', 'm', 'red', 200, '2025-04-04 18:30:00.000000', 'Requested', 'Its urgent to complete within ', 80, 'smutt.jpeg', '', 0, 0, '0'),
(84, 'Tshirts', 'Cotton', 'small', 'red', 222, '2025-03-18 18:30:00.000000', 'Requested', '', 200, 'img1.jpeg', '', 0, 0, '0'),
(85, 'T-shirt', 'Cotton', 'small', 'red', 300, '2025-03-21 09:45:42.632473', 'finished', 'It is urgent', 300000, 'Screenshot 2024-12-18 103935.png', '', 0, 0, ''),
(86, 'T-shirt', 'Cotton', 'small', 'Blue', 330, '2025-03-27 18:30:00.000000', 'Requested', 'make it fast', 120, 'sb.jpeg', '', 0, 0, ''),
(87, 'pant', 'Rayon', 'small', 'White', 500, '2025-03-25 18:30:00.000000', 'Requested', '', 280, 'whitepant2.jpeg', '', 0, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `raw`
--

CREATE TABLE `raw` (
  `dealerid` int(11) NOT NULL,
  `rid` int(15) NOT NULL,
  `material` varchar(30) NOT NULL,
  `quantity` int(30) NOT NULL,
  `price` int(40) NOT NULL,
  `date_update` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `color` varchar(50) NOT NULL,
  `image` varchar(40) NOT NULL,
  `dealer_name` varchar(20) NOT NULL,
  `business_name` varchar(30) NOT NULL,
  `mail` varchar(40) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `location` varchar(40) NOT NULL,
  `ordermat` varchar(30) NOT NULL,
  `orderclrone` varchar(30) NOT NULL,
  `orderclrtwo` varchar(30) NOT NULL,
  `orderclrthree` varchar(40) NOT NULL,
  `orderqone` int(40) NOT NULL,
  `orderqtwo` int(50) NOT NULL,
  `orderqthree` int(30) NOT NULL,
  `orderqtotal` int(30) NOT NULL,
  `orderptotal` int(30) NOT NULL,
  `order_status` varchar(40) NOT NULL,
  `payment_status` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `raw`
--

INSERT INTO `raw` (`dealerid`, `rid`, `material`, `quantity`, `price`, `date_update`, `color`, `image`, `dealer_name`, `business_name`, `mail`, `phone`, `location`, `ordermat`, `orderclrone`, `orderclrtwo`, `orderclrthree`, `orderqone`, `orderqtwo`, `orderqthree`, `orderqtotal`, `orderptotal`, `order_status`, `payment_status`) VALUES
(1, 26, 'Cotton', 200, 9000, '2025-03-24 09:18:55.323164', 'Black, White, Red', 'cotton2.jpeg', 'Dharani', 'Dharani Industries', 'bhavadharanigk@gmail.com', '8563214789', 'Erode', 'Cotton', 'Black', 'None', 'None', 200, 0, 0, 200, 1800000, 'Order Accepted', 'Pending'),
(2, 26, 'Popcorn', 200, 9400, '2025-03-24 09:18:55.323164', 'Black White Red', 'pop.jpeg', 'Dharani', 'Dharani Industries', 'bhavadharanigk@gmail.com', '8563214789', '	 Erode', 'Popcorn', 'Black', 'White', 'Red', 15, 20, 10, 45, 423000, 'Order Pending', 'Pending'),
(3, 26, 'Lycra', 200, 13000, '2025-03-24 09:18:55.323164', 'Black White Blue', 'light-brown-beige-pants-arrangement.jpg', 'Dharani', 'Dharani Industries', 'bhavadharanigk@gmail.com', '8563214789', '	 Erode', 'Lycra', 'Black', 'White', 'Blue', 15, 10, 10, 35, 455000, 'Order Accepted', 'Pending'),
(4, 63, 'Rayon', 200, 12000, '2025-03-24 09:18:55.323164', 'Black White Purple', 'ray1', 'Maha', 'Maha Industries', 'mahachandra05@gmail.com', '9867654637', 'Tiruppur', 'Rayon', 'Black', 'White', 'Purple', 10, 15, 10, 35, 420000, 'Order Accepted', 'Pending'),
(22, 63, 'Cotton', 400, 9000, '2025-03-24 09:18:55.323164', 'Black White Red', 'ccot2.avif', 'Maha', 'Maha Industries', 'mahachandra05@gmail.com', '9867654637', 'Tiruppur', 'Cotton', 'Black', 'White', 'Red', 20, 15, 20, 55, 495000, 'Order Pending', 'Pending'),
(25, 63, 'lycra', 300, 13000, '2025-03-24 09:18:55.323164', 'Black Blue Red', 'close-up-texture-linen-fabric.jpg', 'Maha', 'Maha Industries', 'mahachandra05@gmail.com', '9867654637', 'Tiruppur', 'lycra', 'Black', 'Blue', 'Red', 10, 20, 15, 45, 585000, 'Order Pending', 'Pending'),
(26, 63, 'Popcorn', 300, 9300, '2025-03-24 09:18:55.323164', 'Black White Blue', 'pop2.jpeg', 'Maha', 'Maha Industries', 'mahachandra05@gmail.com', '9867654637', 'Tiruppur', 'Popcorn', 'Black', 'White', 'Blue', 20, 15, 20, 55, 511500, 'Order Accepted', 'Pending'),
(28, 26, 'Rayon', 400, 12000, '2025-03-24 09:18:55.323164', 'White Blue Purple', 'lycra2.jpeg', 'Dharani', 'Dharani Industries', 'bhavadharanigk@gmail.com', '8563214789', '	 Erode', 'Rayon', 'White', 'Blue', 'Purple', 10, 15, 10, 35, 420000, 'Order Accepted', 'Pending'),
(29, 55, 'Cotton', 600, 9000, '2025-03-24 09:18:55.323164', 'Black White Blue', 'images (3).jpeg', 'Saranya', 'Saranya Industries', 'saranyaselvan13@gmail.com', '9097876511', 'Erode', 'Cotton', 'Black', 'None', 'None', 20, 0, 0, 20, 180000, 'Order Accepted', 'Pending'),
(30, 55, 'Rayon', 500, 12000, '2025-03-24 09:18:55.323164', 'Black  Blue Purple', 'images (2).jpeg', 'Saranya', 'Saranya Industries', 'saranyaselvan13@gmail.com', '9097876511', 'Erode', 'Rayon', 'Black', 'Blue', 'Purple', 20, 15, 10, 45, 540000, 'Order Pending', 'Pending'),
(31, 55, 'lycra', 400, 13000, '2025-03-24 09:18:55.323164', 'Black White Red', 'download (1).jpeg', 'Saranya', 'Saranya Industries', 'saranyaselvan13@gmail.com', '9097876511', 'Erode', 'lycra', 'Black', 'White', 'Red', 10, 15, 10, 35, 455000, 'Order Pending', 'Pending'),
(32, 55, 'Popcorn', 600, 9400, '2025-03-24 09:18:55.323164', 'White Blue Red', 'pop3.jpeg', 'Saranya', 'Saranya Industries', 'saranyaselvan13@gmail.com', '9097876511', 'Erode', 'Popcorn', 'Black', 'None', 'None', 20, 0, 0, 20, 188000, 'Order Pending', 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `name` varchar(40) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `subject` varchar(40) NOT NULL,
  `address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `wholesaler`
--

CREATE TABLE `wholesaler` (
  `id` int(15) NOT NULL,
  `fullname` varchar(30) NOT NULL,
  `business_name` varchar(30) NOT NULL,
  `mail` varchar(40) NOT NULL,
  `phno` varchar(10) NOT NULL,
  `location` varchar(50) NOT NULL,
  `license` varchar(30) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  `image` varchar(40) NOT NULL,
  `liimg` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wholesaler`
--

INSERT INTO `wholesaler` (`id`, `fullname`, `business_name`, `mail`, `phno`, `location`, `license`, `username`, `password`, `status`, `image`, `liimg`) VALUES
(1, 'Guna', 'Global textiles', 'saranyaselvan13@gmail.com', '9687456320', 'Tiruppur', 'GI-95789', 'FK1', 'GuiruS9', 'approved', 'whollogo1.png', 'dealer2li.jpeg'),
(4, 'Ezhil', 'Ezhil Exports', 'saranselvan2002@gmail.com', '9934772188', 'Erode', 'EE-90729', 'FK4', 'Ezrodtt', 'approved', 'wlogo2.png', 'lii.jpeg'),
(5, 'Nandha', 'Nandha Industries', 'bhavadharanigk@gmail.com', '8032660173', 'Tiruppur', 'NI-90729', 'FK5', 'NairubF', 'approved', 'whole3.jpeg', 'images (4dealer3lis.jpeg'),
(6, 'Guru', 'Global textiles', 'saranselvan@gmail.com', '9456789088', 'Erode', 'GI-95789', NULL, NULL, 'rejected', 'dharanilogo.png', 'wholeli3.png'),
(8, 'saran', 'sataan', 'sara@gmail.com', '9087654432', 'erosd', 'haggshd', NULL, NULL, 'False', 'wholeli3.png', 'wholeli.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `wholesale_order`
--

CREATE TABLE `wholesale_order` (
  `wholesaler_id` int(40) NOT NULL,
  `product_id` int(30) NOT NULL,
  `quantity` int(40) NOT NULL,
  `price` int(30) NOT NULL,
  `total_price` int(30) NOT NULL,
  `payment_method` varchar(30) NOT NULL,
  `payment_details` varchar(40) NOT NULL,
  `order_date` varchar(40) NOT NULL,
  `payment_status` varchar(30) NOT NULL,
  `product_name` varchar(40) NOT NULL,
  `material` varchar(30) NOT NULL,
  `size` varchar(40) NOT NULL,
  `status` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `wholesale_order`
--

INSERT INTO `wholesale_order` (`wholesaler_id`, `product_id`, `quantity`, `price`, `total_price`, `payment_method`, `payment_details`, `order_date`, `payment_status`, `product_name`, `material`, `size`, `status`) VALUES
(1, 73, 1, 200, 200, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 09:47:16', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 73, 1, 200, 200, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 10:00:51', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 73, 1, 200, 200, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 10:00:55', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 11, 50, 280, 14000, 'Bank Transfer', '{\"accountNumber\":\"hqehbawh\",\"ifscCode\":\"', '2025-03-21 10:01:33', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 11, 21, 280, 5880, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 14:19:50', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 11, 21, 280, 5880, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 14:26:45', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 73, 1, 200, 200, 'UPI', '{\"upiId\":\"8934932\"}', '2025-03-21 14:41:32', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 73, 1, 200, 200, 'UPI', '{\"upiId\":\"8934932\"}', '2025-03-21 14:41:36', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 11, 100, 280, 28000, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 14:41:44', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(4, 29, 100, 280, 28000, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 14:44:04', 'Paid', 'pant', 'lycra', 'small', 'Ordered'),
(4, 30, 10, 280, 2800, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 14:44:31', 'Paid', 'pant', 'lycra', 'small', 'Ordered'),
(0, 0, 0, 0, 0, '', '', '', '', 'T-shirt', 'cotton', '', 'Ordered'),
(4, 30, 10, 280, 2800, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 14:51:52', 'Paid', 'pant', 'lycra', 'small', 'Ordered'),
(4, 30, 10, 280, 2800, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 14:52:10', 'Paid', 'pant', 'lycra', 'small', 'Ordered'),
(4, 29, 1, 280, 280, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 14:52:17', 'Paid', 'pant', 'lycra', 'small', 'Ordered'),
(4, 29, 1, 280, 280, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 15:01:04', 'Paid', 'pant', 'lycra', 'small', 'Ordered'),
(4, 73, 200, 200, 40000, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 15:01:51', 'Paid', 'pant', 'lycra', 'small', 'Ordered'),
(1, 73, 1, 200, 200, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 15:19:50', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 73, 1, 200, 200, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 15:39:17', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 11, 200, 280, 56000, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 15:42:23', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 73, 1, 200, 200, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 15:48:27', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 73, 1, 200, 200, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 15:51:47', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 11, 2, 280, 560, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 15:57:29', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 11, 88, 280, 24640, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 15:57:48', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 11, 200, 280, 56000, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 16:03:32', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 73, 111, 200, 22200, '', '', '2025-03-21 16:05:36', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 26, 100, 250, 25000, '', '', '2025-03-21 16:06:17', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 26, 100, 250, 25000, '', '', '2025-03-21 16:06:34', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 26, 50, 250, 12500, '', '', '2025-03-21 16:06:42', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 26, 50, 250, 12500, '', '', '2025-03-21 16:07:09', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 26, 10, 250, 2500, '', '', '2025-03-21 16:07:17', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 26, 10, 250, 2500, '', '', '2025-03-21 16:07:21', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 73, 10, 200, 2000, '', '', '2025-03-21 16:08:03', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 15, 10, 230, 2300, '', '', '2025-03-21 16:18:59', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 23, 16, 220, 3520, '', '', '2025-03-21 16:19:36', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 51, 10, 69000, 690000, '', '', '2025-03-21 16:20:07', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 29, 10, 280, 2800, '', '', '2025-03-21 16:22:18', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 29, 10, 280, 2800, '', '', '2025-03-21 16:22:24', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 61, 100, 300, 30000, '', '', '2025-03-21 16:24:52', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 61, 100, 300, 30000, '', '', '2025-03-21 16:25:18', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(1, 63, 20, 220, 4400, '', '', '2025-03-21 16:25:35', 'Paid', 'Tshirt', 'cotton', 'medium', 'Ordered'),
(5, 73, 50, 200, 10000, 'Cash on Delivery', '{\"method\":\"COD\"}', '2025-03-21 16:55:50', 'Paid', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `wholesale_orders`
--
-- Error reading structure for table amazon.wholesale_orders: #1932 - Table &#039;amazon.wholesale_orders&#039; doesn&#039;t exist in engine
-- Error reading data for table amazon.wholesale_orders: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near &#039;FROM `amazon`.`wholesale_orders`&#039; at line 1

-- --------------------------------------------------------

--
-- Table structure for table `w_order`
--

CREATE TABLE `w_order` (
  `wholesaler_id` int(40) NOT NULL,
  `product_id` int(30) NOT NULL,
  `product_name` varchar(40) NOT NULL,
  `material` varchar(30) NOT NULL,
  `size` varchar(30) NOT NULL,
  `color` varchar(30) NOT NULL,
  `quantity` int(40) NOT NULL,
  `total_price` int(40) NOT NULL,
  `o_status` varchar(30) NOT NULL,
  `payment_status` varchar(40) NOT NULL,
  `payment_method` varchar(40) NOT NULL,
  `payment_details` varchar(30) NOT NULL,
  `payment_date` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `w_order`
--

INSERT INTO `w_order` (`wholesaler_id`, `product_id`, `product_name`, `material`, `size`, `color`, `quantity`, `total_price`, `o_status`, `payment_status`, `payment_method`, `payment_details`, `payment_date`) VALUES
(1, 23, 'T-Shirt', 'Rayon', 'small', 'Black', 50, 11000, 'Accepted', 'Paid', '', '', '2025-03-23 14:24:54.194707'),
(4, 11, 'T-Shirt', 'Cotton', 'Large', 'White', 10, 2800, 'Accepted', 'Paid', 'Wallet', '', '2025-03-23 14:40:00.887999'),
(1, 10, 'T-Shirt', 'Cotton', 'Large', 'Black', 50, 14000, 'Accepted', 'Paid', 'Credit Card', '', '2025-03-23 14:34:12.914940'),
(4, 15, 'T-Shirt', 'Lycra', 'small', 'Blue', 50, 11500, 'Accepted', 'Pending', '', '', '2025-03-23 13:56:59.926456'),
(4, 43, 'T-Shirt', 'Popcorn', 'large', 'White', 15, 450000, 'Accepted', 'Pending', '', '', '2025-03-23 13:56:59.926456'),
(1, 61, 'Pant', 'Lycra', 'large', 'White', 100, 30000, 'ordered', 'Paid', 'UPI', '', '2025-03-24 08:33:17.763392'),
(1, 11, 'T-Shirt', 'Cotton', 'Large', 'White', 100, 28000, 'ordered', 'Paid', 'UPI', '', '2025-03-24 08:51:21.162233'),
(1, 12, 'T-Shirt', 'Cotton', 'Large', 'Blue', 10, 2800, 'ordered', 'Pending', '', '', '2025-03-24 08:51:47.304805');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dealer`
--
ALTER TABLE `dealer`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `payment_history`
--
ALTER TABLE `payment_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `production`
--
ALTER TABLE `production`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `raw`
--
ALTER TABLE `raw`
  ADD PRIMARY KEY (`dealerid`);

--
-- Indexes for table `wholesaler`
--
ALTER TABLE `wholesaler`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dealer`
--
ALTER TABLE `dealer`
  MODIFY `Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `payment_history`
--
ALTER TABLE `payment_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `production`
--
ALTER TABLE `production`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

--
-- AUTO_INCREMENT for table `raw`
--
ALTER TABLE `raw`
  MODIFY `dealerid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `wholesaler`
--
ALTER TABLE `wholesaler`
  MODIFY `id` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
