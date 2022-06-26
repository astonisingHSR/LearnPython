#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 19:29
# @Author : HongShaoRou
# @Site : 
# @File : demo_dict.py
# @Software: PyCharm

# 字典数据结构
"""
字典：
    即哈希表，对应C++中的unordered_map，能够以o(1)的复杂度实现元素查找。
    python内置的数据结构之一，与列表一样是一个可变序列
    以键值对的方式存储数据，字典是一个无序的序列
    第一个元素为键: key,第二个元素为值： value
创建方式：
    使用大括号{}：字典名 = {key1: value1, key2: value2, ...}
    使用内置函数dict():字典名 = dict(变量1 = key1, 变量2 = value1)
"""
scores = {'张三': 100, '李四': 95, '王五': 76}
print(scores, id(scores), type(scores))

ages = dict(name='jack', age=20)
print(ages, id(ages), type(ages))

d = {}  # 创建空字典
print(d)

"""
字典的特点：
    字典中的元素是一个key-value对，key不允许重复，value可以重复
    字典中的元素是无序的
    字典中的key必须是不可变对象
    字典也可以根据需要动态的伸缩
    字典会浪费较大的内存，是一种使用空间换时间的数据结构
"""

d = {'name': 'jack', 'name': 'peter'}
print(d)  # jack被peter覆盖掉了,因为key：name重复了
d = {'name': 'jack', 'nickname': 'peter'}
print(d)  # value可以重复

lst = [10, 20]
lst.insert(2, 30)
# d = {lst: 20}  # TypeError: unhashable type: 'list'，因为list是一个可变对象，不能作为key值
# print(d)