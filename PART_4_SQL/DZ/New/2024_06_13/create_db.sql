CREATE DATABASE Academy;
use Academy;
       

        -- Диапазоны:
        -- Вариант 1 (с `BETWEEN`):
        -- ```sql
        -- DayOfWeek int NOT NULL CHECK(DayOfWeek BETWEEN 1 AND 7)
        -- ```
        -- Вариант 2 (с `AND`):
        -- ```sql
        -- DayOfWeek int NOT NULL CHECK(DayOfWeek >= 1 AND DayOfWeek <= 7)
        -- ```
        -- Объяснение:
        --  `BETWEEN 1 AND 7` проверяет, находится ли `DayOfWeek` в диапазоне от 1 до 7 включительно.
        --  `DayOfWeek >= 1 AND DayOfWeek <= 7` проверяет, что 
        -- `DayOfWeek` больше или равен 1 и меньше или равен 7. 

    -- Объяснение FORING KEY

            -- Primary Key:  Это главное, что поле `ID` (или `CustomerID`) должно быть Primary Key в таблице `Customers`. Это означает, что оно должно быть уникальным для каждой записи в таблице, а также не может быть пустым.
            --  Внешний ключ: Когда вы устанавливаете внешний ключ в другой таблице (например, `Orders`), он должен ссылаться на `Primary Key` в таблице `Customers`. 

            -- Пример:

            -- ```sql
            -- CREATE TABLE Customers (
            --     ID INT PRIMARY KEY, 
            --     Name VARCHAR(255), 
            --     Email VARCHAR(255) 
            -- );

            -- CREATE TABLE Orders (
            --     OrderID INT PRIMARY KEY,
            --     CustomerID INT,
            --     ...
            --     FOREIGN KEY (CustomerID) REFERENCES Customers(ID)
            -- );
            -- ```

            -- В этом примере поле `ID` в таблице `Customers`  является 
            --`Primary Key` и используется как `Foreign Key` в таблице 
            --`Orders`. 

            -- Вставка значений в таблицу

            --  Предположим, у нас есть две таблицы:

            --  Customers:
            --      `CustomerID` (INT, PRIMARY KEY) - Идентификатор клиента
            --      `Name` (VARCHAR(255)) - Имя клиента
            --      `Email` (VARCHAR(255)) - Электронная почта клиента
            --  Orders:
            --      `OrderID` (INT, PRIMARY KEY) - Идентификатор заказа
            --      `CustomerID` (INT, FOREIGN KEY REFERENCES Customers(CustomerID)) - Идентификатор клиента, который сделал заказ
            --      `OrderDate` (DATE) - Дата заказа
            --      `TotalAmount` (DECIMAL(10,2)) - Сумма заказа

            -- Заполнение таблицы Customers:

            -- ```sql
            -- -- Вставка данных в таблицу Customers
            -- INSERT INTO Customers (CustomerID, Name, Email) VALUES
            --     (1, 'Иван Иванов', 'ivan.ivanov@example.com'),
            --     (2, 'Мария Петрова', 'maria.petrova@example.com'),
            --     (3, 'Алексей Сидоров', 'alexey.sidorov@example.com');
            -- ```

            -- Заполнение таблицы Orders:

            -- ```sql
            -- -- Вставка данных в таблицу Orders
            -- INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
            --     (101, 1, '2023-10-27', 150.00),
            --     (102, 2, '2023-10-28', 250.50),
            --     (103, 3, '2023-10-29', 100.75),
            --     (104, 1, '2023-10-30', 75.25);
            -- ```

            -- Важно:

            --  Убедитесь, что типы данных вставляемых значений соответствуют типам данных в столбцах таблиц.
            --  Внешние ключи должны соответствовать существующим значениям в первичных ключах в связанных таблицах.

            -- Дополнительные замечания:

            --  Вы можете использовать оператор `INSERT INTO ... SELECT ...` для копирования данных из других таблиц.
            --  Вы можете использовать оператор `LOAD DATA INFILE` для импорта данных из файла.
            --  Для больших объемов данных рекомендуется использовать пакетные операции (например, `INSERT INTO ... SELECT ...` или `LOAD DATA INFILE`) для повышения эффективности.

            -- Пример с `LOAD DATA INFILE`:

            -- ```sql
            -- LOAD DATA INFILE 'customers.csv' 
            -- INTO TABLE Customers 
            -- FIELDS TERMINATED BY ',' 
            -- ENCLOSED BY '"' 
            -- LINES TERMINATED BY '\n' 
            -- IGNORE 1 ROWS;
            -- ```

            -- Этот запрос загружает данные из файла `customers.csv` в таблицу `Customers`. Убедитесь, что файл `customers.csv` находится в том же каталоге, что и ваш файл `mysql` и что файл содержит данные в следующем формате:

            -- ```
            -- CustomerID,Name,Email
            -- 1,"Иван Иванов","ivan.ivanov@example.com"
            -- 2,"Мария Петрова","maria.petrova@example.com"
            -- 3,"Алексей Сидоров","alexey.sidorov@example.com"
            -- ```

            -- Прежде чем выполнять запросы на изменение данных в базе, рекомендуется сделать резервную копию. 

            -- Если вам нужна помощь с конкретными SQL-запросами для ваших таблиц, пожалуйста, предоставьте мне:

            --  Структуру ваших таблиц (имена столбцов и типы данных)
            --  Данные, которые вы хотите вставить в таблицы

            -- Я помогу вам сформулировать правильные запросы!


