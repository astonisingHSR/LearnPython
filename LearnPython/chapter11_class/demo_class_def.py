#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/20 22:11
# @Author : HongShaoRou
# @Site : 
# @File : demo_class_def.py
# @Software: PyCharm

# 类的创建
"""
创建类的语法：
    class 类名：
        类属性
        实例方法
        静态方法
        类方法
"""


class Student:
    native_place = '吉林'  # 写在类里的变量，成为类属性

    def __init__(self, name, age):   # 类的构造方法
        self.name = name  # self.name成为实体属性，进行了一个赋值操作，将局部变量name的值赋给实体属性
        self.age = age

    def eat(self):  # 实例方法
        print(self.name, '正在吃饭...')

    # 静态方法
    @staticmethod
    def stamethod():  # 不允许出现self
        print('这是一个静态方法')

    # 类方法
    @classmethod
    def clsmethod(cls):  # 必须传入cls
        print('这是一个类方法')


print(id(Student))
print(type(Student))
print(Student)
print('=========================================')

"""===================对象的创建=================="""
"""
对象的创建也称为类的实例化
语法：
    实例名 = 类名 ()
意义：
    有了实例，就可以调用类中的内容
"""

stu1 = Student('Peter', 20)
print(id(stu1))
print(type(stu1))
print(stu1)
print('========================')
print(stu1.name)
print(stu1.age)

stu1.eat()
Student.eat(stu1)

stu1.stamethod()
Student.stamethod()

stu1.clsmethod()

