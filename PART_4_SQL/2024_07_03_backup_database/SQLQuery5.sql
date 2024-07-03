-- ������� �1.1 Full backup

backup database University
to disk = 'D:\backup\University.bak'
with init;

--���������� 576 ������� ��� ���� ������ "University", ���� "University_Data" ��� ����� 1.
--���������� 1 ������� ��� ���� ������ "University", ���� "University_Log" ��� ����� 1.
--BACKUP DATABASE ������� ��������� 577 ������� �� 0.133 ������ (33.845 M�/���).

--Completion time: 2024-07-03T20:30:43.7954835+05:00


-- ������� �1.2 �������, ��������, ���������� ����������

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

-- ������� �1.3 ����������, ���������������� ��������� �����


backup database University
to disk = 'D:\backup\University_differential.bak'
with differential;

--���������� 248 ������� ��� ���� ������ "University", ���� "University_Data" ��� ����� 1.
--���������� 1 ������� ��� ���� ������ "University", ���� "University_Log" ��� ����� 1.
--BACKUP DATABASE WITH DIFFERENTIAL ������� ��������� 249 ������� �� 0.334 ������ (5.805 M�/���).

--Completion time: 2024-07-03T20:29:56.1046881+05:00


-- ������� �1.4 �������, ��������, ���������� ����������

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

-- ������� �1.5 ��������� ����� ������� ���������� (Log backup)

BACKUP LOG University
to disk = 'D:\backup\University_log_backup.bak'
with NO_TRUNCATE;

-- � ������ Simple �� �� ����� ������ ����� �����, ��� ���� ����� ��� ���������� ���������� ����� � 
-- ����� ���� ������ � �������� ������ ��������������. ��� ����� ������ �������� �� ���� ������
-- ���������, �����, � ������ ������� ���� ����������� �� full

-- ���������� 3 ������� ��� ���� ������ "University", ���� "University_Log" ��� ����� 1.
-- BACKUP LOG ������� ��������� 3 ������� �� 0.116 ������ (0.143 M�/���).

-- Completion time: 2024-07-03T20:45:09.0985086+05:00


-- ������ ��������� ������������ � �������������������� �����, � �� ��������������������� �����.
-- ��� �������������� ���� ������ ��������� �������������������� �����
USE master
GO

ALTER DATABASE University
SET SINGLE_USER
WITH ROLLBACK IMMEDIATE;
GO

ALTER DATABASE University
SET MULTI_USER
GO;


-- ������� �2.1 
-- ������ �������������� ���� ������

RESTORE DATABASE University
FROM DISK = 'D:\backup\University.bak'


--WITH MOVE 'University'
--to 'C:\Progran Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\University.mdf';

RESTORE DATABASE University
FROM DISK = 'D:\backup\University_differential.bak'
WITH PARTIAL;