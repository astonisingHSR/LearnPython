#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/19 14:28
# @Author : HongShaoRou
# @Site : 
# @File : demo_func_return.py
# @Software: PyCharm

# 函数返回值
"""
函数的返回值：
    如果没有返回值，return可以省略不写
    如果返回1个值，直接返回类型
    如果返回多个值时，结果为元组
"""


def func(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


myLst = range(0, 20)
print(func(num=myLst))
