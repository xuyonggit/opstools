# -*- coding: utf-8 -*-
import random


class MakePassword(object):
    def __init__(self):
        pass

    @staticmethod
    def __get_num(num):
        templates = "0123456789"
        return random.sample(templates, num)

    @staticmethod
    def __get_lword(num):
        L = []
        for i in range(97, 123):
            L.append(chr(i))
        return random.sample(L, num)

    @staticmethod
    def __get_bword(num):
        L = []
        for i in range(65, 91):
            L.append(chr(i))
        return random.sample(L, num)

    @staticmethod
    def __get_fuhao(num):
        S = "!~`@$^&*()_+}{[]:;?/>.<,|"
        return random.sample(S, num)

    def getsamplepassword(self, num=8):
        self.passwd = ""
        # 1/2 数字 & 1/2 小写字母 & other 小写字母
        nums = num // 2
        lw = num // 2
        other = num % 2
        listofpasswd = self.__get_num(nums) + self.__get_lword(lw) + self.__get_lword(other)
        temp_l = [x for x in range(0, len(listofpasswd))]
        while len(temp_l) > 0:
            l = random.sample(temp_l, 1)
            self.passwd = self.passwd + str(listofpasswd[l[0]])
            temp_l.remove(l[0])
        return self.passwd

    def getpassword(self, num=12):
        self.passwd = ""
        # 1/3 数字 & 1/3 小写字母 & 1/3 大写字母  & other 小写字母
        nums = num // 3
        lw = num // 3
        bw = num // 3
        other = num % 3
        listofpasswd = self.__get_num(nums) + self.__get_lword(lw) + self.__get_bword(bw) + self.__get_lword(other)
        temp_l = [x for x in range(0, len(listofpasswd))]
        while len(temp_l) > 0:
            l = random.sample(temp_l, 1)
            self.passwd = self.passwd + str(listofpasswd[l[0]])
            temp_l.remove(l[0])
        return self.passwd

    def gethardpassword(self, num=18):
        self.passwd = ""
        # 1/5 数字 & 1/5 小写字母 & 1/5 大写字母 1/5 特殊符号 & other 小写字母
        nums = num // 5
        lw = num // 5
        bw = num // 5
        fh = num // 5
        other = num % 5
        listofpasswd = self.__get_num(nums) + self.__get_lword(lw) + self.__get_bword(bw) + self.__get_fuhao(fh) + self.__get_lword(other)
        temp_l = [x for x in range(0, len(listofpasswd))]
        while len(temp_l) > 0:
            l = random.sample(temp_l, 1)
            self.passwd = self.passwd + str(listofpasswd[l[0]])
            temp_l.remove(l[0])
        return self.passwd