
-- Выводит список значений в таблице


SELECT TOP (1000) [Id]
      ,[ProductName]
      ,[ProductType]
      ,[Quantity_in_Stock]
      ,[ProductCost]
      ,[ProductDeveloper]
      ,[ProductPrice]
  FROM [Sportshop].[dbo].[Products]


  -- Команда выполняет действие до вставки
   
  INSTEAD OF INSERT

  -- Выполяняется вставка содержимого в таблицу:

INSERT INTO [dbo].[Products]
           ([ProductName]
           ,[ProductType]
           ,[Quantity_in_Stock]
           ,[ProductCost]
           ,[ProductDeveloper]
           ,[ProductPrice])
     VALUES
           ('Mountain Bike' 
           ,'Bicycles'
           ,8
           ,25000
           ,'Velta'
		   ,36000)
GO


-- Создание переменной из вставки
DECLARE @ADDProductName NVARCHAR (MAX)
SELECT @ADDProductName = ProductName FROM INSERTED


-- Выполняет проверку присутствия вставляемого продукта в таблице
IF EXISTS (SELECT 1 FROM Products WHERE ProductName = @ADDProductName)

-- Если есть строчка, то добавляем количество к существующей записи
    BEGIN
        UPDATE Products
        -- Вариант для добавления с использованием переменной
        -- SET Quantity_in_Stock += @ADDQuantity_in_Stock
        -- Вариант, без добавления переменной
        SET Quantity_in_Stock = Quantity_in_Stock + (SELECT Quantity_in_Stock FROM INSERTED)
        WHERE ProductName IN (SELECT ProductName FROM INSERTED)
        PRINT('UPDATE QUANTITY IN STOCK FOR PRODUCT' + @ADDProductName)
    End
ELSE
	-- Если продукта нет в таблице, то строка вставляется в таблицу из INSERTED
    BEGIN
        INSERT INTO Products (ProductName, ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice)
        SELECT ProductName, ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice
        FROM INSERTED
        PRINT('ADD NEW STRING IN PRODUCTS')
    End