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
-- Table structure for table `address_contact`
--

DROP TABLE IF EXISTS `address_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `address_contact` (
  `id` int NOT NULL AUTO_INCREMENT,
  `noiDung` text NOT NULL,
  `trangThai` enum('ACTIVE','HIDE') DEFAULT 'ACTIVE',
  `ngayTao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address_contact`
--

LOCK TABLES `address_contact` WRITE;
/*!40000 ALTER TABLE `address_contact` DISABLE KEYS */;
INSERT INTO `address_contact` VALUES (1,'CN1: 28/8 Phạm Huy Thông, Phường 7, Quận Gò Vấp, HCM','ACTIVE','2025-12-23 10:18:13'),(2,'CN2: Lô S8.03 Vinhome Grand Park, Quận 9, HCM','ACTIVE','2025-12-23 10:34:59'),(3,'CN3: 567/4 Lê Quang Định, Phường 1, Quận Gò Vấp, HCM ','ACTIVE','2025-12-23 10:35:08');
/*!40000 ALTER TABLE `address_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amtras`
--

DROP TABLE IF EXISTS `amtras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amtras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tenAmTra` varchar(255) NOT NULL,
  `gia` decimal(12,2) NOT NULL,
  `soLuong` int DEFAULT NULL,
  `xuatXu` varchar(255) NOT NULL,
  `moTa` text,
  `chatLieu` text,
  `thietKe` text,
  `cachSuDung` text,
  `anh` varchar(255) DEFAULT NULL,
  `trangThai` enum('ACTIVE','HIDE') DEFAULT 'ACTIVE',
  `ngayTao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amtras`
--

LOCK TABLES `amtras` WRITE;
/*!40000 ALTER TABLE `amtras` DISABLE KEYS */;
INSERT INTO `amtras` VALUES (1,'Bộ Khải pha trà',380000.00,3,'Triều Châu, Trung Quốc','Bộ khải pha trà là một sản phẩm truyền thống tinh tế được thiết kế để thể hiện nghệ thuật thưởng trà độc đáo của khu vực này. Bộ trà Triều Châu thường mang trong mình nét đẹp tinh xảo và sự đơn giản mộc mạc, phản ánh văn hóa trà đạo lâu đời của Trung Quốc.','Bộ khải pha trà được làm từ đất sét nung hoặc sứ, hai loại chất liệu phổ biến trong sản xuất đồ trà. Chất liệu này giúp giữ nhiệt tốt và truyền tải hương vị trà một cách tự nhiên và tinh khiết.','Bộ trà Triều Châu thường có kích thước nhỏ gọn, lý tưởng cho việc pha những loại trà có hương vị tinh tế như trà ô long hoặc trà xanh. Từng chi tiết được chăm chút kỹ lưỡng, từ đường nét của ấm trà cho đến hoa văn trên các chén trà.\nẤm trà có nắp khít, vòi trà được thiết kế để chảy đều và mượt, không gây đổ tràn. Tay cầm thường nhỏ, vừa đủ để cầm tay mà không gây nóng.\nChén trà (khải) thường có hình dạng đơn giản, với đường viền mảnh, nhẹ nhàng để dễ dàng cầm khi thưởng thức.','Các bước pha trà bằng bộ khải này thường bao gồm việc đun nước, tráng ấm và chén trà bằng nước sôi.\nSau đó đổ trà vào ấm và thưởng thức từng ngụm trà nhỏ để cảm nhận hương thơm và vị ngọt nhẹ của trà.','/images/teapots/productTea1_1766487203_d60040.jpg','ACTIVE','2025-12-23 10:53:41'),(2,'Ấm Tử Sa',728000.00,5,'Triều Châu, Trung Quốc','Ấm Tử Sa là một loại ấm trà nổi tiếng và quý giá, được làm từ đất sét đặc biệt có nguồn gốc từ khu vực Tử Sa, thuộc tỉnh Giang Tô, Trung Quốc. Ấm Tử Sa không chỉ là một công cụ pha trà đơn thuần mà còn là một tác phẩm nghệ thuật tinh xảo, được yêu thích trong văn hóa thưởng trà Trung Hoa, đặc biệt là ở Triều Châu.','Đất Tử Sa có đặc điểm độc đáo là không có chất tráng men, nhưng nhờ cấu trúc đất sét vi thể, ấm vẫn có khả năng \"thở\", giúp giữ lại và phát huy hương vị tự nhiên của trà.','Ấm Tử Sa thường có nhiều hình dạng khác nhau, từ kiểu dáng tròn truyền thống đến các thiết kế vuông, đa giác, hoặc hình dáng độc đáo như hình cây, hoa quả, động vật, tùy thuộc vào tay nghề của nghệ nhân.\nDung tích ấm Tử Sa thường nhỏ gọn, phù hợp cho việc pha trà trong những buổi trà nhỏ, mang tính cá nhân hoặc nhóm nhỏ.\nNắp ấm được thiết kế khít với miệng ấm để giữ nhiệt độ và hương vị trà bên trong. Tay cầm được làm chắc chắn, vừa vặn để người dùng có thể cầm mà không bị nóng tay.','Trước khi sử dụng lần đầu, ấm Tử Sa thường được \"nuôi ấm\" bằng cách đun nước sôi và tráng nhiều lần để làm sạch và \"đánh thức\" đất sét.\nSau đó, ấm được dùng để pha trà, thường sử dụng một loại trà cố định để không làm lẫn lộn hương vị.','/images/teapots/productTea2_1766495214_161b84.jpg','ACTIVE','2025-12-23 13:06:58');
/*!40000 ALTER TABLE `amtras` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
-- Table structure for table `donthanhtoan`
--

DROP TABLE IF EXISTS `donthanhtoan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donthanhtoan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `hoTen` varchar(100) NOT NULL,
  `sdt` varchar(20) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `diaChi` text NOT NULL,
  `tenSanPham` text NOT NULL,
  `soLuong` text NOT NULL,
  `thongTinCK` varchar(20) NOT NULL,
  `soTien` decimal(12,0) NOT NULL,
  `trangThai` enum('choXacNhan','daXacNhan','huyXacNhan') DEFAULT 'choXacNhan',
  `ngayTao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donthanhtoan`
