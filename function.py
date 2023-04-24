# -*- coding: utf-8 -*-
import math


def my_abs(x):      # 自定义绝对值函数
    if not isinstance(x, (int, float)):     # 如果传参不为整型和浮点型，打印下一行TypeError中的报错
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, z, n=0.0):       # 多参函数
    mx = x+z*math.cos(n)
    my = y-z*math.sin(n)
    return mx, my


def quadratic(x, y, z):     # 解一元二次方程
    m1 = (-y+math.sqrt(math.pow(y, 2)-4*x*z))/(2*x)
    m2 = (-y-math.sqrt(math.pow(y, 2)-4*x*z))/(2*x)
    return m1, m2


if __name__ == '__main__':
    a = my_abs(-908)
    print(a)
    r = move(100, 200, 300, math.pi / 6)
    print(r)
    print(100+300*math.cos(math.pi/6))
    print(200-300*math.sin(math.pi/6))
    w = quadratic(1, 0, -1)
    print(w)


"""
@author: jiaopengyu
@file: function.py
@project:study
@software: PyCharm
@time: 2022/7/12 14:32
"""
