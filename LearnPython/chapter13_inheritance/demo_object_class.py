#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/21 21:08
# @Author : HongShaoRou
# @Site : 
# @File : demo_object_class.py
# @Software: PyCharm

# python中的objec类
"""
object类：
    object类是所有类的父类，因此所有类都有object类的属性和方法
    内置函数dir()可以查看指定对象所有属性
    object类有一个__str__()方法，用于返回一个关于"对象的描述"，
    对应内置函数str()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对__str__()进行重写
"""


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名：{0},今年{1}岁'.format(self.name, self.age)


stu = Student('Peter', 20)
print(dir(stu))
print(stu)  # 默认会调用__str__()方法
print(type(stu))
