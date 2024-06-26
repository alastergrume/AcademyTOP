

-- DECLARE @NAMRE NVARCHAR
-- SELECT @NAMRE = Name_Of_Buyer
-- FROM dbo.Customers
-- WHERE Name_Of_Buyer = 'Bob Smith'

-- IF @NAMRE = 'Bob Smith'
-- BEGIN
-- Print('Все получилось!')
-- End;


DECLARE @Del_Name_Of_Buyer NVARCHAR
SELECT @Del_Name_Of_Buyer = 'Bob Smith'

IF (@Del_Name_Of_Buyer IN (SELECT Name_Of_Buyer FROM dbo.Customers))
begin
    Print('OK')
	-- raiserror('You dont delete this item', 0, 1)
	-- rollback transaction 
end 