#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/19 20:51
# @Author : HongShaoRou
# @Site : 
# @File : demo_try_except.py
# @Software: PyCharm

# python的异常处理机制

"""
Python提供了异常处理机制，可以在异常出现时及时捕获，然后内部消化，让程序继续运行
语法：
1个except结构：
    try:
        可能出现异常代码
    except 异常类型：
        异常处理代码

多个except结构：
    try:
        可能出现异常代码
    except 异常类型1：
        异常处理代码
    except 异常类型2：
        异常处理代码
    except BaseException：
        异常处理代码
"""

try:
    num1 = float(input('请输入被除数：'))
    num2 = float(input('请输入除数：'))
    ret = num1 / num2
except ZeroDivisionError:
    print('除数不能为0！')
except ValueError:
    print('请输入一个数！')
except BaseException as e:
    print(e)
else:    # 如果没有捕获到异常，执行else
    print('结果为：', ret)
finally:  # 无论是否捕获到异常，总会被执行的代码
    print('程序结束')




