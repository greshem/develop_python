use cdn;

CREATE TABLE `cdn_flows` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `domain_id` varchar(64) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `flows` decimal(8,2) NOT NULL DEFAULT '0.00',
  `date` char(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=174 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
