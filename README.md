# 运维工具库
### 包含：
* #### 封装mysql
* #### 封装企业微信接口
* #### 封装发送邮件接口
### 安装
pip install git+https://github.com/xuyonggit/opstools.git
### 封装mysql
```python
from opstools.Base.mysql_api import BaseMysql


class TestMysql(BaseMysql):
    def init_conf(self):
        self.MYSQL_HOST = ''
        self.MYSQL_USER = ''
        self.MYSQL_DATABASE = ''
        self.MYSQL_PW = ''


if __name__ == '__main__':
    Test = TestMysql()
    # 查询操作
    with Test as T:
        print(T.query_sql("select * from dag"))
    # 写入操作以及更新操作
    with Test as T:
        T.do_sql("update | insert ...")
```
### 封装企业微信接口
```python
from opstools.wechat.wechat_api import WechatApi

GLOBAL_WECHAR_CONFIG = {
        'NAME': '金山小额',

        #企业的id，在管理端->"我的企业" 可以看到
        'CORP_ID': '',

        #应用列表 可以配置多个应用
        'APP_LIST': {
            'warning_robot': {           #报警机器人
                'APP_ID': '',           #APPID
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
```
### 封装发送邮件接口
```python
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
    ea.add_table([['姓名', '年龄', '性别'], ['xuyong1', 25, '男']])
    # 添加附件
    ea.add_attr("C:\\Users\\xu's\\PycharmProjects\\opstools\\examples\\wechat.py")
    status, res = ea.send_email()
    print(res)
```
###### 效果图
![avatar](https://github.com/xuyonggit/opstools/blob/master/examples/image/emailapi.png)
