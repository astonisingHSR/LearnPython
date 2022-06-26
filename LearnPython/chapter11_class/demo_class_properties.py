#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/21 19:25
# @Author : HongShaoRou
# @Site : 
# @File : demo_class_properties.py
# @Software: PyCharm

# 动态绑定属性与方法
"""
Python是动态语言，在创建对象后，可以动态的绑定属性和方法
"""


class Student:
    def __init__(self, name, age):  # 类的构造方法
        self.name = name  # self.name成为实体属性，进行了一个赋值操作，将局部变量name的值赋给实体属性
        self.age = age

    def eat(self):
        print(self.name, '正在吃饭...')


stu1 = Student('Peter', 20)
stu2 = Student('Jack', 18)
print('=================为stu1动态绑定属性==============')
stu1.gender = '男'

print(stu1.name, stu1.age, stu1.gender)
print(stu2.name, stu2.age)

print('==============================')
stu1.eat()
stu2.eat()


def show():
    print('定义在类外的函数')


stu1.show = show
stu1.show()

# stu2.show()  # error,因为stu2没有绑定show()方法
