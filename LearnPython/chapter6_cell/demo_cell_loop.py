#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/16 11:58
# @Author : HongShaoRou
# @Site : 
# @File : demo_cell_loop.py
# @Software: PyCharm

# 元组的遍历
"""
元组是可迭代对象，可以采用 for in 进行遍历
"""

t = ('hello', 'world', 98)

'''使用索引进行遍历'''
print(t[0])
print(t[1])
print(t[2])

'''使用for in 进行遍历'''
for item in t:
    print(item)
