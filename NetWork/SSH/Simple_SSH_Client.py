# -*- coding: utf-8 -*-

import paramiko


def simple_ssh_connect(ip, port, user, passwd, cmd):
    new_ssh = paramiko.SSHClient()  # 创建一个新的SSH连接
    try:
        new_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 用户名密码登录方式
        new_ssh.connect(hostname=ip, port=port, username=user, password=passwd, timeout=5, compress=True)
        stdin, stdout, stderr = new_ssh.exec_command(command=cmd)
        print(stdout.read().decode())
        print(stderr.read().decode())
    except Exception as e:
        print("%s:%s" % (e.__class__, e))
    finally:
        new_ssh.close()


"""
@author: jiaopengyu
@file: Simple_SSH_Client.py.py
@project:study
@software: PyCharm
@time: 2023/4/7 10:18
"""