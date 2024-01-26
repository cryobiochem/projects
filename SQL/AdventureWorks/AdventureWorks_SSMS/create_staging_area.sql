/* Script to create staging area for AdventureWorks */
use [master]
go

create database [AW_staging]
go

use [AW_staging]
GO

/****** Create entity relationship procedure schema ******/
CREATE SCHEMA [erp]
GO

/****** Create schema for HR specific tables ******/
CREATE SCHEMA [hr]
GO

/****** Business Entity table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [erp].[Business_Entity](
									[rowguid] uniqueidentifier NULL,
									[ModifiedDate] datetime NULL,
									[BusinessEntityID] int NULL,
									[Created_Dt] datetime NULL,
									[SSISTrackId] int NULL
) ON [PRIMARY]

GO

/****** Currency table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [erp].[Currency](
								[CurrencyCode] nvarchar(3) NULL,
								[Name] nvarchar(50) NULL,
								[ModifiedDate] datetime NULL,
								[Created_Dt] datetime NULL,
								[SSISTrackId] int NULL
) ON [PRIMARY]

GO

/****** Customer table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [erp].[Customer](
							[CustomerID] int NULL,
							[PersonID] int NULL,
							[StoreID] int NULL,
							[TerritoryID] int NULL,
							[AccountNumber] varchar(10) NULL,
							[rowguid] uniqueidentifier NULL,
							[ModifiedDate] datetime NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO

/****** Person table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [erp].[Person](
							[rowguid] uniqueidentifier NULL,
							[ModifiedDate] datetime NULL,
							[BusinessEntityID] int NULL,
							[PersonType] nvarchar(2) NULL,
							[NameStyle] bit NULL,
							[Title] nvarchar(8) NULL,
							[FirstName] nvarchar(50) NULL,
							[MiddleName] nvarchar(50) NULL,
							[LastName] nvarchar(50) NULL,
							[Suffix] nvarchar(10) NULL,
							[EmailPromotion] int NULL,
							[AdditionalContactInfo] nvarchar(max) NULL,
							[Demographics] nvarchar(max) NULL,
							[Created_Dt] datetime NULL,
							[SSISTrackId] int NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

/****** Person Address table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [erp].[PersonAddress](
									[BusinessEntityID] int NULL,
									[AddressID] int NULL,
									[AddressTypeID] int NULL,
									[rowguid] uniqueidentifier NULL,
									[ModifiedDate] datetime NULL,
									[AddressLine1] nvarchar(60) NULL,
									[City] nvarchar(30) NULL,
									[PostalCode] nvarchar(15) NULL,
									[StateProvinceID] int NULL,
									[Created_Dt] datetime NULL,
									[SSISTrackId] int NULL
) ON [PRIMARY]

GO

/****** Product table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [erp].[Product](
							[ProductID] int NULL,
							[Name] nvarchar(50) NULL,
							[ProductNumber] nvarchar(25) NULL,
							[MakeFlag] bit NULL,
							[FinishedGoodsFlag] bit NULL,
							[Color] nvarchar(15) NULL,
							[SafetyStockLevel] smallint NULL,
							[ReorderPoint] smallint NULL,
							[StandardCost] money NULL,
							[ListPrice] money NULL,
							[Size] nvarchar(5) NULL,
							[SizeUnitMeasureCode] nvarchar(3) NULL,
							[WeightUnitMeasureCode] nvarchar(3) NULL,
							[Weight] numeric(8, 2) NULL,
							[DaysToManufacture] int NULL,
							[ProductLine] nvarchar(2) NULL,
							[Class] nvarchar(2) NULL,
							[Style] nvarchar(2) NULL,
							[ProductSubcategoryID] int NULL,
							[ProductModelID] int NULL,
							[SellStartDate] datetime NULL,
							[SellEndDate] datetime NULL,
							[DiscontinuedDate] datetime NULL,
							[rowguid] uniqueidentifier NULL,
							[ModifiedDate] datetime NULL,
							[Created_Dt] datetime NULL,
							[SSISTrackId] int NULL
) ON [PRIMARY]

GO

/****** Product Category table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [erp].[ProductCategory](
									[ModifiedDate] datetime NULL,
									[ProductCategoryID] int NULL,
									[Name] nvarchar(50) NULL,
									[rowguid] uniqueidentifier NULL,
									[Created_Dt] datetime NULL,
									[SSISTrackId] int NULL
) ON [PRIMARY]

GO

/****** Product Sub-Category table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [erp].[ProductSubCategory](
										[ProductSubcategoryID] int NULL,
										[ProductCategoryID] int NULL,
										[Name] nvarchar(50) NULL
) ON [PRIMARY]

GO

/****** Sales Header table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [erp].[SalesHeader](
								[SalesOrderID] int NULL,
								[rowguid] uniqueidentifier NULL,
								[ModifiedDate] datetime NULL,
								[RevisionNumber] tinyint NULL,
								[OrderDate] datetime NULL,
								[DueDate] datetime NULL,
								[ShipDate] datetime NULL,
								[Status] tinyint NULL,
								[OnlineOrderFlag] bit NULL,
								[SalesOrderNumber] nvarchar(25) NULL,
								[PurchaseOrderNumber] nvarchar(25) NULL,
								[AccountNumber] nvarchar(15) NULL,
								[CustomerID] int NULL,
								[SalesPersonID] int NULL,
								[TerritoryID] int NULL,
								[BillToAddressID] int NULL,
								[ShipToAddressID] int NULL,
								[ShipMethodID] int NULL,
								[CreditCardID] int NULL,
								[CreditCardApprovalCode] varchar(15) NULL,
								[CurrencyRateID] int NULL,
								[SubTotal] money NULL,
								[TaxAmt] money NULL,
								[Freight] money NULL,
								[TotalDue] money NULL,
								[Comment] nvarchar(128) NULL,
								[SSIS_ID] bigint NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO

/****** Sales Order Detail table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [erp].[SalesOrderDetail](
										[SalesOrderID] int NULL,
										[SalesOrderDetailID] int NULL,
										[CarrierTrackingNumber] nvarchar(25) NULL,
										[OrderQty] smallint NULL,
										[ProductID] int NULL,
										[SpecialOfferID] int NULL,
										[UnitPrice] money NULL,
										[UnitPriceDiscount] money NULL,
										[LineTotal] numeric(38, 6) NULL,
										[rowguid] uniqueidentifier NULL,
										[ModifiedDate] datetime NULL,
										[Created_Dt] datetime NULL,
										[SSISTrackId] int NULL
) ON [PRIMARY]

GO
/****** Sales Territory table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [erp].[SalesTerritory](
									[TerritoryID] int NULL,
									[Name] nvarchar(50) NULL,
									[CountryRegionCode] nvarchar(3) NULL,
									[Group] nvarchar(50) NULL
) ON [PRIMARY]

GO

/****** Store table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [erp].[Store](
							[rowguid] uniqueidentifier NULL,
							[ModifiedDate] datetime NULL,
							[Name] nvarchar(50) NULL,
							[Demographics] nvarchar(max) NULL,
							[BusinessEntityID] int NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

/****** Object:  HR Employee table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [hr].[Employee](
							[BusinessEntityID] int NULL,
							[NationalIDNumber] nvarchar(15) NULL,
							[LoginID] nvarchar(256) NULL,
							[OrganizationNode] binary(892) NULL,
							[OrganizationLevel] smallint NULL,
							[JobTitle] nvarchar(50) NULL,
							[BirthDate] date NULL,
							[MaritalStatus] nvarchar(1) NULL,
							[Gender] nvarchar(1) NULL,
							[HireDate] date NULL,
							[SalariedFlag] bit NULL,
							[VacationHours] smallint NULL,
							[SickLeaveHours] smallint NULL,
							[CurrentFlag] bit NULL,
							[rowguid] uniqueidentifier NULL,
							[ModifiedDate] datetime NULL,
							[Created_Dt] datetime NULL,
							[SSISTrackId] int NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO

/****** HR Employee Department History table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [hr].[EmployeeDepartmentHistory](
												[BusinessEntityID] int NULL,
												[DepartmentID] smallint NULL,
												[ShiftID] tinyint NULL,
												[StartDate] date NULL,
												[EndDate] date NULL,
												[ModifiedDate] datetime NULL,
												[DepartmentName] nvarchar(50) NULL,
												[Created_Dt] datetime NULL,
												[SSISTrackId] int NULL
) ON [PRIMARY]

GO

/****** HR Employee Pay History table ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [hr].[EmployeePayHistory](
										[BusinessEntityID] int NULL,
										[RateChangeDate] datetime NULL,
										[Rate] money NULL,
										[PayFrequency] tinyint NULL,
										[ModifiedDate] datetime NULL
) ON [PRIMARY]