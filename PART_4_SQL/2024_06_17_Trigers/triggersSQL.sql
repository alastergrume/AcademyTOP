--Триггер Начинается все с фразы:
--После запуска хранятся в ядре базы, после выполннения запроса выполняются автоматически.

---Создание, обновление, вставка и удаление
--имеют параметры по инициализации
--имют ключи, сохдаются один раз

--тип Автор только для таблиц.



-- use University
CREATE TRIGGER addStudents
on Students
for insert, update
as
raiserror('%d строк добавлено или модифицировано', 0, 1, @@rowcount)
return

insert into Students(Id, Firstname, LastName, BirthDate, Grants, Email, GroupsId)
values(11, 'Tony', 'Stark', '03-05-24', 4567, 'tony@super.com', 2)



