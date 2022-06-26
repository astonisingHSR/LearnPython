#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/19 14:36
# @Author : HongShaoRou
# @Site : 
# @File : demo_func_param.py
# @Software: PyCharm

# 函数的参数定义

"""
函数定义默认值参数
    函数定义时，给形参设置默认值，只有与默认值不符时才需要传递实参
"""


def myfunc(num1, num2=100):
    print(num1, num2)


myfunc(10)  # 只传递一个值，则传递给未定义默认值的形参

myfunc(20, 30)

"""
函数的参数定义：
    个数可变的位置参数：
        定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
        使用 * 定义个数可变的位置形参
        结果为一个元组
    个数可变的关键字形参：
        定义函数时，无法事先确定传递的关键字实参的个数时，使用可变的关键字形参
        使用 ** 定义个数可变的关键字形参
        结果为一个字典
"""


def func1(*args):
    print(args)


func1(10)
func1(10, 20, 30)


def func2(**args):
    print(args)


func2(a=10)
func2(a=10, b=20, c=30)


# def func3(*args, *a):  # 程序报错，个数可变的位置参数只能有1个，个数可变关键字参数也只能有1个
#     print(args)


def func4(*arg1, **arg2):
    pass


# def func5(**arg1, *arg2):   #  程序报错，个数可变的位置形参必须放在个数可变的关键字形参之前
#     pass


"""
函数的参数总结

序号                  参数的类型                       函数的定义               函数的调用               备注
1                     位置实参                                                  √
             将序列中的每个元素都转换为位置实参                                      √                   使用*
2                    关键字实参                                                  √
            将字典中的每个键值对都转换为关键字实参                                    √                   使用**
3                    默认值形参                           √
4                    关键字形参                           √                                          使用*
5                 个数可变的位置形参                        √                                         使用*
6                个数可变的关键字形参                       √                                          使用**
"""


def func5(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


# 函数的调用
func5(10, 20, 30)  # 函数调用时的参数传递，成为位置传参
lst = [11, 22, 33]
func5(*lst)  # 在函数调用时，将列表中的每个元素都转换为位置实参传入

dic1 = {'a': 100, 'b': 200, 'c': 300}
func5(**dic1)  # 在函数调用时，将字典中的每个键值对都转换为关键字实参传入


def func6(a, b, *, d, c):  # *号后面的参数只能采用关键字传参
    pass


def func7(*arg1, **arg2):
    pass


def func8(a, b=10, *arg1, **arg2):
    pass



