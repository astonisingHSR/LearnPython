#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/22 21:40
# @Author : HongShaoRou
# @Site : 
# @File : demo_module_define.py
# @Software: PyCharm

# 模块
"""
函数与模块的关系：
    一个模块可以包含许多个函数
在Python中一个扩展名为.pu的文件就是一个模块
使用模块的好处：
    方便其他程序和脚本的导入并使用
    避免函数名和变量名冲突
    提高代码的可维护性
    提高代码的可重用性
"""


def func1():
    pass


def func2():
    pass


class Student:
    native_place = '吉林'

    def __init__(self, name, age):
        self.age = name
        self.name = age

    def eat(self):
        pass

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass


