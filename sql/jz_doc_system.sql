/*
 Navicat Premium Data Transfer

 Source Server         : 10.10.80.124
 Source Server Type    : SQL Server
 Source Server Version : 11002100
 Source Host           : 10.10.80.124:1433
 Source Catalog        : jz_doc_system
 Source Schema         : dbo

 Target Server Type    : SQL Server
 Target Server Version : 11002100
 File Encoding         : 65001

 Date: 07/08/2023 15:38:34
*/


-- ----------------------------
-- Table structure for approve_file
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[approve_file]') AND type IN ('U'))
	DROP TABLE [dbo].[approve_file]
GO

CREATE TABLE [dbo].[approve_file] (
  [ID] int  NOT NULL,
  [Uname] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_name] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [filepath] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_size] float(53)  NULL,
  [upload_time] datetime  NULL,
  [send_time] datetime  NULL,
  [id_number] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [finish_flag] int  NULL,
  [finish_status] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [server_status] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [server_path] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [popup_flag] int  NULL
)
GO

ALTER TABLE [dbo].[approve_file] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for approve_job
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[approve_job]') AND type IN ('U'))
	DROP TABLE [dbo].[approve_job]
GO

CREATE TABLE [dbo].[approve_job] (
  [job_id] int  NOT NULL,
  [id_number] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user_action] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user_content] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [enter_time] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [finish_flag] int  NULL,
  [approve_level] int  NULL,
  [job_flag] int DEFAULT 0 NULL,
  [idc] int  IDENTITY(1,1) NOT FOR REPLICATION NOT NULL
)
GO

ALTER TABLE [dbo].[approve_job] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for approve_user
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[approve_user]') AND type IN ('U'))
	DROP TABLE [dbo].[approve_user]
GO

CREATE TABLE [dbo].[approve_user] (
  [ID] int  NOT NULL,
  [approve_name] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user1] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user2] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user3] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user4] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user5] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user6] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user7] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user8] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user9] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [user10] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_type] int  NULL
)
GO

ALTER TABLE [dbo].[approve_user] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for cancel_list
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[cancel_list]') AND type IN ('U'))
	DROP TABLE [dbo].[cancel_list]
GO

CREATE TABLE [dbo].[cancel_list] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [cancel_date] datetime  NULL,
  [pro_code] varchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_desc] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_type] varchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_type_cn] nchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [list_file_name] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [remark] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[cancel_list] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for chip_price
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[chip_price]') AND type IN ('U'))
	DROP TABLE [dbo].[chip_price]
GO

CREATE TABLE [dbo].[chip_price] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [create_date] datetime  NULL,
  [pro_code] varchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [chip_price] money  NULL,
  [pro_desc] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_type] nvarchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [remark] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[chip_price] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for dept
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[dept]') AND type IN ('U'))
	DROP TABLE [dbo].[dept]
GO

CREATE TABLE [dbo].[dept] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [parent_id] int  NULL,
  [dept_name] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [type] varchar(5) COLLATE Chinese_PRC_CI_AS  NULL,
  [type_cn] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [leader] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [phone] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [email] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [status] int  NULL,
  [remark] varchar(max) COLLATE Chinese_PRC_CI_AS  NULL,
  [address] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [create_at] datetime  NULL,
  [update_at] datetime  NULL
)
GO

ALTER TABLE [dbo].[dept] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for document_issue
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[document_issue]') AND type IN ('U'))
	DROP TABLE [dbo].[document_issue]
GO

CREATE TABLE [dbo].[document_issue] (
  [ID] int  NOT NULL,
  [file_name] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_code] varchar(100) COLLATE Chinese_PRC_CI_AS  NULL,
  [version] nchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [department] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [receipt_user] nvarchar(100) COLLATE Chinese_PRC_CI_AS  NULL,
  [createdate] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [number] int  NULL,
  [page_number] nvarchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_flag] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [recover_status] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [recoverdate] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [invalid_status] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [invaliddate] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_type] nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT N'文件发放' NULL,
  [remark] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[document_issue] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for exec_log
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[exec_log]') AND type IN ('U'))
	DROP TABLE [dbo].[exec_log]
GO

