
/*Задает диапазон допустимых значений в поле*/

ALTER TABLE dbo.Departments
ADD CHECK (Building >= 1 AND Building <= 5)

/*Не может быть пустым*/

ALTER TABLE dbo.Departments
ADD CHECK (Name != '')




/* Показывает заданные параматры полей таблицы */ 

SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION, NUMERIC_SCALE, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_NAME = 'Departments'

/* Показывает информацию о параматрах полей таблицы */ 

EXEC sp_help 'Departments'

/*Удаляет установленное ограничение, установленное с помощью ADD CHECK. Для применения необходимо узнать название
правила, применив команду EXEC sp_help 'table_name' 
Синтаксис:

ALTER TABLE table_name DROP CONSTRAINT constraint_name;

где:

table_name — имя таблицы, из которой удаляется ограничение; 2
constraint_name — наименование удаляемого ограничения
*/
ALTER TABLE dbo.Departments
DROP CONSTRAINT CK__Department__Name__59FA5E80


/*Не может быть пустым*/

ALTER TABLE dbo.Doctors
ADD CHECK (Name != '')
EXEC sp_help 'Doctors'

/*Не может быть менше ноля*/

ALTER TABLE dbo.Doctors
ADD CHECK (Premium >= 0)

ALTER TABLE dbo.Doctors 
ALTER COLUMN Premium SET DEFAULT 0;
