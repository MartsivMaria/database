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
-- Table structure for table `sensor_notification`
--

DROP TABLE IF EXISTS `sensor_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sensor_notification` (
  `sensor_id` int NOT NULL,
  `notification_id` int NOT NULL,
  `event_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`sensor_id`,`notification_id`),
  KEY `notification_id` (`notification_id`),
  CONSTRAINT `sensor_notification_ibfk_1` FOREIGN KEY (`sensor_id`) REFERENCES `sensors` (`sensor_id`) ON DELETE CASCADE,
  CONSTRAINT `sensor_notification_ibfk_2` FOREIGN KEY (`notification_id`) REFERENCES `notifications` (`notification_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor_notification`
--

LOCK TABLES `sensor_notification` WRITE;
/*!40000 ALTER TABLE `sensor_notification` DISABLE KEYS */;
INSERT INTO `sensor_notification` VALUES (11,1,'2024-11-24 12:42:14'),(11,2,'2024-11-24 12:42:14'),(11,6,'2024-11-28 06:29:19'),(12,4,'2024-11-28 06:03:11'),(13,2,'2024-11-24 12:42:14'),(13,3,'2024-11-24 12:42:14'),(15,3,'2024-11-24 12:42:14'),(15,5,'2024-11-24 12:42:14'),(18,3,'2024-11-24 12:42:14'),(18,6,'2024-11-24 12:42:14'),(19,1,'2024-11-24 12:42:14'),(21,5,'2024-11-24 12:42:14'),(21,10,'2024-11-24 12:42:14');
/*!40000 ALTER TABLE `sensor_notification` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-06  1:27:41
