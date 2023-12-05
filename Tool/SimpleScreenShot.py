# -*- coding: utf-8 -*-

"""
@author: jiaopengyu991212@gmail.com
@file: SimpleScreenShot.py
@project:study
@software: PyCharm
@time: 23/12/5 16:46
"""
from PIL import ImageGrab
from datetime import datetime


# 此函数默认截取整个屏幕，若要截取部分屏幕，可参考如下网址
# https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html
def simple_screen_shot(path):
    """
    :param path:保存路径
    :return: 无返回值
    """
    try:
        new_screen_shot = ImageGrab.grab(include_layered_windows=False, all_screens=False, xdisplay=None)
        new_screen_shot.save("%s%s.jpg" % (path, datetime.now().strftime("%Y-%m-%d %H-%M-%S")))
    except Exception as e:
        print("时间：%s：%s:%s" % (datetime.now(), e.__class__, e))
