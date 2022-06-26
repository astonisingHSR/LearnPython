#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 16:15
# @Author : HongShaoRou
# @Site : 
# @File : demo_list_increase.py
# @Software: PyCharm

# 列表的增删改

# 增加
"""
append()方法：在列表的末尾添加一个元素
extend()方法：在列表的末尾至少添加一个元素
insert()方法：在列表的任意位置添加一个元素
切片：在列表的任意位置至少添加一个元素
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 末尾添加一个元素
print(lst, id(lst))
lst.append(11)  # 并没有改变列表的id值
print(lst, id(lst))

lst2 = [20, 30, 40]

# lst.append(lst2)   # 将lst2作为一个元素添加的lst的末尾
lst.extend(lst2)  # 添加多个元素
print(lst)

# 在任意位置添加元素
lst.insert(1, 90)  # 在索引1位置添加元素90
print(lst)

# 在任意位置添加多个元素
lst[1:5] = lst2  # 把指定位置元素替换
print(lst)
