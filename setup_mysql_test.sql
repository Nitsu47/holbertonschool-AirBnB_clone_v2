-- Test module to verify the correct operation of 'setup_mysql_dev' module.
-- Verify the correct creation of database, tables, users and privileges.

-- Use of performance_schema, where performance and internal activities
-- are stored, like user privileges, databases, tables, etc.

-- Verification of database creation.
SELECT COUNT(*)
FROM information_schema.schemata
WHERE schema_name = 'hbnb_dev_db';

-- Verification of user creation.
SELECT COUNT(*)
FROM mysql.user
WHERE user = 'hbnb_dev'
AND localhost = 'localhost';

--Verification of user password.
SELECT COUNT(*) autenticathion_string
FROM mysql.user
WHERE user = hbnb_dev
AND localhost = 'localhost';

-- Verification of user privileges in main database.
SELECT COUNT(*)
from information_schema.schema_privileges
WHERE grantee = "'hbnb_dev'@'localhost'"
AND table_schema = 'hbnb_dev_db'
AND privilege_type = 'ALL PRIVILEGES';

-- Verification of user privileges in performance_schema.
SELECT COUNT(*)
from information_schema.schema_privileges
WHERE grantee = "'hbnb_dev'@'localhost'"
AND table_schema = 'performance_schema'
AND privilege_type = 'SELECT';
