CREATE DATABASE Academy;
USE Academy;

CREATE TABLE Departments (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Financing DECIMAL(10,2) DEFAULT(0) NOT NULL CHECK(Financing >= 0),
    Name VARCHAR(100) UNIQUE NOT NULL CHECK (Name != ''),
    FacultyId INT NOT NULL 
);

CREATE TABLE Faculties (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) UNIQUE NOT NULL CHECK(Name != '')
);

CREATE TABLE Groups (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100), 
    Year INT NOT NULL CHECK(Year BETWEEN 1 AND 5), 
    DepartmentId INT NOT NULL 
);

CREATE TABLE GroupsLectures (
    Id INT AUTO_INCREMENT PRIMARY KEY, 
    DayOfWeek INT NOT NULL CHECK(DayOfWeek BETWEEN 1 AND 7),
    GroupId INT NOT NULL,
    LectureId INT NOT NULL,
    FOREIGN KEY (GroupId) REFERENCES Groups (Id),
    FOREIGN KEY (LectureId) REFERENCES Lectures (Id)
);

CREATE TABLE Lectures (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    LectureRoom VARCHAR(max) NOT NULL CHECK(LectureRoom != ''),
    SubjectId INT NOT NULL,
    TeacherId INT NOT NULL,
    FOREIGN KEY (SubjectId) REFERENCES Subjects (Id),
    FOREIGN KEY (TeacherId) REFERENCES Teachers (Id)
);

CREATE TABLE Subjects (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) UNIQUE NOT NULL CHECK(Name != '')
);

CREATE TABLE Teachers (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(max) NOT NULL CHECK(Name != ''),
    Surname VARCHAR(max) NOT NULL CHECK(Surname != ''),
    Salary DECIMAL(10,2) NOT NULL CHECK(Salary > 0)
);

-- Вставка данных

INSERT INTO Faculties(Name) VALUES 
    ('Programming on basic C#'), ('TomorowLand'), ('What does if not music in oure live');

INSERT INTO Departments(Financing, Name, FacultyId) VALUES 
    (235000, 'Programming langs', 1), (123546123, 'Heroes study', 2), (986543215, 'Music base', 3);

INSERT INTO Groups(Name, Year, DepartmentId) VALUES 
    ('GekksGR', 2, 1), ('HeroesGR', 3, 2), ('JazzGR', 1, 3);

INSERT INTO Subjects(Name) VALUES 
    ('Programing'), ('Heroeses'), ('Music');

INSERT INTO Teachers(Name, Salary, Surname) VALUES 
    ('Josef', 20, 'Bezose'), ('Benedict', 40, 'Cumberbage'), ('Paul', 30, 'Makkartny');

INSERT INTO Lectures(DayOfWeek, LectureRoom, SubjectId, TeacherId) VALUES 
    (1, 'Programming room', 1, 1), (2, 'Herose Room', 2, 2), (3, 'Music Room', 3, 3);

INSERT INTO GroupsLectures(GroupId, LectureId) VALUES 
    (1, 1), (2, 2), (3, 3);