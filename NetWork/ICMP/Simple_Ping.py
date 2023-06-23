# -*- coding: utf-8 -*-

"""
@author: jiaopengyu991212@gmail.com
@file: Simple_Ping.py
@project:study
@software: PyCharm
@time: 23/6/23 11:12
"""
import time
from ping3 import ping
# from ping3 import verbose_ping
from datetime import datetime


def simple_ping(dst_addr, src_addr, timeout, num, time_sleep):
    """
    :param time_sleep: ping间隔
    :param dst_addr: 目的地址
    :param src_addr: 源地址
    :param timeout: 超时时间
    :param num: 循环次数
    :return: 0:成功，1:失败
    """
    x = y = i = 0
    while i < num:
        try:
            a = ping(dst_addr, src_addr=src_addr, timeout=timeout)
            if a is None or a is False:
                x += 1
                i += 1
                print("时间：%s：第 %s 次ping %s 失败" % (datetime.now(), i, dst_addr))
            else:
                y += 1
                i += 1
                print("时间：%s：第 %s 次ping %s 成功，耗时 %f 秒" % (datetime.now(), i, dst_addr, a))
        except Exception as e:
            print("时间：%s：%s:%s" % (datetime.now(), e.__class__, e))
            x += 1
            i += 1
        time.sleep(time_sleep)
    result = y / num
    if result >= 0.80:
        print("%f%% 成功率，ping %s 成功" % (result * 100, dst_addr))
        return 0
    else:
        print("%f%% 丢包率，ping %s 失败" % ((1 - result) * 100, dst_addr))
        return 1
