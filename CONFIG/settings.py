# encoding:utf-8
"""
@file = settings
@author = zouju
@create_time = 2023-08-07- 14:04
"""
import os
import shutil

# 数据库配置, 数据库sql server
server = '10.10.80.124:1433'
database = 'jz_doc_system'
user = 'sa'
password = 'atue_201*'


# MES-对应的数据库配置
mes_server = '192.168.168.251:1433'
mes_database = 'LEANMES_ATUEYW_PROD_8_5_2'
mes_user = 'sa'
mes_password = 'atue_201*'

# 共享盘路径
document_path = r'\\10.10.80.80\share\品质部\体系文件（新）'
server_temp_path = r'\\10.10.80.80\share\临时共享\temp_document'
server_path = r'\\10.10.80.80\share\品质部\体系文件（新）'
lj_path = r'\\10.10.80.80\share\宇视\临技\已处理'
# 极智模板excel
jz_file_path = r'\\10.10.80.80\share\宇视\临技\已转换\lj_model.xlsx'

# 文件路径
path = os.getcwd()
excel_path = fr'{path}\excel'
png_path = fr'{path}\png'
ys_xlsx_file_path = fr'{path}\ys'
download_path = fr'{path}\download'
user_png = fr'{path}\image\user.png'
pic_arrow = fr'{path}\image\arrow.png'


header = ("序号", "文件编号", "文件名称", "版本", "生效日期", "部门", "文件类型", "备注")
header1 = ("序号", "文件编号", "文件名称", "版本", "部门", "签收人", "日期", "份数", "页数", "文件类型",
               "回收", "回收日期", "作废", "作废日期", "备注",)
file_dict = {'二阶文件': 'level2_document', '三阶文件': 'level3_document', '四阶文件': 'level4_document',
                 '外来文件': 'foreign_document', '临时文件': 'temp_document', '文件发放': 'document_issue',
                 '临技文件': 'lj_document', '所有文件': 'all_table'}
depart_dict = {'管理者代表': 'GM', '财务部': 'FN', '计划部': 'PL', '行政部': 'XZ', '工程部': 'PE', '人事部': 'HR',
                   '品管部': 'QC', '采购部': 'PU', '生产部': 'PD', 'OEM业务部': 'PM', '业务部': 'SA', '研发部': 'RD',
                   '维修部': 'WX', 'PE组': 'PE', 'ME组': 'ME', 'IE组': 'IE', 'TE组': 'TE', '文控中心': 'DCC',
                   '生产部SMT': 'SMT', 'SMT工程部': 'SMT', '法务部': 'LW', '其他': '', '体系组': 'TX',
                   '制造中心': 'ZZZX',
                   '': ''}

document_dict = {'二阶文件': 'P', '三阶文件': 'WI', '四阶文件': 'QR'}

approve_file_para = 'ROW_NUMBER() OVER ( ORDER BY ID ) AS row_number,file_name,ID,id_number,send_time,finish_status,Uname'

