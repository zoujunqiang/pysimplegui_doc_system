# encoding:utf-8
"""
@file = gui_exec
@author = zouju
@create_time = 2023-08-07- 14:40
"""
from API.SqlExec.sql_exec import exec_sql_server_utf8


def user_login_role1(window1):
    window1['GENERATE_CODE'].update(disabled=False)
    window1['MOD-BUTTON'].update(disabled=False)
    window1['DEL-BUTTON'].update(disabled=False)
    window1['QR-UPDATE-BUTTON'].update(disabled=False)
    window1['CIRCLE-BUTTON'].update(disabled=False)
    window1['DISABLE-BUTTON'].update(disabled=False)
    window1['INFO-BUTTON'].update(disabled=False)
    window1['LOGIN-BUTTON'].update(visible=False)
    window1['LOGIN-OUT'].update(visible=True)
    window1['ONLINE-USER'].update(visible=True)
    window1['USER-PNG'].update(visible=True)
    window1['ADD-FILE'].update(disabled=False)
    window1['FILE-INFO'].update(disabled=False)
    window1['DEL-FILE'].update(disabled=False)
    window1['OPEN-FILE'].update(disabled=False)
    window1['DOWN-FILE'].update(disabled=False)
    window1['APPROVE-INFO'].update(disabled=False)
    window1['LOOK-APPROVE'].update(disabled=False)
    window1['ADD-APPROVE'].update(visible=True)
    window1['EDIT-APPROVE'].update(visible=True)
    window1['DEL-APPROVE'].update(visible=True)
    window1['SEND-APPROVE'].update(disabled=False)
    window1['AGREE-APPROVE'].update(disabled=False)
    window1['REJECT-APPROVE'].update(disabled=False)
    window1['MY-SEND'].update(disabled=False)
    window1['WAIT-APPROVE'].update(disabled=False)
    window1['FINISH-APPROVE'].update(disabled=False)
    # window1['REJECT-SEND'].update(disabled=False)
    window1['ADD-USER'].update(disabled=False)
    window1['ADD-USER'].update(disabled=False)
    window1['LOOK-MES-LJTABLE'].update(disabled=False)
    window1['APPROVE-EXPORT'].update(disabled=False)
    window1['LJ-CONVER'].update(disabled=False)
    window1['DEL-LJ-INFO'].update(disabled=False)


def user_login_role0(window1):
    window1['GENERATE_CODE'].update(disabled=False)
    window1['LOGIN-BUTTON'].update(visible=False)
    window1['LOGIN-OUT'].update(visible=True)
    window1['USER-PNG'].update(visible=True)
    window1['ADD-FILE'].update(disabled=False)
    window1['FILE-INFO'].update(disabled=False)
    window1['DEL-FILE'].update(disabled=False)
    window1['OPEN-FILE'].update(disabled=False)
    window1['DOWN-FILE'].update(disabled=False)
    window1['APPROVE-INFO'].update(disabled=False)
    window1['LOOK-APPROVE'].update(disabled=False)
    window1['ADD-APPROVE'].update(visible=False)
    window1['EDIT-APPROVE'].update(visible=False)
    window1['DEL-APPROVE'].update(visible=False)
    window1['SEND-APPROVE'].update(disabled=False)
    window1['AGREE-APPROVE'].update(disabled=False)
    window1['REJECT-APPROVE'].update(disabled=False)
    window1['MY-SEND'].update(disabled=False)
    window1['WAIT-APPROVE'].update(disabled=False)
    window1['FINISH-APPROVE'].update(disabled=False)
    # window1['REJECT-SEND'].update(disabled=False)
    window1['ADD-USER'].update(disabled=True)
    window1['LOOK-MES-LJTABLE'].update(disabled=False)
    window1['APPROVE-EXPORT'].update(disabled=False)
    window1['LJ-CONVER'].update(disabled=False)
    window1['DEL-LJ-INFO'].update(disabled=False)


