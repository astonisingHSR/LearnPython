#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/22 21:01
# @Author : HongShaoRou
# @Site : 
# @File : demo_class_copy.py
# @Software: PyCharm

# 类的浅拷贝与深拷贝
"""
变量的赋值操作：
    只是形成两个变量，实际上还是指向同一个对象
浅拷贝：
    python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象
深拷贝：
    使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
"""
import copy


class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的幅值
cpu1 = CPU()
cpu2 = cpu1  # 实际上指向同一个对象
print(cpu1, cpu2)

# 类的浅拷贝
print('===================================')
disk = Disk()  # 创建一个硬盘类的实例对象
computer = Computer(cpu1, disk)

# 浅拷贝
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)  # 两个computer对象的cpu和disk指向同一个对象


# 深拷贝
print('===================================')
computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)  # 两个computer对象的cpu和disk指向不同对象实例

