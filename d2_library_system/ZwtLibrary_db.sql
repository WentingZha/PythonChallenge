mysql -u root -p

CREATE DATABASE ZwtLibrary;

USE ZwtLibrary;

CREATE TABLE Book(
ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
Name VARCHAR(225) NOT NULL, 
Author VARCHAR(20) NOT NULL
);

INSERT INTO Book (Name, Author)
VALUES
('Self Reference Engine','Toh Enjoe'),
('Book of No Sleep','Reddit'),
('Enders Game','Orson');


ALTER TABLE Book ADD COLUMN `price` DECIMAL(10,2) NULL ;

UPDATE Book SET price=100.11 WHERE ID=1;
UPDATE Book SET price=98.22 WHERE ID=2;
UPDATE Book SET price=100 WHERE ID=3;