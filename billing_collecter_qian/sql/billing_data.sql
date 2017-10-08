-- MySQL dump 10.14  Distrib 5.5.44-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: billing
-- ------------------------------------------------------
-- Server version	5.5.44-MariaDB-log

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
-- Table structure for table `account`
--
drop  database billing;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`billing` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

use billing;

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account` (
  `account_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `username` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `cash_balance` decimal(8,2) DEFAULT NULL,
  `gift_balance` decimal(8,2) DEFAULT NULL,
  `type` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `credit_line` decimal(8,2) DEFAULT NULL,
  `status` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`account_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='账户';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES ('account_888','account_888',1888.88,888.88,'credt',NULL,'normal','2015-09-07 22:32:47',NULL);
INSERT INTO `account` VALUES ('account_999','username_999',1999.00,999.00,'credt',NULL,'normal','2015-09-07 22:34:06',NULL);
INSERT INTO `account` VALUES ('account_777','acount_888',169.84,100.04,'credit',2000.00,'normal','2015-09-08 06:33:13','2015-08-24 18:23:10');
INSERT INTO `account` VALUES ('user_id_2222','user_id_222',200.35,100.04,'credt',NULL,'normal','2015-09-07 21:16:44',NULL);
INSERT INTO `account` VALUES ('have_no_discount','have_not_discount',200.35,100.04,'credt',NULL,'normal','2015-09-07 21:16:44',NULL);
INSERT INTO `account` VALUES ('count_id_1111','bao',1170.13,5600.67,'credit',5000.00,'deleted','2015-09-08 03:20:05','2015-08-25 02:37:59');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `address` (
  `address_id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `post_code` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mobile` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`address_id`),
  KEY `FK_fk_address_account_id` (`account_id`),
  CONSTRAINT `FK_fk_address_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`account_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='鍦板潃';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bill` (
  `bill_id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `no` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  `started_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `ended_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `amount` decimal(8,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`bill_id`),
  KEY `FK_fk_bill_account_id` (`account_id`),
  CONSTRAINT `FK_fk_bill_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='璐﹀崟';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1,'count_id_1111','1213213','2015-02-28 16:00:00','2015-03-31 15:59:59',1045.89,'2015-08-20 19:30:26');
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_item`
--

DROP TABLE IF EXISTS `bill_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bill_item` (
  `bill_item_id` int(11) NOT NULL AUTO_INCREMENT,
  `bill_id` int(11) NOT NULL,
  `resource_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `region_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `type` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `started_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `ended_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `amount` decimal(8,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`bill_item_id`),
  KEY `FK_fk_bill_detail_bill_id` (`bill_id`),
  CONSTRAINT `FK_fk_bill_detail_bill_id` FOREIGN KEY (`bill_id`) REFERENCES `bill` (`bill_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='璐﹀崟瀛愰」';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_item`
--

LOCK TABLES `bill_item` WRITE;
/*!40000 ALTER TABLE `bill_item` DISABLE KEYS */;
INSERT INTO `bill_item` VALUES (1,1,'asdada','region1','instance','2015-07-31 16:00:00','2015-08-31 15:59:59',154.25,'2015-08-25 18:13:14');
/*!40000 ALTER TABLE `bill_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `billing_item`
--

DROP TABLE IF EXISTS `billing_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `billing_item` (
  `billing_item_id` int(11) NOT NULL AUTO_INCREMENT,
  `region_id` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `billing_item` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `unit` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` decimal(10,4) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`billing_item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='计费项';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billing_item`
--

