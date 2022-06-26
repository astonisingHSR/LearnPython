#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/19 15:16
# @Author : HongShaoRou
# @Site : 
# @File : demo_recursiveFunc.py
# @Software: PyCharm


# 递归函数

# 使用递归来计算阶乘

def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num - 1)


print(fac(6))


def fibo(num):
    if num <= 2:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)


print(fibo(6))

for i in range(1,7):
    print(fibo(i))

