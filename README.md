# 运维工具库
### 包含：
* #### 封装mysql
## 安装
pip install git+https://github.com/xuyonggit/opstools.git
#### 封装mysql
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
#### 封装企业微信接口
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