LOCK TABLES `billing_item` WRITE;
/*!40000 ALTER TABLE `billing_item` DISABLE KEYS */;
INSERT INTO `billing_item` VALUES (1,'region1','instance_1','yuan/hour',0.1234,'2015-08-25 18:04:35',NULL);
INSERT INTO `billing_item` VALUES (2,'region1','cpu_1_core','yuan/core.hour',0.2345,'2015-08-25 17:27:58',NULL);
INSERT INTO `billing_item` VALUES (3,'region1','memory_1024_M','yuan/1024M.hour',0.7894,'2015-08-25 18:17:16',NULL);
INSERT INTO `billing_item` VALUES (4,'region1','systemdisk_1_G','yuan/G.hour',0.4567,'2015-08-25 18:04:12',NULL);
INSERT INTO `billing_item` VALUES (5,'region1','clouddisk_1_G','yuan/G.hour',0.7894,'2015-08-25 18:04:25',NULL);
INSERT INTO `billing_item` VALUES (6,'region1','snapshotdisk_1_G','yuan/G.hour',0.4568,'2015-08-25 18:05:32',NULL);
INSERT INTO `billing_item` VALUES (7,'region1','route_1','yuan/hour',0.2345,'2015-08-25 18:06:12',NULL);
INSERT INTO `billing_item` VALUES (8,'region1','ip_1','yuan/hour',0.1234,'2015-08-25 18:06:36',NULL);
INSERT INTO `billing_item` VALUES (9,'region1','bandwidth_1_M','yuan/M.hour',0.9999,'2015-08-25 18:07:26',NULL);
INSERT INTO `billing_item` VALUES (10,'region1','cdnflow_1_G','yuan/G.month',100.1234,'2015-08-25 18:09:07',NULL);
INSERT INTO `billing_item` VALUES (11,'region1','cdnbandwidth_1_M','yuan/M.month',98.2500,'2015-08-25 18:10:01',NULL);
INSERT INTO `billing_item` VALUES (12,'region1','vpn_1','yuan/hour','0.3400','2015-09-02 19:38:56',NULL);
/*!40000 ALTER TABLE `billing_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consumption`
--

DROP TABLE IF EXISTS `consumption`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `consumption` (
  `consumption_id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `amount` decimal(8,2) NOT NULL,
  `billing_item` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sum` int(5) DEFAULT NULL,
  `price` decimal(10,4) DEFAULT NULL,
  `unit` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `discount_ratio` decimal(3,2) DEFAULT NULL,
  `resource_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `resource_name` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `parent_id` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `region_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `discounted_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `discount_by` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `resource_type` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`consumption_id`),
  KEY `FK_fk_consumption_account_id` (`account_id`),
  CONSTRAINT `FK_fk_consumption_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='娑堣垂';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consumption`
--

LOCK TABLES `consumption` WRITE;
/*!40000 ALTER TABLE `consumption` DISABLE KEYS */;
INSERT INTO `consumption` VALUES (1,'asdasjdjajsdjsajdj',100.00,NULL,NULL,NULL,NULL,NULL,'1','instance1',NULL,'region1','2015-08-24 23:20:56',NULL,'');
INSERT INTO `consumption` VALUES (2,'asdasjdjajsdjsajdj',200.00,NULL,NULL,NULL,NULL,NULL,'2','instance2',NULL,'region1','2015-08-24 23:25:56',NULL,'');
INSERT INTO `consumption` VALUES (3,'asdasjdjajsdjsajdj',100.00,NULL,NULL,NULL,NULL,NULL,'1','instance1',NULL,'region1','2015-08-24 23:27:33',NULL,'');
/*!40000 ALTER TABLE `consumption` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discount`
--

DROP TABLE IF EXISTS `discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discount` (
  `discount_id` int(11) NOT NULL AUTO_INCREMENT,
  `billing_item_id` int(11) DEFAULT NULL,
  `account_id` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `discount_ratio` decimal(3,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`discount_id`),
  KEY `FK_fk_discount_account_id` (`account_id`),
  KEY `FK_fk_discount_billing_item_id` (`billing_item_id`),
  CONSTRAINT `FK_fk_discount_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`account_id`),
  CONSTRAINT `FK_fk_discount_billing_item_id` FOREIGN KEY (`billing_item_id`) REFERENCES `billing_item` (`billing_item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=223 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='折扣';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount`
--

LOCK TABLES `discount` WRITE;
/*!40000 ALTER TABLE `discount` DISABLE KEYS */;
INSERT INTO `discount` VALUES (1,1,'count_id_1111',0.111,'2015-08-25 18:11:34',NULL);
INSERT INTO `discount` VALUES (2,1,'account_888',0.88,'2015-08-25 18:11:34',NULL);
INSERT INTO `discount` VALUES (3,1,'account_999',0.99,'2015-08-25 18:11:34',NULL);
INSERT INTO `discount` VALUES (4,1,'user_id_2222',0.22,'2015-09-08 05:35:30',NULL);
/*!40000 ALTER TABLE `discount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `invoice` (
  `invoice_id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `address_id` int(11) DEFAULT NULL,
  `type` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tiltle` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `amount` decimal(8,2) DEFAULT NULL,
  `prove` varchar(256) COLLATE utf8_unicode_ci DEFAULT NULL,
  `apply_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `post_by` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `express_no` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`invoice_id`),
  KEY `FK_fk_invoice_account_id` (`account_id`),
  KEY `FK_fk_invoice_address_id` (`address_id`),
  CONSTRAINT `FK_fk_invoice_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`account_id`),
  CONSTRAINT `FK_fk_invoice_address_id` FOREIGN KEY (`address_id`) REFERENCES `address` (`address_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='鍙戠エ';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice`
--

LOCK TABLES `invoice` WRITE;
/*!40000 ALTER TABLE `invoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `invoice` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-08 14:36:00
