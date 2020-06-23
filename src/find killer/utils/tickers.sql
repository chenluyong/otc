/*
Navicat MySQL Data Transfer

Source Server         : 公信宝节点
Source Server Version : 50724
Source Host           : 47.96.171.142:3306
Source Database       : echain

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2020-06-22 23:28:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tickers
-- ----------------------------
DROP TABLE IF EXISTS `tickers`;
CREATE TABLE `tickers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `base` varchar(64) DEFAULT NULL,
  `currency` varchar(64) DEFAULT NULL,
  `symbol` varchar(64) DEFAULT NULL,
  `high_price` varchar(64) DEFAULT NULL,
  `low_price` varchar(64) DEFAULT NULL,
  `open_price` varchar(64) DEFAULT NULL,
  `close_price` varchar(64) DEFAULT NULL,
  `exchange_name` varchar(64) DEFAULT NULL,
  `update_time` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `symbol` (`symbol`,`exchange_name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4;
