# -*- coding: utf-8 -*-

"""
@author: jiaopengyu991212@gmail.com
@file: Simple_Telnet_Client.py
@project:study
@software: PyCharm
@time: 23/6/24 11:25
"""
from telnetlib import Telnet    # telnetlib模块在python3.13版本及之后被移除，需要安装telnetlib3，并重写函数
from datetime import datetime


def simple_telnet_connect(login, password, command, result_cmd, ip, port, user, passwd, debuglevel, cmd):
    """
    :param login: 登录提示符
    :param password: 密码提示符
    :param command: 命令提示符
    :param result_cmd: 命令执行结果提示符
    :param ip: 目的地址
    :param port: 端口号
    :param user: 用户名
    :param passwd: 密码
    :param debuglevel: 调试级别
    :param cmd: 命令
    :return: 0:成功，1:失败
    """
    try:
        new_telnet = Telnet(ip, port, timeout=5)
        new_telnet.set_debuglevel(debuglevel)   # 设置调试级别，debuglevel值越高，显示信息越多
        new_telnet.read_until(login.encode('ascii'), timeout=5)  # 读取到登录提示符（例如“login:”）时，停止读取，超时时间为5秒
        new_telnet.write(user.encode('ascii') + b"\n")  # 发送用户名
        new_telnet.read_until(password.encode('ascii'), timeout=5)  # 读取到密码提示符（例如“Password:”）时，停止读取，超时时间为5秒
        new_telnet.write(passwd.encode('ascii') + b"\n")  # 发送密码
        new_telnet.read_until(command.encode('ascii'), timeout=5)  # 读取到命令提示符（例如“$”）时，停止读取，超时时间为5秒
        new_telnet.write(cmd.encode('ascii') + b"\n")  # 发送命令
        # new_telnet.read_until(b"$", timeout=5)  # 读取到“$”时，停止读取，超时时间为5秒
        # a = new_telnet.expect([], timeout=5)[2].decode().strip()  # 超时时间5秒后停止读取
        a = new_telnet.expect([result_cmd.encode('ascii')], timeout=5)[2].decode().strip()  # 读取到命令结果结束提示符（例如用户名或“#”或“$”）时，停止读取，超时时间为5秒
        print(a)
        new_telnet.close()
        print("时间：%s：telnet %s 成功" % (datetime.now(), ip))
        return 0
    except Exception as e:
        print("时间：%s：%s:%s" % (datetime.now(), e.__class__, e))
        print("时间：%s：telnet %s 失败" % (datetime.now(), ip))
        return 1
