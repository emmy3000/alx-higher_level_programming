-- creates `force_name` table on MySQL server
-- table consists of columns: ud (INT) and name (VARCHAR(256))
-- name column cannot be null
-- if table already exists, script won't fail

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
