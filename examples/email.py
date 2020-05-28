# -*- coding: utf-8 -*-
from opstools.email.tools.Coreapi import EmailApi
CONFIG = {
    # 组
    'test1': {
        'name': '',         # 组名 即邮件主题
        'user': '',         # 发件人
        'alias': '',        # 发件人别名 可为空
        'password': '',     # 发件人密码
        'smtp': '',         # smtp服务器
        'port': 25,
        'to_list': ['xuyong1@wps.cn'],      # 收件人列表
        'cc_list': []       # 抄送列表
    }
}

if __name__ == '__main__':
    ea = EmailApi(CONFIG).apps['test1']
    # 添加文本
    ea.add_str('lalala')
    # 添加图片
    ea.add_image("C:\\Users\\xu's\\PycharmProjects\\opstools\\examples\\123.jpg")
    # 添加表格
    ea.add_table([['姓名', '年龄', '性别'], ['xuyong1', 25, '男'], ['刘龙', 25, '男']])
    # 添加附件
    ea.add_attr("C:\\Users\\xu's\\PycharmProjects\\opstools\\examples\\wechat.py")
    status, res = ea.send_email()
    print(res)
