#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/10 23:56
# @Author : HongShaoRou
# @Site : 
# @File : demo_compare_operator.py
# @Software: PyCharm

# 比较运算符
a, b = 10, 20
print('is a > b?', a > b)  # False
print('is a < b?', a < b)  # True
print('is a <= b?', a <= b)  # True
print('is a == b?', a == b)  # False
print('is a != b?', a != b)  # True

'''
== 比较的是变量的值
如果要比较变量的id，则应该使用 is
'''

a = 10
b = 10
print(a == b)  # True
print(a is b)  # True，说明a与b的值和id均相等
lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # 比较的是值，True
print(lst1 is lst2)  # 比较的是id,False
print(id(lst1), id(lst2))
print(a is not b)  # a,b的id是相等，所以为False
print(lst1 is not lst2)  # lst1,lst2的id不相等，所以为True
