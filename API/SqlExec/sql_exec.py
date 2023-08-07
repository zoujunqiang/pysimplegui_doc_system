# encoding:utf-8
"""
@file = sql_exec
@author = zouju
@create_time = 2023-08-07- 13:49
"""

import pymssql
import PySimpleGUI as sg
from API.Log.log import logger
from CONFIG.settings import *
from pymssql import _mssql
from pymssql import _pymssql



def get_db_table(sql):
    table_db = []  # 先清空
    res = exec_sql_server_utf8(sql)
    for i in range(len(res)):
        item = res[i]
        item1 = list(item)
        table_db.append(item1)
    return table_db


def get_db_table_mes(sql):
    table_db = []  # 先清空
    res = exec_sql_server_mes(sql)
    for i in range(len(res)):
        item = res[i]
        item1 = list(item)
        table_db.append(item1)
    return table_db


def table_max_id(table):
    sql_maxvalue = f"SELECT MAX(ID) FROM {table}"
    res_maxvalue = exec_sql_server(sql_maxvalue)
    if res_maxvalue[0][0] is None:
        id_value = 1
    else:
        id_value = int(res_maxvalue[0][0]) + 1
    return id_value


def exec_sql_server(sql):
    try:
        logger.info(f'查询SQL:{sql}')
        print(f'查询SQL:{sql}')
        db = pymssql.connect(server, user, password, database, charset='cp936')  # 连接到sql server数据库 charset='utf8'
        cur = db.cursor()  # 获取该数据库连接下的环境变量
        cur.execute(sql)  # 执行语句

    except Exception as e:
        sg.popup_error(e, font=('宋体', 18))

    else:
        result = cur.fetchall()  # get result
        print(result)
        db.commit()  # 一定要commit，pymssql包默认是需要手动commit的，否则事务不生效
        db.close()  # 关闭数据库连接
        return result


def exec_sql_server_utf8(sql):
    try:
        logger.info(f'查询SQL:{sql}')
        print(f'查询SQL:{sql}')
        db = pymssql.connect(server, user, password, database, charset='utf8')  # 连接到sql server数据库 charset='utf8'
        cur = db.cursor()  # 获取该数据库连接下的环境变量
        cur.execute(sql)  # 执行语句

    except Exception as e:
        sg.popup_error(e, font=('宋体', 18))

    else:
        result = cur.fetchall()  # get result
        db.commit()  # 一定要commit，pymssql包默认是需要手动commit的，否则事务不生效
        db.close()  # 关闭数据库连接
        return result


def exec_sql_server_utf8_no_log(sql):
    try:
        db = pymssql.connect(server, user, password, database, charset='utf8')  # 连接到sql server数据库 charset='utf8'
        cur = db.cursor()  # 获取该数据库连接下的环境变量
        cur.execute(sql)  # 执行语句

    except Exception as e:
        sg.popup_error(e, font=('宋体', 18))

    else:
        result = cur.fetchall()  # get result
        db.commit()  # 一定要commit，pymssql包默认是需要手动commit的，否则事务不生效
        db.close()  # 关闭数据库连接
        return result


def update_sql_server(sql):
    global res_flag
    res_flag = 1

    try:
        logger.info(f'更新SQL:{sql}')
        print(f'更新SQL:{sql}')
        db = pymssql.connect(server, user, password, database, charset='utf8')  # 连接到sql server数据库 charset='utf8'
        cur = db.cursor()  # 获取该数据库连接下的环境变量
        cur.execute(sql)  # 执行语句
        res_flag = 1

    except Exception as e:
        res_flag = 0
        sg.popup_error(e, font=('宋体', 18))

    else:
        db.commit()  # 一定要commit，pymssql包默认是需要手动commit的，否则事务不生效
        db.close()  # 关闭数据库连接
        if res_flag == 1:
            return 1
        else:
            return 0


def exec_sql_server_mes(sql):
    try:
        logger.info(f'查询SQL-MES:{sql}')
        print(f'查询SQL-MES:{sql}')
        db = pymssql.connect(mes_server, mes_user, mes_password, mes_database, charset='utf8')
        cur = db.cursor()  # 获取该数据库连接下的环境变量
        cur.execute(sql)  # 执行语句

    except Exception as e:
        sg.popup_error(e, font=('宋体', 18))

    else:
        result = cur.fetchall()  # get result
        db.commit()  # 一定要commit，pymssql包默认是需要手动commit的，否则事务不生效
        db.close()  # 关闭数据库连接
        return result


