-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: employee
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `user_id` int NOT NULL,
  `username` varchar(45) NOT NULL,
  `email` varchar(255) NOT NULL,
  `age` int NOT NULL,
  `gender` varchar(10) NOT NULL,
  `phoneNo` varchar(128) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `address_id` bigint NOT NULL,
  `id` bigint NOT NULL,
  `qualifications_id` bigint NOT NULL,
  `workExperience_id` bigint NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `address_id` (`address_id`),
  UNIQUE KEY `qualifications_id` (`qualifications_id`),
  UNIQUE KEY `workExperience_id` (`workExperience_id`),
  KEY `employee_id_0b8b667e_fk_project_id` (`id`),
  CONSTRAINT `employee_address_id_ec265512_fk_address_id` FOREIGN KEY (`address_id`) REFERENCES `address` (`id`),
  CONSTRAINT `employee_id_0b8b667e_fk_project_id` FOREIGN KEY (`id`) REFERENCES `project` (`id`),
  CONSTRAINT `employee_qualifications_id_37b663c5_fk_qualification_id` FOREIGN KEY (`qualifications_id`) REFERENCES `qualification` (`id`),
  CONSTRAINT `employee_user_id_cc4f5a1c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `employee_workExperience_id_fc940f10_fk_work_experience_id` FOREIGN KEY (`workExperience_id`) REFERENCES `work_experience` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (6,'Prasanth','prasanthkumar.jeeru10@gmail.com',28,'Male','7680026148','Users/blank_profile.webp',9,6,6,6),(7,'sasikala','sashipemmanaboidi@gmail.com',25,'Female','8688145688','Users/sasikala/photo.jpeg',10,7,7,7),(8,'Ramu','ramudadi404@gmail.com',31,'Male','9978997534','Users/Ramu/image.jpg',11,8,8,8);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-09 15:01:28
