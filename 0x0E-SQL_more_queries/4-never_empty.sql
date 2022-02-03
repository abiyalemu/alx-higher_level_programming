-- creates the table id_not_null on MySQL server
-- id_not_null description: id INT with the default valuev1, name VARCHAR(256)
-- the datebase name will be pass as an argument of the mysql command
-- if the table id_not_null already exists, your script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
