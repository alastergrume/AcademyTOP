-- ������� ������� ���������� � ���, ������� ����� ��������������� ���� ���������

--CREATE TRIGGER addStudents
--on Students
--for insert, update
--as 
--raiserror('%d ����� ��������� ��� ��������������', 0, 1, @@rowcount)
--return

--insert into Students(Id, Firstname, LastName, BirthDate, Grants, Email, GroupsId)
--values(18, 'Tony2', 'Stark2', '03-05-24', 4567, 'tony@super.com', 1)




-- ������� ����������� ���������� �� �������

-- �������, ����� ������� �� ����������� � ����������



CREATE TRIGGER addTeacher
on Teachers
for insert
as 
begin
	-- ������� ���������� � ����������� �� �������� �� �������
	declare @BirthDate1 smalldatetime -- ��������� ����������, � ������� ����� ������� ������ �� �������
	select @BirthDate1 = BirthDate
	from inserted 
	if (@BirthDate1 >= (getdate()-9125))
	begin
		print(getdate()-9125)
		print('������������� � ����� ������� ��������')
	end
	else
	begin
		raiserror('������������ ����',0,1)
		rollback transaction 
	end

End 

/*
-- ������� � ����������� ���� �������� � ����������

CREATE TRIGGER addTeacher2
on Teachers
for insert
as 
begin

	-- ������� ���������� � ����������� �� �������� �� �������

	declare @BirthDate2 smalldatetime
	declare @BirthDateUserInsert smalldatetime
	SET @BirthDateUserInsert = getdate()-9125
	select @BirthDate2 = BirthDate
	from inserted 
	if (@BirthDate2 >= @BirthDateUserInsert)
	begin
		print(@BirthDateUserInsert)
		print('������������� � ����� ������� ��������' + @BirthDateUserInsert)
	end
	else
	begin
		raiserror('������������ ����',0,1)
		rollback transaction 	
	end
End


*/

insert into Teachers(LastName, Firstname, BirthDate, DepartmentId)
values('Seal', 'Soul', '-03-23', 2)



-- ������� ����������� ��������

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