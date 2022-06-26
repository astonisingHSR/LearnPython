#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/23 20:56
# @Author : HongShaoRou
# @Site : 
# @File : demo_useful_module.py
# @Software: PyCharm

# python中常用的内置模块
"""
模块名                 描  述
sys         与Python解释器及其环境操作相关的标准库
time        提供与时间相关的各种函数的标准库
os          提供了访问操作系统服务功能的标准库
calendar    提供与日期相关的各种函数的标准库
urllib      用于读取来自网上(服务器)的数据标准库
json        用于使用JSON序列化和反序列化对象
re          用于在字符串中执行正则表达式匹配和替换
math        提供标准算术运算函数的标准库
decimal     用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
logging     提供了灵活的记录时间、错误、警告和调试信息等日志信息的功能
"""

import sys
import time
import urllib.request

# sys标准库
print('=====================================')
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

# time标准库
print('=====================================')
print(time.time())
print(time.localtime(time.time()))

# urllib标准库
print('=====================================')
print(urllib.request.urlopen('http://www.baidu.com').read())
