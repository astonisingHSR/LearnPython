#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 20:45
# @Author : HongShaoRou
# @Site : 
# @File : demo_cell.py
# @Software: PyCharm

# 元组数据结构

"""
可变序列：
    列表
    字典
"""

print('----------------不可变序列------------')
str1 = 'hello'
print(id(str1))
str1 = str1 + 'world'
print(id(str1))  # 返回新的引用对象


print('----------------可变序列------------')
lst = [1, 2, 3]
print(id(lst))
lst.append(4)
print(id(lst))

"""
不可变序列：
    字符串
    元组:python内置的数据结构之一
"""

"""
元组的创建方式：
    直接小括号： 元组名 = (cell1, cell2, cell3, ...)
    使用内置函数tuple(): 元组名 = tuple( (cell1, cell2, cell3, ...) )
    只包含一个元素的元组需要使用逗号,和小括号(): 元组名 = (cell1, )
"""

# 小括号方式，小括号可以省略
t = ('hello', 'world', 23)
t2 = 'hello', 'world', 98
print(type(t), t)
print(type(t2), t2)

# 内置函数tuple()
t = tuple(('hello', 'world', 23))
print(type(t), t)

# 只包含一个元素的元组,逗号必须加上
t = (10, )
print(type(t), t)

# 空元组
t = ()
print(type(t), t)

"""
为什么要将元组设计为不可变序列：
    在多任务环境下，同时操作对象不需要加锁
    因此在程序中尽量使用不可变序列
    注意事项：元组存储的是对象的引用
        如果元组中对象本身是不可变对象，则不能再引用其他对象
        如果元组中的对象是可变对象，则可变对象的引用不允许改变，但数据可以改变
"""