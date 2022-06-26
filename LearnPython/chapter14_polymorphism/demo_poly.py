#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/21 21:16
# @Author : HongShaoRou
# @Site : 
# @File : demo_poly.py
# @Software: PyCharm

# 多态
"""
多态就是"具有多种形态"，他指的是：
    即便不知道一个变量所引用的对象到底 是什么类型，仍然可以通过这个变量调用方法，
    在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法
"""


class Animal(object):
    def eat(self):
        print('动物正在吃东西...')


class Dog(Animal):
    def eat(self):
        print('狗正在吃肉...')


class Cat(Animal):
    def eat(self):
        print('猫正在吃鱼...')


class Person():
    def eat(self):
        print('人正在吃饭...')


# 定义一个函数
def func(obj):
    obj.eat()


func(Cat())
func(Dog())
func(Animal())
print('=====================')
func(Person())
