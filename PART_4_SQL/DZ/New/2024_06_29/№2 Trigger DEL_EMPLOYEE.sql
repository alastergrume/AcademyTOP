
-- При увольнении сотрудника триггер переносит информацию 
-- об уволенном сотруднике в таблицу «Архив сотрудников»


-- Если нет такой таблицы, то создадим новую таблицу Архив сотрудников:
-- CREATE TABLE [dbo].[Archiv_Employee](
-- 	[Id] [int] IDENTITY(1,1) NOT NULL,
-- 	[Name_of_Employee] [nvarchar](100) NOT NULL,
-- 	[Post] [nvarchar](max) NOT NULL,
-- 	[Date_of_employment] [date] NOT NULL,
-- 	[Gender] [nvarchar](max) NOT NULL,
-- 	[Salary] [money] NOT NULL,
-- PRIMARY KEY CLUSTERED 
-- (
-- 	[Id] ASC
-- )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
-- ) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
-- GO

-- Триггер

CREATE TRIGGER DELL_EMPLOYEE 
ON Employee
-- Выбираем событие - после удаления
AFTER DELETE
AS
-- Инициализируем вставку
BEGIN
    INSERT INTO Archiv_Employee (Name_of_Employee, Post, Date_of_employment, Gender, Salary)
    SELECT Name_of_Employee, Post, Date_of_employment, Gender, Salary
    FROM DELETED;
    print('ADD NEW HISTORY STRING')
End;