-- creates the table force_name on MySQl server.
-- force_name describtion: id INT, name VARCHAR(256) can't be null
-- the dataa base name will be passed as an argument of the mysql command
-- if the table force_name alrady exists, your script should not fail

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);

