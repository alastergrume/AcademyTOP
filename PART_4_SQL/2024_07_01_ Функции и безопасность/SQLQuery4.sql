-- Создание функции поиска однофамильцев в /БД гже покупатель и продавец являются однофамильцем
-- Многотабличные

create function dbo.Famio3()
-- Сервисная строчка, которая определяет какой фармот данных будет выводиться
returns table as return
SELECT Id, Name_Of_Buyer, gender
from [Customers]
where [Name_Of_Buyer] in (select [Name_of_Employee] from [Employee])
UNION
SELECT Id, Name_of_Employee, Gender
from [Employee]
where [Name_of_Employee] in (select [Name_Of_Buyer] from [Customers])

go
-- Это стандартный вызов функиции
SELECT * from dbo.Famio3()
go

-- Обращение к системным таблицам
SELECT * FROM sys.database_files


-- Создание пользователя
create login Vasia
with password = '<JlbyLdfNhb123>';