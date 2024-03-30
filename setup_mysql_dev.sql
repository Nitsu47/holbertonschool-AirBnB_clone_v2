-- Creates a basic setup(database, user, psswd and privileges)
-- Database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- User
CREATE USER IF NOT EXISTS
'hbnb_dev'@'localhost';
ALTER USER 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';
-- Privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.*
TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.*
TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;