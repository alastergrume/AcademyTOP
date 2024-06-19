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