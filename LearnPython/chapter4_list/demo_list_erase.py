#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 16:16
# @Author : HongShaoRou
# @Site : 
# @File : demo_list_erase.py
# @Software: PyCharm

# 列表的删除操作
"""
remove()方法：
    一次删除一个元素
    重复元素只删除第一个
    元素不存在输出ValueError
pop()方法：
    删除一个指定索引位置上的元素
    指定索引不存在输出IndexError
    不指定索引，删除列表中最后一个元素
切片：一次至少删除一个元素
clear()方法：清空列表
del: 删除列表
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lst)

lst.remove(3)  # 从列表中移除第一个目标元素
print(lst)

lst.pop()  # 删除列表最后一个元素
print(lst)

lst.pop(2)  # 删除索引为2的元素
print(lst)

lst[1:3] = []  # 删除 1~3索引位置的元素，不包括索引3
print(lst)

lst.clear()  # 清空列表所有元素
print(lst)

del lst  # 删除lst对象实例
