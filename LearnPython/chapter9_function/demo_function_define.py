#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/19 13:24
# @Author : HongShaoRou
# @Site : 
# @File : demo_function_define.py
# @Software: PyCharm

# 函数的定义与调用

"""
函数的创建：
    def 函数名([输入参数]):
        函数体
        [return xxx]
"""


def add(add1, add2):
    return add1 + add2


ret = add(add1=10, add2=20)
print(ret)
print(add(10, 20))

"""
函数的参数传递：
    位置实参：
        根据形参对应的位置进行实参传递
    关键字实参：
        根据形参名称进行实参传递
"""
ret = add(add2=20, add1=20)
print(ret)


def func(arg1, arg2):
    print(arg1)
    print(arg2)
    arg1 = 100
    arg2.append(10)
    print(arg1)
    print(arg2)
"""
如果是不可变对象，函数体内的修改不会影响实参的值
如果是可变对象，在函数体内进行修改会影响实参的值
"""

n1 = 11
n2 = [22, 33, 44]
print('============函数执行前===========')
print('n1=', n1)
print('n2=', n2)
func(n1, n2)
print('============函数执行后===========')
print('n1=', n1)
print('n2=', n2)
"""
可以发现,n1没有发生改变，但是n2发生了改变，原因在于
    1、传递方式是引用传递
    2、n1是不可变对象，改变值也会改变其id，n2是可变对象。
"""