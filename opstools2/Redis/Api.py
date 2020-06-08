# -*- coding: utf-8 -*-
#   Copyright (C) 2020 All rights reserved.
#
#  FileName      ：redisdel.py
#  Author        ：xuyong1
#  Email         ：xuyong1@kingsoft.com
#  Date          ：2020年06月04日
#  Description   ：Redis 操作封装 生产环境批量删除key有风险，操作请谨慎
#
import redis
import time
import re


class redisops(object):
    def __init__(self, host, port, password=None):
        self.host = host
        self.port = port
        self.password = password
        self.redis = self.init()
        self.notallowkeys = []

    def init(self):
        pool = redis.ConnectionPool(host=self.host, port=self.port, password=self.password)
        return redis.Redis(
                connection_pool=pool,
                decode_responses=True
                )

    def deny(self, rex):
        """
        自定义拒绝key格式
        :param rex: re正则格式 eg: "^[a-z]"
        :return: None
        """
        if not isinstance(rex, (str, list)):
            raise TypeError("rex must be str or list , but gave {}".format(type(rex)))
        if isinstance(rex, list):
            for i in rex:
                self.notallowkeys.append(i)
        else:
            self.notallowkeys.append(rex)

    def __check_option(self, option):
        """
        检查参数，避免恶意匹配以及手误操作
        :param option: 键或者模糊键
        :return: 键或者模糊键
        """
        self.notallowkeys += ["^(\\*)+$", "^\\*.*\\*$"]
        for i in self.notallowkeys:
            if re.match(i, option):
                raise Exception('Key match error: The key need not match: "^(\\*)+$", "^\\*.*\\*$", "{}"'.format('\", \"'.join(x for x in self.notallowkeys)))
        return option

    def getkeys(self, option):
        """
        获取key或者批量获取key
        :param option: 键或者模糊键
        :return:
        """
        option = self.__check_option(option)
        begin_pos = 0
        count = 0
        _data = []
        while True:
            result = self.redis.scan(begin_pos, option, 1000)
            return_pos, datalist = result
            if len(datalist) > 0:
                for i in datalist:
                    count += 1
                    _data.append(i.decode())
            begin_pos = return_pos
            if begin_pos == 0:
                break
        return count, _data

    def delkeys(self, option, deltime=0.1):
        """
        删除key或者批量删除key
        :param option: 键或者模糊键
        :param deltime: 删除间隔
        :return:
        """
        option = self.__check_option(option)
        begin_pos = 0
        count = 0
        fcount = 0
        while True:
            result = self.redis.scan(begin_pos, option, 1000)
            return_pos, datalist = result
            if len(datalist) > 0:
                for i in datalist:
                    print('delete key : {}'.format(i.decode()), end="...")
                    time.sleep(deltime)
                    res = self.redis.delete(i)
                    if res == 1:
                        print('success')
                        count += 1
                    else:
                        print('failed')
                        fcount += 1
            begin_pos = return_pos
            if begin_pos == 0:
                break
        print("delete done, {} success, {} failed".format(count, fcount))

    def test(self, option):
        print(self.__check_option(option))
