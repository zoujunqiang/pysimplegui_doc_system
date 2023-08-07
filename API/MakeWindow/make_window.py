# encoding:utf-8
"""
@file = make_window
@author = zouju
@create_time = 2023-08-07- 11:08
"""


# encoding=utf-8
import os
import PySimpleGUI as sg

dep = ('管理者代表', '财务部', '计划部', '人事部', '行政部', '工程部', '品管部', '采购部', '生产部', 'OEM业务部', '业务部', '研发部',
       '维修部', 'PE组', 'ME组', 'IE组', 'TE组', '体系组', '文控中心', '生产部SMT', 'SMT工程部', '制造中心', '法务部', '其他')


def make_window1():
    header_table = ['ID', '文件编号', '文件名称', '版本', '生效时间', '部门', '文件类型', '备注']
    file = ('二阶文件', '三阶文件', '四阶文件', '外来文件', '临时文件', '文件发放', '所有文件')
    header_table1 = ['序号', '文件名', '任务ID', '申请人', '申请时间', '审批状态', '流程名称']
    right_click_menu = ['&Right', ['打开文件夹', '打开文件']]
    right_click_menu1 = ['&Right', ['添加文件', '审批详情']]
    right_click_menu2 = ['&Right', ['打开临技', '临技审批详情']]
    listbox_value = ('')

    listbox_column = [
        [sg.Listbox(values=listbox_value, size=(102, 5), font=('宋体', 18), key='LIST-BOX')]
    ]

    table_column = [
        [sg.Table(values=[
            ["      ", "                                              ", "       ", "           ",
             "                     ", "              ", "                 "]],
            headings=header_table1,
            max_col_width=500,
            auto_size_columns=True,  # 自动调整列宽（根据上面第一次的values默认值为准，update时不会调整）
            display_row_numbers=False,  # 序号
            justification='center',  # 字符排列 left right center
            num_rows=8,  # 行数
            row_height=30,  # 行高
            key='TABLE2',
            font=('宋体', 14),
            text_color='black',
            background_color='white',
            enable_events=True,
            bind_return_key=True,
            # right_click_menu=right_click_menu1,
            tooltip='文件信息')],

    ]

    button1_column = [
        [
            sg.FilesBrowse('添加文件', font=('宋体', 16), size=(10, 1), key='ADD-FILE', enable_events=True,
                           target='FILE-INPUT', disabled=True),
            sg.Input('', font=('宋体', 16), key='FILE-INPUT', enable_events=True, visible=False)],
        [sg.Button('文件详情', size=(10, 1), font=('宋体', 16), key='FILE-INFO', disabled=True)],
        [sg.Button('审批详情', size=(10, 1), font=('宋体', 16), key='APPROVE-INFO', disabled=True)],
        [sg.Button('打开文件', size=(10, 1), font=('宋体', 16), key='OPEN-FILE', disabled=True)],
        [sg.Button('删除文件', size=(10, 1), font=('宋体', 16), key='DEL-FILE', disabled=True)],
        [sg.Button('下载文件', size=(10, 1), font=('宋体', 16), key='DOWN-FILE', disabled=True)],
    ]

    button2_column = [
        [sg.Button('查看流程', size=(10, 1), font=('宋体', 16), key='LOOK-APPROVE', disabled=True)],
        [sg.Button('新增流程', size=(10, 1), font=('宋体', 16), key='ADD-APPROVE', visible=False)],
        [sg.Button('编辑流程', size=(10, 1), font=('宋体', 16), key='EDIT-APPROVE', visible=False)],
        [sg.Button('删除流程', size=(10, 1), font=('宋体', 16), key='DEL-APPROVE', visible=False)]
    ]

    qrcode_left_column = [
        [sg.Multiline(default_text='', size=(30, 600), key='-QRCODE-OUTPUT-')]
    ]
    qrcode_right_column = [
        [sg.Text("二维码", font=('宋体', 18))],
        [sg.Image(key="-IMAGE-")],
    ]

    frame1_layout = [
        [sg.InputCombo(file, font=('宋体', 16),
                       size=(12, 8), default_value='二阶文件', key='FILE_TYPE'),
         sg.InputCombo(dep, font=('宋体', 16),
                       size=(16, 10), default_value='', key='DEPART'),
         sg.Text('文件编号', font=('宋体', 14), size=(8, 1)),
         sg.Input('', font=('宋体', 14), size=(20, 1), key='FILE_CODE_INPUT'),
         sg.Text('文件名称', font=('宋体', 14), size=(8, 1)),
         sg.Input('', font=('宋体', 14), size=(20, 1), key='FILE_NAME_INPUT'),
         sg.Text('备注', font=('宋体', 14), size=(4, 1)),
         sg.Input('', font=('宋体', 14), size=(20, 1), key='REMARK_INPUT')
         ],
        [sg.Text('外来文件客户代码', font=('宋体', 14), size=(16, 1)),
         sg.Input('', font=('宋体', 14), size=(17, 1), key='WL_FILE_CODE', pad=((0, 550), 0)),
         sg.Button('编号申请', font=('宋体', 16), key='GENERATE_CODE', disabled=True),
         sg.Button('导出', font=('宋体', 16), size=(10, 1), key='FILE_OUTPUT', disabled=False),
         sg.Button('打开文件夹', font=('宋体', 16), size=(10, 1), key='OPEN-DIR', disabled=False),
         sg.Button('查询', font=('宋体', 16), size=(10, 1), key='FRAME1_QUERY', disabled=False)],
        [sg.Multiline(default_text='', size=(200, 50), font=('宋体', 12), key='-FILE_SYSTEM-', reroute_cprint=True,
                      autoscroll=True)]
    ]

    frame2_layout = [
        [sg.Text('生成内容', font=('宋体', 14), size=(8, 1), justification='center'),
         sg.Input('', font=('宋体', 14), size=(100, 1), key='-INPUT_QRCODE-'),
         sg.Button('生成二维码', font=('宋体', 16), key='-MAKE_QRCODE-', disabled=False)],
        [sg.HSeparator()],
        [sg.Text("二维码", font=('宋体', 18))],
        [sg.Text("图片路径", font=('宋体', 14)), sg.Input("", font=('宋体', 14), size=(100, 1), key='QRCODE_PNG_PATH'),
         sg.Button('打开文件夹', font=('宋体', 16), key='OPEN-QR-DIR', disabled=False)],
        [sg.Image(size=(1440, 960), key="-IMAGE-")],
        # [
        #     sg.Column(qrcode_left_column),
        #     sg.VSeperator(),
        #     sg.Column(qrcode_right_column),
        # ]

    ]

    frame3_layout = [
        [sg.InputCombo(file, font=('宋体', 16),
                       size=(12, 8), default_value='二阶文件', key='FILE_TYPE_DB'),
         sg.InputCombo(dep, font=('宋体', 16),
                       size=(16, 10), default_value='', key='DEPART_DB'),
         sg.Text('文件编号', font=('宋体', 14), size=(8, 1), justification='center'),
         sg.Input('', font=('宋体', 14), size=(20, 1), key='FILE_CODE_DB_INPUT'),
         sg.Text('文件名称', font=('宋体', 14), size=(8, 1)),
         sg.Input('', font=('宋体', 14), size=(20, 1), key='FILE_NAME_DB_INPUT'),
         sg.Text('备注', font=('宋体', 14), size=(4, 1)),
         sg.Input('', font=('宋体', 14), size=(20, 1), key='REMARK_DB_INPUT'),
         sg.Button('查询', font=('宋体', 16), size=(10, 1), key='FRAME3_QUERY', disabled=False)],
        [sg.Button('打开文件夹', font=('宋体', 16), disabled=False),
         sg.Button('打开文件', font=('宋体', 16), disabled=False),
         sg.Button('修改', font=('宋体', 16), disabled=True, key='MOD-BUTTON'),
         sg.Button('删除', font=('宋体', 16), disabled=True, key='DEL-BUTTON'),
         sg.Text('文件发放:', font=('宋体', 16), size=(8, 1), pad=((100, 0), 0), key='FILE-TEXT'),
         sg.Button('二维码更新', font=('宋体', 16), disabled=True, key='QR-UPDATE-BUTTON'),
         sg.Button('回收', font=('宋体', 16), disabled=True, key='CIRCLE-BUTTON'),
         sg.Button('作废', font=('宋体', 16), disabled=True, key='DISABLE-BUTTON'),
         sg.Button('详情', font=('宋体', 16), disabled=True, key='INFO-BUTTON'),
         sg.Text('用户:', font=('宋体', 16), size=(4, 1), pad=((100, 0), 0), key='USER-TEXT'),
         sg.Button('新增用户', font=('宋体', 16), disabled=True, key='ADD-USER'),
         sg.Button('用户信息', font=('宋体', 16), visible=False, key='ONLINE-USER')
         ],
        [sg.Table(values=[
            ["      ", "                ", "                                       ", "              ",
             "           ", "             ", "          ", "             "]],
            headings=header_table,
            max_col_width=500,
            auto_size_columns=True,  # 自动调整列宽（根据上面第一次的values默认值为准，update时不会调整）
            display_row_numbers=True,  # 序号
            justification='center',  # 字符排列 left right center
            num_rows=25,  # 行数
            row_height=30,  # 行高
            key='-TABLE-',
            font=('宋体', 16),
            text_color='black',
            background_color='white',
            enable_events=True,
            bind_return_key=True,
            right_click_menu=right_click_menu,
            tooltip='数据库维护')]
    ]

    mutli_column = [
        [sg.Multiline(default_text='', size=(111, 16), font=('宋体', 16), key='MT-OUTPUT', reroute_cprint=False,
                      autoscroll=True, right_click_menu=['&Right', ['清空']])]
    ]
    button3_column = [
        [sg.Button('发送', size=(10, 1), font=('宋体', 16), key='SEND-APPROVE', disabled=True)],
        [sg.Button('同意', size=(10, 1), font=('宋体', 16), key='AGREE-APPROVE', button_color='green', disabled=True)],
        [sg.Button('拒绝', size=(10, 1), font=('宋体', 16), key='REJECT-APPROVE', button_color='red', disabled=True)],
        [sg.Text('', size=(10, 1), font=('宋体', 16))],
        [sg.Text('', size=(10, 1), font=('宋体', 16))],
        [sg.Text('', size=(10, 1), font=('宋体', 16))],
        [sg.Text('', size=(10, 1), font=('宋体', 16))],
        [sg.Text('', size=(10, 1), font=('宋体', 16))]
    ]

    frame4_layout = [
        [
            sg.Button('我的申请', font=('宋体', 16), key='MY-SEND', disabled=True),
            sg.Button('待审批', font=('宋体', 16), key='WAIT-APPROVE', disabled=True, button_color='#ff7e00'),
            sg.Button('已审批', font=('宋体', 16), key='FINISH-APPROVE', disabled=True, button_color='green'),
            sg.Button('已退回', font=('宋体', 16), key='REJECT-SEND', disabled=True, button_color='red'),
            sg.Button('导出', font=('宋体', 16), key='APPROVE-EXPORT', size=(8, 1), disabled=True),
            sg.Button('文件审批流程', font=('宋体', 16), key='FILE-APPROVE', pad=((0, 0), 0), size=(12, 1))
        ],
        [
            sg.Text('审批状态', font=('宋体', 14), size=(8, 1)),
            sg.InputCombo(('已完成', '已归档', '审批中', '已退回'), font=('宋体', 14), key='APP-STATUS-INPUT', size=(15, 4)),
            sg.Text('文件名', font=('宋体', 14), size=(6, 1)),
            sg.Input('', font=('宋体', 14), key='FRAME4-INPUT', size=(15, 1)),
            sg.Text('申请人', font=('宋体', 14), size=(6, 1), key='ID-NUMBER-TEXT'),
            sg.Input('', font=('宋体', 14), key='ID-NUMBER-INPUT', size=(15, 1)),
            sg.Button('日期', font=('宋体', 14), size=(6, 1), target='DATE-INPUT', key='DATE-BUTTON'),
            sg.Input('', font=('宋体', 14), key='DATE-INPUT', size=(15, 1))
        ],
        [
            sg.Column(table_column),
            # sg.VSeperator(),
            sg.Column(button1_column),
        ],

        [sg.Button('文件审批流程', size=(12, 1), font=('宋体', 16), key='FILE-REVIEW'),
         sg.Button('临技下发流程', size=(12, 1), font=('宋体', 16), key='TEMP-RELEASE')],

        [
            sg.Column(listbox_column),
            # sg.VSeperator(),
            sg.Column(button2_column),
        ],
        [sg.Text('申请/审批内容', size=(14, 1), font=('宋体', 16)),
         sg.Button('清空', size=(6, 1), font=('宋体', 16))],

        [
            sg.Column(mutli_column),
            # sg.VSeperator(),
            sg.Column(button3_column),
        ]

    ]

    header_table_lj = ['ID', '临技编号', '产品编码', '任务令', '开始时间', '截止时间', '影响工序', '临技类别', '备注']
    frame5_layout = [
        [
            sg.Text('临技编号', font=('宋体', 14), size=(8, 1), justification='center'),
            sg.Input('', font=('宋体', 14), size=(20, 1), key='FILE_CODE_LJ'),
            sg.Text('产品编码', font=('宋体', 14), size=(8, 1)),
            sg.Input('', font=('宋体', 14), size=(20, 1), key='PRO_CODE_LJ'),
            sg.Text('任务令', font=('宋体', 14), size=(6, 1)),
            sg.Input('', font=('宋体', 14), size=(20, 1), key='RWL_LJ'),
            sg.Text('备注', font=('宋体', 14), size=(4, 1)),
            sg.Input('', font=('宋体', 14), size=(20, 1), key='REMARK_LJ'),
            sg.Text('类型', font=('宋体', 14), size=(4, 1)),
            sg.InputCombo(('期间有效', '一次性有效'), font=('宋体', 14), size=(15, 2), key='TYPE_LJ')],
        [sg.CalendarButton('日期', font=('宋体', 14), size=(8, 1), target='TIME_LJ'),
         sg.Input('', size=(18, 1), font=('宋体', 16), key='TIME_LJ')],
        [
            sg.Button('转JZ文档', font=('宋体', 16), size=(10, 1), disabled=True, key='LJ-CONVER'),
            sg.Button('删除', font=('宋体', 16), size=(10, 1), disabled=True, key='DEL-LJ-INFO'),
            sg.Button('查看MES临技表', font=('宋体', 16), size=(12, 1), disabled=True, pad=((0, 0), 0),
                      key='LOOK-MES-LJTABLE'),
            sg.Button('打开临技-JZ', font=('宋体', 16), size=(10, 1), disabled=False),
            sg.Button('打开临技', font=('宋体', 16), size=(10, 1), disabled=False),
            sg.Button('临技审批详情', font=('宋体', 16), size=(12, 1), disabled=False),
            sg.Button('导出', font=('宋体', 16), size=(10, 1), key='LJ-FILE-OUTPUT', disabled=False),
            sg.Button('查询', font=('宋体', 16), size=(10, 1), key='FRAME5_QUERY', disabled=False)],
        [sg.Table(values=[
            ["     ", "                ", "                              ", "                ",
             "           ", "           ", "             ", "            ", "           "]],
            headings=header_table_lj,
            max_col_width=500,
            auto_size_columns=True,  # 自动调整列宽（根据上面第一次的values默认值为准，update时不会调整）
            display_row_numbers=False,  # 序号
            justification='left',  # 字符排列 left right center
            num_rows=25,  # 行数
            row_height=30,  # 行高
            key='TABLE-LJ',
            font=('宋体', 16),
            text_color='black',
            background_color='white',
            enable_events=True,
            bind_return_key=True,
            right_click_menu=right_click_menu2,
            tooltip='临技查询')]
    ]

    layout = [
        [sg.Text('', pad=((600, 0), 0)),
         sg.Text('极智文件系统', font=('宋体', 24), size=(12, 1), justification='center'),
         sg.Text('', pad=((300, 0), 0)),
         sg.Text('', font=('宋体', 16), size=(20, 1), key='LOGIN-TEXT'),
         sg.Image('', key='USER-PNG', tooltip='修改用户信息', enable_events=True, visible=False)],
        [
            sg.Button('文件查询', font=('宋体', 16)),
            sg.Button('二维码', font=('宋体', 16)),
            sg.Button('数据库', font=('宋体', 16)),
            sg.Button('临技查询', font=('宋体', 16)),
            sg.Button('审批申请', font=('宋体', 16)),
            sg.Text('', size=(50, 1), font=('宋体', 16), pad=((60, 160), 0), text_color='red', key='NEW-JOB-TEXT'),
            sg.Button('登录', font=('宋体', 18), key='LOGIN-BUTTON', visible=True, size=(10, 1), button_color='green'),
            sg.Button('注销', font=('宋体', 18), key='LOGIN-OUT', visible=False, size=(10, 1))
        ],
        [sg.Frame(title='文件查询', layout=frame1_layout, key='FRAME1', font=('宋体', 14), visible=True,
                  right_click_menu=right_click_menu),
         sg.Frame(title='二维码', layout=frame2_layout, key='FRAME2', font=('宋体', 14), visible=False),
         sg.Frame(title='数据库维护', layout=frame3_layout, key='FRAME3', font=('宋体', 14), visible=False),
         sg.Frame(title='临技查询', layout=frame5_layout, key='FRAME5', font=('宋体', 14), visible=False),
         sg.Frame(title='审批申请', layout=frame4_layout, key='FRAME4', font=('宋体', 14), visible=False)

         ]
    ]

    return sg.Window('极智文件系统V2.57', layout, size=(1440, 960), resizable=True, enable_close_attempted_event=True,
                     finalize=True, location=(200, 10))


