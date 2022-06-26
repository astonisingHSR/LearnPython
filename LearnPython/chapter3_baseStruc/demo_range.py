#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/11 18:00
# @Author : HongShaoRou
# @Site : 
# @File : demo_range.py
# @Software: PyCharm

# 内置函数range的使用
"""
用于生成一个整数序列
创建range对象的三种方式：
    range(stop)     创建一个 0~stop之间的序列，步长为1
    range(start,stop)   创建一个 start~stop之间的整数序列，步长为1
    range(start,stop,step)  创建一个 start~stop之间的整数序列，步长为step
返回值是一个迭代器对象
range类型的优点：
    与整数序列长度无关，所有range对象占用的空间是相同的
    in 和 not in 判断整数序列中是否存在（不存在）目标值
"""

# 第一种创建方式
ite = range(10)
print(list(ite))  # 可以用于查看range对象中的整数序列    list是列表

# 第二种创建方式
ite = range(1, 10)
print(list(ite))

# 第三种创建方式
ite = range(0, 10, 2)
print(list(ite))

print(1 in ite)  # False
print(1 not in ite)  # True
