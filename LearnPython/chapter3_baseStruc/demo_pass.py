#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/11 17:56
# @Author : HongShaoRou
# @Site : 
# @File : demo_compare_operator.py
# @Software: PyCharm

# pass语句
"""
pass 语句什么都不做
只是一个占位符，用在语法上需要语句的地方
"""

age = int(input('请输入您的年龄：'))

if age:
    pass
else:
    print('您的年龄为：', age)
