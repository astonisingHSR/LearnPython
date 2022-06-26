#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/25 13:26
# @Author : HongShaoRou
# @Site : 
# @File : demo_with.py
# @Software: PyCharm

# with语句
"""
with语句：上下文管理器
    with语句可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确的关闭，以此来达到释放资源的目的
语法：
    with open('文件名'，mode) as 文件对象名:
        代码块
作用：
    with语句调用__enter__()方法。离开with语句块，自动调用__exit__()方法
"""

with open('readFile.txt', 'r', encoding='utf-8') as file:
    print(file.read(2))

