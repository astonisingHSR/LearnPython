#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/21 19:58
# @Author : HongShaoRou
# @Site : 
# @File : demo_method_rewrite.py
# @Software: PyCharm

# 方法重写
"""
方法重写：
    如果父类的某个属性或方法对子类不适用，可以在子类中对其(方法体)进行重新编写
    子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法
"""


class Person(object):  # Person类继承了object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0},年龄：{1}岁'.format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no  # 通过super().xxx()调用父类中被重写的方法

    def info(self):
        print('姓名：{0},年龄：{1}岁,学号：{2}'.format(self.name, self.age, self.stu_no))

    def fatherinfo(self):
        super().info()


class Teacher(Person):
    def __init__(self, name, age, teachforyear):
        super().__init__(name, age)
        self.teachforyear = teachforyear

    def info(self):
        print('姓名：{0},年龄：{1}岁,教学时长：{2}年'.format(self.name, self.age, self.teachforyear))


stu = Student('Peter', 18, '1206')
teacher = Teacher('Rose', 32, 8)

print('=========================')
stu.info()
stu.fatherinfo()
teacher.info()
