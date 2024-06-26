CREATE TRIGGER AddKlient
on [dbo].[Customers]
for insert
as 
begin
	declare @FIO char 
	select @FIO= [Name_Of_Buyer] from inserted
	declare @cust_email char
	select @cust_email = [Email] from inserted
	-- Сравнение информации из 
	if (@FIO != (select Name_Of_Buyer
				from Customers
				where @FIO = Name_Of_Buyer))
		begin
		if (@cust_email != (select [Email]
				from Customers
				where @cust_email = [Email]))
				begin
					INSERT INTO [dbo].[Customers]
						([Name_Of_Buyer]
						,[Email]
						,[Phone]
						,[gender]
						,[order_history]
						,[discount]
						,[Subscription])
					SELECT
						[Name_Of_Buyer]
						,[Email]
						,[Phone]
						,[gender]
						,[order_history]
						,[discount]
						,[Subscription]
					from inserted
				end
		end
	else
		begin
			raiserror('Такой уже есть', 0, 1)
		end;
End;

