#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 19:24
# @Author : HongShaoRou
# @Site : 
# @File : demo_list_generator.py
# @Software: PyCharm

# 列表生成式
"""
语法格式：
    [列表元素表达式 for 自定义变量 in 可迭代对象(range())]
注意事项：
    列表元素表达式中 通常包含自定义变量
"""

lst = [i for i in range(2, 11, 2)]
print(lst)

lst = [i**2 for i in range(2, 11, 2)]
print(lst)
