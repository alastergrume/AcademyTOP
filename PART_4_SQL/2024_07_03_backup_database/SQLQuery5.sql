-- Задание №1.1 Full backup

backup database University
to disk = 'D:\backup\University.bak'
with init;

--Обработано 576 страниц для базы данных "University", файл "University_Data" для файла 1.
--Обработано 1 страниц для базы данных "University", файл "University_Log" для файла 1.
--BACKUP DATABASE успешно обработал 577 страниц за 0.133 секунд (33.845 MБ/сек).

--Completion time: 2024-07-03T20:30:43.7954835+05:00


-- Задание №1.2 Вставка, удаление, обновление эллементов

INSERT INTO [dbo].[Teachers]
           ([LastName]
           ,[FirstName]
           ,[BirthDate]
           ,[DepartmentId])
     VALUES
           ('Serg'
           ,'Gorelikov'
           ,'1986-10-12'
           ,1)
GO

DELETE FROM [dbo].[Teachers]
      WHERE FirstName = 'skale'
GO

-- Задание №1.3 Разностная, дифференциальная резервная копия


backup database University
to disk = 'D:\backup\University_differential.bak'
with differential;

--Обработано 248 страниц для базы данных "University", файл "University_Data" для файла 1.
--Обработано 1 страниц для базы данных "University", файл "University_Log" для файла 1.
--BACKUP DATABASE WITH DIFFERENTIAL успешно обработал 249 страниц за 0.334 секунд (5.805 MБ/сек).

--Completion time: 2024-07-03T20:29:56.1046881+05:00


-- Задание №1.4 Вставка, удаление, обновление эллементов

INSERT INTO [dbo].[Teachers]
           ([LastName]
           ,[FirstName]
           ,[BirthDate]
           ,[DepartmentId])
     VALUES
           ('Relax'
           ,'Sergeev'
           ,'1986-10-12'
           ,1)
GO

DELETE FROM [dbo].[Teachers]
      WHERE LastName = 'fuck'
GO

-- Задание №1.5 Резервная копия журнала транзакций (Log backup)

BACKUP LOG University
to disk = 'D:\backup\University_log_backup.bak'
with NO_TRUNCATE;

-- В режиме Simple он не будет делать бэкап логов, для того чтобы все заработало необходимо зайти в 
-- опции быза дынных и изменить модель восстановления. Для этого правой клавишей по базе данных
-- параметры, опции, в правом врехнем углу переключить на full

-- Обработано 3 страниц для базы данных "University", файл "University_Log" для файла 1.
-- BACKUP LOG успешно обработал 3 страниц за 0.116 секунд (0.143 MБ/сек).

-- Completion time: 2024-07-03T20:45:09.0985086+05:00


-- Скрипт выполняет переключение в однопользовательский режим, и во многопользовательский режим.
-- Для восстановления базы данных необходим однопользовательский режим
USE master
GO

ALTER DATABASE University
SET SINGLE_USER
WITH ROLLBACK IMMEDIATE;
GO

ALTER DATABASE University
SET MULTI_USER
GO;


-- Задание №2.1 
-- Полное восстановление базы данных

RESTORE DATABASE University
FROM DISK = 'D:\backup\University.bak'


--WITH MOVE 'University'
--to 'C:\Progran Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\University.mdf';

RESTORE DATABASE University
FROM DISK = 'D:\backup\University_differential.bak'
WITH PARTIAL;