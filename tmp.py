# -*- coding: utf-8 -*-

"""
@author: jiaopengyu991212@gmail.com
@file: tmp.py
@software: vscode
@time: 2023/06/05 13:17:29
"""

from NetWork.Telnet import Simple_Telnet_Client

if __name__ == '__main__':
    a = Simple_Telnet_Client.simple_telnet_connect("login:", "Password:", "$", "mikasa", "192.168.1.250", 23, "mikasa", "0000", 0, "ip -4 a")
    print(a)
