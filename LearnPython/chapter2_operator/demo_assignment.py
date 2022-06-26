#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/10 23:45
# @Author : HongShaoRou
# @Site : 
# @File : demo_assignment.py
# @Software: PyCharm

# 赋值运算符
a = 3 + 4
print(a)

a = b = c = 2  # 链式赋值
d = 2
print(a, b, c, d, id(a), id(b), id(c), id(d))  # 标识都相同，即意味着指向同一个地址，
# 参数赋值
a = 30
a //=3
print(a, type(a))  # int类型
a /=3
print(a, type(a))  # float类型
a*=3
print(a, type(a))  # float类型

# 系列解包赋值
a, b, c = 20, 30, 40
print(a, b, c, id(a), id(b), id(c))

# 交换两个参数的值
a, b = 10, 20
print('before swap：', a, b)
a, b = b, a
print('after swap', a, b)
