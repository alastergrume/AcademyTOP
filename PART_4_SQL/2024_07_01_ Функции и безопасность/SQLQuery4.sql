-- �������� ������� ������ ������������� � /�� ��� ���������� � �������� �������� �������������
-- ��������������

create function dbo.Famio3()
-- ��������� �������, ������� ���������� ����� ������ ������ ����� ����������
returns table as return
SELECT Id, Name_Of_Buyer, gender
from [Customers]
where [Name_Of_Buyer] in (select [Name_of_Employee] from [Employee])
UNION
SELECT Id, Name_of_Employee, Gender
from [Employee]
where [Name_of_Employee] in (select [Name_Of_Buyer] from [Customers])

go
-- ��� ����������� ����� ��������
SELECT * from dbo.Famio3()
go

-- ��������� � ��������� ��������
SELECT * FROM sys.database_files


-- �������� ������������
create login Vasia
with password = '<JlbyLdfNhb123>';