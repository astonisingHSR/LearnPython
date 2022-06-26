#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 19:12
# @Author : HongShaoRou
# @Site : 
# @File : demo_list_update.py
# @Software: PyCharm

# 列表元素修改
lst = [10, 20, 30, 40]
print(lst)

# 一次修改一个值
lst[2] = 100
print(lst)

# 一次修改多个值
lst[1:3] = [100,  200, 300, 400]
print(lst)
