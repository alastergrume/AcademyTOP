

select LastName, FirstName

From my_db.dbo.Students /*����� ����� ��������� dbo.Student*/


/*������� � ������� ������������ ��� ���� � ����*/

select LastName + ' ' + FirstName as FullName

From my_db.dbo.Students


/*
��� �������, ������� ��������� ���� � �� ��, ���������� �������� �������
cast() - �������������� ���� ������, ��������� ���� ��� ��� ������ cast(Grants as nvarchar(10)
convert() - �������������� ���� ������, ��������� ��� ������, ����� 
*/
select 'Student' + LastName + ' receives' + cast(Grants as nvarchar(10))
from my_db.dbo.Students


select 'Student' + LastName + ' receives' + convert(nvarchar(10), Grants)
from my_db.dbo.Students

/*
������� TOP - �������� ������ �������� (������) ������� � ������ ����������
*/
/*������� ��� ������ ��������*/
SELECT TOP 2 LastName, FirstName, BirthDay
from my_db.dbo.Students

/* ������� ������ 20% �������*/
SELECT TOP 30 PERCENT LastName, FirstName, BirthDay
from my_db.dbo.Students

/* DISTINCT - ������� ���������� ������ � �������, � �������� ���������� */

SELECT DISTINCT FirstName
from my_db.dbo.Students

/*WHERE - ����������� ����� �������� ������������� �������, ��������� � ���� 
����������� ����� ��������� � �����������:
<> - �� ����� (������ ��� ��� ������ ���)
!> - ������ ���
<! - ������ ���
*/


SELECT Email
FROM my_db.dbo.Students
WHERE id > 3

/* LEN() - ����� */

SELECT Grants
FROM my_db.dbo.Students
WHERE LEN(Grants) > 6

/* AND, OR -  �, ���*/
SELECT LastName, BirthDay
FROM my_db.dbo.Students
WHERE MONTH(BirthDay) >= 9 AND MONTH(BirthDay) <= 11

/*MONTH, YEAR, DAY*/

SELECT LastName, BirthDay
FROM my_db.dbo.Students
WHERE YEAR(BirthDay) % 2 = 0 AND DAY(BirthDay) % 2 <> 0 /*���� ��� ������, � ���� �� ������*/

/*IS - �������� ��������� */

SELECT Grants
FROM my_db.dbo.Students
WHERE Grants IS NULL
print('���� ���') /*��������� � ���������, ��� ��� ������ ��� � ���� ������ � ������� � ��������� ������ �� ��������*/

/* 
Order BY - ����������� ����������, ����� ������
ASC - ���������� �� �����������
DESC - ���������� �� ��������
*/

SELECT *
FROM my_db.dbo.Students
Order BY BirthDay DESC, FirstName ASC /*��������� �� ���������� ����*/

/* IN - �������*/

SELECT *
FROM my_db.dbo.Students
Where LastName IN ('��������', '������', '��������') /*������� ������ ���, ��� ������ � ��������� ������*/

/*BETWEEN - ��������*/

SELECT *
FROM my_db.dbo.Students
Where BirthDay BETWEEN '1993-01-01' AND '2023-01-01' /*������� ������, ������� ������ � ��������� ��������*/

SELECT *
FROM my_db.dbo.Students
Where BirthDay NOT BETWEEN '1993-01-01' AND '2023-01-01' /*������� ������, ������� �� ������ � ��������� ��������*/

/*������� ��� ����� ����������, ������� ���������� �� ��������� �������*/
SELECT FirstName, ID
FROM my_db.dbo.Students
Where FirstName BETWEEN '�' AND '�' /*������� ������, ������� ������ � ��������� ��������*/

SELECT FirstName, ID
FROM my_db.dbo.Students
Where FirstName NOT BETWEEN '�' AND '�' /*������� ������, ������� �� ������ � ��������� ��������*/

/*like - ����� �� ��������� ����� ������

%  ����� ������. ��������
_ - ���� ��������� ������
[] - ������ ������������������
[^] - ������ ������������������ ���������� 
*/

SELECT LastName, FirstName, ID
FROM my_db.dbo.Students
WHERE FirstName like '%�%' and LastName like '%�%'

/*���������, ������� ������ �� ������ � �������:
INSERT - �������
*/


INSERT INTO my_db.dbo.Students(Id, BirthDay, FirstName, LastName)
VALUES (12, '1666-06-06', '���', '���������') /*VALUES - �������, ������� ��������� ��������*/


SELECT *
FROM my_db.dbo.Students

/* update - ��������� ����� ������*/

update my_db.dbo.Students
SET Grants += 500
WHERE Grants IS NOT NULL

SELECT *
FROM my_db.dbo.Students

/* delete - ������� ������ � ������� */

/*DELETE FROM my_db.dbo.Students
WHERE Grants > 9*/

SELECT *
FROM Backup_KUPA.dbo.Student


create table table_name
(	Id Int,
	FirstName Varchar(50),
	LastName Varchar(50),
	Grants int, 
)


