# -*- coding: utf-8 -*-

from tcping import Ping


def simple_tcping(ip, num):
    new_tcping = Ping(ip, 80, 3)    # ip，端口，超时时间
    new_tcping.ping(num)
#    res = new_tcping.result.table   # 以表格形式展现（ping.result.raw  # 原始形态，ping.result.rows  # 行显示）
    ret = new_tcping.result.raw
    ret_list = list(ret.split('\n'))
    success_rata = ret_list[2].split(',')[3].split(' ')[1]  # 获取成功Ping通比率
#    return res, success_rata
    if float(success_rata.strip("%")) > 80.0:
        return 0
    else:
        return 1


"""
@author: jiaopengyu
@file: TcpPing.py
@project:study
@software: PyCharm
@time: 2023/4/15 13:14
"""
