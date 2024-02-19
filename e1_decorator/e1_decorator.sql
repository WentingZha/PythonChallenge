CREATE DATABASE e1_decorator;

USE e1_decorator;

CREATE TABLE Animal(
ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
NAME VARCHAR(225) NOT NULL, 
AGE int NOT NULL
);

insert into Animal (NAME, AGE) values ('Dove',3);

insert into Animal (NAME, AGE) values ('Duck',1);

