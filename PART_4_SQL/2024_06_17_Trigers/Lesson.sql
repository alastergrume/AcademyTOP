-- Триггер выводит информацию о том, сколько строк модифицированно иили добавлено

--CREATE TRIGGER addStudents
--on Students
--for insert, update
--as 
--raiserror('%d строк добавлено или модифицировано', 0, 1, @@rowcount)
--return

--insert into Students(Id, Firstname, LastName, BirthDate, Grants, Email, GroupsId)
--values(18, 'Tony2', 'Stark2', '03-05-24', 4567, 'tony@super.com', 1)




-- Триггер запрещающий добавление по условию

-- Вариант, когда функция не сохраняется в переменную



CREATE TRIGGER addTeacher
on Teachers
for insert
as 
begin
	-- Создаем переменную и присваиваем ей значение из вставки
	declare @BirthDate1 smalldatetime -- Объявляем переменную, в которой будме хранить данные от запроса
	select @BirthDate1 = BirthDate
	from inserted 
	if (@BirthDate1 >= (getdate()-9125))
	begin
		print(getdate()-9125)
		print('Преподаватель с датой успешно добавлен')
	end
	else
	begin
		raiserror('Некорректная дата',0,1)
		rollback transaction 
	end

End 

/*
-- Вариант с сохранением даты рождения в переменную

CREATE TRIGGER addTeacher2
on Teachers
for insert
as 
begin

	-- Создаем переменную и присваиваем ей значение из вставки

	declare @BirthDate2 smalldatetime
	declare @BirthDateUserInsert smalldatetime
	SET @BirthDateUserInsert = getdate()-9125
	select @BirthDate2 = BirthDate
	from inserted 
	if (@BirthDate2 >= @BirthDateUserInsert)
	begin
		print(@BirthDateUserInsert)
		print('Преподаватель с датой успешно добавлен' + @BirthDateUserInsert)
	end
	else
	begin
		raiserror('Некорректная дата',0,1)
		rollback transaction 	
	end
End


*/

insert into Teachers(LastName, Firstname, BirthDate, DepartmentId)
values('Seal', 'Soul', '-03-23', 2)



-- Триггер запрещающий удаление

CREATE TRIGGER CheckGroupeDellete
on Groups
for delete
as
	begin
		declare @NameGroup varchar(25), @IdFaculty int
		select @NameGroup = deleted.GroupName
		from deleted
		if (@NameGroup = 'Math' or @NameGroup = 'teory')
		begin
			raiserror('You dont delete this item', 0, 1)
			rollback transaction 
		end

		else
		begin
			print('Delete this groupe completed')	
		end

	End

delete FROM Groups
where GroupName = 'teory'



/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [Id]
      ,[GroupName]
      ,[FacultyId]
  FROM [University].[dbo].[Groups]