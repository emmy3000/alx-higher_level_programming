-- creates the `hbtn_0d_usa` database and a table `states` if both don't exist

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(256) NOT NULL
);
