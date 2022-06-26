#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 15:33
# @Author : HongShaoRou
# @Site : 
# @File : demo_list.py
# @Software: PyCharm

# python中的列表list

# 变量存储的是一个对象的引用
a = 10
lst = ['hello', 'world', 98]
print(id(lst))
print(type(lst))
print(lst)

# 列表对象的创建
"""
使用中括号[],元素之间用, 隔开
使用内置函数list
"""

# 使用第二种方式
lst = list(['hello', 'world', 98, 'hello'])   # 新建了一个list对象，返回其引用
print(id(lst))
print(type(lst))
print(lst)

"""
列表的特点
    元素按照顺序排列
    索引映射唯一一个数据
    列表可以存储重复数据
    任意数据类型混存
    根据需要动态分配和内存回收
"""
print(lst[0], lst[-1])  # 正数索引 0 ~ n-1，负数索引 -n ~ -1

# 获取指定元素的索引
print(lst.index('hello'))  # 如果列表中有相同的目标元素，只返回第一个目标元素的索引
# print(lst.index(20))  # 如果列表中不存在目标元素，则程序异常

print(lst.index('hello', 1, 4))  # 从第1个元素到第4个元素之间进行查找，不包括第四个元素

# 列表的查询操作


lst = ['hello', 'hello', 'world', 98, 234]
# 获取列表的多个元素
"""
列表名[start:stop:step],默认start = 0;stop = n;step = 1;不包括stop
"""
sublst = lst[0:7:2]   # 原列表的拷贝
print(id(lst))
print(id(sublst))
print(lst[0:5])   # 默认步长为1
print(lst[::2])

print(lst[4::-2])  # step为负数
