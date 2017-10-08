/*
SQLyog Community v8.4 
MySQL - 5.5.41-MariaDB : Database - using
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`using` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

USE `using`;

/*Table structure for table `billing_resource` */

DROP TABLE IF EXISTS `billing_resource`;

CREATE TABLE `billing_resource` (
  `resource_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `resource_name` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `billing_item` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `region_id` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sum` int(5) NOT NULL,
  `parent_id` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `account_id` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `resource_type` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`resource_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='璁¤垂璧勬簮';

/*Table structure for table `using` */

DROP TABLE IF EXISTS `using`;

CREATE TABLE `using` (
  `using_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `resource_id` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `started_at` timestamp NULL DEFAULT NULL,
  `ended_st` timestamp NULL DEFAULT NULL,
  `tran_status` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`using_id`),
  KEY `FK_fk_resource_use_resource_id` (`resource_id`),
  CONSTRAINT `FK_fk_resource_use_resource_id` FOREIGN KEY (`resource_id`) REFERENCES `billing_resource` (`resource_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='璧勬簮浣跨敤';

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
