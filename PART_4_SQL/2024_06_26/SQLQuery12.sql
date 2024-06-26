USE [Sportshop]
GO

INSERT INTO [dbo].[Customers]
           ([Name_Of_Buyer]
           ,[Email]
           ,[Phone]
           ,[gender]
           ,[order_history]
           ,[discount]
           ,[Subscription])
     VALUES
           ('John Doe','johndoe@example.com','555-1234','Male',1,0, 'Monthly')
GO




/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [Id]
      ,[Name_Of_Buyer]
      ,[Email]
      ,[Phone]
      ,[gender]
      ,[order_history]
      ,[discount]
      ,[Subscription]
  FROM [Sportshop].[dbo].[Customers]