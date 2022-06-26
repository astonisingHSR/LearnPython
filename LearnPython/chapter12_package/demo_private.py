#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/21 19:38
# @Author : HongShaoRou
# @Site : 
# @File : demo_private.py
# @Software: PyCharm

# 类的私有属性
"""
在python中没有专门的修饰符用于表示私有属性，如果不希望该属性在类外被访问，在前边使用两个'_'
"""


class Student:
    def __init__(self, name, age):  # 类的构造方法
        self.name = name  # self.name成为实体属性，进行了一个赋值操作，将局部变量name的值赋给实体属性
        self.__age = age  # age不希望在类外被访问

    def show(self):
        print(self.name, self.__age)


stu1 = Student('Peter', 18)
stu1.show()

print(stu1.name)
# print(stu1.age)
print(dir(stu1))
print(stu1._Student__age)  # 类的外部可以通过 _Student__age 进行访问

