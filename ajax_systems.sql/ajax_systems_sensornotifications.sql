-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: ajax_systems
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `sensornotifications`
--

DROP TABLE IF EXISTS `sensornotifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sensornotifications` (
  `id` int NOT NULL,
  `notification_id` int DEFAULT NULL,
  `status` enum('надіслано','не вдалося надіслати') NOT NULL,
  `timestamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `FK_sensorNotifications_notification` (`notification_id`),
  CONSTRAINT `FK_sensorNotifications_notification` FOREIGN KEY (`notification_id`) REFERENCES `notifications` (`notification_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensornotifications`
--

LOCK TABLES `sensornotifications` WRITE;
/*!40000 ALTER TABLE `sensornotifications` DISABLE KEYS */;
INSERT INTO `sensornotifications` VALUES (10,1,'надіслано','2024-11-24 14:42:14'),(11,2,'надіслано','2024-11-24 14:42:14'),(12,3,'не вдалося надіслати','2024-11-24 14:42:14'),(13,4,'надіслано','2024-11-24 14:42:14'),(14,5,'не вдалося надіслати','2024-11-24 14:42:14'),(15,6,'надіслано','2024-11-24 14:42:14'),(16,7,'надіслано','2024-11-24 14:42:14'),(17,8,'надіслано','2024-11-24 14:42:14'),(18,9,'надіслано','2024-11-24 14:42:14'),(19,10,'не вдалося надіслати','2024-11-24 14:42:14'),(20,11,'надіслано','2024-11-24 14:42:14');
/*!40000 ALTER TABLE `sensornotifications` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-06  1:27:44
