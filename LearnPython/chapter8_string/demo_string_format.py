#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/18 21:28
# @Author : HongShaoRou
# @Site : 
# @File : demo_string_format.py
# @Software: PyCharm

# 格式化字符串
"""
为什么需要格式化字符串：
    当需要一些固定格式的文本时，有些文本可见，有些文本不可见
    如果使用拼接操作，将浪费很多内存，因此需要格式化字符串
格式化字符串的两种方式:
    % 作占位符：
        '我的名字叫：%s，今年%d岁了' % (name, age)
    {} 作占位符:
        '我的名字叫：{0}，今年{1}岁了，我真的叫{0}'.format(name, age)
"""
# 使用%作为占位符
name = 'peter'
age = 20
print('我叫%s,今年%d岁' % (name, age))

# 使用{}作为占位符
print('我叫{0}，今年{1}岁，我真的叫{0}'.format(name, age))

# f-string格式化
print(f'我叫{name}，今年{age}岁，我真的叫{name}')

# 表示精度和宽度的格式化
print('%10d' % 99)
print('%.4f' % 3.141592654)  # 保留小数点后四位
print('%10.4f' % 3.141592654)  # 总宽度为10，保留小数点后4为
print('0123456789')

print('{0}'.format(3.141592654))
print('{0:.3}'.format(3.141592654))  # 表示一共三位数
print('{0:.3f}'.format(3.141592654))  # 表示三位小数
print('{0:10.3f}'.format(3.141592654))  # 表示总宽度10，三位小数