CREATE TABLE [dbo].[exec_log] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [method] varchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [uid] int  NULL,
  [url] varchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [desc] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [ip] varchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [success] int  NULL,
  [user_agent] varchar(max) COLLATE Chinese_PRC_CI_AS  NULL,
  [create_time] datetime  NULL
)
GO

ALTER TABLE [dbo].[exec_log] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for file_info
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[file_info]') AND type IN ('U'))
	DROP TABLE [dbo].[file_info]
GO

CREATE TABLE [dbo].[file_info] (
  [id] bigint  IDENTITY(1,1) NOT NULL,
  [file_name] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_size] bigint  NULL,
  [upload_time] datetime  NULL,
  [file_is_ok] int  NULL
)
GO

ALTER TABLE [dbo].[file_info] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for foreign_document
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[foreign_document]') AND type IN ('U'))
	DROP TABLE [dbo].[foreign_document]
GO

CREATE TABLE [dbo].[foreign_document] (
  [ID] int  NOT NULL,
  [file_code] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [file_name] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [version] nchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [createdate] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [department] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_type] nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT N'外来文件' NULL,
  [remark] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[foreign_document] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for level2_document
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[level2_document]') AND type IN ('U'))
	DROP TABLE [dbo].[level2_document]
GO

CREATE TABLE [dbo].[level2_document] (
  [ID] int  NOT NULL,
  [file_code] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [file_name] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [version] nchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [createdate] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [department] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_type] nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT N'二阶文件' NULL,
  [remark] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[level2_document] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for level3_document
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[level3_document]') AND type IN ('U'))
	DROP TABLE [dbo].[level3_document]
GO

CREATE TABLE [dbo].[level3_document] (
  [ID] int  NOT NULL,
  [file_code] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [file_name] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [version] nchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [createdate] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [department] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_type] nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT N'三阶文件' NULL,
  [remark] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[level3_document] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for level4_document
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[level4_document]') AND type IN ('U'))
	DROP TABLE [dbo].[level4_document]
GO

CREATE TABLE [dbo].[level4_document] (
  [ID] int  NOT NULL,
  [file_code] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [file_name] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [version] nchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [createdate] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [department] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_flag] nchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [valid] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_type] nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT N'四阶文件' NULL,
  [remark] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[level4_document] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for lj_document
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[lj_document]') AND type IN ('U'))
	DROP TABLE [dbo].[lj_document]
GO

CREATE TABLE [dbo].[lj_document] (
  [ID] int  NOT NULL,
  [file_code] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [product_code] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [rwl] varchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [createdate] datetime  NULL,
  [validdate] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [lj_info] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [station] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [lj_type] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [remark] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_path] nvarchar(100) COLLATE Chinese_PRC_CI_AS  NULL,
  [job_id] int  NULL
)
GO

ALTER TABLE [dbo].[lj_document] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for login_info
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[login_info]') AND type IN ('U'))
	DROP TABLE [dbo].[login_info]
GO

CREATE TABLE [dbo].[login_info] (
  [id_number] varchar(10) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [login_ip] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [login_time] datetime  NULL,
  [login_status] char(10) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[login_info] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for login_log
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[login_log]') AND type IN ('U'))
	DROP TABLE [dbo].[login_log]
GO

CREATE TABLE [dbo].[login_log] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [method] varchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [uid] int  NULL,
  [url] varchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [desc] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [ip] varchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [success] int  NULL,
  [user_agent] varchar(max) COLLATE Chinese_PRC_CI_AS  NULL,
  [create_time] datetime  NULL
)
GO

ALTER TABLE [dbo].[login_log] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for logo
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[logo]') AND type IN ('U'))
	DROP TABLE [dbo].[logo]
GO

CREATE TABLE [dbo].[logo] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [name] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [desc] varchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [type] varchar(1) COLLATE Chinese_PRC_CI_AS  NULL,
  [url] varchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [parent_id] int  NULL,
  [icon] varchar(128) COLLATE Chinese_PRC_CI_AS  NULL,
  [sort] int  NULL
)
GO

ALTER TABLE [dbo].[logo] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for member
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[member]') AND type IN ('U'))
	DROP TABLE [dbo].[member]
GO

