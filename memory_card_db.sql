/*
Navicat MySQL Data Transfer

Source Server         : 111
Source Server Version : 50725
Source Host           : localhost:3306
Source Database       : memory_card_db

Target Server Type    : MYSQL
Target Server Version : 50725
File Encoding         : 65001

Date: 2019-05-16 20:34:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for card
-- ----------------------------
DROP TABLE IF EXISTS `card`;
CREATE TABLE `card` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `card_name` varchar(30) NOT NULL DEFAULT '' COMMENT '卡片名字',
  `card_content` varchar(1000) NOT NULL DEFAULT '' COMMENT '卡片内容',
  `study_status` tinyint(2) NOT NULL DEFAULT '0' COMMENT '复习状态 已复习一次：1，以此类推',
  `status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '状态 0 未归档 1 已归档',
  `last_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  `fromid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COMMENT='卡片表';

-- ----------------------------
-- Table structure for images
-- ----------------------------
DROP TABLE IF EXISTS `images`;
CREATE TABLE `images` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `file_key` varchar(100) NOT NULL DEFAULT '' COMMENT '文件名',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for member
-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nickname` varchar(100) NOT NULL DEFAULT '' COMMENT '会员名',
  `mobile` varchar(11) NOT NULL DEFAULT '' COMMENT '会员手机号码',
  `sex` tinyint(1) NOT NULL DEFAULT '0' COMMENT '性别 1：男 2：女',
  `avatar` varchar(200) NOT NULL DEFAULT '' COMMENT '会员头像',
  `salt` varchar(32) NOT NULL DEFAULT '' COMMENT '随机salt',
  `reg_ip` varchar(100) NOT NULL DEFAULT '' COMMENT '注册ip',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态 1：有效 0：无效',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COMMENT='会员表';

-- ----------------------------
-- Table structure for oauth_access_token
-- ----------------------------
DROP TABLE IF EXISTS `oauth_access_token`;
CREATE TABLE `oauth_access_token` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `access_token` varchar(600) NOT NULL DEFAULT '',
  `expired_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '过期时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_expired_time` (`expired_time`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='微信的access_token 用户调用其他接口的';

-- ----------------------------
-- Table structure for oauth_member_bind
-- ----------------------------
DROP TABLE IF EXISTS `oauth_member_bind`;
CREATE TABLE `oauth_member_bind` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `client_type` varchar(20) NOT NULL DEFAULT '' COMMENT '客户端来源类型。qq,weibo,weixin',
  `type` tinyint(3) NOT NULL DEFAULT '0' COMMENT '类型 type 1:wechat ',
  `openid` varchar(80) NOT NULL DEFAULT '' COMMENT '第三方id',
  `unionid` varchar(100) NOT NULL DEFAULT '',
  `extra` text NOT NULL COMMENT '额外字段',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_type_openid` (`type`,`openid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COMMENT='第三方登录绑定关系';

-- ----------------------------
-- Table structure for queue_list
-- ----------------------------
DROP TABLE IF EXISTS `queue_list`;
CREATE TABLE `queue_list` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `queue_name` varchar(30) NOT NULL DEFAULT '' COMMENT '队列名字',
  `next_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '下一次复习时间',
  `status` tinyint(1) NOT NULL DEFAULT '-1' COMMENT '状态 -1 待处理 1 已处理',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COMMENT='事件队列表';
