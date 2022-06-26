#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/22 21:48
# @Author : HongShaoRou
# @Site : 
# @File : demo_import.py
# @Software: PyCharm

# 自定义模块的导入
"""
创建模块：
    新建一个.py文件，名称不要与python自带的标准模块名称相同
导入模块：
    import 模块名称 (as 别名)
    from 模块名称 import 函数/变量/类
"""

import math

print(id(math))
print(type(math))
print(math)
print(math.pi)
print('================================')
print(dir(math))
print(math.pow(2, 3), type(math.pow(2, 3)))
print(math.ceil(9.0001))
print(math.floor(9.99999))

from math import pi
print('=================================')
print(pi)

from demo_module_define import Student
print('===================================')
stu1 = Student('Peter', 18)
print(stu1)
stu1.eat()
