-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: ehremployee
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add employee attachment slim log',7,'add_employeeattachmentslimlog'),(20,'Can change employee attachment slim log',7,'change_employeeattachmentslimlog'),(21,'Can delete employee attachment slim log',7,'delete_employeeattachmentslimlog'),(22,'Can add employee attachment',8,'add_employeeattachment'),(23,'Can change employee attachment',8,'change_employeeattachment'),(24,'Can delete employee attachment',8,'delete_employeeattachment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'imageslim','employeeattachment'),(7,'imageslim','employeeattachmentslimlog'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
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
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-10-27 03:11:24.966394'),(2,'auth','0001_initial','2017-10-27 03:11:26.633784'),(3,'admin','0001_initial','2017-10-27 03:11:27.020039'),(4,'admin','0002_logentry_remove_auto_add','2017-10-27 03:11:27.063757'),(5,'contenttypes','0002_remove_content_type_name','2017-10-27 03:11:27.236046'),(6,'auth','0002_alter_permission_name_max_length','2017-10-27 03:11:27.331706'),(7,'auth','0003_alter_user_email_max_length','2017-10-27 03:11:27.428005'),(8,'auth','0004_alter_user_username_opts','2017-10-27 03:11:27.459358'),(9,'auth','0005_alter_user_last_login_null','2017-10-27 03:11:27.554528'),(10,'auth','0006_require_contenttypes_0002','2017-10-27 03:11:27.558101'),(11,'auth','0007_alter_validators_add_error_messages','2017-10-27 03:11:27.588524'),(12,'auth','0008_alter_user_username_max_length','2017-10-27 03:11:27.736313'),(13,'imageslim','0001_initial','2017-10-27 03:11:27.978835'),(14,'sessions','0001_initial','2017-10-27 03:11:28.033331'),(15,'imageslim','0002_auto_20171031_1012','2017-10-31 10:13:15.798862');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imageslim_employeeattachment`
--

DROP TABLE IF EXISTS `imageslim_employeeattachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `imageslim_employeeattachment` (
  `c_id` char(32) NOT NULL,
  `c_employee_id` varchar(100) NOT NULL,
  `c_company_id` varchar(500) DEFAULT NULL,
  `c_attachment_type` int(11) NOT NULL,
  `c_attachment_url` varchar(500) DEFAULT NULL,
  `c_add_by` varchar(100) DEFAULT NULL,
  `c_add_dt` datetime(6) NOT NULL,
  `c_update_by` varchar(300) DEFAULT NULL,
  `c_update_dt` datetime(6) DEFAULT NULL,
  `c_sort` int(11) NOT NULL,
  `c_filename` varchar(50) DEFAULT NULL,
  `c_filename_ext` varchar(10) DEFAULT NULL,
  `c_file_size` int(11) DEFAULT NULL,
  `c_is_delete` tinyint(1) NOT NULL,
  `c_is_slimed` tinyint(1) NOT NULL,
  `c_view_name` varchar(200) DEFAULT NULL,
  `c_upload_by` char(32) NOT NULL,
  `c_upload_by_name` varchar(30) NOT NULL,
  `c_upload_by_type` int(11) NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imageslim_employeeattachment`
--

LOCK TABLES `imageslim_employeeattachment` WRITE;
/*!40000 ALTER TABLE `imageslim_employeeattachment` DISABLE KEYS */;
INSERT INTO `imageslim_employeeattachment` VALUES ('2fc0cc9c63a649f8bdc8eeeed3e0a478','employee1','company1',2,'ie_43db12e4210445f1b7f18d03b7c98675',NULL,'2017-10-30 07:38:49.298197',NULL,'2017-10-31 10:42:04.113907',0,NULL,NULL,221565,0,0,NULL,'ce994a1010b444be915eed806893ac4e','',0),('665cf20a4f7b40589c2b175c0a7d6a84','employee4','company4',5,'ie_912594cabf3045b8b6d692dc1c4901e4',NULL,'2017-10-30 07:38:49.365645',NULL,'2017-10-31 10:38:16.949403',0,NULL,NULL,294517,0,0,NULL,'76d22bac68474cca928e4fcc688e03f9','',0),('9b9b71f30d454f65b8a747e13fe5ebb4','employee2','company2',3,'ie_51ab0e48001a4b78aca1e40ee8e7ce2d',NULL,'2017-10-30 07:38:49.343584',NULL,'2017-10-31 10:38:17.185926',0,NULL,NULL,294517,0,0,NULL,'4165a803570d4826b0913f4da37147da','',0),('bac77823d00c4521a3705aa4414c931f','employee0','company0',1,'ie_0ea63c5d287840b2a9600701d8306f3e',NULL,'2017-10-30 07:38:49.223371',NULL,'2017-10-31 10:38:17.543995',0,NULL,NULL,46768,0,0,NULL,'c05e7d006305474d9d84488965cd5b6b','',0),('dfd27934374e414687633bb3c5fcdcbc','employee3','company3',4,'ie_7393ee2589a44e5b89492cdc48d0297a',NULL,'2017-10-30 07:38:49.357976',NULL,'2017-10-31 10:38:17.848015',0,NULL,NULL,386473,0,0,NULL,'2ab3e114828e4164ae050db6dd15eb91','',0);
/*!40000 ALTER TABLE `imageslim_employeeattachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imageslim_employeeattachmentslimlog`
--

DROP TABLE IF EXISTS `imageslim_employeeattachmentslimlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `imageslim_employeeattachmentslimlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `c_slim_time` datetime(6) NOT NULL,
  `c_down_time` datetime(6),
  `c_attachment_url` varchar(500) DEFAULT NULL,
  `c_persistent_id` varchar(100) DEFAULT NULL,
  `c_is_slimed` tinyint(1) NOT NULL,
  `employeeattachment_id` char(32) NOT NULL,
  `c_got_size` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `imageslim_employeeat_employeeattachment_i_12d3b852_fk_imageslim` (`employeeattachment_id`),
  CONSTRAINT `imageslim_employeeat_employeeattachment_i_12d3b852_fk_imageslim` FOREIGN KEY (`employeeattachment_id`) REFERENCES `imageslim_employeeattachment` (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imageslim_employeeattachmentslimlog`
--

LOCK TABLES `imageslim_employeeattachmentslimlog` WRITE;
/*!40000 ALTER TABLE `imageslim_employeeattachmentslimlog` DISABLE KEYS */;
INSERT INTO `imageslim_employeeattachmentslimlog` VALUES (36,'2017-10-31 10:41:14.866052','2017-10-31 10:41:14.878536',NULL,NULL,0,'2fc0cc9c63a649f8bdc8eeeed3e0a478',1);
/*!40000 ALTER TABLE `imageslim_employeeattachmentslimlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t_employee_attachment`
--

DROP TABLE IF EXISTS `t_employee_attachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_employee_attachment` (
  `c_id` varchar(32) NOT NULL,
  `c_company_id` varchar(32) NOT NULL COMMENT '企业Id',
  `c_employee_id` varchar(32) NOT NULL COMMENT '员工Id',
  `c_attachment_type` smallint(5) NOT NULL COMMENT '附件类型:',
  `c_attachment_sub_type` tinyint(3) NOT NULL COMMENT '附件类型:',
  `c_attachment_url` varchar(200) NOT NULL COMMENT '附件url',
  `c_sort` smallint(11) DEFAULT '0',
  `c_update_by` varchar(32) DEFAULT NULL,
  `c_update_dt` datetime DEFAULT NULL,
  `c_add_by` varchar(32) DEFAULT NULL COMMENT '创建用户id',
  `c_add_dt` datetime DEFAULT NULL COMMENT '创建时间',
  `c_view_name` varchar(200) DEFAULT NULL,
  `c_filename` varchar(200) DEFAULT '' COMMENT '附件文件名',
  `c_filename_ext` varchar(10) DEFAULT '' COMMENT '文件扩展名',
  `c_file_size` int(11) DEFAULT '0' COMMENT '文件大小',
  `c_is_delete` tinyint(1) DEFAULT '0' COMMENT '是否删除',
  `c_upload_by` varchar(32) DEFAULT NULL COMMENT '上传人的id',
  `c_upload_by_name` varchar(50) DEFAULT '' COMMENT '上传人的姓名',
  `c_upload_by_type` tinyint(3) DEFAULT '0' COMMENT '上传人的类型',
  PRIMARY KEY (`c_id`),
  KEY `ix_employee_id` (`c_company_id`,`c_employee_id`) USING BTREE,
  KEY `ix_add_dt` (`c_add_dt`),
  KEY `ix_employee_id_attachment_type` (`c_employee_id`,`c_attachment_type`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='附件';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_employee_attachment`
--

LOCK TABLES `t_employee_attachment` WRITE;
/*!40000 ALTER TABLE `t_employee_attachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_employee_attachment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-02 17:04:06
