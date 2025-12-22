-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: thanhtamtraquan
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `anhnens`
--

DROP TABLE IF EXISTS `anhnens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `anhnens` (
  `id` int NOT NULL AUTO_INCREMENT,
  `duongDan` varchar(255) NOT NULL,
  `trangThai` enum('ACTIVE','HIDE') DEFAULT 'ACTIVE',
  `ngayTao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anhnens`
--

LOCK TABLES `anhnens` WRITE;
/*!40000 ALTER TABLE `anhnens` DISABLE KEYS */;
INSERT INTO `anhnens` VALUES (1,'/images/background/bg_1766101631_sp-tea.jpg','ACTIVE','2025-12-19 06:47:11'),(2,'/images/background/bg_1766108055_checkout.jpg','ACTIVE','2025-12-19 08:34:15');
/*!40000 ALTER TABLE `anhnens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nguoidungs`
--

DROP TABLE IF EXISTS `nguoidungs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nguoidungs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `hoTen` varchar(255) DEFAULT NULL,
  `gioiTinh` tinyint DEFAULT NULL,
  `ngaySinh` date DEFAULT NULL,
  `diaChi` varchar(255) DEFAULT NULL,
  `SDT` varchar(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `taiKhoan` varchar(100) DEFAULT NULL,
  `matKhau` varchar(255) DEFAULT NULL,
  `role` enum('ADMIN','USER') DEFAULT 'USER',
  `ngayTao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `taiKhoan` (`taiKhoan`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nguoidungs`
--

LOCK TABLES `nguoidungs` WRITE;
/*!40000 ALTER TABLE `nguoidungs` DISABLE KEYS */;
INSERT INTO `nguoidungs` VALUES (1,'Quoc Phong',1,'1990-01-01','HCM','0123456789','admin@example.com','admin','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','ADMIN','2025-12-08 09:29:54'),(2,'Trần Thanh Bảo Khánh',0,'2004-10-20','Gò Vấp, TPHCM','','','khanh','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','ADMIN','2025-12-09 02:37:01');
/*!40000 ALTER TABLE `nguoidungs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sanphams`
--

DROP TABLE IF EXISTS `sanphams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sanphams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tenSanPham` varchar(255) NOT NULL,
  `gia` decimal(12,2) NOT NULL,
  `khoiLuongHop` varchar(64) NOT NULL,
  `soLuong` int DEFAULT NULL,
  `xuatXu` varchar(255) NOT NULL,
  `moTa` text,
  `huongVi` text,
  `congDung` text,
  `cachPha` text,
  `anh` varchar(255) DEFAULT NULL,
  `trangThai` enum('ACTIVE','HIDE') DEFAULT 'ACTIVE',
  `ngayTao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanphams`
--

LOCK TABLES `sanphams` WRITE;
/*!40000 ALTER TABLE `sanphams` DISABLE KEYS */;
INSERT INTO `sanphams` VALUES (1,'Đơn Tùng Bát Tiên',700000.00,'240g / hộp',4,'Núi Phượng Hoàng, Triều Châu, Trung Quốc','Trà Đơn Tung Bát Tiên là một loại trà Ô Long độc đáo được thu hái từ những ngọn núi Phượng Hoàng huyền thoại. Từng lá trà được chọn lọc kỹ lưỡng từ các cây trà cổ thụ, trải qua quy trình chế biến thủ công tỉ mỉ để mang đến hương vị đặc trưng không thể tìm thấy ở bất kỳ nơi nào khác.','Đơn Tùng Bát Tiên mang đến hương thơm ngọt ngào của hoa lan, hòa quyện với vị ngọt dịu và hậu vị kéo dài. Trà có vị nhẹ nhàng, thanh mát ban đầu, sau đó là sự phức hợp của hương quả chín và một chút đậm đà của gỗ, tạo nên cảm giác thư thái và an lành.','Thanh lọc cơ thể: Giúp giảm căng thẳng, thanh nhiệt và điều hòa tâm trí.\nTăng cường sức khỏe: Thích hợp cho những buổi sáng tinh mơ hoặc giữa buổi chiều để khởi động lại tinh thần.\nHỗ trợ tiêu hóa: Giúp hỗ trợ tiêu hóa và cải thiện sức khỏe đường ruột.','Dùng khoảng 5-7g trà cho mỗi ấm (khoảng 200ml nước).\nĐổ nước nóng (khoảng 90-95°C) vào ấm và hãm trà trong 30 giây - 1 phút.\nThưởng thức từ 3-5 lần nước, mỗi lần pha lại thêm nước nóng và tăng thời gian hãm để cảm nhận trọn vẹn hương vị của trà.','/images/products/1re_1765186921_ebe86a.jpg','ACTIVE','2025-12-08 09:44:20'),(2,'Đơn Tùng Áp Thị Hương',1190000.00,'250g / hộp',4,'Núi Cao Sơn, Triều Châu, Trung Quốc','Trà Đơn Tùng Áp Thị Hương là một loại trà Ô Long hiếm và đặc biệt, nổi bật với hương thơm hoa cỏ tự nhiên và vị ngọt đậm đà, được ví như \"hương thơm khiến cả thị trấn ngưỡng mộ\". Trà được thu hoạch thủ công từ những cây trà đơn tùng cổ thụ, sau đó trải qua quá trình chế biến tỉ mỉ để giữ lại tinh túy của hương vị núi rừng.','Trà Đơn Tùng Áp Thị Hương nổi tiếng với hương thơm tinh tế của hoa nhài và hoa cúc, kết hợp với hương mật ong ngọt ngào. Khi thưởng thức, trà mang lại một vị thanh mát, nhẹ nhàng với chút đắng nhẹ ban đầu, nhanh chóng chuyển sang vị ngọt ngào với hậu vị kéo dài. Hương thơm của trà đọng lại lâu, tạo cảm giác thư giãn và sảng khoái.','Giảm căng thẳng: Hương thơm dễ chịu và vị ngọt thanh của trà giúp giải tỏa căng thẳng, thư giãn tinh thần.\nThanh lọc cơ thể: Trà Đơn Tùng Áp Thị Hương có tác dụng thanh nhiệt, giải độc, hỗ trợ cải thiện sức khỏe tổng thể.\nTăng cường sức khỏe: Trà giúp duy trì sự tỉnh táo và nâng cao năng lượng, rất phù hợp để uống vào buổi sáng hoặc khi cần sự tập trung.\nHỗ trợ tiêu hóa: Trà có khả năng hỗ trợ tiêu hóa và giúp cân bằng chức năng đường ruột.','Dùng khoảng 5-7g trà cho mỗi ấm (khoảng 200-250ml nước).\nĐổ nước nóng (khoảng 90-95°C) vào ấm và hãm trà trong 30 giây - 1 phút.\nSau đó, có thể pha thêm từ 4-5 lần nước, mỗi lần thêm nước nóng và tăng thời gian hãm để thưởng thức trọn vẹn hương vị tinh túy của trà.','/images/products/1trung_1765357813_180b65.jpg','ACTIVE','2025-12-10 09:13:57');
/*!40000 ALTER TABLE `sanphams` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-22 16:45:42
