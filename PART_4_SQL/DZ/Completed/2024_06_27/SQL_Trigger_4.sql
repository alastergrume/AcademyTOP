CREATE TRIGGER do_not_delete_customers
on dbo.Customers
INSTEAD OF DELETE
AS
BEGIN
	raiserror('You dont delete this item2', 16, 1)        
End;