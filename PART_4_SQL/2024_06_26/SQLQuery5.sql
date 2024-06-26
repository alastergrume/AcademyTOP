CREATE TRIGGER UpdateHistory 
ON Sales
AFTER INSERT
AS
-- Здесь сохраняется информация в переменную, из связанной таблицы по айдишнику
declare @ID int
SELECT @ID = [Name_Of_Buyer] from inserted

	begin
		INSERT INTO Sales_History (ProductName,	ProductCost, Qauntity_sale, Sale_data, Name_of_Employee, Name_Of_Buyer)
		SELECT ProductName,	ProductCost, Qauntity_sale, Sale_data, Name_of_Employee, @ID
		FROM inserted;
	begin
		print('ADD NEW HISTORY STRING')
	end
End;


-- Тригер, записывает информацию в Архив, после обновления информации о количестве продукции в таблице Продукты.



CREATE TRIGGER UpdateProducts
ON dbo.Products
AFTER UPDATE
AS
begin
	INSERT INTO Products (ProductName,ProductType,Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice)
	SELECT ProductName, ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice
	FROM inserted
	WHERE Quantity_in_Stock = 0
End;


-- Триггер №3

CREATE TRIGGER AddKlient
on [dbo].[Customers]
for insert
as 
begin
	declare @FIO char 
	select @FIO= [Name_Of_Buyer] from inserted
	declare @cust_email char
	select @cust_email = [Email] from inserted
	-- Сверяются данные, которые производят проверку на индивидуальность
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
			--raiserror('Такой уже есть', 0, 1)
			
			print('Такой уже есть')
			rollback transaction -- Отменяет все произведенные действия
		end;
End;

