USE [University]
GO
/****** Object:  Trigger [dbo].[addTeacher2]    Script Date: 17.06.2024 20:25:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[addTeacher2]
on [dbo].[Teachers]
for insert
as 
begin

	-- Создаем переменную и присваиваем ей значение из вставки

	declare @BirthDate2 smalldatetime
	declare @BirthDateUserInsert smalldatetime
	SET @BirthDateUserInsert = getdate()-9125
	select @BirthDate2 = BirthDate
	from inserted 
	if (@BirthDate2 <= @BirthDateUserInsert)
	begin
		print(@BirthDateUserInsert)
		print('ADD NEW TEACHER for Trigger 2'+ convert(char,@BirthDateUserInsert))
	end
	else
	begin
		raiserror('Incorrect DATE for Trigger 2',0,1)
		rollback transaction 	
	end
End