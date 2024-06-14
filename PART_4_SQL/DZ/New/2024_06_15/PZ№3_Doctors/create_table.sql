CREATE DATABASE Hospital
use Hospital


CREATE TABLE Departments (
    Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Building INT NOT NULL CHECK(Building BETWEEN 1 AND 5),
    Financing money DEFAULT(0) NOT NULL CHECK(Financing >= 0),
    Floor INT NOT NULL CHECK(Floor >= 1),
    Name nvarchar(100) UNIQUE NOT NULL CHECK(Name != '')
);

-- Заболевания
CREATE TABLE Diseases ( 
    Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY, 
    Name nvarchar(100) UNIQUE NOT NULL CHECK(Name != ''), -- Название заболевания
    Severity INT DEFAULT(1) NOT NULL CHECK(Severity >= 1), -- Степень тяжести заболевания
);

-- Врачи
CREATE TABLE Doctors (
	Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	Name nvarchar(max) NOT NULL CHECK(Name != ''),
	Surename nvarchar(max) NOT NULL CHECK(Surename != ''),
	Phone char(10),
	Premium money DEFAULT(0) NOT NULL CHECK(Premium >= 0),
	Salary money NOT NULL CHECK(Salary > 0)
);

CREATE TABLE Examinations (
	Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	Name nvarchar(100) UNIQUE NOT NULL CHECK(Name != ''),
	DayOfWeek INT NOT NULL CHECK(DayOfWeek BETWEEN 1 AND 7),
	StartTime time NOT NULL CHECK(StartTime BETWEEN '08:00:00' AND '18:00:00'),
	EndTime time NOT NULL CHECK(EndTime BETWEEN '08:00:00' AND '18:00:00'),
	CHECK(EndTime > StartTime)
);

CREATE TABLE Wards(
	Id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	Building INT NOT NULL CHECK(Building BETWEEN 1 AND 5),
	Floor int NOT NULL CHECK(Floor >= 1),
	Name nvarchar(20) UNIQUE NOT NULL CHECK(Name !='')
)

