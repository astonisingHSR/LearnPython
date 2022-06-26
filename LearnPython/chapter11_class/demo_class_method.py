#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/20 22:41
# @Author : HongShaoRou
# @Site : 
# @File : demo_class_method.py
# @Software: PyCharm

# 类属性、类方法、静态方法

"""
类属性：类中方法外的变量成为类属性，被该类的所有对象所共享，类似与c++中类的静态属性
类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
       类名.类方法(参数)
静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
        类名.静态方法(参数)
"""


class Student:
    native_place = '吉林'  # 写在类里的变量，成为类属性

    def __init__(self, name, age):  # 类的构造方法
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


# 类属性的使用方式
# print(Student.native_place)
stu1 = Student('Peter', 20)
stu2 = Student('Jack', 18)

print(stu1.native_place)
print(stu1.native_place)
Student.native_place = '黑龙江'
print(stu1.native_place)
print(stu1.native_place)
print('===============================')
Student.clsmethod()
Student.stamethod()
