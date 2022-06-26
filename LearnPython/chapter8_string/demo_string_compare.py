#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/18 20:59
# @Author : HongShaoRou
# @Site : 
# @File : demo_string_compare.py
# @Software: PyCharm

# 字符串的比较操作
"""
字符串的比较操作：
    运算符：>, >=, <, <=, ==, !=
    比较规则：首先比较两个字符串的第一个字符，如果相等则继续比较下一个字符，
            依次比较下去，直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果
            两个字符串中的所有后续字符将不再被比较
    比较原理：两字符进行比较时。比较的是其ordinal value(原始值)
            调用内置函数ord()可以得到指定字符的ordinal value(原始值)。
            与内置函数ord()对应的是内置函数chr()，调用内置函数chr()可以得到指定ordinal value(原始值)对应的字符。
"""


print('abcdef' > 'abcd')  # True
print('apple' > 'banana')  # False  相当于97>98?
print(ord('a'), ord('b'))

print(chr(97), chr(98))
print(ord('刘'))
print(chr(21016))

"""
==与is的区别：
    ==比较的是value是否相等
    is 比较的是id是否相等
"""

s1 = s2 = 'Hello'
s3 = 'Hello'
print(s1 == s2)  # True
print(s1 == s3)  # True
print(s1 is s2)  # True
print(s1 is s3)  # True  python的字符串驻留机制


