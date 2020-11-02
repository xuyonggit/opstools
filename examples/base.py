# -*- coding: utf-8 -*-
from opstools2.Base.password import makepassword

if __name__ == '__main__':
    # 生成简单密码
    print(makepassword.getsamplepassword())
    # 生成普通密码
    print(makepassword.getpassword())
    # 生成困难密码
    print(makepassword.gethardpassword())
