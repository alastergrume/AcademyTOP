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


-- Варинат в котором сравнивается после UPDATE

-- CREATE TRIGGER
-- ON Sales
-- AFTER UPDATE
-- AS
-- BEGIN
--     DECLARE @product_quality
--     @product_quality = Quantity_in_Stock
--     FROM updated
--     IF @product_quality == 0
--         begin
-- 			INSERT INTO Archive (ProductName,	ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice)
-- 			SELECT ProductName,	ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice
-- 			FROM updated;
--         end
-- End