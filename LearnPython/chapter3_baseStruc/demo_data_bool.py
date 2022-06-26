#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/11 16:06
# @Author : HongShaoRou
# @Site : 
# @File : demo_math_operator.py
# @Software: PyCharm

# 对象的布尔值，python的一切皆为对象，所有的对象都有一个bool值

# 以下对象的布尔值为False
"""
False;
数值0
None
空字符串
空列表
空元组
空字典
空集合
"""

print(bool(False))  # False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(None))  # False
print(bool(''))  # False 空字符串

print(bool([]))  # False 空列表
print(bool(list()))  # False 空列表
print(bool(()))  # False 空元组
print(bool(tuple()))  # False 空元组

print(bool({}))  # False 空字典
print(bool(dict()))  # False 空字典

print(bool(set()))  # False 空集合

print('----------其他对象的bool值均为True-------------')
print(bool(18))
print(bool(True))
print(bool('hello'))