def update_sql_server_mes(sql):
    global res_flag
    res_flag = 1
    try:
        logger.info(f'更新SQL-MES:{sql}')
        print(f'更新SQL-MES:{sql}')
        db = pymssql.connect(mes_server, mes_user, mes_password, mes_database, charset='utf8')
        cur = db.cursor()  # 获取该数据库连接下的环境变量
        cur.execute(sql)  # 执行语句
        res_flag = 1

    except Exception as e:
        res_flag = 0
        sg.popup_error(e, font=('宋体', 18))

    else:
        db.commit()  # 一定要commit，pymssql包默认是需要手动commit的，否则事务不生效
        db.close()  # 关闭数据库连接
        if res_flag == 1:
            return 1
        else:
            return 0


def document_issue_sql(department, filecode, filename, remark_info):
    data_table = 'document_issue'
    col_para = 'ROW_NUMBER() OVER ( ORDER BY ID ) AS row_number,file_code,file_name,version,department,' \
               'receipt_user,createdate,number,page_number,file_flag,recover_status,recoverdate,' \
               'invalid_status,invaliddate,remark '

    if department == '' and filecode == '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} "

    elif department != '' and filecode == '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' "

    elif department == '' and filecode != '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' "

    elif department == '' and filecode == '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_name like '%{filename}%' "

    elif department == '' and filecode == '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where remark like '%{remark_info}%' "

    elif department != '' and filecode != '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and file_code like '%{filecode}%' "

    elif department != '' and filecode == '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and file_name like '%{filename}%' "

    elif department != '' and filecode == '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode != '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' and file_name like '%{filename}%' "

    elif department == '' and filecode != '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode == '' and filename != '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_name like '%{filename}%' and remark like '%{remark_info}%' "

    elif department != '' and filecode != '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and " \
              f"file_code like '%{filecode}%' and file_name like '%{filename}%' "

    elif department != '' and filecode != '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and " \
              f"file_code like '%{filecode}%' and remark like '%{remark_info}%' "

    elif department != '' and filecode == '' and filename != '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and " \
              f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode != '' and filename != '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' and " \
              f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    else:
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and file_code like '%{filecode}%' and " \
              f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    return sql


def all_table_sql(department, filecode, filename, remark_info):
    col_para = 'ROW_NUMBER() OVER ( ORDER BY ID ) AS row_number,file_code,file_name,' \
               'version,createdate,department,file_type,remark '
    col_para1 = 'ID, file_code,file_name,version,createdate,department,file_type,remark'

    sql_select = f"select {col_para} from " \
                 f"(SELECT {col_para1} FROM level2_document " \
                 f"UNION SELECT {col_para1} FROM level3_document " \
                 f"UNION SELECT {col_para1} FROM level4_document " \
                 f"UNION SELECT {col_para1} FROM foreign_document " \
                 f"UNION SELECT {col_para1} FROM temp_document " \
                 f"UNION SELECT {col_para1} FROM document_issue) as a "

    if department == '' and filecode == '' and filename == '' and remark_info == '':
        sql = sql_select

    elif department != '' and filecode == '' and filename == '' and remark_info == '':
        sql = sql_select + f"where department LIKE '%{department}%' "

    elif department == '' and filecode != '' and filename == '' and remark_info == '':
        sql = sql_select + f"where file_code like '%{filecode}%' "

    elif department == '' and filecode == '' and filename != '' and remark_info == '':
        sql = sql_select + f"where file_name like '%{filename}%' "

    elif department == '' and filecode == '' and filename == '' and remark_info != '':
        sql = sql_select + f"where remark like '%{remark_info}%' "

    elif department != '' and filecode != '' and filename == '' and remark_info == '':
        sql = sql_select + f"where department LIKE '%{department}%' and file_code like '%{filecode}%' "

    elif department != '' and filecode == '' and filename != '' and remark_info == '':
        sql = sql_select + f"where department LIKE '%{department}%' and file_name like '%{filename}%' "

    elif department != '' and filecode == '' and filename == '' and remark_info != '':
        sql = sql_select + f"where department LIKE '%{department}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode != '' and filename != '' and remark_info == '':
        sql = sql_select + f"where file_code like '%{filecode}%' and file_name like '%{filename}%' "

    elif department == '' and filecode != '' and filename == '' and remark_info != '':
        sql = sql_select + f"where file_code like '%{filecode}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode == '' and filename != '' and remark_info != '':
        sql = sql_select + f"where file_name like '%{filename}%' and remark like '%{remark_info}%' "

    elif department != '' and filecode != '' and filename != '' and remark_info == '':
        sql = sql_select + f"where department LIKE '%{department}%' and " \
                           f"file_code like '%{filecode}%' and file_name like '%{filename}%' "

    elif department != '' and filecode != '' and filename == '' and remark_info != '':
        sql = sql_select + f"where department LIKE '%{department}%' and " \
                           f"file_code like '%{filecode}%' and remark like '%{remark_info}%' "

    elif department != '' and filecode == '' and filename != '' and remark_info != '':
        sql = sql_select + f"where department LIKE '%{department}%' and " \
                           f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode != '' and filename != '' and remark_info != '':
        sql = sql_select + f"where file_code like '%{filecode}%' and " \
                           f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    else:
        sql = sql_select + f"where department LIKE '%{department}%' and file_code like '%{filecode}%' and " \
                           f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    return sql


