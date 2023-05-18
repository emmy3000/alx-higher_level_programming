-- creates the database `hbtn_0d_2 if it doesn't exist and user `user_0d_2`
-- grants SELECT privilege on the `hbtn_0d_2` database to user_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
