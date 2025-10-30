-- sudo apt update && sudo apt install -y mysql-server

-- sudo service mysql start

-- sudo mysql

ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';

CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;