CREATE TABLE [dbo].[member] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [id_number] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [id_password] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [name] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [department] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [position] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [role] int  NULL,
  [user_status] int  NULL,
  [email] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO



ALTER TABLE [dbo].[member] SET (LOCK_ESCALATION = TABLE)
GO

-- ----------------------------
-- Records of member
-- ----------------------------
SET IDENTITY_INSERT [dbo].[member] ON
GO

INSERT INTO [dbo].[member] ([id], [id_number], [id_password], [name], [department], [position], [role], [user_status], [email]) VALUES (N'26', N'root', N'63a9f0ea7bb98050796b649e85481845', N'管理员', N'其他', N'管理员', N'1', N'0', NULL)
GO


SET IDENTITY_INSERT [dbo].[member] OFF
GO

-- ----------------------------
-- Auto increment value for member
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[member]', RESEED, 4054)
GO


-- ----------------------------
-- Primary Key structure for table member
-- ----------------------------
ALTER TABLE [dbo].[member] ADD CONSTRAINT [PK_member] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO




-- ----------------------------
-- Table structure for order_price
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[order_price]') AND type IN ('U'))
	DROP TABLE [dbo].[order_price]
GO

CREATE TABLE [dbo].[order_price] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [so_id] varchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [po_id] varchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [rwl] varchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [customer] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_code] varchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_desc] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_ver] varchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [order_num] float(53)  NULL,
  [u9_num] float(53)  NULL,
  [untax_unit_price] float(53)  NULL,
  [unit_price] float(53)  NULL,
  [untaxed_price] float(53)  NULL,
  [tax_price] float(53)  NULL,
  [all_price] float(53)  NULL,
  [order_date] datetime  NULL,
  [status] int DEFAULT 1 NULL
)
GO

ALTER TABLE [dbo].[order_price] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for pcb_scrapy
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[pcb_scrapy]') AND type IN ('U'))
	DROP TABLE [dbo].[pcb_scrapy]
GO

CREATE TABLE [dbo].[pcb_scrapy] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [create_time] datetime  NULL,
  [po_num] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [rwl] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_code] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_desc] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [number] int  NULL,
  [price] float(53)  NULL,
  [sum] float(53)  NULL,
  [protocol_num] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [bill_info] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [po_info] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [remark] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [scrap_flag] int DEFAULT 0 NULL
)
GO

ALTER TABLE [dbo].[pcb_scrapy] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for power
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[power]') AND type IN ('U'))
	DROP TABLE [dbo].[power]
GO

CREATE TABLE [dbo].[power] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [name] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [type] varchar(1) COLLATE Chinese_PRC_CI_AS  NULL,
  [code] varchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [url] varchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [open_type] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [parent_id] int  NULL,
  [icon] varchar(128) COLLATE Chinese_PRC_CI_AS  NULL,
  [sort] int  NULL,
  [create_time] datetime  NULL,
  [update_time] datetime  NULL,
  [enable] int  NULL
)
GO

ALTER TABLE [dbo].[power] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for rma_file
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[rma_file]') AND type IN ('U'))
	DROP TABLE [dbo].[rma_file]
GO

CREATE TABLE [dbo].[rma_file] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [upload_time] datetime  NULL,
  [file_name] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [file_type] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [finish_flag] int  NULL
)
GO

ALTER TABLE [dbo].[rma_file] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for rma_repair
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[rma_repair]') AND type IN ('U'))
	DROP TABLE [dbo].[rma_repair]
GO

CREATE TABLE [dbo].[rma_repair] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [order_date] date  NULL,
  [post_date] date  NULL,
  [so_num] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [po_num] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [rwl] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_code] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_desc] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [pro_ver] varchar(5) COLLATE Chinese_PRC_CI_AS  NULL,
  [order_num] int  NULL,
  [rec_num] int  NULL,
  [u9_num] int DEFAULT 0 NULL,
  [unsend_num] int  NULL,
  [scrap_num] int DEFAULT 0 NULL,
  [diff_num] int  NULL,
  [diff_desc] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [special_desc] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [remark] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [u9_remark] ntext COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[rma_repair] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for role
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[role]') AND type IN ('U'))
	DROP TABLE [dbo].[role]