def user_loginout(window1):
    window1['GENERATE_CODE'].update(disabled=True)
    window1['MOD-BUTTON'].update(disabled=True)
    window1['DEL-BUTTON'].update(disabled=True)
    window1['QR-UPDATE-BUTTON'].update(disabled=True)
    window1['CIRCLE-BUTTON'].update(disabled=True)
    window1['DISABLE-BUTTON'].update(disabled=True)
    window1['INFO-BUTTON'].update(disabled=True)
    window1['LOGIN-BUTTON'].update(visible=True)
    window1['LOGIN-OUT'].update(visible=False)
    window1['LOGIN-TEXT'].update('')
    window1['USER-PNG'].update(visible=False)
    window1['ADD-FILE'].update(disabled=True)
    window1['DEL-FILE'].update(disabled=True)
    window1['OPEN-FILE'].update(disabled=True)
    window1['APPROVE-INFO'].update(disabled=True)
    window1['LOOK-APPROVE'].update(disabled=True)
    window1['ADD-APPROVE'].update(visible=False)
    window1['EDIT-APPROVE'].update(visible=False)
    window1['DEL-APPROVE'].update(visible=False)
    window1['SEND-APPROVE'].update(disabled=True)
    window1['AGREE-APPROVE'].update(disabled=True)
    window1['REJECT-APPROVE'].update(disabled=True)
    window1['MY-SEND'].update(disabled=True)
    window1['WAIT-APPROVE'].update(disabled=True)
    window1['FINISH-APPROVE'].update(disabled=True)
    window1['ADD-USER'].update(disabled=True)
    window1['DOWN-FILE'].update(disabled=True)
    window1['FILE-INFO'].update(disabled=True)
    window1['ONLINE-USER'].update(visible=False)
    window1['LOOK-MES-LJTABLE'].update(disabled=True)
    window1['APPROVE-EXPORT'].update(disabled=True)
    window1['LJ-CONVER'].update(disabled=True)
    window1['DEL-LJ-INFO'].update(disabled=True)
    window1['-TABLE-'].update('')
    window1['TABLE2'].update('')
    window1['NEW-JOB-TEXT'].update('')
    window1.refresh()


def update_combo_user1(window_add_approve):
    list_name_cn = []
    res = exec_sql_server_utf8(f"SELECT name FROM member WHERE role in (0,1) ")
    for item in res:
        name_cn = item[0]
        list_name_cn.append(name_cn)
    window_add_approve['ADD-USER1'].update(values=list_name_cn, size=(30, 20))
    window_add_approve['ADD-USER2'].update(values=list_name_cn, size=(30, 20))
    window_add_approve['ADD-USER3'].update(values=list_name_cn, size=(30, 20))
    window_add_approve['ADD-USER4'].update(values=list_name_cn, size=(30, 20))
    window_add_approve['ADD-USER5'].update(values=list_name_cn, size=(30, 20))
    window_add_approve['ADD-USER6'].update(values=list_name_cn, size=(30, 20))
    window_add_approve['ADD-USER7'].update(values=list_name_cn, size=(30, 20))
    window_add_approve['ADD-USER8'].update(values=list_name_cn, size=(30, 20))
    window_add_approve['ADD-USER9'].update(values=list_name_cn, size=(30, 20))
    window_add_approve['ADD-USER10'].update(values=list_name_cn, size=(30, 20))


def update_combo_user2(window_edit_approve):
    list_name_cn = []
    res = exec_sql_server_utf8(f"SELECT name FROM member WHERE role in (0,1) ")
    for item in res:
        name_cn = item[0]
        list_name_cn.append(name_cn)
    window_edit_approve['EDIT-USER1'].update(values=list_name_cn, size=(30, 20))
    window_edit_approve['EDIT-USER2'].update(values=list_name_cn, size=(30, 20))
    window_edit_approve['EDIT-USER3'].update(values=list_name_cn, size=(30, 20))
    window_edit_approve['EDIT-USER4'].update(values=list_name_cn, size=(30, 20))
    window_edit_approve['EDIT-USER5'].update(values=list_name_cn, size=(30, 20))
    window_edit_approve['EDIT-USER6'].update(values=list_name_cn, size=(30, 20))
    window_edit_approve['EDIT-USER7'].update(values=list_name_cn, size=(30, 20))
    window_edit_approve['EDIT-USER8'].update(values=list_name_cn, size=(30, 20))
    window_edit_approve['EDIT-USER9'].update(values=list_name_cn, size=(30, 20))
    window_edit_approve['EDIT-USER10'].update(values=list_name_cn, size=(30, 20))