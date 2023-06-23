# -*- coding: utf-8 -*-
"""
@author: jiaopengyu991212@gmail.com
@file: tmp.py
@software: vscode
@time: 2023/06/05 13:17:29
"""

from NetWork.ICMP import Simple_Ping

if __name__ == '__main__':
    a = Simple_Ping.simple_ping("baidu.com", "192.168.1.254", 0.2, 10, 0.02)
    print(a)
