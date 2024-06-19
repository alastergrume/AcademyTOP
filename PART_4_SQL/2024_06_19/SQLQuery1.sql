CREATE DATABASE Sportshop

USE Sportshop

CREATE TABLE Products (
	Id INT IDENTITY(1,1) PRIMARY KEY,
	ProductName nvarchar(100) UNIQUE NOT NULL CHECK(ProductName != ''),
	ProductType nvarchar(100) NOT NULL CHECK(ProductType != ''),
	Quantity_in_Stock money DEFAULT(0) NOT NULL CHECK(Quantity_in_Stock >= 0),    -- ���������� ������ � �������
	ProductCost money NOT NULL,-- ������������� ������
	ProductDeveloper nvarchar(100) NOT NULL, -- �������������
	ProductPrice money NOT NULL, -- ���� �������
);

CREATE TABLE Sales (
	Id INT IDENTITY(1,1) PRIMARY KEY,
	ProductName nvarchar(100) UNIQUE NOT NULL CHECK(ProductName != ''),
	ProductCost  money DEFAULT(0) NOT NULL CHECK(ProductCost >= 0), -- ������������� ������
	Qauntity_sale money DEFAULT(0) NOT NULL CHECK(Qauntity_sale >= 0), -- ���������� ������ � �������
	Sale_data date NOT NULL, -- ���� �������
	Name_of_Employee nvarchar(max) NOT NULL CHECK(Name_of_Employee != ''), -- ��������� FORIGN KEY
	Name_Of_Buyer nvarchar(max) -- ���������� FORIGN KEY
);

CREATE TABLE Sales_History (
	Id INT IDENTITY(1,1) PRIMARY KEY,
	ProductName nvarchar(100) UNIQUE NOT NULL CHECK(ProductName != ''),
	ProductCost  money DEFAULT(0) NOT NULL CHECK(ProductCost >= 0), -- ������������� ������
	Qauntity_sale money DEFAULT(0) NOT NULL CHECK(Qauntity_sale >= 0), -- ���������� ������ � �������
	Sale_data date NOT NULL, -- ���� �������
	Name_of_Employee nvarchar(max) NOT NULL CHECK(Name_of_Employee != ''), -- ��������� FORIGN KEY
	Name_Of_Buyer nvarchar(max) -- ���������� FORIGN KEY
);

CREATE TABLE Archiv (
	Id INT IDENTITY(1,1) PRIMARY KEY,
	ProductName nvarchar(100) UNIQUE NOT NULL CHECK(ProductName != ''),
	ProductCost  money DEFAULT(0) NOT NULL CHECK(ProductCost >= 0), -- ������������� ������
	Qauntity_sale money DEFAULT(0) NOT NULL CHECK(Qauntity_sale >= 0), -- ���������� ������ � �������
	Sale_data date NOT NULL, -- ���� �������
	Name_of_Employee nvarchar(max) NOT NULL CHECK(Name_of_Employee != ''), -- ��������� FORIGN KEY
	Name_Of_Buyer nvarchar(max) -- ���������� FORIGN KEY
);

CREATE TABLE Employee( 
	Id INT IDENTITY(1,1) PRIMARY KEY,
	Name_of_Employee NVARCHAR(100) NOT NULL, -- ���������
	Post NVARCHAR(max) NOT NULL,                     -- ���������
	Date_of_employment date NOT NULL,       -- ���� ������ �� ������
	Gender NVARCHAR(max) NOT NULL,                    -- ���
	Salary money NOT NULL                   -- ��������
);

CREATE TABLE Customers ( 
	Id INT IDENTITY(1,1) PRIMARY KEY,
	Name_Of_Buyer nvarchar(max) NOT NULL,
	Email nvarchar(max), -- Email
	Phone INT, -- �������
	gender NVARCHAR(50) NOT NULL, -- ���
	order_history INT NOT NULL,   -- ������� ������� FORIGN KEY

	discount INT CHECK(discount BETWEEN 1 AND 100),  -- ������� ������
	Subscription NVARCHAR(50) -- ��������
);

ALTER TABLE Sales
ADD CONSTRAINT FK_Sales_Employee
FOREIGN KEY (Name_of_Employee) REFERENCES Employee(Id);


ALTER TABLE Sales
ADD CONSTRAINT FK_Sales_Customers
FOREIGN KEY (Name_Of_Buyer) REFERENCES Customers(Id);


ALTER TABLE Customers
ADD CONSTRAINT FK_Customers_Sales
FOREIGN KEY (order_history) REFERENCES Sales_History(Id);


------------------��������------------------

-- �1
-- ��� ������� ������, �������� ���������� � ������� � 
-- ������� ���������. ������� ��������� ������������ ��� 
-- ������� ���������� � ���� ��������

CREATE TRIGGER ADD_History
on Sales
AFTER INSERT
as
begin
    INSERT INTO Sales_History (ProductName,	ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice)
	SELECT ProductName,	ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice
	FROM inserted;
End;


-- №2
-- Если после продажи товара не осталось ни одной единицы данного товара, необходимо перенести информацию
-- о полностью проданном товаре в таблицу «Архив»


CREATE TRIGGER
ON Sales
FOR UPDATE
AS
BEGIN
    DECLARE @product_quality
    @product_quality = Quantity_in_Stock
    FROM updated
    IF @product_quality == 0
        begin

        INSERT INTO Archive (ProductName,	ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice)
        SELECT ProductName,	ProductType, Quantity_in_Stock, ProductCost, ProductDeveloper, ProductPrice
        FROM updated;
        end
End

