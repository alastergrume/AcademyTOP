-- SELECT TOP (1000)
--     Id,
--     ProductName,
--     ProductType,
--     Quantity_in_Stock,
--     ProductCost,
--     ProductDeveloper,
--     ProductPrice
-- FROM Products

CREATE TRIGGER NewProduct 
ON Products
INSTEAD OF INSERT
AS
-- После вставки нового продукта, тригер проверяет наличие данного товара на складе, если Товар есть, то тригер, добавляет к нему вводимое количество
-- 1. Найдем продукт в таблице из вставки
-- 2. Обновим количество
-- 3. Отменим вставку
-- 4. Если товара нет, то вставим его вновь
BEGIN
-- Сохраняем в переменную количество из вставки  
DECLARE @ADDProductName NVARCHAR (MAX)
SELECT @ADDProductName = ProductName FROM INSERTED

-- Сохраняем в переменную наименование продукта из вставки, используя вариант 
-- добавления из переменной
-- declare @ADDQuantity_in_Stock INT
-- SELECT @ADDQuantity_in_Stock = [Quantity_in_Stock] from INSERTED

-- Выполняем проверку присутствия вставляемого продукта в таблице
IF EXISTS (SELECT 1 FROM Products WHERE ProductName = @ADDProductName)

-- Если есть, то прибавляем добавляем количество к существующей записи
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
    BEGIN
        INSERT INTO Products (ProductName, ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice)
        SELECT ProductName, ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice
        FROM INSERTED
        PRINT('ADD NEW STRING IN PRODUCTS')
    End
END;