#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/16 12:01
# @Author : HongShaoRou
# @Site : 
# @File : demo_set.py
# @Software: PyCharm

# 集合数据结构
"""
集合：
    python内置的数据结构之一
    与列表、字典一样都属于可变类型的序列
    集合是没有value的字典
"""

"""
集合的创建方式：
    直接{}: 
        集合名 = {key1, key2, ...}
    使用内置函数set():
        集合名 = set(可迭代对象)
"""

# 第一种创建方式
mySet = {'python', 'world', 98, 98}  # 重复元素会自动删除
print(mySet, type(mySet))

# 第二种创建方式
mySet = set(range(0, 6, 2))
print(mySet, type(mySet))

mySet = set([1, 2, 3, 4, 5, 6, 6])  # 通过列表创建
print(mySet, type(mySet))

mySet = set((1, 2, 3, 4, 65, 6, 6))  # 通过元组创建
print(mySet, type(mySet))  # 集合的元素是无序的

mySet = set('helloworld')
print(mySet, type(mySet))  # 集合的元素是无序的

mySet = set({1, 2, 2, 65, 65, 124, 1})
print(mySet, type(mySet))  # 集合的元素是无序的

# 定义一个空集合
s = set()
print(s, type(s))
