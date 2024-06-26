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
