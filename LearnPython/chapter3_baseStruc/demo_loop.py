#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/11 18:10
# @Author : HongShaoRou
# @Site : 
# @File : demo_loop.py
# @Software: PyCharm

# 循环结构

# while循环
"""
while四步循环法：
    初始化变量
    条件判断
    条件执行体
    改变变量
初始化变量与改变的变量为同一个
"""

i = 0
tmp = 0
while i in range(10):
    i += 1
    tmp += i

print(tmp)
# for in 循环
"""
in从字符串、序列中依次取值，即便利
for-in遍历的对象必须是可迭代对象
循环体内不需要自定义变量，可以将自定义变量替代为下划线_
"""
tmp = 0
for j in range(10):
    tmp += j

print(tmp)

for letter in 'Hello World':
    print(letter)

for _ in range(0, 10, 2):
    print(0)

sum = 0
for i in range(0, 101, 2):
    sum += i

print(sum)