#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/16 12:37
# @Author : HongShaoRou
# @Site : 
# @File : demo_set_generator.py
# @Software: PyCharm

# 集合生成式
"""
集合名 = {集合元素表达式 for 自定义变量 in 可迭代对象}
"""

# 列表生成式
myLst = [i**2 for i in range(0, 10)]
print(myLst)

mySet = {i**2 for i in range(0, 10)}
print(mySet)

"""
列表、字典、元组、集合总结
数据结构    是否可变    是否重复    是否有序    定义符号
列表(list)   可变       可重复      有序        []
元组(tuple)  不可变     可重复      有序        ()
字典(dict)   可变     key不可重复   无序    {key:value}
                    value可重复              
集合(set)    可变     不可重复      无序        {}
"""