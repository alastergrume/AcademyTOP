-- Изменение струкутры имеющихся в базе таблиц с помощью команды ALTER TABLE


/*������ �������� ���������� �������� � ����*/

ALTER TABLE dbo.Departments
ADD CHECK (Building >= 1 AND Building <= 5)

/*�� ����� ���� ������*/

ALTER TABLE dbo.Departments
ADD CHECK (Name != '')




/* ���������� �������� ��������� ����� ������� */ 

SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION, NUMERIC_SCALE, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'Departments'

/* ���������� ���������� � ���������� ����� ������� */ 

EXEC sp_help 'Departments'

/*������� ������������� �����������, ������������� � ������� ADD CHECK. ��� ���������� ���������� ������ ��������
�������, �������� ������� EXEC sp_help 'table_name' 
���������:

ALTER TABLE table_name DROP CONSTRAINT constraint_name;

���:

table_name � ��� �������, �� ������� ��������� �����������; 2
constraint_name � ������������ ���������� �����������
*/
ALTER TABLE dbo.Departments
DROP CONSTRAINT CK__Department__Name__59FA5E80


/*�� ����� ���� ������*/

ALTER TABLE dbo.Doctors
ADD CHECK (Name != '')
EXEC sp_help 'Doctors'

/*�� ����� ���� ����� ����*/

ALTER TABLE dbo.Doctors
ADD CHECK (Premium >= 0)

ALTER TABLE dbo.Doctors 
ALTER COLUMN Premium SET DEFAULT 0;