def other_table_sql(data_table, department, filecode, filename, remark_info):  # department-部门简写

    col_para = 'ROW_NUMBER() OVER ( ORDER BY ID ) AS row_number,file_code,file_name,' \
               'version,createdate,department,file_type,remark '

    if department == '' and filecode == '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} "

    elif department != '' and filecode == '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' "

    elif department == '' and filecode != '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' "

    elif department == '' and filecode == '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_name like '%{filename}%' "

    elif department == '' and filecode == '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where remark like '%{remark_info}%' "

    elif department != '' and filecode != '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and file_code like '%{filecode}%' "

    elif department != '' and filecode == '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and file_name like '%{filename}%' "

    elif department != '' and filecode == '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode != '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' and file_name like '%{filename}%' "

    elif department == '' and filecode != '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode == '' and filename != '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_name like '%{filename}%' and remark like '%{remark_info}%' "

    elif department != '' and filecode != '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and " \
              f"file_code like '%{filecode}%' and file_name like '%{filename}%' "

    elif department != '' and filecode != '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and " \
              f"file_code like '%{filecode}%' and remark like '%{remark_info}%' "

    elif department != '' and filecode == '' and filename != '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and " \
              f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode != '' and filename != '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' and " \
              f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    else:
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and file_code like '%{filecode}%' and " \
              f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    return sql


def flush_display(data_table, department, filecode, filename, remark_info):
    global list_table_db
    col_para = 'ID, file_code,file_name,version,createdate,department,file_type,remark'
    if data_table == '':
        data_table = 'level2_document'

    if department == '' and filecode == '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} ORDER BY ID"

    elif department != '' and filecode == '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' ORDER BY ID"

    elif department == '' and filecode != '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' ORDER BY ID"

    elif department == '' and filecode == '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_name like '%{filename}%' ORDER BY ID"

    elif department == '' and filecode == '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where remark like '%{remark_info}%' ORDER BY ID"

    elif department != '' and filecode != '' and filename == '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and file_code like '%{filecode}%' " \
              f"ORDER BY ID"

    elif department != '' and filecode == '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and file_name like '%{filename}%' " \
              f"ORDER BY ID"

    elif department != '' and filecode == '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and remark like '%{remark_info}%' " \
              f"ORDER BY ID"

    elif department == '' and filecode != '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' and file_name like '%{filename}%' " \
              f"ORDER BY ID"

    elif department == '' and filecode != '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' and remark like '%{remark_info}%' " \
              f"ORDER BY ID"

    elif department == '' and filecode == '' and filename != '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_name like '%{filename}%' and remark like '%{remark_info}%' " \
              f"ORDER BY ID"

    elif department != '' and filecode != '' and filename != '' and remark_info == '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and " \
              f"file_code like '%{filecode}%' and file_name like '%{filename}%' " \
              f"ORDER BY ID"

    elif department != '' and filecode != '' and filename == '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and " \
              f"file_code like '%{filecode}%' and remark like '%{remark_info}%' " \
              f"ORDER BY ID"

    elif department != '' and filecode == '' and filename != '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and " \
              f"file_name like '%{filename}%' and remark like '%{remark_info}%' " \
              f"ORDER BY ID"

    elif department == '' and filecode != '' and filename != '' and remark_info != '':
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where file_code like '%{filecode}%' and " \
              f"file_name like '%{filename}%' and remark like '%{remark_info}%' " \
              f"ORDER BY ID"

    else:
        sql = f"SELECT {col_para} FROM {data_table} " \
              f"where department LIKE '%{department}%' and file_code like '%{filecode}%' and " \
              f"file_name like '%{filename}%' and remark like '%{remark_info}%' " \
              f"ORDER BY ID"
    try:
        list_table_db = get_db_table(sql)
        # window1['-TABLE-'].update(values=list_table_db)

    except Exception as results:
        sg.popup_error(results, font=('宋体', 18))


