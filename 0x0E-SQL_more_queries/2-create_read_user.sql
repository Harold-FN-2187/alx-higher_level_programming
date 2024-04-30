/* -- Creates the database hbtn_0d_2 and the user user_0d_2
-- The user_0d_2 has SELECT privilege on hbtn_0d_2 with password user_0d_2_pwd
CREATE DATABASE
    IF NOT EXISTS `hbtn_0d_2`;
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
   ON `hbtn_0d_2`.*
   TO 'user_0d_2'@'localhost'
   IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES; */


CREATE DATABASE IF NOT EXISTS `htbn_0d_2`;CREATE USER IF NOT EXISTS 'user_0d_2' @'localhost' IDENTIFIED BY 'password';GRANT ALL PRIVILEGES ON `htbn_0d_2`.* TO 'user_0d_2' @'localhost';
