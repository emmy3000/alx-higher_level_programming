-- creates the table `unique_id` if it doesnn't exist in the database
-- `unique_id` description: (`id` INT) with the default value 1 and must be unique,
-- (`name` VARCHAR(256))

CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT NOT NULL DEFAULT 1,
	`name` VARCHAR(256),
	UNIQUE (id)
);
