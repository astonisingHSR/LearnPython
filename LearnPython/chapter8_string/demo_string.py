#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/18 14:30
# @Author : HongShaoRou
# @Site : 
# @File : demo_string.py
# @Software: PyCharm

# 字符串操作

"""
字符串的驻留机制：
    字符串是一个不可变的字符序列
    仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中。
    python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量
"""

myStr1 = 'hello'
myStr2 = 'hello'
print(myStr1, id(myStr1))  # 两者id相同,说明myStr1与myStr2指向同一份内存空间
print(myStr2, id(myStr2))
myStr3 = 'world'
print(myStr3, id(myStr3))

"""
驻留机制的几种情况（交互模式）：
    字符串长度为0或者1时
    符合标识符的字符串
    字符串只在编译时进行驻留，而非运行时
    [-5,256]之间的整数数字
sys中的intern方法强制2个字符串指向同一个对象
PyCharm对字符串进行了优化处理
"""

"""
字符串驻留机制的优缺点：
    当需要相同值的字符串时，可以直接从字符串池里拿来进行使用，避免频繁的创建和销毁，提升效率和节约内存，因此拼接字符串和修改字符串是比较影响性能的
    
    在需要进行字符串拼接时建议使用str类型的join方法，而非 + ,因为join()方法是先计算出所有字符串的长度，然后再拷贝，只new一次对象，效率要比+效率高
"""