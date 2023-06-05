# -*- coding: utf-8 -*-
'''
@author: jiaopengyu991212@gmail.com
@file: tmp.py
@software: vscode
@time: 2023/06/05 13:17:29
'''

from NetWork.TCP import TcpPing


if  __name__ == '__main__':
    a = TcpPing.simple_tcping("192.168.1.253", 10)
    print (a)

