# -*- coding: utf-8 -*-
from opstools2.Redis.Api import redisops

if __name__ == '__main__':
    R = redisops(host='10.90.128.41', port=6379, password='123456')  # password 可选

    # 增加用户自定义拒绝keys正则格式
    R.deny(11111)

    # 模糊批量查询keys
    _count, _data = R.getkeys('session-*')
    print(_count)  # 数据量特别大时不建议操作返回值：_data

    # 模糊批量删除keys
    # R.delkeys('session-*', deltime=0.2)  # deltime 可选，删除间隔（单位：s)，默认0.1s