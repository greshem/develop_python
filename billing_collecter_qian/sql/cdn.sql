-- MySQL dump 10.14  Distrib 5.5.44-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: cdn
-- ------------------------------------------------------
-- Server version	5.5.44-MariaDB

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
-- Table structure for table `cdn_cache_refresh_cacherule`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/`cdn` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

use cdn;
DROP TABLE IF EXISTS `cdn_cache_refresh_cacherule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cdn_cache_refresh_cacherule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cache_type` varchar(64) NOT NULL,
  `cache_time` int(11) NOT NULL,
  `status` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cdn_cache_refresh_cacherule`
--

LOCK TABLES `cdn_cache_refresh_cacherule` WRITE;
/*!40000 ALTER TABLE `cdn_cache_refresh_cacherule` DISABLE KEYS */;
/*!40000 ALTER TABLE `cdn_cache_refresh_cacherule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cdn_domain_manager_accesscontrol`
--

DROP TABLE IF EXISTS `cdn_domain_manager_accesscontrol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cdn_domain_manager_accesscontrol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain_id` int(11) NOT NULL,
  `pathPattern` varchar(64) NOT NULL,
  `allowNullReffer` tinyint(1) NOT NULL,
  `validRefers` varchar(128) NOT NULL,
  `invalidRefers` varchar(128) NOT NULL,
  `forbiddenIps` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cdn_domain_manager_accesscontrol_e8b327e7` (`domain_id`),
  CONSTRAINT `domain_id_refs_id_f0114c65` FOREIGN KEY (`domain_id`) REFERENCES `cdn_domain_manager_domain` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cdn_domain_manager_accesscontrol`
--

LOCK TABLES `cdn_domain_manager_accesscontrol` WRITE;
/*!40000 ALTER TABLE `cdn_domain_manager_accesscontrol` DISABLE KEYS */;
/*!40000 ALTER TABLE `cdn_domain_manager_accesscontrol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cdn_domain_manager_cacherule`
--

DROP TABLE IF EXISTS `cdn_domain_manager_cacherule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cdn_domain_manager_cacherule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain_id` int(11) NOT NULL,
  `pathPattern` varchar(64) NOT NULL,
  `ignoreCacheControl` tinyint(1) NOT NULL,
  `cacheTtl` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cdn_domain_manager_cacherule_e8b327e7` (`domain_id`),
  CONSTRAINT `domain_id_refs_id_8967b4d0` FOREIGN KEY (`domain_id`) REFERENCES `cdn_domain_manager_domain` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cdn_domain_manager_cacherule`
--

LOCK TABLES `cdn_domain_manager_cacherule` WRITE;
/*!40000 ALTER TABLE `cdn_domain_manager_cacherule` DISABLE KEYS */;
/*!40000 ALTER TABLE `cdn_domain_manager_cacherule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cdn_domain_manager_domain`
--

DROP TABLE IF EXISTS `cdn_domain_manager_domain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cdn_domain_manager_domain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tenant_id` varchar(64) NOT NULL,
  `domain_id` varchar(64) DEFAULT NULL,
  `domain_name` varchar(64) NOT NULL,
  `domain_cname` varchar(64) DEFAULT NULL,
  `create_time` date NOT NULL,
  `source_type` varchar(10) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `Enable` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cdn_domain_manager_domain`
--

LOCK TABLES `cdn_domain_manager_domain` WRITE;
/*!40000 ALTER TABLE `cdn_domain_manager_domain` DISABLE KEYS */;
INSERT INTO `cdn_domain_manager_domain` VALUES (1,'f3773d5249864d358e0b40fec6566228','219151','images.mtgcr7.cn','mfgo5aukwipygp.wscloudcdn.com','2015-08-07','ip','Deployed','True'),(2,'f3773d5249864d358e0b40fec6566228','1228328','downloads.phoneunet.com','hjdbh1802goaxl.wscloudcdn.com','2015-08-19','ip','Deployed','True'),(3,'6b31ba9a345e40a3a16a3e9fde98450b',NULL,'www.baidu.com','-','2015-09-01','ip','unverified','');
/*!40000 ALTER TABLE `cdn_domain_manager_domain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cdn_domain_manager_sourceaddress`
--

DROP TABLE IF EXISTS `cdn_domain_manager_sourceaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cdn_domain_manager_sourceaddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain_id` int(11) NOT NULL,
  `source_address` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cdn_domain_manager_sourceaddress_e8b327e7` (`domain_id`),
  CONSTRAINT `domain_id_refs_id_3d251825` FOREIGN KEY (`domain_id`) REFERENCES `cdn_domain_manager_domain` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cdn_domain_manager_sourceaddress`
--

LOCK TABLES `cdn_domain_manager_sourceaddress` WRITE;
/*!40000 ALTER TABLE `cdn_domain_manager_sourceaddress` DISABLE KEYS */;
INSERT INTO `cdn_domain_manager_sourceaddress` VALUES (1,3,'192.168.100.50');
/*!40000 ALTER TABLE `cdn_domain_manager_sourceaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-06 16:13:47
