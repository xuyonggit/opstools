# -*- coding: utf-8 -*-
import random


class MakePassword(object):
    def __init__(self):
        pass

    @staticmethod
    def _get_num(num):
        _l = []
        templates = "0123456789"
        for i in range(num):
            _l.append(random.sample(templates, 1)[0])
        return _l

    @staticmethod
    def _get_lword(num):
        templates = []
        _l = []
        for i in range(97, 123):
            templates.append(chr(i))
        for i in range(num):
            _l.append(random.sample(templates, 1)[0])
        return _l

    @staticmethod
    def _get_bword(num):
        templates = []
        _l = []
        for i in range(65, 91):
            templates.append(chr(i))
        for i in range(num):
            _l.append(random.sample(templates, 1)[0])
        return _l

    @staticmethod
    def _get_fuhao(num):
        _l = []
        templates = "!~`@$^&*()_+}{[]:;?/>.<,|"
        for i in range(num):
            _l.append(random.sample(templates, 1)[0])
        return _l

    @staticmethod
    def _make_pwd(pwd_list):
        passwd = ""
        temp_l = [x for x in range(0, len(pwd_list))]
        while len(temp_l) > 0:
            l = random.sample(temp_l, 1)
            passwd = passwd + str(pwd_list[l[0]])
            temp_l.remove(l[0])
        return passwd

    def getsamplepassword(self, num=8):
        # 1/2 数字 & 1/2 小写字母 & other 小写字母
        nums = num // 2
        lw = num // 2
        other = num % 2
        listofpasswd = self._get_num(nums) + self._get_lword(lw) + self._get_lword(other)
        return self._make_pwd(listofpasswd)

    def getpassword(self, num=12):
        # 1/3 数字 & 1/3 小写字母 & 1/3 大写字母  & other 小写字母
        nums = num // 3
        lw = num // 3
        bw = num // 3
        other = num % 3
        listofpasswd = self._get_num(nums) + self._get_lword(lw) + self._get_bword(bw) + self._get_lword(other)
        return self._make_pwd(listofpasswd)

    def gethardpassword(self, num=18):
        # 1/4 数字 & 1/4 小写字母 & 1/4 大写字母 1/4 特殊符号 & other 小写字母
        nums = num // 4
        lw = num // 4
        bw = num // 4
        fh = num // 4
        other = num % 4
        listofpasswd = self._get_num(nums) + self._get_lword(lw) + self._get_bword(bw) + self._get_fuhao(fh) + self._get_lword(other)
        return self._make_pwd(listofpasswd)