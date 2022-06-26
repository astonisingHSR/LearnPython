#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/21 21:42
# @Author : HongShaoRou
# @Site : 
# @File : demo_special_method.py
# @Software: PyCharm

# 类的特殊方法
"""
特殊方法    __len__()        通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
          __add__()        通过重写__add__()方法，可以让自定义对象具有"+"功能
          __new__()        用于创建对象
          __init__()       对创建的对象进行初始化
"""


"""
__new__()方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。
还有就是实现自定义的metaclass。
"""


# a = 20
# b = 100
#
# c = a + b
# d = a.__add__(b)
# print(c, d)


class Student(object):
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return Student(self.name+other.name)

    def __len__(self):
        return len(self.name)

    def __new__(cls, *args, **kwargs):
        print('__new__ of Student is called')
        return super().__new__(cls)


stu1 = Student('Peter')
stu2 = Student('Jack')
s = stu1 + stu2
s1 = stu1.__add__(stu2)
print(s.name, s1.name)
print('=============================')
print(len(stu1), len(s1))

print('====================')


class Person(object):
    def __init__(self, name, age):
        print('__init__ called,id of self:{0}'.format(id(self)))
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print('__new__ called,id of cls:{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('id of obj：{0}'.format(id(obj)))
        return obj


print('object类对象的id为：{0}'.format(id(object)))
print('Person类对象的id为：{0}'.format(id(Person)))

# Person类的实例对象
p1 = Person('Peter', 20)
print('p1的id值为：{0}'.format(id(p1)))
