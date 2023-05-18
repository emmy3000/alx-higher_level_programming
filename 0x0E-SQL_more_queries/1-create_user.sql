-- creates a user `user_0d_1` if it doesn't exist in MySQL server
-- all privileges will be granted to the said user
-- password is set to `user_0d_1_pwd

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
