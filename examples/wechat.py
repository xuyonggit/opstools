# -*- coding: utf-8 -*-

from opstools.wechat.wechat_api import WechatApi

GLOBAL_WECHAR_CONFIG = {
        'NAME': '金山小额',

        #企业的id，在管理端->"我的企业" 可以看到
        'CORP_ID': '',

        #应用列表 可以配置多个应用
        'APP_LIST': {
            'warning_robot': {           #报警机器人
                'APP_ID': '1000004',           #APPID
                'APP_SECRET': '',       #APP密钥
                'switch': 'on',          #是否开启
            },
        }
    }

if __name__ == '__main__':
    we = WechatApi(GLOBAL_WECHAR_CONFIG)
    status, res = we.apps['warning_robot'].send(
        msg_type='text',
        to_users_list=['小明'],
        msg_string='报警test'
    )
    if not status:
        print(res)
