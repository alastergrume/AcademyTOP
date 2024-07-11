
-- Тригге запрещает добавлять нового продавца, 
-- если количество существующих продавцов больше 6


CREATE TRIGGER DONT_INSERT_EMPLOYEE
ON Employee
FOR INSERT
AS
BEGIN

    -- Если количество строк превышает допустимое значение, 
    -- то отменяем вставку

    IF (SELECT COUNT(Id) FROM Emploeyy) > 22
    BEGIN
        RAISERROR('You cannot insert this item. The limit of 22 employees is reached.', 16, 1)
        ROLLBACK TRANSACTION;
    END
END;