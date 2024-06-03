Select 
		[LastName] +
		[FirstName] as FullName, Name

FROM [Backup_KUPA].[dbo].[Student], [Backup_KUPA].[dbo].[Subjects]
WHERE [Backup_KUPA].[dbo].[Student].id = [Backup_KUPA].[dbo].[Subjects].Id