#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/11 0:07
# @Author : HongShaoRou
# @Site : 
# @File : demo_logic_operator.py
# @Software: PyCharm

# bool类型变量的运算

a, b = 1, 2
print(a == 1 and b == 2)  # 与运算符 True
print(a == 1 and b < 2)  # False

print(a == 1 or b < 2)  # True
print(not a == 1)  # 非 运算符  False
print(not a > 1)  # True

print('-------------------in 和 not in------------')
s = 'helloworld'
print('w' in s)  # True
print('w' not in s)  # False
print('k' in s)  # False

print('---------------位运算符---------------')
a = 4
b = 3
print(a, b)
print(a & b)  # 按位与
print(a | b)  # 按位或 相当于 + ？

# 左移位运算符，高位溢出舍弃，低位补0，相当于乘2
print(a << 1)  # 左移1位,不改变a的值
print(a << 2)

print(a >> 1)  # 右移1位，
print(a >> 2)

'''
运算符优先级
1、幂运算 **
2、乘除 *，/，//，%
3、加减 +，-
4、移位运算 >>,<<
5、位运算 $,|
6、比较运算 ==，>,<,<=,>=,!=
7、布尔运算 and, or ,
8、赋值运算 =
'''