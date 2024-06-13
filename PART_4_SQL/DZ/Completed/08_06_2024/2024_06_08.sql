CREATE TABLE IF NOT EXISTS Groups (

    Id int PRIMARY KEY AUTO_INCREMENT, 
        -- + ▷ Тип данных — int. 
        -- + Авто приращение., AUTO_INCREMENT
        -- + Не может содержать null-значения., Для первичного ключа по умолчанию значение NOT NULL
        -- + Первичный ключ PRIMARY KEY

    Name nvarchar(10) UNIQUE NOT NULL CHECK(Name != ''), 
        --  + Тип данных — nvarchar(10)., 
        -- + ▷ Не может содержать null-значения., 
        -- + ▷ Не может быть пустым. 
        -- + ▷ Должно быть уникальным.

    Rating int NOT NULL CHECK(0 <= Rating <= 5), 
        -- + ▷ Тип данных int, 
        -- + ▷ Не может содержать null-значения., 
        -- + ▷ Должно быть в диапазоне от 0 до 5

    Year int NOT NULL CHECK(1 <= Year <= 5), 
        -- + Тип даных int, 
        -- + ▷ Не может содержать null-значения., 
        -- + ▷ Должно быть в диапазоне от 1 до 5
)

CREATE TABLE IF NOT EXISTS Departments (

    Id int PRIMARY KEY AUTO_INCREMENT, 
        -- + ▷ Тип данных - int 
        -- + ▷ Авто приращение. 
        -- + ▷ Не может содержать null-значения. 
        -- + ▷ Первичный ключ.
    Financing money DEFAULT(0) NOT NULL CHECK(Financing >= 0),  
        -- + ▷ Типа даных money
        -- + ▷ Не может содержать null-значения.
        -- + ▷ Не может быть меньше 0.
        -- + ▷ Значение по умлолчанию - 0

    Name nvarchar(100) UNIQUE NOT NULL CHECK(Name != '') 
        -- + ▷Тип данных - nvvarchar(100)
        -- + ▷ Не может содержать null-значения.
        -- + ▷ Не может быть пустым.
        -- + ▷ Должно быть уникальным
)

CREATE TABLE IF NOT EXISTS Faculties (

    Id int PRIMARY KEY AUTO_INCREMENT, 
        -- + ▷ тип данных int
        -- + ▷ Авто приращение.
        -- + ▷ Не может содержать null-значения.
        -- + ▷ Первичный ключ.

    Name nvarchar(100) UNIQUE NOT NULL CHECK(Name != '')  
        -- + ▷ Тип данных - nvarchar(100)
        -- + ▷ Не может содержать null-значения.
        -- + ▷ Не может быть пустым.
        -- + ▷ Должно быть уникальным
)

CREATE TABLE IF NOT EXISTS Teachers (
    
    Id int PRIMARY KEY AUTO_INCREMENT,
        -- + ▷ Тип данных - int 
        -- + ▷ Авто приращение.
        -- + ▷ Не может содержать null-значения.
        -- + ▷ Первичный ключ.

    EmploymentDate date NOT NULL CHECK(EmploymentDate >= '1990-01-01'), 
        -- + ▷ Тип данных - date
        -- + ▷ Не может содержать null-значения.
        -- + ▷ Не может быть меньше 01.01.1990.

    Name nvarchar(max) NOT NULL CHECK(Name != ''),
        -- + ▷ Не может содержать null-значения.
        -- + ▷ Не может быть пустым

    Premium money DEFAULT(0) NOT NULL CHECK(Premium >= 0),
        -- + ▷ Не может содержать null-значения.
        -- + ▷ Не может быть меньше 0
        -- + Значение по умолчанию - 0 
    
    Salary money NOT NULL CHECK (Salary >= 0),
        -- + ▷ Не может содержать null-значения.
        -- + ▷ Не может быть меньше либо равно 0.
    
    Surname nvarchar(max) NOT NULL CHECK(Surname !='')
        -- + ▷ Не может содержать null-значения.
        -- + ▷ Не может быть пустым
)