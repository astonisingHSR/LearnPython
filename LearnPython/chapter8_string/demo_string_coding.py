#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/18 21:56
# @Author : HongShaoRou
# @Site : 
# @File : demo_string_coding.py
# @Software: PyCharm

# 字符串的编码转换
"""
为什么需要字符串的编码转换
    computerA:str在内存中以Unicode表示-----encode----->>byte字节传输------uncoding------>>ComputerB  显示
编码与解码的方式：
    编码：将字符串转换为二进制数据(bytes)
    解码：将bytes类型的数据转换成字符串类型
"""

s = '艺术家今晚不适合喝酒'
print('=======================编码=========================')
print(s.encode(encoding='GBK'))  # 在GBK编码格式中，一个中文占2个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8编码格式中，一个中文占3个字节
print('=======================解码=========================')
# byte表示的是一个二进制数据
byte1 = s.encode(encoding='GBK')
byte2 = s.encode(encoding='UTF-8')
print(byte1.decode(encoding='GBK'))
print(byte2.decode(encoding='UTF-8'))