GO

CREATE TABLE [dbo].[role] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [role_value] int  NULL,
  [name] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [code] varchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [enable] int  NULL,
  [remark] nvarchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [details] varchar(255) COLLATE Chinese_PRC_CI_AS  NULL,
  [sort] int  NULL,
  [create_time] datetime  NULL,
  [update_time] datetime  NULL
)
GO

ALTER TABLE [dbo].[role] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for role_power
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[role_power]') AND type IN ('U'))
	DROP TABLE [dbo].[role_power]
GO

CREATE TABLE [dbo].[role_power] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [role_id] int  NULL,
  [power_id] int  NULL,
  [power_type] varchar(10) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[role_power] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for soft_info
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[soft_info]') AND type IN ('U'))
	DROP TABLE [dbo].[soft_info]
GO

CREATE TABLE [dbo].[soft_info] (
  [ID] int  NOT NULL,
  [SoftID] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [SoftCode] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [SoftDescrip] ntext COLLATE Chinese_PRC_CI_AS  NULL,
  [ChipCode] varchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [ChipDescrip] ntext COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[soft_info] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for software
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[software]') AND type IN ('U'))
	DROP TABLE [dbo].[software]
GO

CREATE TABLE [dbo].[software] (
  [id] int  IDENTITY(1,1) NOT NULL,
  [create_time] datetime  NULL,
  [mo_id] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [number] int  NULL,
  [pro_code] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [material_code] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [material_info] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [device_code] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [soft_info] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [check_code] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [solder] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [checker] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [soft_remark] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [remark] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [checker_time] datetime  NULL,
  [checker_status] int DEFAULT 0 NULL
)
GO

ALTER TABLE [dbo].[software] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Table structure for temp_document
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[temp_document]') AND type IN ('U'))
	DROP TABLE [dbo].[temp_document]
GO

CREATE TABLE [dbo].[temp_document] (
  [ID] int  NOT NULL,
  [file_code] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NOT NULL,
  [file_name] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [version] nchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [createdate] varchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [department] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [file_type] nvarchar(50) COLLATE Chinese_PRC_CI_AS DEFAULT N'临时文件' NULL,
  [remark] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL
)
GO

ALTER TABLE [dbo].[temp_document] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- View structure for View_1
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[View_1]') AND type IN ('V'))
	DROP VIEW [dbo].[View_1]
GO

CREATE VIEW [dbo].[View_1] AS SELECT   TOP (100) PERCENT ID, Uname, file_name, filepath, file_size, upload_time, send_time, id_number, finish_flag, 
                finish_status, server_status, server_path, popup_flag, ID AS Expr1, finish_flag AS Expr2, send_time AS Expr3
FROM      dbo.approve_file
WHERE   (finish_flag <> N'1') AND (send_time IS NOT NULL) AND (finish_flag <> N'2')
ORDER BY Expr1
GO


-- ----------------------------
-- View structure for VIEW_FILE_3000
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[VIEW_FILE_3000]') AND type IN ('V'))
	DROP VIEW [dbo].[VIEW_FILE_3000]
GO

CREATE VIEW [dbo].[VIEW_FILE_3000] AS SELECT   dbo.approve_file.ID AS Expr1, dbo.approve_job.id_number AS Expr2, dbo.approve_job.user_action AS Expr3, 
                dbo.approve_job.user_content AS Expr4, dbo.approve_job.enter_time, dbo.approve_job.finish_flag
FROM      dbo.approve_file INNER JOIN
                dbo.approve_job ON dbo.approve_file.ID = dbo.approve_job.job_id
WHERE   (dbo.approve_file.ID > 3000)
GO


-- ----------------------------
-- View structure for View_wait_approve
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[View_wait_approve]') AND type IN ('V'))
	DROP VIEW [dbo].[View_wait_approve]
GO

CREATE VIEW [dbo].[View_wait_approve] AS SELECT   TOP (100) PERCENT dbo.approve_file.*, ID AS Expr1, finish_flag AS Expr2, send_time AS Expr3
FROM      dbo.approve_file
WHERE   (finish_flag <> N'1' AND finish_flag <> N'2') AND (send_time IS NOT NULL)
ORDER BY Expr1
GO


-- ----------------------------
-- procedure structure for FileInfoProc1
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[FileInfoProc1]') AND type IN ('P', 'PC', 'RF', 'X'))
	DROP PROCEDURE[dbo].[FileInfoProc1]
GO

CREATE PROCEDURE [dbo].[FileInfoProc1]
@sid int
as
SELECT * FROM file_info where id=@sid
GO


-- ----------------------------
-- Indexes structure for table approve_file
-- ----------------------------
CREATE UNIQUE CLUSTERED INDEX [ClusteredIndex-id]
ON [dbo].[approve_file] (
  [ID] ASC
)  
FILESTREAM_ON [NULL]
GO


-- ----------------------------
-- Primary Key structure for table approve_file
-- ----------------------------
ALTER TABLE [dbo].[approve_file] ADD CONSTRAINT [PK_approve_file] PRIMARY KEY NONCLUSTERED ([ID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for approve_job
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[approve_job]', RESEED, 40218)
GO


-- ----------------------------
-- Indexes structure for table approve_job
-- ----------------------------
CREATE CLUSTERED INDEX [ClusteredIndex-id]
ON [dbo].[approve_job] (
  [job_id] ASC
)  
FILESTREAM_ON [NULL]
GO


-- ----------------------------
-- Primary Key structure for table approve_job
-- ----------------------------
ALTER TABLE [dbo].[approve_job] ADD CONSTRAINT [PK_approve_job] PRIMARY KEY NONCLUSTERED ([idc])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Primary Key structure for table approve_user
-- ----------------------------
ALTER TABLE [dbo].[approve_user] ADD CONSTRAINT [PK_approve_user] PRIMARY KEY CLUSTERED ([ID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for cancel_list
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[cancel_list]', RESEED, 3507)
GO


-- ----------------------------
-- Primary Key structure for table cancel_list
-- ----------------------------
ALTER TABLE [dbo].[cancel_list] ADD CONSTRAINT [PK__cancel_l__3213E83FAA7FC570] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for chip_price
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[chip_price]', RESEED, 78)
GO


-- ----------------------------
-- Primary Key structure for table chip_price
-- ----------------------------
ALTER TABLE [dbo].[chip_price] ADD CONSTRAINT [PK__chip_pri__3213E83F97791635] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for dept
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[dept]', RESEED, 35)
GO


-- ----------------------------
-- Primary Key structure for table dept
-- ----------------------------
ALTER TABLE [dbo].[dept] ADD CONSTRAINT [PK__dept__3213E83FA85BB817] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for exec_log
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[exec_log]', RESEED, 31066)
GO


-- ----------------------------
-- Primary Key structure for table exec_log
-- ----------------------------
ALTER TABLE [dbo].[exec_log] ADD CONSTRAINT [PK__exec_log__3213E83F30E98A0F] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for file_info
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[file_info]', RESEED, 345848)
GO


-- ----------------------------
-- Primary Key structure for table file_info
-- ----------------------------
ALTER TABLE [dbo].[file_info] ADD CONSTRAINT [PK_file_info] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Primary Key structure for table foreign_document
-- ----------------------------
ALTER TABLE [dbo].[foreign_document] ADD CONSTRAINT [PK_foreign_document] PRIMARY KEY CLUSTERED ([ID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Indexes structure for table level2_document
-- ----------------------------
CREATE UNIQUE CLUSTERED INDEX [ClusteredIndex-id]
ON [dbo].[level2_document] (
  [ID] ASC
)  
FILESTREAM_ON [NULL]
GO


-- ----------------------------
-- Primary Key structure for table level2_document
-- ----------------------------
ALTER TABLE [dbo].[level2_document] ADD CONSTRAINT [PK_level2_document] PRIMARY KEY NONCLUSTERED ([ID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Indexes structure for table level3_document
-- ----------------------------
CREATE UNIQUE CLUSTERED INDEX [ClusteredIndex-id]
ON [dbo].[level3_document] (
  [ID] ASC
)  
FILESTREAM_ON [NULL]
GO


-- ----------------------------
-- Primary Key structure for table level3_document
-- ----------------------------
ALTER TABLE [dbo].[level3_document] ADD CONSTRAINT [PK_level3_document] PRIMARY KEY NONCLUSTERED ([ID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Indexes structure for table level4_document
-- ----------------------------
CREATE UNIQUE CLUSTERED INDEX [ClusteredIndex-id]
ON [dbo].[level4_document] (
  [ID] ASC
)  
FILESTREAM_ON [NULL]
GO


-- ----------------------------
-- Primary Key structure for table level4_document
-- ----------------------------
ALTER TABLE [dbo].[level4_document] ADD CONSTRAINT [PK_level4_document] PRIMARY KEY NONCLUSTERED ([ID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for login_log
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[login_log]', RESEED, 30151)
GO


-- ----------------------------
-- Primary Key structure for table login_log
-- ----------------------------
ALTER TABLE [dbo].[login_log] ADD CONSTRAINT [PK__login_lo__3213E83F139A55E1] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for logo
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[logo]', RESEED, 3)
GO


-- ----------------------------
-- Primary Key structure for table logo
-- ----------------------------
ALTER TABLE [dbo].[logo] ADD CONSTRAINT [PK__logo__3213E83F00F88660] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for member
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[member]', RESEED, 4054)
GO


-- ----------------------------
-- Primary Key structure for table member
-- ----------------------------
ALTER TABLE [dbo].[member] ADD CONSTRAINT [PK_member] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for order_price
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[order_price]', RESEED, 7193)
GO


-- ----------------------------
-- Primary Key structure for table order_price
-- ----------------------------
ALTER TABLE [dbo].[order_price] ADD CONSTRAINT [PK__order_pr__3213E83FA108D881] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for pcb_scrapy
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[pcb_scrapy]', RESEED, 17757)
GO


-- ----------------------------
-- Primary Key structure for table pcb_scrapy
-- ----------------------------
ALTER TABLE [dbo].[pcb_scrapy] ADD CONSTRAINT [PK__pcb_scra__3213E83FDE845F6E] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for power
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[power]', RESEED, 3106)
GO


-- ----------------------------
-- Primary Key structure for table power
-- ----------------------------
ALTER TABLE [dbo].[power] ADD CONSTRAINT [PK__power__3213E83F8E88F370] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for rma_file
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[rma_file]', RESEED, 10145)
GO


-- ----------------------------
-- Primary Key structure for table rma_file
-- ----------------------------
ALTER TABLE [dbo].[rma_file] ADD CONSTRAINT [PK__rma_file__3213E83F2C6164E3] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for rma_repair
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[rma_repair]', RESEED, 14079)
GO


-- ----------------------------
-- Primary Key structure for table rma_repair
-- ----------------------------
ALTER TABLE [dbo].[rma_repair] ADD CONSTRAINT [PK__rma_repa__3213E83F39E7280F] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for role
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[role]', RESEED, 10)
GO


-- ----------------------------
-- Primary Key structure for table role
-- ----------------------------
ALTER TABLE [dbo].[role] ADD CONSTRAINT [PK__role__3213E83FAD681C24] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for role_power
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[role_power]', RESEED, 4724)
GO


-- ----------------------------
-- Primary Key structure for table role_power
-- ----------------------------
ALTER TABLE [dbo].[role_power] ADD CONSTRAINT [PK__role_pow__3213E83FB0C89C4C] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Auto increment value for software
-- ----------------------------
DBCC CHECKIDENT ('[dbo].[software]', RESEED, 26198)
GO


-- ----------------------------
-- Primary Key structure for table software
-- ----------------------------
ALTER TABLE [dbo].[software] ADD CONSTRAINT [PK__software__3213E83FFD80B10A] PRIMARY KEY CLUSTERED ([id])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Indexes structure for table temp_document
-- ----------------------------
CREATE UNIQUE CLUSTERED INDEX [ClusteredIndex-id]
ON [dbo].[temp_document] (
  [ID] ASC
)  
FILESTREAM_ON [NULL]
GO


-- ----------------------------
-- Primary Key structure for table temp_document
-- ----------------------------
ALTER TABLE [dbo].[temp_document] ADD CONSTRAINT [PK_temp_document] PRIMARY KEY NONCLUSTERED ([ID])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO

