-- Creates the user user_0d_1 with all privileges.

/* CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
   ON *.*
   TO 'user_0d_1'@'localhost' */


CREATE DATABASE IF NOT EXISTS `htbn_0d_2`;CREATE USER IF NOT EXISTS 'user_0d_2' @'localhost' IDENTIFIED BY 'password';GRANT ALL PRIVILEGES ON `htbn_0d_2`.* TO 'user_0d_2' @'localhost';
