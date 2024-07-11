-- 1. ������� ������� �����
-- 2. ��������� ��� ����� ������������ ������ � ���� ������, � Login Properties �� ������� User Mapping
--    ��� �� �������������� ����� ������� � ���� ������ (�� ����� T-SQL ������ �������� �������� 
--    ����� �4 �� ��������� ����������)
-- 3. ��������� ����� �������� ��������� sp_helplogins ������ � ��������� ����
-- 4. �������� ������������ USER ��� ����� ����� �� ������ Login
-- 5. ������ �������� � �������� - ����� � ���������� ������� �� ������� Permissions 
--    ��������� ����� � ��������� �������, �� �������� � ��������.

create login Mark
with password = 'JlbyLdfNhb123!';


-- ���������� � ����� ����� ����� ���������� ������������, � ��� �� ������ ����������
exec sp_helplogins 'Mark'

-- �������� ������������ ��� ����� �����

USE Sportshop;
CREATE USER Mark
FOR LOGIN Mark;
Go


-- ������� �1

-- ������ �������� � �������� - �������� �� ���������� ������� �� ������� Permissions ��������� ����� � ��������� �������, �� �������� SELCET.

-- ���� �� T-SQL
deny select
on dbo.Employee
to Mark

--�������� ���� ������� � �������� ��
exec sp_helprotect NULL, Mark

-- ��� ���������� Select 

SELECT TOP (1000) [Id]
      ,[Name_of_Employee]
      ,[Post]
      ,[Date_of_employment]
      ,[Gender]
      ,[Salary]
  FROM [Sportshop].[dbo].[Employee]


-- ��������� ���������
-- Msg 229, Level 14, State 5, Line 26
-- The SELECT permission was denied on the object 'Employee', database 'Sportshop', schema 'dbo'.

-- Completion time: 2024-07-11T21:58:18.5670626+05:00

-- ��� ����������, ���������: 

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


--������� �2
USE Sportshop;


create login David
with password = 'JlbyLdfNhb123!';


-- ���������� � ����� ����� ����� ���������� ������������, � ��� �� ������ ����������
exec sp_helplogins 'David'

-- ���������� ���� db_owner (������ ����� ��� �����)
sp_addrolemember 'db_owner', 'David'

grant select
on dbo.Employee
to David

exec sp_helprotect NULL, David

-- �������� ������������ ��� ����� �����

USE Sportshop;
CREATE USER David
FOR LOGIN David;
GO;

--������� �3
USE Sportshop;
GO;

create login Olga
with password = 'JlbyLdfNhb123!';


-- ���������� � ����� ����� ����� ���������� ������������, � ��� �� ������ ����������
exec sp_helplogins 'Olga'

-- �������� ������������ ��� ����� �����

USE Sportshop;
CREATE USER Olga
FOR LOGIN Olga;
Go
-- ���������� ���� db_owner (������ ����� ��� �����)

sp_addrolemember 'db_owner', 'Olga'

grant CONTROL
on OBJECT:: Sportshop
to Olga


--������� �4
USE Sportshop;
GO;

create login Konstantin
with password = 'JlbyLdfNhb123!';


-- ���������� � ����� ����� ����� ���������� ������������, � ��� �� ������ ����������
exec sp_helplogins 'Konstantin'

-- �������� ������������ ��� ����� �����

USE Sportshop;
CREATE USER Konstantin
FOR LOGIN Konstantin;
Go
-- ���������� ���� db_owner (������ ����� ��� �����). ����������� �� master

sp_addrolemember 'db_owner', 'Konstantin'


-- ��� ��������� ������ ����� ���� ������, ������������
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

