#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/18 19:49
# @Author : HongShaoRou
# @Site : 
# @File : demo_string_operations2.py
# @Software: PyCharm


# -----------------字符串的常用操作2---------------
"""
字符串的分割操作：
    split()：从字符串左边开始分割，默认分割字符为空格，返回一个列表
            通过参数sep指定分割字符
            通过参数maxsplit指定最大分割次数，经过最大次数分割后，剩余的子串会单独作为一部分
    rsplit()：从字符串右边开始分割，默认分割字符为空格，返回一个列表
            通过参数sep指定分割字符
            通过参数maxsplit指定最大分割次数，经过最大次数分割后，剩余的子串会单独作为一部分
"""

s1 = 'hello world and python'
strLst = s1.split()
print(type(strLst), strLst)

s1 = 'hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))
print('------------from right split-------------')
print(s1.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|', maxsplit=1))


"""
字符串的判断操作：
    isidentifier():判断指定字符串是不是合法的标识符
    isspace():判断指定字符串是否全部由空白字符组成(回车、换行、水平制表符)
    isalpha()：判断指定字符串是否全部由字母组成
    isdemical():判断指定字符串是否全部由十进制的数字组成
    isnumeric():判断指定的字符串是否全部由数字组成
    isalnum()：判断指定的字符串是否全部由字母和数字组成
"""
print('-----------------字符串判断操作-----------------')
s1 = 'hello,world'
print('1.', s1.isidentifier())  # False
print('2.', 'hello'.isidentifier())  # True
print('3.', '张三_'.isidentifier())  # True
print('4.', '张三_123'.isidentifier())  # True

print('5.', '\t'.isspace())  # True
print('6.', '\n'.isspace())  # True

print('7.', 'abc'.isalpha())  # True
print('8.', '张三'.isalpha())  # True
print('9.', '张三1'.isalpha())  # False

print('10', '123'.isdecimal())  # True
print('11.', '123四'.isdecimal())  # False
print('12.', 'ⅠⅡⅢ'.isdecimal())  # False

print('13.', '123'.isnumeric())  # True
print('14.', '123四'.isnumeric())  # True
print('15.', 'ⅠⅡⅢ'.isnumeric())  # True

print('16.', 'abc123'.isalnum())  # True
print('17.', '张三123'.isalnum())  # True
print('18.', 'abc!'.isalnum())  # False

"""
字符串操作的其他方法：
    replace()：字符串替换
               第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，
               第三个参数指定最大替换次数(可选)
               返回替换后得到的字符串，替换前的字符串不发生变化
    join(): 字符串的合并
           将列表或元组中的字符串合并成一个字符串
"""
print('----------------字符串的其他操作------------------')
s1 = 'hello world'
print(s1.replace('world', 'python'))

s1 = 'hello world world world'
print(s1.replace('world', 'python', 2))

strLst = ['hello', 'world', 'python', 'cpp']
print(''.join(strLst))
print(' '.join(strLst))
print('|'.join(strLst))

strTuple = ('hello', 'world', 'python', 'cpp')
print(''.join(strTuple))
print(' '.join(strTuple))
print('|'.join(strTuple))

print('*'.join('Hello'))
