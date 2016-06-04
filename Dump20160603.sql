CREATE DATABASE  IF NOT EXISTS `traveldb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `travelDB`;
-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: localhost    Database: travelDB
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `trips`
--

DROP TABLE IF EXISTS `trips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trips` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `trvlPlan_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_trips_users_idx` (`user_id`),
  KEY `fk_trips_trvlPlans1_idx` (`trvlPlan_id`),
  CONSTRAINT `fk_trips_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_trips_trvlPlans1` FOREIGN KEY (`trvlPlan_id`) REFERENCES `trvlPlans` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trips`
--

LOCK TABLES `trips` WRITE;
/*!40000 ALTER TABLE `trips` DISABLE KEYS */;
INSERT INTO `trips` VALUES (1,3,1),(2,3,4),(3,1,4);
/*!40000 ALTER TABLE `trips` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trvlPlans`
--

DROP TABLE IF EXISTS `trvlPlans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trvlPlans` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `destination` varchar(255) DEFAULT NULL,
  `plan` varchar(255) DEFAULT NULL,
  `trvlStartDate` date DEFAULT NULL,
  `trvlEndDate` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_trvlPlans_users1_idx` (`user_id`),
  CONSTRAINT `fk_trvlPlans_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trvlPlans`
--

LOCK TABLES `trvlPlans` WRITE;
/*!40000 ALTER TABLE `trvlPlans` DISABLE KEYS */;
INSERT INTO `trvlPlans` VALUES (1,'Minneapolis, MN','Visit Mall of America - Nickelodeon World','2016-07-01','2016-07-10','2016-06-03 15:26:33',4),(2,'Nepal','Lake Mansarovar','2016-10-18','2016-10-30','2016-06-03 15:27:13',1),(3,'Tokyo, Japan','Olympics','2020-06-20','2020-06-30','2016-06-03 15:27:53',2),(4,'LA, CA','Universal Studio - Harry Potter World','2016-08-10','2016-08-15','2016-06-03 15:28:25',3);
/*!40000 ALTER TABLE `trvlPlans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Meena Kamran','Meena','$2b$12$sMmlvFGOM./jQH73556Coer2.m4UCAVQZy2G2C1lv9BxqMtSqlOF6','2016-06-03 15:23:49'),(2,'Radhika Kamran','Radz','$2b$12$xbcYjtM4MteG1.0IdHn.NeT93symkOaSQWUuglDWTNr/B2a2mEuCG','2016-06-03 15:24:08'),(3,'Anjali K','Vani','$2b$12$nbQdRHPlucQBlmz14EQ8hetcagEB0agNs9AHoZTxlxG3sP4ZmSZgu','2016-06-03 15:24:41'),(4,'Kapil K','Kai','$2b$12$ha10TB7vGmmD3AwGeHTW1eWif88YPhGGnKUJUS9weNdVrUaSETR2W','2016-06-03 15:25:10');
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

-- Dump completed on 2016-06-03 16:56:51
