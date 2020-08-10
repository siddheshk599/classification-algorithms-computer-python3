-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: dataMining
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

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
-- Current Database: `dataMining`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `dataMining` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `dataMining`;

--
-- Table structure for table `id3Data`
--

DROP TABLE IF EXISTS `id3Data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `id3Data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `outlook` varchar(10) NOT NULL,
  `temperature` varchar(5) NOT NULL,
  `humidity` varchar(7) NOT NULL,
  `windy` varchar(7) NOT NULL,
  `play` varchar(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `id3Data`
--

LOCK TABLES `id3Data` WRITE;
/*!40000 ALTER TABLE `id3Data` DISABLE KEYS */;
INSERT INTO `id3Data` VALUES (1,'sunny','hot','high','false','N'),(2,'sunny','hot','high','true','N'),(3,'overcast','hot','high','false','P'),(4,'rain','mild','high','false','P'),(5,'rain','cool','normal','false','P'),(6,'rain','cool','normal','true','N'),(7,'overcast','cool','normal','true','P'),(8,'sunny','mild','high','false','N'),(9,'sunny','cool','normal','false','P'),(10,'rain','mild','normal','false','P'),(11,'overcast','hot','normal','false','P'),(12,'sunny','mild','normal','true','P'),(13,'overcast','mild','high','true','P'),(14,'rain','mild','high','true','N');
/*!40000 ALTER TABLE `id3Data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `naiveBayesData`
--

DROP TABLE IF EXISTS `naiveBayesData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `naiveBayesData` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `age` varchar(15) NOT NULL,
  `income` varchar(8) NOT NULL,
  `employee` varchar(4) NOT NULL,
  `credit_rating` varchar(10) NOT NULL,
  `buys_car` varchar(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `naiveBayesData`
--

LOCK TABLES `naiveBayesData` WRITE;
/*!40000 ALTER TABLE `naiveBayesData` DISABLE KEYS */;
INSERT INTO `naiveBayesData` VALUES (1,'youth','high','no','fair','no'),(2,'youth','high','no','excellent','no'),(3,'middle_aged','high','no','fair','yes'),(4,'senior','medium','no','fair','yes'),(5,'senior','low','yes','fair','yes'),(6,'senior','low','yes','excellent','no'),(7,'middle_aged','low','yes','excellent','yes'),(8,'youth','medium','no','fair','no'),(9,'youth','low','yes','fair','yes'),(10,'senior','medium','yes','fair','yes'),(11,'youth','medium','yes','excellent','yes'),(12,'middle_aged','medium','no','excellent','yes'),(13,'middle_aged','high','yes','fair','yes'),(14,'senior','medium','no','excellent','no');
/*!40000 ALTER TABLE `naiveBayesData` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-10 13:48:01
