#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/21 21:26
# @Author : HongShaoRou
# @Site : 
# @File : demo_special_properties.py
# @Software: PyCharm

# 类的特殊属性
"""
  名称                              描  述
__dict__        获取类对象或实例对象所绑定的所有属性和方法的字典
__class__       获取类对象或实例对象所属的类
__bases__       获取类对象或实例对象的所有父类
__mro__         获取类对象或实例对象的层次结构
__subclasses__()获取类对象或实例对象的所有子类
"""


class Father1:
    pass


class Father2:
    pass


class Son(Father1, Father2):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Son2(Father1):
    pass


# 创建子类对象
son = Son('Jack', 20)
print(son.__dict__)  # 实例对象的属性
print(Son.__dict__)
print('==========================')
print(son.__class__)  # <class '__main__.Son'> 输出了对象所属的类
print(Son.__bases__)  # 输出Son的父类类型的元素
print(Son.__mro__)  # 输出类的层次结构
print(Father1.__subclasses__())
