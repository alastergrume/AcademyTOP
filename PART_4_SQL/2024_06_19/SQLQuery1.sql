CREATE DATABASE Sportshop

USE Sportshop

CREATE TABLE Products (
	Id INT IDENTITY(1,1) PRIMARY KEY,
	ProductName nvarchar(100) UNIQUE NOT NULL CHECK(ProductName != ''),
	ProductType nvarchar(100) NOT NULL CHECK(ProductType != ''),
	Quantity_in_Stock money DEFAULT(0) NOT NULL CHECK(Quantity_in_Stock >= 0),    -- Количество товара в наличии
	ProductCost money NOT NULL,-- Себестоимость товара
	ProductDeveloper nvarchar(100) NOT NULL, -- Производитель
	ProductPrice money NOT NULL, -- Цена продажи
);

CREATE TABLE Sales (
	Id INT IDENTITY(1,1) PRIMARY KEY,
	ProductName nvarchar(100) UNIQUE NOT NULL CHECK(ProductName != ''),
	ProductCost  money DEFAULT(0) NOT NULL CHECK(ProductCost >= 0), -- Себестоимость товара
	Qauntity_sale money DEFAULT(0) NOT NULL CHECK(Qauntity_sale >= 0), -- Количество Товара в продаже
	Sale_data date NOT NULL, -- Дата продажи
	Name_of_Employee nvarchar(max) NOT NULL CHECK(Name_of_Employee != ''), -- Сотрудник FORIGN KEY
	Name_Of_Buyer nvarchar(max) -- Покупатель FORIGN KEY
);

CREATE TABLE Sales_History (
	Id INT IDENTITY(1,1) PRIMARY KEY,
	ProductName nvarchar(100) UNIQUE NOT NULL CHECK(ProductName != ''),
	ProductCost  money DEFAULT(0) NOT NULL CHECK(ProductCost >= 0), -- Себестоимость товара
	Qauntity_sale money DEFAULT(0) NOT NULL CHECK(Qauntity_sale >= 0), -- Количество Товара в продаже
	Sale_data date NOT NULL, -- Дата продажи
	Name_of_Employee nvarchar(max) NOT NULL CHECK(Name_of_Employee != ''), -- Сотрудник FORIGN KEY
	Name_Of_Buyer nvarchar(max) -- Покупатель FORIGN KEY
);


CREATE TABLE Employee( 
	Id INT IDENTITY(1,1) PRIMARY KEY,
	Name_of_Employee NVARCHAR(100) NOT NULL, -- Сотрудник
	Post NVARCHAR(max) NOT NULL,                     -- Должность
	Date_of_employment date NOT NULL,       -- Дата приема на работу
	Gender NVARCHAR(max) NOT NULL,                    -- Пол
	Salary money NOT NULL                   -- Зарплата
);

CREATE TABLE Customers ( 
	Id INT IDENTITY(1,1) PRIMARY KEY,
	Name_Of_Buyer nvarchar(max) NOT NULL,
	Email nvarchar(max), -- Email
	Phone INT, -- Телефон
	gender NVARCHAR(50) NOT NULL, -- Пол
	order_history INT NOT NULL,   -- История Заказов FORIGN KEY

	discount INT CHECK(discount BETWEEN 1 AND 100),  -- Процент скидки
	Subscription NVARCHAR(50) -- Подписка
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


------------------ТРИГГЕРЫ------------------

-- №1
-- При продаже товара, заносить информацию о продаже в 
-- таблицу «История». Таблица «История» используется для 
-- дубляжа информации о всех продажах

CREATE TRIGGER Delete_history
on Sales
for insert as 
begin


	

End
