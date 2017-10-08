/*
SQLyog Community v8.4 
MySQL - 5.5.41-MariaDB : Database - billing
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`billing` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

USE `billing`;

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

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

/*Table structure for table `address` */

DROP TABLE IF EXISTS `address`;

CREATE TABLE `address` (
  `address_id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `post_code` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `mobile` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `status` varchar(32) COLLATE utf8_unicode_ci DEFAULT 'using',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`address_id`),
  KEY `FK_fk_address_account_id` (`account_id`),
  CONSTRAINT `FK_fk_address_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='鍦板潃';

/*Table structure for table `bill` */

DROP TABLE IF EXISTS `bill`;

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='璐﹀崟';

/*Table structure for table `bill_item` */

DROP TABLE IF EXISTS `bill_item`;

CREATE TABLE `bill_item` (
  `bill_item_id` int(11) NOT NULL AUTO_INCREMENT,
  `bill_id` int(11) NOT NULL,
  `resource_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `region_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `resource_type` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `started_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `ended_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `amount` decimal(8,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `resource_name` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`bill_item_id`),
  KEY `FK_fk_bill_detail_bill_id` (`bill_id`),
  CONSTRAINT `FK_fk_bill_detail_bill_id` FOREIGN KEY (`bill_id`) REFERENCES `bill` (`bill_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='璐﹀崟瀛愰」';

/*Table structure for table `billing_item` */

DROP TABLE IF EXISTS `billing_item`;

CREATE TABLE `billing_item` (
  `billing_item_id` int(11) NOT NULL AUTO_INCREMENT,
  `region_id` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `billing_item` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `unit` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` decimal(10,4) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`billing_item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='计费项';

/*Table structure for table `consumption` */

DROP TABLE IF EXISTS `consumption`;

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
  `start` timestamp NULL DEFAULT NULL,
  `end` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`consumption_id`),
  KEY `FK_fk_consumption_account_id` (`account_id`),
  CONSTRAINT `FK_fk_consumption_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='娑堣垂';

/*Table structure for table `discount` */

DROP TABLE IF EXISTS `discount`;

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
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='折扣';

/*Table structure for table `invoice` */

DROP TABLE IF EXISTS `invoice`;

CREATE TABLE `invoice` (
  `invoice_id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `address_id` int(11) DEFAULT NULL,
  `type` varchar(32) COLLATE utf8_unicode_ci DEFAULT NULL,
  `title` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='鍙戠エ';

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
