-- 1. Сначала создаем логин
-- 2. Открываем для этого пользователя доступ к базе данных, в Login Properties на вкладке User Mapping
--    тут же устианавливаем права доступа к базе данных (На языке T-SQL данная процедра заменяет 
--    пункт №4 из настоящей инструкции)
-- 3. Проверяем через хранимую процедуру sp_helplogins доступ к указанной базе
-- 4. Создание пользователя USER для имени входа на сервер Login
-- 5. Запрет действий с таблицей - Можно в параметрах таблицы на вкладке Permissions 
--    назначить права к отдельной таблице, на действия с таблицей.

create login Mark
with password = 'JlbyLdfNhb123!';


-- Показывает к каким базам может обращаться пользователь, а так же другую информацию
exec sp_helplogins 'Mark'

-- Создание пользователя для имени входа

USE Sportshop;
CREATE USER Mark
FOR LOGIN Mark;
Go


-- Задание №1

-- Запрет действий с таблицей - Выполнен из параметров таблицы на вкладке Permissions назначены права к отдельной таблице, на действия SELCET.

-- Тоже на T-SQL
deny select
on dbo.Employee
to Mark

--просмотр прав доступа к объектам БД
exec sp_helprotect NULL, Mark

-- При выполнении Select 

SELECT TOP (1000) [Id]
      ,[Name_of_Employee]
      ,[Post]
      ,[Date_of_employment]
      ,[Gender]
      ,[Salary]
  FROM [Sportshop].[dbo].[Employee]


-- выводится сообщение
-- Msg 229, Level 14, State 5, Line 26
-- The SELECT permission was denied on the object 'Employee', database 'Sportshop', schema 'dbo'.

-- Completion time: 2024-07-11T21:58:18.5670626+05:00

-- При добавлении, сообщение: 

INSERT INTO [dbo].[Employee]
           ([Name_of_Employee]
           ,[Post]
           ,[Date_of_employment]
           ,[Gender]
           ,[Salary])
     VALUES
           ('Richard Chandler',
           'richard@aol.com'
           ,'2024-03-16'
           ,'Male'
           ,350000)
GO


--(1 row affected)

--Completion time: 2024-07-11T22:00:22.8870619+05:00


--Задание №2
USE Sportshop;


create login David
with password = 'JlbyLdfNhb123!';


-- Показывает к каким базам может обращаться пользователь, а так же другую информацию
exec sp_helplogins 'David'

-- Добавление роли db_owner (Полные права над базой)
sp_addrolemember 'db_owner', 'David'

grant select
on dbo.Employee
to David

exec sp_helprotect NULL, David

-- Создание пользователя для имени входа

USE Sportshop;
CREATE USER David
FOR LOGIN David;
GO;

--Задание №3
USE Sportshop;
GO;

create login Olga
with password = 'JlbyLdfNhb123!';


-- Показывает к каким базам может обращаться пользователь, а так же другую информацию
exec sp_helplogins 'Olga'

-- Создание пользователя для имени входа

USE Sportshop;
CREATE USER Olga
FOR LOGIN Olga;
Go
-- Добавление роли db_owner (Полные права над базой)

sp_addrolemember 'db_owner', 'Olga'

grant CONTROL
on OBJECT:: Sportshop
to Olga


--Задание №4
USE Sportshop;
GO;

create login Konstantin
with password = 'JlbyLdfNhb123!';


-- Показывает к каким базам может обращаться пользователь, а так же другую информацию
exec sp_helplogins 'Konstantin'

-- Создание пользователя для имени входа

USE Sportshop;
CREATE USER Konstantin
FOR LOGIN Konstantin;
Go
-- Добавление роли db_owner (Полные права над базой). Назначается на master

sp_addrolemember 'db_owner', 'Konstantin'


-- Для просмотра членов ролей базы данных, используется
exec sp_helpuser;

grant select
on dbo.Customers
to Konstantin

grant select
on dbo.Products
to Konstantin

deny INSERT, UPDATE, DELETE 
on dbo.Products
to Konstantin

deny INSERT, UPDATE, DELETE 
on dbo.Customers
to Konstantin

deny SELECT, INSERT, UPDATE, DELETE
on [Sales_History]
to Konstantin
deny SELECT, INSERT, UPDATE, DELETE
on [dbo].[Sales]
to Konstantin
deny SELECT, INSERT, UPDATE, DELETE
on [dbo].[Employee]
to Konstantin
deny SELECT, INSERT, UPDATE, DELETE
on [dbo].[Archiv_Employee]
to Konstantin
deny SELECT, INSERT, UPDATE, DELETE
on [dbo].[Archiv]
to Konstantin


exec sp_helprotect NULL, Konstantin 