--

LOCK TABLES `donthanhtoan` WRITE;
/*!40000 ALTER TABLE `donthanhtoan` DISABLE KEYS */;
INSERT INTO `donthanhtoan` VALUES (1,'Nguyễn Đăng Khôi','079657546463','','22 Nguyễn Thị Thập, Quận 7, TP.HCM','Đơn Tùng Áp Thị Hương, Bộ Khải pha trà','1,1','DH36806',1570000,'choXacNhan','2026-01-06 20:24:45');
/*!40000 ALTER TABLE `donthanhtoan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `email_contact`
--

DROP TABLE IF EXISTS `email_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `email_contact` (
  `id` int NOT NULL AUTO_INCREMENT,
  `noiDung` varchar(255) NOT NULL,
  `trangThai` enum('ACTIVE','HIDE') DEFAULT 'ACTIVE',
  `ngayTao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email_contact`
--

LOCK TABLES `email_contact` WRITE;
/*!40000 ALTER TABLE `email_contact` DISABLE KEYS */;
INSERT INTO `email_contact` VALUES (1,'thanhtamtraquan.1996@gmail.com','ACTIVE','2025-12-23 10:34:29'),(2,'cscscscsc','HIDE','2025-12-26 19:03:46');
/*!40000 ALTER TABLE `email_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `luottruycap_ngay`
--

DROP TABLE IF EXISTS `luottruycap_ngay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `luottruycap_ngay` (
  `date` date NOT NULL,
  `total` int DEFAULT '0',
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `luottruycap_ngay`
--

LOCK TABLES `luottruycap_ngay` WRITE;
/*!40000 ALTER TABLE `luottruycap_ngay` DISABLE KEYS */;
INSERT INTO `luottruycap_ngay` VALUES ('2026-01-04',0),('2026-01-05',28);
/*!40000 ALTER TABLE `luottruycap_ngay` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nguoidungs`
--

LOCK TABLES `nguoidungs` WRITE;
/*!40000 ALTER TABLE `nguoidungs` DISABLE KEYS */;
INSERT INTO `nguoidungs` VALUES (1,'Quoc Phong',1,'1990-01-01','HCM','0123456789','admin@example.com','admin','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','ADMIN','2025-12-08 09:29:54'),(5,'Trần Thanh Bảo Khánh',0,'2004-10-20','Gò Vấp, TPHCM','','','khanh','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','ADMIN','2025-12-25 10:51:03');
/*!40000 ALTER TABLE `nguoidungs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phone_contact`
--

DROP TABLE IF EXISTS `phone_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phone_contact` (
  `id` int NOT NULL AUTO_INCREMENT,
  `noiDung` varchar(50) NOT NULL,
  `trangThai` enum('ACTIVE','HIDE') DEFAULT 'ACTIVE',
  `ngayTao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone_contact`
--

LOCK TABLES `phone_contact` WRITE;
/*!40000 ALTER TABLE `phone_contact` DISABLE KEYS */;
INSERT INTO `phone_contact` VALUES (1,'039 5759357','ACTIVE','2025-12-23 10:34:40');
/*!40000 ALTER TABLE `phone_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rollup_log`
--

DROP TABLE IF EXISTS `rollup_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rollup_log` (
  `date` date NOT NULL,
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rollup_log`
--

LOCK TABLES `rollup_log` WRITE;
/*!40000 ALTER TABLE `rollup_log` DISABLE KEYS */;
INSERT INTO `rollup_log` VALUES ('2026-01-04'),('2026-01-05');
/*!40000 ALTER TABLE `rollup_log` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanphams`
--

LOCK TABLES `sanphams` WRITE;
/*!40000 ALTER TABLE `sanphams` DISABLE KEYS */;
INSERT INTO `sanphams` VALUES (1,'Đơn Tùng Bát Tiên',700000.00,'240g / hộp',4,'Núi Phượng Hoàng, Triều Châu, Trung Quốc','Trà Đơn Tung Bát Tiên là một loại trà Ô Long độc đáo được thu hái từ những ngọn núi Phượng Hoàng huyền thoại. Từng lá trà được chọn lọc kỹ lưỡng từ các cây trà cổ thụ, trải qua quy trình chế biến thủ công tỉ mỉ để mang đến hương vị đặc trưng không thể tìm thấy ở bất kỳ nơi nào khác.','Đơn Tùng Bát Tiên mang đến hương thơm ngọt ngào của hoa lan, hòa quyện với vị ngọt dịu và hậu vị kéo dài. Trà có vị nhẹ nhàng, thanh mát ban đầu, sau đó là sự phức hợp của hương quả chín và một chút đậm đà của gỗ, tạo nên cảm giác thư thái và an lành.','Thanh lọc cơ thể: Giúp giảm căng thẳng, thanh nhiệt và điều hòa tâm trí.\nTăng cường sức khỏe: Thích hợp cho những buổi sáng tinh mơ hoặc giữa buổi chiều để khởi động lại tinh thần.\nHỗ trợ tiêu hóa: Giúp hỗ trợ tiêu hóa và cải thiện sức khỏe đường ruột.','Dùng khoảng 5-7g trà cho mỗi ấm (khoảng 200ml nước).\nĐổ nước nóng (khoảng 90-95°C) vào ấm và hãm trà trong 30 giây - 1 phút.\nThưởng thức từ 3-5 lần nước, mỗi lần pha lại thêm nước nóng và tăng thời gian hãm để cảm nhận trọn vẹn hương vị của trà.','/images/products/1re_1765186921_ebe86a.jpg','ACTIVE','2025-12-08 09:44:20'),(2,'Đơn Tùng Áp Thị Hương',1190000.00,'250g / hộp',4,'Núi Cao Sơn, Triều Châu, Trung Quốc','Trà Đơn Tùng Áp Thị Hương là một loại trà Ô Long hiếm và đặc biệt, nổi bật với hương thơm hoa cỏ tự nhiên và vị ngọt đậm đà, được ví như \"hương thơm khiến cả thị trấn ngưỡng mộ\". Trà được thu hoạch thủ công từ những cây trà đơn tùng cổ thụ, sau đó trải qua quá trình chế biến tỉ mỉ để giữ lại tinh túy của hương vị núi rừng.','Trà Đơn Tùng Áp Thị Hương nổi tiếng với hương thơm tinh tế của hoa nhài và hoa cúc, kết hợp với hương mật ong ngọt ngào. Khi thưởng thức, trà mang lại một vị thanh mát, nhẹ nhàng với chút đắng nhẹ ban đầu, nhanh chóng chuyển sang vị ngọt ngào với hậu vị kéo dài. Hương thơm của trà đọng lại lâu, tạo cảm giác thư giãn và sảng khoái.','Giảm căng thẳng: Hương thơm dễ chịu và vị ngọt thanh của trà giúp giải tỏa căng thẳng, thư giãn tinh thần.\nThanh lọc cơ thể: Trà Đơn Tùng Áp Thị Hương có tác dụng thanh nhiệt, giải độc, hỗ trợ cải thiện sức khỏe tổng thể.\nTăng cường sức khỏe: Trà giúp duy trì sự tỉnh táo và nâng cao năng lượng, rất phù hợp để uống vào buổi sáng hoặc khi cần sự tập trung.\nHỗ trợ tiêu hóa: Trà có khả năng hỗ trợ tiêu hóa và giúp cân bằng chức năng đường ruột.','Dùng khoảng 5-7g trà cho mỗi ấm (khoảng 200-250ml nước).\nĐổ nước nóng (khoảng 90-95°C) vào ấm và hãm trà trong 30 giây - 1 phút.\nSau đó, có thể pha thêm từ 4-5 lần nước, mỗi lần thêm nước nóng và tăng thời gian hãm để thưởng thức trọn vẹn hương vị tinh túy của trà.','/images/products/1trung_1765357813_180b65.jpg','ACTIVE','2025-12-10 09:13:57'),(5,'Đơn Tùng Dạ Lai Hương',1050000.00,'125g / hộp',3,'Núi Ô Đông, Triều Châu, Trung Quốc','Trà Đơn Tùng Dạ Lai Hương là một loại trà Ô Long đặc biệt, nổi bật với hương thơm của hoa nhài nở về đêm, thường được gọi là \"Dạ Lai Hương\". Loại trà này được thu hái vào thời điểm lý tưởng khi lá trà đạt đến độ hoàn hảo, sau đó trải qua quá trình ủ men công phu. Sản phẩm kết hợp hài hòa giữa hương hoa nhài thanh thoát và hương vị trà Ô Long đậm đà, mang đến một trải nghiệm thưởng thức trà đầy lôi cuốn.','Đơn Tùng Dạ Lai Hương có hương thơm ngọt ngào, quyến rũ của hoa nhài về đêm, hòa quyện cùng vị trà đậm đà và một chút hậu vị ngọt dịu. Khi thưởng thức, bạn sẽ cảm nhận được sự thanh khiết và tinh tế của hương hoa cùng với vị trà dịu nhẹ, lưu lại trên đầu lưỡi, mang đến cảm giác thư giãn và sảng khoái.','Thư giãn tinh thần: Hương thơm của hoa nhài giúp làm dịu căng thẳng, giảm stress và mang lại sự thư thái cho tâm hồn.\nTăng cường sức khỏe: Trà chứa nhiều chất chống oxy hóa, giúp bảo vệ cơ thể khỏi các gốc tự do, cải thiện sức khỏe tim mạch và làm đẹp da.\nHỗ trợ tiêu hóa: có tác dụng hỗ trợ hệ tiêu hóa, kích thích quá trình trao đổi chất và duy trì vóc dáng.','Dùng khoảng 5-7g trà cho mỗi ấm (khoảng 200ml nước).\nĐổ nước nóng (khoảng 90-95°C) vào ấm và hãm trà trong 30 giây - 1 phút.\nCó thể pha lại 3-5 lần nước, mỗi lần thêm nước nóng và tăng thời gian hãm để thưởng thức trọn vẹn hương vị của trà.','/images/products/2mac_1766736822_08e450.jpg','ACTIVE','2025-12-26 08:17:05');
/*!40000 ALTER TABLE `sanphams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taikhoan_thanhtoan`
--

DROP TABLE IF EXISTS `taikhoan_thanhtoan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taikhoan_thanhtoan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nganHang` varchar(100) NOT NULL,
  `soTaiKhoan` varchar(50) NOT NULL,
  `chuTaiKhoan` varchar(255) NOT NULL,
  `anhQR` varchar(255) NOT NULL,
  `trangThai` enum('ACTIVE','HIDE') DEFAULT 'ACTIVE',
  `ngayTao` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taikhoan_thanhtoan`
--

LOCK TABLES `taikhoan_thanhtoan` WRITE;
/*!40000 ALTER TABLE `taikhoan_thanhtoan` DISABLE KEYS */;
INSERT INTO `taikhoan_thanhtoan` VALUES (2,'MoMo','07976755','Phonggsfh','/images/payment/qr_1767619590_minhchung20.png','ACTIVE','2026-01-05 20:26:30');
/*!40000 ALTER TABLE `taikhoan_thanhtoan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `truycap_logs`
--

DROP TABLE IF EXISTS `truycap_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `truycap_logs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ip_address` varchar(45) DEFAULT NULL,
  `visited_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `truycap_logs`
--

LOCK TABLES `truycap_logs` WRITE;
/*!40000 ALTER TABLE `truycap_logs` DISABLE KEYS */;
INSERT INTO `truycap_logs` VALUES (29,'127.0.0.1','2026-01-06 18:30:30'),(30,'127.0.0.1','2026-01-06 18:30:33'),(31,'127.0.0.1','2026-01-06 18:34:55'),(32,'127.0.0.1','2026-01-06 18:35:53'),(33,'127.0.0.1','2026-01-06 18:41:58'),(34,'127.0.0.1','2026-01-06 18:42:08'),(35,'127.0.0.1','2026-01-06 18:42:08'),(36,'127.0.0.1','2026-01-06 18:51:59'),(37,'127.0.0.1','2026-01-06 18:52:01'),(38,'127.0.0.1','2026-01-06 18:52:42'),(39,'127.0.0.1','2026-01-06 19:07:50'),(40,'127.0.0.1','2026-01-06 19:12:18'),(41,'127.0.0.1','2026-01-06 19:12:29'),(42,'127.0.0.1','2026-01-06 19:12:31'),(43,'127.0.0.1','2026-01-06 19:17:00'),(44,'127.0.0.1','2026-01-06 19:21:46'),(45,'127.0.0.1','2026-01-06 19:22:53'),(46,'127.0.0.1','2026-01-06 19:23:04'),(47,'127.0.0.1','2026-01-06 19:35:54'),(48,'127.0.0.1','2026-01-06 19:36:20'),(49,'127.0.0.1','2026-01-06 19:36:37'),(50,'127.0.0.1','2026-01-06 19:37:39'),(51,'127.0.0.1','2026-01-06 19:37:51'),(52,'127.0.0.1','2026-01-06 19:49:21'),(53,'127.0.0.1','2026-01-06 19:54:48'),(54,'127.0.0.1','2026-01-06 19:54:57'),(55,'127.0.0.1','2026-01-06 19:55:08'),(56,'127.0.0.1','2026-01-06 19:55:53'),(57,'127.0.0.1','2026-01-06 19:55:55'),(58,'127.0.0.1','2026-01-06 19:57:24'),(59,'127.0.0.1','2026-01-06 19:57:25'),(60,'127.0.0.1','2026-01-06 19:57:26'),(61,'127.0.0.1','2026-01-06 19:58:53'),(62,'127.0.0.1','2026-01-06 19:58:56'),(63,'127.0.0.1','2026-01-06 19:59:01'),(64,'127.0.0.1','2026-01-06 19:59:04'),(65,'127.0.0.1','2026-01-06 19:59:06'),(66,'127.0.0.1','2026-01-06 19:59:07'),(67,'127.0.0.1','2026-01-06 19:59:09'),(68,'127.0.0.1','2026-01-06 19:59:11'),(69,'127.0.0.1','2026-01-06 20:00:11'),(70,'127.0.0.1','2026-01-06 20:06:46'),(71,'127.0.0.1','2026-01-06 20:06:54'),(72,'127.0.0.1','2026-01-06 20:06:57'),(73,'127.0.0.1','2026-01-06 20:07:00'),(74,'127.0.0.1','2026-01-06 20:07:04'),(75,'127.0.0.1','2026-01-06 20:07:06'),(76,'127.0.0.1','2026-01-06 20:11:17'),(77,'127.0.0.1','2026-01-06 20:11:29'),(78,'127.0.0.1','2026-01-06 20:16:12'),(79,'127.0.0.1','2026-01-06 20:23:05'),(80,'127.0.0.1','2026-01-06 20:23:08'),(81,'127.0.0.1','2026-01-06 20:23:11'),(82,'127.0.0.1','2026-01-06 20:23:17'),(83,'127.0.0.1','2026-01-06 20:23:23'),(84,'127.0.0.1','2026-01-06 20:23:57'),(85,'127.0.0.1','2026-01-06 20:23:59'),(86,'127.0.0.1','2026-01-06 20:24:02'),(87,'127.0.0.1','2026-01-06 20:24:03'),(88,'127.0.0.1','2026-01-06 20:24:05'),(89,'127.0.0.1','2026-01-06 20:24:08'),(90,'127.0.0.1','2026-01-06 20:24:10'),(91,'127.0.0.1','2026-01-06 20:24:12'),(92,'127.0.0.1','2026-01-06 20:24:47');
/*!40000 ALTER TABLE `truycap_logs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-06 20:27:03
