#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 20:32
# @Author : HongShaoRou
# @Site : 
# @File : demo_dict_generator.py
# @Software: PyCharm

# 字典生成式
"""
内置函数zip():
    用于将可迭代对象作为参数，将对象中对应元素打包成一个元组，然后返回由这些元组组成列表
    语法：列表名 = zip(key_list, value_list)
字典生成式：
    字典名 = {key表达式：value表达式 for 自定义key变量，自定义value变量 in zip(key_list,value_list)}
"""

item_lst = ["apple", "banana", "orange"]
price_lst = [5, 8, 6]


d = {item.upper(): price for item, price in zip(item_lst, price_lst)}  # item.upper()表示字母升大写
print(d)

price_lst = [5, 8, 6, 12, 10]


d1 = {item.upper(): price for item, price in zip(item_lst, price_lst)}  # 元素个数不同时按照元素少的list为准
print(d1)
