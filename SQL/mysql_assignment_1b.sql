CREATE DATABASE testDB;
USE testDB;
CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    PRIMARY KEY (ID)
);
CREATE INDEX idx_lastname
ON Persons (LastName);
CREATE TABLE Orders (
    OrderID int NOT NULL,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES Persons(ID)
);
INSERT INTO Persons (ID, LastName, FirstName, Age)
VALUES ('1', 'Levine', 'Sam', '22');
SELECT * FROM Persons;
INSERT INTO Persons 
VALUES ('2', 'Levine', 'Adam', '41'),('3', 'Princeloo', 'Behati', '29');
ALTER TABLE Persons
ADD Email varchar(255);
ALTER TABLE Persons
DROP COLUMN Email;
UPDATE Persons
SET Age=30
WHERE ID = 3;
DELETE FROM Persons WHERE LastName='Levine';
DROP TABLE Orders;