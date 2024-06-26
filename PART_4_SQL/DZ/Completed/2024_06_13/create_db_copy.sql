CREATE DATABASE Academy;
USE Academy;

CREATE TABLE Departments (
    DepartmentId INT NOT NULL PRIMARY KEY,
    Financing DECIMAL(10,2) DEFAULT(0) NOT NULL CHECK(Financing >= 0),
    Name VARCHAR(100) UNIQUE NOT NULL CHECK (Name != ''),
    FacultyId INT NOT NULL
);


INSERT INTO Departments(DepartmentId, Financing, Name, FacultyId) VALUES 
    (1, 235, 'Programming langs', 1), (2, 123, 'Heroes study', 2), (3, 986, 'Music base', 3);

