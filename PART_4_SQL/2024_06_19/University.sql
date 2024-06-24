USE [master]
GO
/****** Object:  Database [University]    Script Date: 24.06.2024 18:43:49 ******/
CREATE DATABASE [University]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'University_Data', FILENAME = N'C:\Progran Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\University.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 1024KB )
 LOG ON 
( NAME = N'University_Log', FILENAME = N'C:\Progran Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\University.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 10%)
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [University] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [University].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [University] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [University] SET ANSI_NULLS ON 
GO
ALTER DATABASE [University] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [University] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [University] SET ARITHABORT OFF 
GO
ALTER DATABASE [University] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [University] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [University] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [University] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [University] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [University] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [University] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [University] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [University] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [University] SET  DISABLE_BROKER 
GO
ALTER DATABASE [University] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [University] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [University] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [University] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [University] SET PARAMETERIZATION FORCED 
GO
ALTER DATABASE [University] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [University] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [University] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [University] SET  MULTI_USER 
GO
ALTER DATABASE [University] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [University] SET DB_CHAINING OFF 
GO
ALTER DATABASE [University] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [University] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [University] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [University] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [University] SET QUERY_STORE = OFF
GO
USE [University]
GO
/****** Object:  Table [dbo].[achievements]    Script Date: 24.06.2024 18:43:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[achievements](
	[Id] [int] NOT NULL,
	[StudentId] [int] NULL,
	[SubjectId] [int] NULL,
	[Assesment] [int] NULL,
 CONSTRAINT [PK_achievements] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Groups]    Script Date: 24.06.2024 18:43:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Groups](
	[Id] [int] NOT NULL,
	[GroupName] [nchar](70) NULL,
	[FacultyId] [nchar](70) NULL,
 CONSTRAINT [PK_Groups] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Students]    Script Date: 24.06.2024 18:43:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Students](
	[Id] [int] NOT NULL,
	[LastName] [nchar](50) NOT NULL,
	[FirstName] [nchar](50) NOT NULL,
	[BirthDate] [date] NOT NULL,
	[Grants] [decimal](6, 2) NULL,
	[Email] [nchar](50) NULL,
	[GroupsId] [int] NULL,
 CONSTRAINT [PK_Students] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Subjects]    Script Date: 24.06.2024 18:43:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Subjects](
	[Id] [int] NOT NULL,
	[Name] [nchar](30) NULL,
 CONSTRAINT [PK_Subjects] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Teachers]    Script Date: 24.06.2024 18:43:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Teachers](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[LastName] [nchar](10) NOT NULL,
	[FirstName] [nchar](10) NOT NULL,
	[BirthDate] [date] NOT NULL,
	[DepartmentId] [int] NOT NULL,
 CONSTRAINT [PK_Teachers] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TeachersSubjects]    Script Date: 24.06.2024 18:43:49 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TeachersSubjects](
	[TeacherId] [int] NOT NULL,
	[SubjectId] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Index [IX_TeachersSubjects]    Script Date: 24.06.2024 18:43:49 ******/
CREATE NONCLUSTERED INDEX [IX_TeachersSubjects] ON [dbo].[TeachersSubjects]
(
	[TeacherId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[achievements]  WITH CHECK ADD  CONSTRAINT [FK_achievements_Students] FOREIGN KEY([StudentId])
REFERENCES [dbo].[Students] ([Id])
GO
ALTER TABLE [dbo].[achievements] CHECK CONSTRAINT [FK_achievements_Students]
GO
ALTER TABLE [dbo].[achievements]  WITH CHECK ADD  CONSTRAINT [FK_achievements_Subjects] FOREIGN KEY([SubjectId])
REFERENCES [dbo].[Subjects] ([Id])
GO
ALTER TABLE [dbo].[achievements] CHECK CONSTRAINT [FK_achievements_Subjects]
GO
ALTER TABLE [dbo].[TeachersSubjects]  WITH CHECK ADD  CONSTRAINT [FK_TeachersSubjects_Subjects] FOREIGN KEY([SubjectId])
REFERENCES [dbo].[Subjects] ([Id])
GO
ALTER TABLE [dbo].[TeachersSubjects] CHECK CONSTRAINT [FK_TeachersSubjects_Subjects]
GO
ALTER TABLE [dbo].[TeachersSubjects]  WITH NOCHECK ADD  CONSTRAINT [FK_TeachersSubjects_Teachers] FOREIGN KEY([TeacherId])
REFERENCES [dbo].[Teachers] ([Id])
GO
ALTER TABLE [dbo].[TeachersSubjects] NOCHECK CONSTRAINT [FK_TeachersSubjects_Teachers]
GO
USE [master]
GO
ALTER DATABASE [University] SET  READ_WRITE 
GO
