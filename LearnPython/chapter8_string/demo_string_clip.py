#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/18 21:12
# @Author : HongShaoRou
# @Site : 
# @File : demo_string_clip.py
# @Software: PyCharm

# 字符串的切片操作
"""
字符串是不可变类型
    不具备增、删、改等操作
    切片将产生新的对象
"""

s = 'hello world'
s1 = s[:5]  # 起始位置默认为0
print(s1)
s2 = s[6:]  # 结束位置默认为字符串末尾
print(s2)
print('-------------------------')
s3 = '|'
str1 = s1 + s3 + s2
print(str1)

print('=====================字符串名[start:end:step]=====================')
print(s[1:5:1])  # 从索引1开始，直到索引5，步长为1，不包括5
print(s[::2])  # 默认从0开始，到末尾结束，步长为2
print(s[::-1])  # 默认从最后一个字符开始，到第1个字符结束，因为步长为-1
print(s[-5::1])


