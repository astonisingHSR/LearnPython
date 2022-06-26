#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/12 19:15
# @Author : HongShaoRou
# @Site : 
# @File : demo_list_sort.py
# @Software: PyCharm

# 列表的排序操作
"""
列表的排序操作：
    调用sort()方法：对列表中元素按照升序进行排序，可以指定 reverse = True，来实现降序排序
    调用内置函数sorted(),可以指定 reverse = True，来实现降序排序，原列表不发生改变
"""
lst = [2, 3, 5, 1, 4, 6, 7]
print('排序前：', lst, id(lst))

lst.sort()  # 默认升序排序,原列表id不发生改变
print('排序后', lst, id(lst))

lst.sort(reverse=True)  # 降序排列
print('排序后', lst, id(lst))
lst.sort(reverse=False)  # 升序排列
print('排序后', lst, id(lst))

# 调用内置函数sorted()
lst2 = sorted(lst)  # 内置函数sorted()将产生一个新列表
print('排序前', lst, id(lst))
print('排序后', lst2, id(lst2))

lst3 = sorted(lst, reverse=True)  # 内置函数sorted()将产生一个新列表,
print('排序后', lst3, id(lst3))

