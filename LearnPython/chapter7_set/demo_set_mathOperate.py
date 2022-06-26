#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/16 12:31
# @Author : HongShaoRou
# @Site : 
# @File : demo_set_mathOperate.py
# @Software: PyCharm

# 集合的数学操作
"""
交集、并集、差集、对称差集
"""

s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}

# 交集操作
print(s1.intersection(s2))
print(s1 & s2)  # 运算符&表示交集操作

# 并集操作
print(s1.union(s2))
print(s1 | s2)  # 运算符|表示交集操作

# 差集操作
print(s1.difference(s2))
print(s1 - s2)

# 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

