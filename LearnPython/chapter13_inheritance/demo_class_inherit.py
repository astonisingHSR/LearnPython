#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/21 19:50
# @Author : HongShaoRou
# @Site : 
# @File : demo_class_inherit.py
# @Software: PyCharm

# 类的继承
"""
语法：
    class 子类类名(父类1， 父类2，...):
        pass
如果一个类没有继承任何类，默认继承object类
python支持多继承
定义子类时，必须在其构造函数中调用父类的构造函数
"""


class Person(object):  # Person类继承了object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no


class Teacher(Person):
    def __init__(self, name, age, teachForYear):
        super().__init__(name, age)  # 初始化父类对象
        self.teachForYear = teachForYear


stu = Student('Peter', 18, '1206')
teacher = Teacher('Rose', 32, 8)

stu.info()
teacher.info()
