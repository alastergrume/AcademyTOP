USE master
GO

CREATE LOGIN Mark4
with PASSWORD = '<JlbyLdfNhb123!>'
GO

USE Alaster_G__Hospital_db
create User Mark
for login Mark
GO

USE [Alaster_G__Hospital_db]
GO
ALTER ROLE [db_securityadmin] ADD MEMBER [Mark]
GO

ALTER ROLE [db_sysadmin] ADD MEMBER [Mark]
GO

exec sp_helprole
exec sp_helprole 'sysadmin'


exec sp_helpuser 'Mark'
select * from sys.database_role_members

exec sp_helprotect 'db_owner'
exec sp_helprotect @username = 'Mark'
exec sp_helprotect NULL, Mark
@username = 'Mark',
@grantorname = 'Mark',
@permissionarea = 'os'