def make_window2():  # 二维码页面
    layout = [
        [sg.Text('通过二维码更新', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text('二维码 ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='QR-INPUT'), sg.Button('更新', font=('宋体', 16))],
        [sg.Text('  ID  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='QR-ID', disabled=True, background_color='gray')],
        [sg.Text('文件名称', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='QR-NAME')],
        [sg.Text('文件编号', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='QR-CODE')],
        [sg.Text('  版本  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='QR-VER')],
        [sg.Text('  部门  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(dep, font=('宋体', 16),
                       size=(30, 10), default_value='生产部', key='QR-DEP')],
        [sg.Text(' 签收人 ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='QR-USER'), sg.Text('*')],
        [sg.Text('  日期  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='QR-DATE')],
        [sg.Text('  份数  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='QR-NUM')],
        [sg.Text('  页数  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='QR-PAGE')],
        [sg.Text('文件类型', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(('内部', '外部', '临技'), font=('宋体', 16),
                       size=(30, 3), default_value='内部', key='QR-FLAG')],
        [sg.Text('  备注  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='QR-REMARK')],

        [sg.Text()],
        [sg.Text('', pad=((0, 150), 0)),
         sg.Button('保存', font=('宋体', 18), pad=((0, 100), 0)), sg.Button('取消', font=('宋体', 18))]
    ]
    return sg.Window('新增', layout, finalize=True, size=(600, 530))


def make_window3():  # 修改页面
    layout = [
        [sg.Text('更新数据', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text(' 二维码 ', font=('宋体', 16), size=(12, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='MOD-INPUT'),
         sg.Button('更新', font=('宋体', 16), key='MOD-UPDATE')],
        [sg.Text('  ID  ', font=('宋体', 16), size=(12, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='MOD-ID', disabled=True, background_color='gray')],
        [sg.Text('文件编号', font=('宋体', 16), size=(12, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='MOD-CODE')],
        [sg.Text('文件名称', font=('宋体', 16), size=(12, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='MOD-NAME')],
        [sg.Text('版本', font=('宋体', 16), size=(12, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='MOD-VER')],
        [sg.Text('生效时间', font=('宋体', 16), size=(12, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='MOD-TIME')],
        [sg.Text('部门', font=('宋体', 16), size=(12, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='MOD-DEP')],
        [sg.Text('文件类型', font=('宋体', 16), size=(12, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='MOD-TYPE')],
        [sg.Text('  备注  ', font=('宋体', 16), size=(12, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='MOD-REMARK')],
        [sg.Text()],
        [sg.Text('', pad=((0, 150), 0)),
         sg.Button('保存', font=('宋体', 18), pad=((0, 100), 0)),
         sg.Button('取消', font=('宋体', 18))]
    ]
    return sg.Window('修改', layout, finalize=True, size=(580, 450))


def make_window4():  # 详情页面
    layout = [
        [sg.Text('文件发放详请', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text('  ID  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-ID')],
        [sg.Text('文件编号', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-CODE')],
        [sg.Text('文件名称', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-NAME')],
        [sg.Text('  版本 ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-VER')],
        [sg.Text('  部门 ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-DEP')],
        [sg.Text(' 签收人 ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-USER')],
        [sg.Text('签收日期', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-RDATE')],
        [sg.Text('  份数  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-NUM')],
        [sg.Text('  页数  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-PAGE')],
        [sg.Text('文件类型', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-TYPE')],
        [sg.Text('回收状态', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-RECOVER')],
        [sg.Text('回收日期', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-HDATE')],
        [sg.Text('作废状态', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-INVALID')],
        [sg.Text('作废日期', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-IDATE')],
        [sg.Text('  备注  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='INFO-REMARK')],
        [sg.Text()],
        [sg.Text('', pad=((0, 120), 0)), sg.Button('保存', font=('宋体', 18), key='INFO-UPDATE'),
         sg.Button('取消', font=('宋体', 18))]
    ]
    return sg.Window('详情', layout, finalize=True, size=(400, 620))


def make_window_login():
    layout = [
        [sg.Text('文件系统登录', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text('账号', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='LOGIN-USER')],
        [sg.Text('密码', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='LOGIN-PASSWD', password_char='*')],
        [sg.Text('', font=('宋体', 16), size=(8, 1), justification='center')],
        [sg.Text()],
        [sg.Text('', pad=((0, 100), 0)), sg.Button('登录', font=('宋体', 18), key='LOGIN', pad=((0, 60), 0)),
         sg.Button('取消', font=('宋体', 18))]
    ]
    return sg.Window('登录', layout, finalize=True, size=(400, 300))


def make_window_look_approve():
    layout = [
        [sg.Text('审批流程', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text('')],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG1', pad=((250, 0), 0))],
        [sg.Image(size=(50, 50), key="ARROW-PNG1", pad=((280, 0), 0))],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG2', pad=((250, 0), 0))],
        [sg.Image(size=(50, 50), key="ARROW-PNG2", pad=((280, 0), 0))],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG3', pad=((250, 0), 0))],
        [sg.Image(size=(50, 50), key="ARROW-PNG3", pad=((280, 0), 0))],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG4', pad=((250, 0), 0))],
        [sg.Image(size=(50, 50), key="ARROW-PNG4", pad=((280, 0), 0))],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG5', pad=((250, 0), 0))],
        [sg.Image(size=(50, 50), key="ARROW-PNG5", pad=((280, 0), 0))],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG6', pad=((250, 0), 0))],
        [sg.Image(size=(50, 50), key="ARROW-PNG6", pad=((280, 0), 0))],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG7', pad=((250, 0), 0))],
        [sg.Image(size=(50, 50), key="ARROW-PNG7", pad=((280, 0), 0))],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG8', pad=((250, 0), 0))],
        [sg.Image(size=(50, 50), key="ARROW-PNG8", pad=((280, 0), 0))],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG9', pad=((250, 0), 0))],
        [sg.Image(size=(50, 50), key="ARROW-PNG9", pad=((280, 0), 0))],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG10', pad=((250, 0), 0))],
        [sg.Image(size=(50, 50), key="ARROW-PNG10", pad=((280, 0), 0))],
        [sg.Text('', font=('宋体', 20), size=(20, 1), key='TEXT-PNG11', pad=((250, 0), 0))]
    ]
    return sg.Window('审批流程', layout, finalize=True, size=(600, 800), return_keyboard_events=True)


def make_window_add_approve():
    layout = [
        [sg.Text('新增审批流程', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text(' 序号  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='ADD-ID', disabled=True)],
        [sg.Text('流程类型', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(('文件审批', '临技下发'), font=('宋体', 16),
                       size=(30, 2), default_value='文件审批', key='ADD-TYPE')],
        [sg.Text('流程名称', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='ADD-NAME')],
        [sg.Text('审批人1', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='ADD-USER1')],
        [sg.Text('审批人2', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='ADD-USER2')],
        [sg.Text('审批人3', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='ADD-USER3')],
        [sg.Text('审批人4', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='ADD-USER4')],
        [sg.Text('审批人5', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='ADD-USER5')],
        [sg.Text('审批人6', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='ADD-USER6')],
        [sg.Text('审批人7', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='ADD-USER7')],
        [sg.Text('审批人8', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='ADD-USER8')],
        [sg.Text('审批人9', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='ADD-USER9')],
        [sg.Text('审批人10', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='ADD-USER10')],
        [sg.Text()],
        [sg.Text('', pad=((0, 150), 0)),
         sg.Button('保存', font=('宋体', 18), pad=((0, 100), 0), key='ADD-APPROVE-SAVE'),
         sg.Button('取消', font=('宋体', 18))]
    ]
    return sg.Window('新增', layout, finalize=True, size=(500, 580), return_keyboard_events=True)


def make_window_edit_approve():
    layout = [
        [sg.Text('修改审批流程', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text(' 序号  ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='EDIT-ID', disabled=True)],
        [sg.Text('流程类型', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(('文件审批', '临技下发'), font=('宋体', 16),
                       size=(30, 2), default_value='文件审批', key='EDIT-TYPE')],
        [sg.Text('流程名称', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='EDIT-NAME')],
        [sg.Text('审批人1', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='EDIT-USER1')],
        [sg.Text('审批人2', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='EDIT-USER2')],
        [sg.Text('审批人3', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='EDIT-USER3')],
        [sg.Text('审批人4', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='EDIT-USER4')],
        [sg.Text('审批人5', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='EDIT-USER5')],
        [sg.Text('审批人6', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='EDIT-USER6')],
        [sg.Text('审批人7', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='EDIT-USER7')],
        [sg.Text('审批人8', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='EDIT-USER8')],
        [sg.Text('审批人9', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='EDIT-USER9')],
        [sg.Text('审批人10', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo('', size=(30, 1), font=('宋体', 16), key='EDIT-USER10')],
        [sg.Text()],
        [sg.Text('', pad=((0, 150), 0)),
         sg.Button('保存', font=('宋体', 18), pad=((0, 100), 0), key='EDIT-APPROVE-SAVE'),
         sg.Button('取消', font=('宋体', 18))]
    ]
    return sg.Window('修改', layout, finalize=True, size=(500, 580), return_keyboard_events=True)


def makesure_window():
    layout = [
        [sg.Text('请确认是否删除', font=('宋体', 18), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text('', pad=((0, 50), 0)),
         sg.Button('确认', font=('宋体', 18), pad=((0, 30), 0), key='ENTER-BOTTON'),
         sg.Button('取消', font=('宋体', 18))]
    ]

    return sg.Window('删除', layout, finalize=True, size=(300, 120), return_keyboard_events=True)


def make_winodw_approve_info():
    headers = ['处理人', '审批状态', '内容', '审批时间', ]
    layout = [
        [sg.Text('', font=('宋体', 18), size=(100, 1), justification='center', key='APPROVE-TEXT-INFO')],
        [sg.Text('', font=('宋体', 16), size=(20, 1), pad=((340, 0), 0), key='APPROVE-NAME-INFO'),
         sg.Button('审批撤回', font=('宋体', 16), key='APPROVE-RETRACT', visible=False)],
        [sg.Table(values=[
            ["        ", "            ", "                           ", "                     "]],
            headings=headers,
            max_col_width=500,
            auto_size_columns=True,  # 自动调整列宽（根据上面第一次的values默认值为准，update时不会调整）
            display_row_numbers=False,  # 序号
            justification='center',  # 字符排列 left right center
            num_rows=10,  # 行数
            row_height=30,  # 行高
            key='TABLE-APP-INFO',
            font=('宋体', 16),
            text_color='black',
            background_color='white',
            enable_events=True,
            bind_return_key=True,
            # right_click_menu=right_click_menu2,
            tooltip='审批详情')]
    ]

    return sg.Window('删除', layout, finalize=True, size=(800, 400), return_keyboard_events=True)


def make_window_add_user():
    role = ('用户', '管理员')
    layout = [
        [sg.Text('新增用户', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text('(*为必填项)', font=('宋体', 16), size=(100, 1), justification='center')],
        [sg.Text('账号*', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='ADD-LOGIN-USER')],
        [sg.Text('密码*', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='ADD-LOGIN-PASSWD', password_char='*')],
        [sg.Text('姓名*', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='ADD-USERNAME')],
        [sg.Text('部门', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(dep, font=('宋体', 16), size=(20, 10), default_value='', key='ADD-DEPART')],
        [sg.Text('职位', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='ADD-POSITION')],
        [sg.Text('角色', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(role, font=('宋体', 16), size=(20, 2), default_value='用户', key='ADD-ROLE')],
        [sg.Text()],
        [sg.Button('保存', font=('宋体', 18), pad=((100, 80), 0), key='ADD-USER-SAVE'),
         sg.Button('取消', font=('宋体', 18))]
    ]

    return sg.Window('删除', layout, finalize=True, size=(400, 380), return_keyboard_events=True)


def make_window_edit_user():
    role = ('用户', '管理员')
    layout = [
        [sg.Text('修改用户', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text('(*为必填项)', font=('宋体', 16), size=(100, 1), justification='center')],
        [sg.Text('账号*', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='EDIT-LOGIN-USER', disabled=True)],
        [sg.Text('密码*', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='EDIT-LOGIN-PASSWD', password_char='*')],
        [sg.Text('姓名*', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='EDIT-USERNAME')],
        [sg.Text('部门', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(dep, font=('宋体', 16), size=(20, 10), default_value='', key='EDIT-DEPART')],
        [sg.Text('职位', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='EDIT-POSITION')],
        [sg.Text('角色', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(role, font=('宋体', 16), size=(20, 2), default_value='用户', key='EDIT-ROLE')],
        [sg.Text()],
        [sg.Button('保存', font=('宋体', 18), pad=((100, 80), 0), key='EDIT-USER-SAVE'),
         sg.Button('取消', font=('宋体', 18))]
    ]

    return sg.Window('删除', layout, finalize=True, size=(400, 380), return_keyboard_events=True)


def make_window_display_user_content():
    layout = [
        [sg.Text('详细内容', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Multiline(default_text='', size=(100, 20), font=('宋体', 16), key='USER-CONTENT-OUTPUT', autoscroll=True)]
    ]

    return sg.Window('详情', layout, finalize=True, size=(800, 400))


def make_winodw_online_user():
    headers = ['序号', '用户', '姓名', '在线状态', ]
    layout = [
        [sg.Text('用户信息', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text('1-在线, 0-不在线', font=('宋体', 16), size=(20, 1), justification='center'),
         sg.Button('编辑', font=('宋体', 18), pad=((360, 0), 0), key='EDIT-USER-INFO'),
         sg.Button('删除', font=('宋体', 18), pad=((10, 0), 0), key='DEL-USER-INFO')],
        [sg.Table(values=[
            ["        ", "            ", "                           ", "                     "]],
            headings=headers,
            max_col_width=500,
            auto_size_columns=True,  # 自动调整列宽（根据上面第一次的values默认值为准，update时不会调整）
            display_row_numbers=False,  # 序号
            justification='center',  # 字符排列 left right center
            num_rows=10,  # 行数
            row_height=30,  # 行高
            key='TABLE-ONLINE-USER',
            font=('宋体', 16),
            text_color='black',
            background_color='white',
            enable_events=True,
            bind_return_key=True,
            tooltip='用户在线状态')]
    ]

    return sg.Window('用户状态', layout, finalize=True, size=(800, 400), return_keyboard_events=True)


def make_window_edit_user_info():
    role = ('用户', '管理员')
    layout = [
        [sg.Text('修改用户', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text('(*为必填项)', font=('宋体', 16), size=(100, 1), justification='center')],
        [sg.Text('账号*', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='DIS-LOGIN-USER-INFO', disabled=True)],
        [sg.Text('密码*', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='DIS-LOGIN-PASSWD-INFO', password_char='*')],
        [sg.Text('姓名*', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='DIS-USERNAME-INFO')],
        [sg.Text('部门', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(dep, font=('宋体', 16), size=(20, 10), default_value='', key='DIS-DEPART-INFO')],
        [sg.Text('职位', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='DIS-POSITION-INFO')],
        [sg.Text('角色', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(role, font=('宋体', 16), size=(20, 2), default_value='用户', key='DIS-ROLE-INFO')],
        [sg.Text('状态', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(20, 1), font=('宋体', 16), key='DIS-USER-INFO')],
        [sg.Text()],
        [sg.Button('保存', font=('宋体', 18), pad=((100, 80), 0), key='EDIT-USER-SAVE-INFO'),
         sg.Button('取消', font=('宋体', 18))]
    ]

    return sg.Window('删除', layout, finalize=True, size=(400, 380))


def make_window_file_info():
    layout = [
        [sg.Text('文件详情', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text('任务ID ', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='FILE-INFO-ID')],
        [sg.Text('文件名称', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='FILE-INFO-NAME')],
        [sg.Text('流程名称', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='FILE-INFO-APPROVE')],
        [sg.Text('文件大小', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='FILE-INFO-FILESIZE')],
        [sg.Text('上传时间', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='FILE-INFO-UPLOAD-TIME')],
        [sg.Text('申请时间', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='FILE-INFO-SEND-TIME')],
        [sg.Text('申请人', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='FILE-INFO-ID-NUMBER')],
        [sg.Text('文件状态', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(30, 1), font=('宋体', 16), key='FILE-INFO-FILE-STATUS')],
        [sg.Text('存储路径', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Multiline('', size=(30, 5), font=('宋体', 16), key='FILE-INFO-SERVER-PATH')],
        [sg.Text()],
        [sg.Text('', pad=((0, 200), 0)),
         sg.Button('取消', font=('宋体', 18))]
    ]
    return sg.Window('文件详情', layout, finalize=True, size=(520, 560), return_keyboard_events=True)


def make_window_lj_info():
    layout = [
        [sg.Text('临技详情', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text('ID', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='LJ-ID', disabled=True)],
        [sg.Text('临技编码', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='LJ-CODE')],
        [sg.Text('产品编码', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='LJ-PRO-CODE')],
        [sg.Text('任务令', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='LJ-RWL')],
        [sg.Text('开始时间', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='LJ-START-TIME')],
        [sg.Text('截止时间', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='LJ-STOP-TIME')],
        [sg.Text('影响工序', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='LJ-STATION')],
        [sg.Text('临技类别', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.InputCombo(('期间有效', '一次性有效'), size=(50, 2), font=('宋体', 16), default_value='', key='LJ-TYPE')],
        [sg.Text('备注', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='LJ-REMARK')],
        [sg.Text('临技内容', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Multiline('', size=(50, 10), font=('宋体', 16), key='LJ-INFOMATION')],
        [sg.Text()],
        [sg.Button('保存', font=('宋体', 18), pad=((220, 100), 0), key='LJ-INFO-SAVE'),
         sg.Button('取消', font=('宋体', 18))]
    ]
    return sg.Window('临技详情', layout, finalize=True, size=(720, 670), return_keyboard_events=True)


def make_window_mes_add():
    layout = [
        [sg.Text('临技MES新增', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text('任务令', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='MES-RWL')],
        [sg.Text('产品编码', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='MES-PRO-CODE')],
        [sg.Text('备注', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Multiline('', size=(50, 10), font=('宋体', 16), key='MES-REMARK')],
        [sg.Text()],
        [sg.Button('保存', font=('宋体', 18), pad=((220, 100), 0), key='MES-ADD-SAVE'),
         sg.Button('取消', font=('宋体', 18))]
    ]
    return sg.Window('临技MES新增', layout, finalize=True, size=(720, 470), return_keyboard_events=True)


def make_winodw_mes_ljtable():
    headers_mes = ['ID', '任务令', '产品编码', '备注']
    layout = [
        [sg.Text('MES临技表', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text('任务令', font=('宋体', 16), size=(6, 1), justification='center'),
         sg.Input('', font=('宋体', 16), size=(20, 1), key='MES-RWL-INPUT'),
         sg.Text('产品编码', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', font=('宋体', 16), size=(20, 1), key='MES-CODE-INPUT'),
         sg.Text('备注', font=('宋体', 16), size=(4, 1), justification='center'),
         sg.Input('', font=('宋体', 16), size=(20, 1), key='MES-REMARK-INPUT')],
        [sg.Button('新增', font=('宋体', 16), size=(8, 1), key='MES-ADD'),
         sg.Button('编辑', font=('宋体', 16), size=(8, 1), key='MES-EDIT'),
         sg.Button('删除', font=('宋体', 16), size=(8, 1), key='MES-DEL'),
         sg.Button('查询', font=('宋体', 16), size=(8, 1), key='MES-QUERY')],
        [sg.Table(values=[
            ["      ", "             ", "               ", "                                                    "]],
            headings=headers_mes,
            max_col_width=500,
            auto_size_columns=True,  # 自动调整列宽（根据上面第一次的values默认值为准，update时不会调整）
            display_row_numbers=False,  # 序号
            justification='left',  # 字符排列 left right center
            num_rows=20,  # 行数
            row_height=30,  # 行高
            key='TABLE-MES',
            font=('宋体', 16),
            text_color='black',
            background_color='white',
            enable_events=True,
            bind_return_key=True,
            tooltip='MES临技表')]
    ]

    return sg.Window('MES临技表', layout, finalize=True, size=(960, 600), return_keyboard_events=True)


def make_window_mes_edit():
    layout = [
        [sg.Text('MES临技', font=('宋体', 24), size=(100, 1), justification='center')],
        [sg.Text()],
        [sg.Text('ID', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='MES-EDIT-ID', disabled=True)],
        [sg.Text('任务令', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='MES-EDIT-RWL')],
        [sg.Text('产品编码', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='MES-EDIT-PRO-CODE')],
        [sg.Text('创建人员', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='MES-EDIT-USER')],
        [sg.Text('创建时间', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Input('', size=(50, 1), font=('宋体', 16), key='MES-EDIT-TIME')],
        [sg.Text('备注', font=('宋体', 16), size=(8, 1), justification='center'),
         sg.Multiline('', size=(50, 10), font=('宋体', 16), key='MES-EDIT-REMARK')],
        [sg.Text()],
        [sg.Button('保存', font=('宋体', 18), pad=((220, 100), 0), key='MES-EDIT-SAVE'),
         sg.Button('取消', font=('宋体', 18))]
    ]
    return sg.Window('MES临技', layout, finalize=True, size=(720, 530), return_keyboard_events=True)