CREATE TABLE Departments (
    Id int IDENTITY(1,1) PRIMARY KEY,
    Financing money DEFAULT(0) NOT NULL CHECK(Financing >= 0),
    Name nvarchar(100) UNIQUE NOT NULL CHECK (Name != ''),
    FacultyId int NOT NULL 
);


CREATE TABLE Faculties(
    Id int IDENTITY(1,1) PRIMARY KEY,
    Name nvarchar(100) UNIQUE NOT NULL CHECK(Name != '')
);

CREATE TABLE Groups(
    Id int IDENTITY(1,1) PRIMARY KEY, 
    Name nvarchar(10) UNIQUE NOT NULL CHECK(Name != ''), 
    Year int NOT NULL CHECK(Year BETWEEN 1 AND 5), 
    DepartmentId int NOT NULL 
);

CREATE TABLE GroupsLectures(
    Id int IDENTITY(1,1) PRIMARY KEY, 
    GroupId int NOT NULL,
    LectureId int NOT NULL,
);

CREATE TABLE Lectures (

    Id int IDENTITY(1,1) PRIMARY KEY,
    DayOfWeek int NOT NULL CHECK(DayOfWeek BETWEEN 1 AND 7), -- Может должна быть в GroupsLectures
    LectureRoom nvarchar(max) NOT NULL CHECK(LectureRoom != ''),
    SubjectId int NOT NULL,
    TeacherId int NOT NULL 
);

CREATE TABLE Subjects (
    Id int IDENTITY(1,1) PRIMARY KEY,
    Name nvarchar(100) UNIQUE NOT NULL CHECK(Name != '')
);

CREATE TABLE Teachers(
    Id int IDENTITY(1,1) PRIMARY KEY,
    Name nvarchar(max) NOT NULL CHECK(Name != ''),
    Surname nvarchar(max) NOT NULL CHECK(Surname != ''),
    Salary money NOT NULL CHECK(Salary > 0)
)

-- Присвоение внешних ключей

   -- Добавить внешний ключ с помощью ALTER TABLE: 
   -- После создания таблиц, вы можете добавить внешний ключ с помощью оператора `ALTER TABLE`:

   -- ```sql
   -- ALTER TABLE Orders
   -- ADD CONSTRAINT FK_Orders_Customers 
   -- FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID);
   -- ```

   -- Объяснение:

    -- `ALTER TABLE Orders`:  Изменяем структуру таблицы `Orders`.
    -- `ADD CONSTRAINT FK_Orders_Customers`:  Добавляем ограничение (constraint) с именем `FK_Orders_Customers`.
    -- `FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)`:  Определяем `CustomerID` как внешний ключ, ссылающийся на `CustomerID` в таблице `Customers`.


ALTER TABLE Departments
ADD CONSTRAINT FK_Departments_Faculties
FOREIGN KEY (FacultyId) REFERENCES Faculties (Id);

ALTER TABLE Groups
ADD CONSTRAINT FK_Groups_Departments
FOREIGN KEY (DepartmentId) REFERENCES Departments (Id);

ALTER TABLE GroupsLectures
ADD CONSTRAINT FK_GroupsLectures_Groups
FOREIGN KEY (GroupId) REFERENCES Groups (Id);

ALTER TABLE GroupsLectures
ADD CONSTRAINT FK_GroupsLectures_Lectures
FOREIGN KEY (LectureId) REFERENCES Lectures (Id);

ALTER TABLE Lectures
ADD CONSTRAINT FK_Lectures_Subjects
FOREIGN KEY (SubjectId) REFERENCES Subjects (Id);

ALTER TABLE Lectures
ADD CONSTRAINT FK_Lectures_Teachers
FOREIGN KEY (TeacherId) REFERENCES Teachers (Id);



INSERT INTO Faculties(Name)
VALUES ('Progaramming on basic C#'), ('TomorowLand'), ('What does if not music in oure live');

INSERT iNTO Departments(Financing, Name, FacultyId)
VALUES (235000, 'Programming langs', 1), (123546123, 'Heroes study', 2), (986543215, 'Music base', 3);

INSERT iNTO Groups(Name, Year, DepartmentId)
VALUES ('GekksGR', 2, 1), ('HeroesGR', 3, 2), ('JazzGR', 1, 3);

INSERT iNTO Subjects(Name)
VALUES ('Programing'), ('Heroeses'), ('Music');

INSERT iNTO Teachers(Name, Salary, Surname)
VALUES ('Josef', 20, 'Bezose'), ('Benedict', 40, 'Cumberbage'), ('Paul', 30, 'Makkartny');

INSERT iNTO Lectures(DayOfWeek, LectureRoom, SubjectId, TeacherId)
VALUES (1, 'Programming room', 1, 1), (2, 'Herose Room', 2, 2), (3, 'Music Room', 3, 3);