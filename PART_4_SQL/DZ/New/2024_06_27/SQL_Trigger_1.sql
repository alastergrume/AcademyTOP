CREATE TRIGGER UpdateHistory 
ON Sales
AFTER INSERT
AS
-- ����� ����������� ���������� � ����������, �� ��������� ������� �� ���������
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