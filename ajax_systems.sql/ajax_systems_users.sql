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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL,
  `access_id` int DEFAULT NULL,
  `username` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`),
  KEY `FK_users_access_levels` (`access_id`),
  CONSTRAINT `FK_users_access_levels` FOREIGN KEY (`access_id`) REFERENCES `access_levels` (`access_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,1,'john_doe','john@example.com'),(2,2,'jane_smith','jane@example.com'),(3,3,'olga_shevchenko','shevchenko@example.com'),(4,4,'serhii_dmytrenko','dmytrenko@example.com'),(5,5,'olivia_smith','olivia@example.com'),(6,6,'michael_jones','michael@example.com'),(7,7,'sophia_brown','sophia@example.com'),(8,8,'ivan_petrov','ivan@example.com'),(9,9,'kateryna_ivanova','ivanova@example.com'),(10,10,'andrii_koval','andrii@example.com'),(11,11,'nataliia_stepanov','natalia@example.com'),(12,1,'john_smith','smith@example.com'),(13,2,'olivia_doe','doe@example.com'),(31,3,'jane','brown@example.com'),(32,1,'Noname1','noname1@example.com'),(33,1,'Noname2','noname2@example.com'),(34,1,'Noname3','noname3@example.com'),(35,1,'Noname4','noname4@example.com'),(36,1,'Noname5','noname5@example.com'),(37,1,'Noname6','noname6@example.com'),(38,1,'Noname7','noname7@example.com'),(39,1,'Noname8','noname8@example.com'),(40,1,'Noname9','noname9@example.com'),(41,1,'Noname10','noname10@example.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-06  1:27:42
