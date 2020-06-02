# -*- coding: utf-8 -*-
from opstools2.Base.password import MakePassword

if __name__ == '__main__':
    # 生成简单密码
    print(MakePassword().getsamplepassword())
    # 生成普通密码
    print(MakePassword().getpassword())
    # 生成困难密码
    print(MakePassword().gethardpassword())
