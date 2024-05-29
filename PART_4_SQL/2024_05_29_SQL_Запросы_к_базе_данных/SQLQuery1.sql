

select LastName, FirstName

From my_db.dbo.Students /*Можно сразу указывать dbo.Student*/


/*Варинат в котором объединяются два поля в один*/

select LastName + ' ' + FirstName as FullName

From my_db.dbo.Students


/*
Две функции, которые выполняют одно и то же, отличаются входными данными
cast() - преобразование типа данных, принимает поле как тип данных cast(Grants as nvarchar(10)
convert() - преобразование типа данных, принимает тип данных, через 
*/
select 'Student' + LastName + ' receives' + cast(Grants as nvarchar(10))
from my_db.dbo.Students


select 'Student' + LastName + ' receives' + convert(nvarchar(10), Grants)
from my_db.dbo.Students

/*
Функция TOP - получает первые элементы (записи) таблицы в нужном количестве
*/
/*Выводит два первых элемента*/
SELECT TOP 2 LastName, FirstName, BirthDay
from my_db.dbo.Students

/* Выводит первые 20% таблицы*/
SELECT TOP 30 PERCENT LastName, FirstName, BirthDay
from my_db.dbo.Students

/* DISTINCT - выводит уникальные записи в столбце, и проводит сортировку */

SELECT DISTINCT FirstName
from my_db.dbo.Students

/*WHERE - Предложение после которого прописывается условие, Принимает в себя 
стандартные знаки сравнения и специфичные:
<> - не равно (Больше чем или меньше чем)
!> - Больше чем
<! - Меньше чем
*/


SELECT Email
FROM my_db.dbo.Students
WHERE id > 3

/* LEN() - Длина */

SELECT Grants
FROM my_db.dbo.Students
WHERE LEN(Grants) > 6

/* AND, OR -  И, ИЛИ*/
SELECT LastName, BirthDay
FROM my_db.dbo.Students
WHERE MONTH(BirthDay) >= 9 AND MONTH(BirthDay) <= 11

/*MONTH, YEAR, DAY*/

SELECT LastName, BirthDay
FROM my_db.dbo.Students
WHERE YEAR(BirthDay) % 2 = 0 AND DAY(BirthDay) % 2 <> 0 /*Если год четный, а день не четный*/

/*IS - Проверка вхождений */

SELECT Grants
FROM my_db.dbo.Students
WHERE Grants IS NULL
print('Ноля нет') /*Выводится в сообщении, так как такого нет в базе данных и поэтому в результат ничего не выдается*/

/* 
Order BY - Упорядочить информацию, после выбора
ASC - Сортировка по возрастанию
DESC - Сортировка по убыванию
*/

SELECT *
FROM my_db.dbo.Students
Order BY BirthDay DESC, FirstName ASC /*Сортирует по выбранному полю*/

/* IN - выборка*/

SELECT *
FROM my_db.dbo.Students
Where LastName IN ('Синявкин', 'Клинор', 'Синдарин') /*Выводит только тех, кто входит в указанный список*/

/*BETWEEN - Диапазон*/

SELECT *
FROM my_db.dbo.Students
Where BirthDay BETWEEN '1993-01-01' AND '2023-01-01' /*Выводит данные, которые входят в указанный диапазон*/

SELECT *
FROM my_db.dbo.Students
Where BirthDay NOT BETWEEN '1993-01-01' AND '2023-01-01' /*Выводит данные, которые не входят в указанный диапазон*/

/*Вывести все имена студенотов, которые начинаются на указанные символы*/
SELECT FirstName, ID
FROM my_db.dbo.Students
Where FirstName BETWEEN 'А' AND 'П' /*Выводит данные, которые входят в указанный диапазон*/

SELECT FirstName, ID
FROM my_db.dbo.Students
Where FirstName NOT BETWEEN 'А' AND 'П' /*Выводит данные, которые не входят в указанный диапазон*/

/*like - поиск по текстовым полям таблци

%  любая послед. символов
_ - люой одиночный символ
[] - задаем последовательность
[^] - задаем последовательность отсутствия 
*/

SELECT LastName, FirstName, ID
FROM my_db.dbo.Students
WHERE FirstName like '%П%' and LastName like '%в%'

/*Операторы, которые влияют на данные в таблице:
INSERT - вставка
*/


INSERT INTO my_db.dbo.Students(Id, BirthDay, FirstName, LastName)
VALUES (12, '1666-06-06', 'Юля', 'Васильева') /*VALUES - функция, которая принимает значения*/


SELECT *
FROM my_db.dbo.Students

/* update - Изменение любой записи*/

update my_db.dbo.Students
SET Grants += 500
WHERE Grants IS NOT NULL

SELECT *
FROM my_db.dbo.Students

/* delete - удалить записи в таблице */

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


