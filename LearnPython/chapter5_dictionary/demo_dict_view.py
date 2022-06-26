#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 20:14
# @Author : HongShaoRou
# @Site : 
# @File : demo_dict_view.py
# @Software: PyCharm

# 获取字典视图
"""
获取字典视图的三个方法：
    字典名.keys():获取字典中的所有key
    字典名.values():获取字典中的所有value
    字典名.items():获取字典中的所有key,value对
"""

scores = {'张三': 100, '李四': 95, '王五': 76}
print(scores)

key_lst = scores.keys()
print(key_lst, type(key_lst))
print(list(key_lst))  # 转换为列表

val_lst = scores.values()
print(val_lst, type(val_lst))
print(list(val_lst))  # 转换为列表

item_lst = scores.items()
print(item_lst, type(item_lst))
print(list(item_lst))  # 转换后的列表元素由元组组成
