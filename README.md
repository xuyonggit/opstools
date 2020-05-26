# 运维工具库
### 包含：
* #### 封装mysql
## 安装
pip install git+https://github.com/xuyonggit/opstools.git
#### 封装mysql
```
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