def flush_all_display(department, filecode, filename, remark_info):
    global list_table_db

    col_para1 = 'ID, file_code,file_name,version,createdate,department,file_type,remark'

    sql_select = f"select {col_para1} from " \
                 f"(SELECT {col_para1} FROM level2_document " \
                 f"UNION SELECT {col_para1} FROM level3_document " \
                 f"UNION SELECT {col_para1} FROM level4_document " \
                 f"UNION SELECT {col_para1} FROM foreign_document " \
                 f"UNION SELECT {col_para1} FROM temp_document " \
                 f"UNION SELECT {col_para1} FROM document_issue ) as a "

    if department == '' and filecode == '' and filename == '' and remark_info == '':
        sql = sql_select

    elif department != '' and filecode == '' and filename == '' and remark_info == '':
        sql = sql_select + f"where department LIKE '%{department}%' "

    elif department == '' and filecode != '' and filename == '' and remark_info == '':
        sql = sql_select + f"where file_code like '%{filecode}%' "

    elif department == '' and filecode == '' and filename != '' and remark_info == '':
        sql = sql_select + f"where file_name like '%{filename}%' "

    elif department == '' and filecode == '' and filename == '' and remark_info != '':
        sql = sql_select + f"where remark like '%{remark_info}%' "

    elif department != '' and filecode != '' and filename == '' and remark_info == '':
        sql = sql_select + f"where department LIKE '%{department}%' and file_code like '%{filecode}%' "

    elif department != '' and filecode == '' and filename != '' and remark_info == '':
        sql = sql_select + f"where department LIKE '%{department}%' and file_name like '%{filename}%' "

    elif department != '' and filecode == '' and filename == '' and remark_info != '':
        sql = sql_select + f"where department LIKE '%{department}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode != '' and filename != '' and remark_info == '':
        sql = sql_select + f"where file_code like '%{filecode}%' and file_name like '%{filename}%' "

    elif department == '' and filecode != '' and filename == '' and remark_info != '':
        sql = sql_select + f"where file_code like '%{filecode}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode == '' and filename != '' and remark_info != '':
        sql = sql_select + f"where file_name like '%{filename}%' and remark like '%{remark_info}%' "

    elif department != '' and filecode != '' and filename != '' and remark_info == '':
        sql = sql_select + f"where department LIKE '%{department}%' and " \
                           f"file_code like '%{filecode}%' and file_name like '%{filename}%' "

    elif department != '' and filecode != '' and filename == '' and remark_info != '':
        sql = sql_select + f"where department LIKE '%{department}%' and " \
                           f"file_code like '%{filecode}%' and remark like '%{remark_info}%' "

    elif department != '' and filecode == '' and filename != '' and remark_info != '':
        sql = sql_select + f"where department LIKE '%{department}%' and " \
                           f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    elif department == '' and filecode != '' and filename != '' and remark_info != '':
        sql = sql_select + f"where file_code like '%{filecode}%' and " \
                           f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    else:
        sql = sql_select + f"where department LIKE '%{department}%' and file_code like '%{filecode}%' and " \
                           f"file_name like '%{filename}%' and remark like '%{remark_info}%' "

    try:
        list_table_db = get_db_table(sql)
        # window1['-TABLE-'].update(values=list_table_db)

    except Exception as results:
        sg.popup_error(results, font=('宋体', 18))


def exec_sql_server_mes250(sql):
    try:
        print(f'查询SQL:{sql}')
        db = pymssql.connect(mes_server, mes_database, mes_user, mes_password, charset='utf8')  # 连接到sql server数据库 charset='utf8'
        cur = db.cursor()  # 获取该数据库连接下的环境变量
        cur.execute(sql)  # 执行语句

    except Exception as e:
        print(e)

    else:
        result = cur.fetchall()  # get result
        db.commit()  # 一定要commit，pymssql包默认是需要手动commit的，否则事务不生效
        db.close()  # 关闭数据库连接
        return result