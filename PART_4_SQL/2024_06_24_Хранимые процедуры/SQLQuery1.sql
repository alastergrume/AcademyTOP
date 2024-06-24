-- №1
--Hello World

--CREATE PROCEDURE HelloWorld4
--as
--begin
--print('Hello World')
--end;
--EXECUTE HelloWorld4

-- №2
-- Получить дату

--CREATE PROCEDURE GetDate1
--as
--begin
--print(getdate())
--end;
--EXECUTE GetDate1

-- №4
-- CREATE PROCEDURE GetNumbers
--as
--	begin
--		declare @a int,
--		@b int,
--		@c int,
--		@d int
--		set @a = 5
--		set @b = 6
--		set @c = 7
--      set @d = @a + @b + @c
--
--		print(@d)
--	end;


--EXECUTE GetNumbers

-- №5

--CREATE PROCEDURE SrFr
--as
--	begin
--		declare @a int,
--		@b int,
--		@c int,
--		@d int
--		set @a = 5
--		set @b = 6
--		set @c = 7
--		set @d = (@a + @b + @c)/3

--		print(@d)
--	end;


--EXECUTE SrFr

-- №6

--CREATE PROCEDURE Max_Val
--as
--	begin
--		declare @a int,
--		@b int,
--		@c int,
--		@d int
--		set @a = 5
--		set @b = 6
--		set @c = 7
--		declare @temp1 table(a int)
--		insert into @temp1 values(@a)
--		insert into @temp1 values(@b)
--		insert into @temp1 values(@c)
--		SELECT MAX([a]) FROM @temp1
--	end;
--EXECUTE Max_Val



--№7

--CREATE PROCEDURE MIN_Val
--as
--	begin
--		declare @a int,
--		@b int,
--		@c int,
--		@d int
--		set @a = 5
--		set @b = 6
--		set @c = 7
--		declare @temp1 table(a int)
--		insert into @temp1 values(@a)
--		insert into @temp1 values(@b)
--		insert into @temp1 values(@c)
--		SELECT MIN([a]) FROM @temp1
--	end;
--EXECUTE MIN_Val

--№8

--CREATE PROCEDURE Lines_#7
--as 
--	begin
--		declare
--		@my_line int,
--		@my_result nvarchar(500)
--		set @my_result = ''
--		set @my_line = 5
--		while @my_line != 0
--		begin
--			set @my_result = @my_result + '#' 
--			set @my_line -= 1
--		--print(@my_result)
--		end;
--		print(@my_result)
--	End;
--EXECUTE Lines_#7


--№9

CREATE PROCEDURE Fuck_Fuck2
as
	begin
		declare
		@my_fuck int,
		@temp int,
		@your_fuck int
		set @my_fuck = 5
		set @temp = 0
		set @your_fuck = 0
		while @my_fuck != 0
		begin
			set @temp = @temp + 1
			set @your_fuck = @temp * 1
			set @my_fuck -= 1
		end;
		print(@your_fuck)

	end;

EXECUTE Fuck_Fuck2
